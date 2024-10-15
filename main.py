import streamlit as st
import csv
import os
import datetime
from scrape import (
    scrape_website, 
    split_dom_content, 
    clean_body_content, 
    extract_body_content,
)
from parse import parse_with_ollama

def export_to_csv(data, filename=None):
    # Set the path to the Downloads folder
    downloads_folder = r"C:\Users\leon2\Downloads"
    
    # Create a timestamp for unique filenames
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # If no filename is provided, create one with the timestamp
    if filename is None:
        filename = f"parsed_data_{timestamp}.csv"
    else:
        # If a filename is provided, add the timestamp before the extension
        name, ext = os.path.splitext(filename)
        filename = f"{name}_{timestamp}{ext}"
    
    # Create the full file path
    file_path = os.path.join(downloads_folder, filename)
    
    # Write the data to the CSV file
    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Parsed Data"])  # Header
        for row in data.split('\n'):
            writer.writerow([row])
    
    print(f"CSV file created at: {file_path}")
    return file_path

st.title("AI Web Scrapper")
url = st.text_input("Enter a Website URL:")

if st.button("Scrape Site"):
    st.write("Scraping the website")
    
    result = scrape_website(url)
    body_content = extract_body_content(result)
    cleaned_content = clean_body_content(body_content)
    
    st.session_state.dom_content = cleaned_content
    
    with st.expander("View DOM Content"):
        st.text_area("DOM Content", cleaned_content, height=300)

if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want to parse?")
    
    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content")
            
            dom_chunks = split_dom_content(st.session_state.dom_content)
            result = parse_with_ollama(dom_chunks, parse_description)
            st.write(result)
            
            # Export to CSV
            csv_file_path = export_to_csv(result)
            st.success(f"Data exported to your Downloads folder")
            st.info(f"You can find the CSV file at: {csv_file_path}")
            
            # Provide download button (optional, since file is already in Downloads)
            with open(csv_file_path, 'rb') as file:
                st.download_button(
                    label="Download CSV",
                    data=file,
                    file_name=os.path.basename(csv_file_path),
                    mime="text/csv"
                )