import streamlit as st
import csv
import os
import datetime
import logging
from scrape import (
    scrape_website,
    extract_body_content,
    clean_body_content,
    split_dom_content,
)
from parse import parse_with_ollama, ExtractedInfo

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def export_to_csv(data: list[ExtractedInfo], filename=None):
    downloads_folder = r"C:\Users\leon2\Downloads"
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    
    if filename is None:
        filename = f"parsed_data_{timestamp}.csv"
    else:
        name, ext = os.path.splitext(filename)
        filename = f"{name}_{timestamp}{ext}"
    
    file_path = os.path.join(downloads_folder, filename)
    
    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Content', 'Confidence'])  # Header
        for item in data:
            writer.writerow([item.content, item.confidence])
    
    logger.info(f"CSV file created at: {file_path}")
    return file_path

# Streamlit UI
st.title("AI Web Scraper")
url = st.text_input("Enter Website URL")

# Step 1: Scrape the Website
if st.button("Scrape Website"):
    if url:
        try:
            with st.spinner("Scraping the website..."):
                dom_content = scrape_website(url)
                body_content = extract_body_content(dom_content)
                cleaned_content = clean_body_content(body_content)
                st.session_state.dom_content = cleaned_content
                with st.expander("View DOM Content"):
                    st.text_area("DOM Content", cleaned_content, height=300)
            st.success("Website scraped successfully!")
        except Exception as e:
            logger.error(f"Error during web scraping: {str(e)}")
            st.error(f"An error occurred while scraping the website: {str(e)}")

# Step 2: Ask Questions About the DOM Content
if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want to parse", 
    """Please extract food dishes and their descriptions from the DOM content. 
    For each dish, include its name and full description.""")

    if st.button("Parse Content"):
        if parse_description:
            try:
                with st.spinner("Parsing the content..."):
                    dom_chunks = split_dom_content(st.session_state.dom_content)
                    parsed_result = parse_with_ollama(dom_chunks, parse_description)
                
                if parsed_result:
                    st.write("Parsed Result:")
                    for item in parsed_result:
                        st.write(f"Content: {item.content}")
                        st.write(f"Confidence: {item.confidence}")
                        st.write("---")

                    csv_file_path = export_to_csv(parsed_result)
                    st.success(f"Data exported to your Downloads folder")
                    st.info(f"You can find the CSV file at: {csv_file_path}")
                    
                    with open(csv_file_path, 'rb') as file:
                        st.download_button(
                            label="Download CSV",
                            data=file,
                            file_name=os.path.basename(csv_file_path),
                            mime="text/csv"
                        )
                else:
                    st.warning("No data found matching the description.")
            except Exception as e:
                logger.error(f"Error during parsing: {str(e)}")
                st.error(f"An error occurred while parsing the content: {str(e)}")
