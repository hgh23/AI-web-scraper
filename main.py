import streamlit as st
import csv
import os
import datetime
from scrape import (
    scrape_website,
    extract_body_content,
    clean_body_content,
    split_dom_content,
)
from parse import parse_with_ollama

def export_to_csv(data, filename=None):
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
        for row in data.split('\n'):
            writer.writerow(row.split('|'))
    
    print(f"CSV file created at: {file_path}")
    return file_path

# Streamlit UI
st.title("AI Web Scraper")
url = st.text_input("Enter Website URL")

# Step 1: Scrape the Website
if st.button("Scrape Website"):
    if url:
        st.write("Scraping the website...")

        # Scrape the website
        dom_content = scrape_website(url)
        body_content = extract_body_content(dom_content)
        cleaned_content = clean_body_content(body_content)

        # Store the DOM content in Streamlit session state
        st.session_state.dom_content = cleaned_content

        # Display the DOM content in an expandable text box
        with st.expander("View DOM Content"):
            st.text_area("DOM Content", cleaned_content, height=300)


# Step 2: Ask Questions About the DOM Content
if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want to parse")

    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content...")

            # Parse the content with Ollama
            dom_chunks = split_dom_content(st.session_state.dom_content)
            parsed_result = parse_with_ollama(dom_chunks, parse_description)
            st.write(parsed_result)

            # Export to CSV
            if parsed_result:
                csv_file_path = export_to_csv(parsed_result)
                st.success(f"Data exported to your Downloads folder")
                st.info(f"You can find the CSV file at: {csv_file_path}")
                
                # Provide download button
                with open(csv_file_path, 'rb') as file:
                    st.download_button(
                        label="Download CSV",
                        data=file,
                        file_name=os.path.basename(csv_file_path),
                        mime="text/csv"
                    )
            else:
                st.warning("No data to export.")
