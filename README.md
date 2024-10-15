# AI Web Scraper

## Overview
The AI Web Scraper is a powerful tool that combines web scraping capabilities with AI-powered parsing. 
It allows users to extract specific information from websites based on natural language queries. 
The application uses Streamlit for the user interface, Selenium for web scraping, and the Ollama AI model for intelligent parsing of web content.

## Features
- Web scraping of any given URL
- AI-powered parsing of scraped content
- User-friendly interface built with Streamlit
- Automatic export of parsed data to CSV
- Direct saving of results to the user's Downloads folder

## Requirements
To run the AI Web Scraper, you need:

1. Python 3.7 or higher
2. pip (Python package installer)
3. Chrome browser installed on your system
4. Ollama AI model set up on your local machine

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-repository/ai-web-scraper.git
   cd ai-web-scraper
   ```

2. Install required Python packages:
   ```
   pip install -r requirements.txt
   ```

3. Set up Ollama:
   - Follow the installation instructions at [Ollama's official website](https://ollama.ai/)
   - Make sure the Llama 3.1 model is available in your Ollama installation

## Configuration

1. In `scrape.py`, update the `SBR_WEBDRIVER` variable with your actual Scraping Browser credentials:
   ```python
   SBR_WEBDRIVER = 'https://brd-customer-hl_YOUR_ACTUAL_CREDENTIALS@brd.superproxy.io:9515'
   ```

2. In `main.py`, ensure the Downloads folder path is correct for your system:
   ```python
   downloads_folder = r"C:\Users\YourUsername\Downloads"
   ```

## Usage

1. Start the Streamlit app:
   ```
   streamlit run main.py
   ```

2. Open your web browser and go to the URL provided by Streamlit (usually `http://localhost:8501`)

3. Enter a website URL in the text input field and click "Scrape Site"

4. Once the site is scraped, enter a description of what you want to parse in the text area

5. Click "Parse Content" to extract the desired information

6. The parsed data will be displayed on the screen and automatically saved as a CSV file in your Downloads folder

7. You can also use the "Download CSV" button to download the file directly from the Streamlit interface

## How It Works

1. **Web Scraping (`scrape.py`):**
   - Uses Selenium with Scraping Browser to navigate to the specified URL
   - Handles CAPTCHAs automatically
   - Extracts the full HTML content of the page

2. **Content Cleaning (`scrape.py`):**
   - Extracts the body content from the HTML
   - Removes scripts, styles, and unnecessary whitespace
   - Splits the content into manageable chunks

3. **AI Parsing (`parse.py`):**
   - Utilizes the Ollama AI model (Llama 3.1)
   - Processes each chunk of the scraped content
   - Extracts information based on the user's natural language query

4. **Data Export (`main.py`):**
   - Combines parsed results from all chunks
   - Saves the data as a CSV file in the user's Downloads folder
   - Provides a download link in the Streamlit interface

5. **User Interface (`main.py`):**
   - Built with Streamlit for an interactive experience
   - Allows users to input URLs and parsing instructions
   - Displays results and provides access to exported data

## Troubleshooting

- If you encounter issues with web scraping, ensure your Scraping Browser credentials are correct and active
- For AI parsing problems, check that Ollama is properly installed and the Llama 3.1 model is available
- If CSV files are not appearing in your Downloads folder, verify the path in `main.py` is correct for your system

## Contributing

Contributions to improve the AI Web Scraper are welcome. Please feel free to submit pull requests or open issues for bugs and feature requests.

## License

[Applied Data Science, e.g., MIT License]
