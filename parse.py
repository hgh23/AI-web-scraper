import json
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import List

# Define the structure of your output
class ExtractedInfo(BaseModel):
    content: str = Field(description="The extracted content matching the description")
    confidence: float = Field(description="Confidence score of the extraction (0-1)")

class ParsedResult(BaseModel):
    extracted_info: List[ExtractedInfo] = Field(description="List of extracted information")

# Create a parser
parser = PydanticOutputParser(pydantic_object=ParsedResult)

template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Extract the information that directly matches the provided description: {parse_description}. "
    "2. **Structured Output:** Your response must be in the following format:\n{format_instructions}\n"
    "3. **Empty Response:** If no information matches the description, return an empty list for extracted_info."
    "4. **Important:** Include all relevant information in the JSON output. Do not include any text outside the JSON structure."
)

model = OllamaLLM(model="llama3.1")

def extract_json(text):
    try:
        # Find the start and end of the JSON object
        start = text.find('{')
        end = text.rfind('}') + 1
        if start != -1 and end != -1:
            json_str = text[start:end]
            return json.loads(json_str)
    except json.JSONDecodeError:
        pass
    return None

def parse_with_ollama(dom_chunks, parse_description):
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model

    parsed_results = []

    for i, chunk in enumerate(dom_chunks, start=1):
        response = chain.invoke({
            "dom_content": chunk, 
            "parse_description": parse_description,
            "format_instructions": parser.get_format_instructions()
        })
        print(f"Parsed batch: {i} of {len(dom_chunks)}")
        
        # Extract JSON from the response
        json_data = extract_json(response)
        if json_data:
            try:
                parsed_result = parser.parse(json.dumps(json_data))
                parsed_results.extend(parsed_result.extracted_info)
            except ValueError as e:
                print(f"Error parsing result: {e}")
        else:
            print(f"No valid JSON found in response for batch {i}")

    return parsed_results
