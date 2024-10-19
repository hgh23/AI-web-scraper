# AI Web Scraper

This project is an AI-powered web scraper that uses Streamlit for the user interface, Selenium for web scraping, and the Ollama language model for parsing and extracting specific information from web content.

## Features

- Web scraping using Selenium
- Content parsing and information extraction using Ollama LLM
- User-friendly interface with Streamlit
- CSV export of extracted information

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/ai-web-scraper.git
   cd ai-web-scraper
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

<<<<<<< HEAD
4. Make sure you have Chrome installed, as the scraper uses ChromeDriver.
=======
3. Set up Ollama:
   - Follow the installation instructions at [Ollama's official website](https://ollama.ai/)
   - Make sure the Llama 3.1 model is available in your Ollama installation

## Configuration

1. In `main.py`, ensure the Downloads folder path is correct for your system:
   ```python
   downloads_folder = r"C:\Users\YourUsername\Downloads"
   ```
>>>>>>> ea18134c5f34eef65d565e6f5d228cb542f3b9e1

## Usage

1. Run the Streamlit app:
   ```
   streamlit run main.py
   ```

2. Enter a URL in the text input field and click "Scrape Website".

3. Once the website is scraped, you can view the DOM content in the expandable section.

4. Enter a description of the information you want to extract in the text area.

5. Click "Parse Content" to extract the specified information.

6. View the parsed results in the Streamlit interface.

7. Download the extracted information as a CSV file using the provided button.

## Project Structure

- `main.py`: The main Streamlit application file.
- `scrape.py`: Contains functions for web scraping using Selenium.
- `parse.py`: Handles the parsing and extraction of information using Ollama LLM.
- `requirements.txt`: List of Python dependencies.

## Dependencies

- Streamlit
- Selenium
- BeautifulSoup
- Langchain
- Ollama
- Pydantic

## Notes

- The scraper uses ChromeDriver, so make sure you have Chrome installed on your system.
- The parsing is done using the Ollama language model. Make sure you have it properly set up and running.
- The extracted information is saved as a CSV file in your Downloads folder.

## Troubleshooting

If you encounter any issues:
- Make sure all dependencies are correctly installed.
- Check that Chrome and ChromeDriver are properly set up.
- Ensure that the Ollama language model is running and accessible.
- Check the console output for any error messages.

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check [issues page](https://github.com/yourusername/ai-web-scraper/issues) if you want to contribute.

## License

[MIT](https://choosealicense.com/licenses/mit/)
