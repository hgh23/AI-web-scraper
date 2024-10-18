from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from selenium.common.exceptions import WebDriverException
import traceback

def scrape_website(url):
    print("Launching chrome browser...")
    
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run in headless mode
    
    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        
        print(f"Navigating to {url}")
        driver.get(url)
        
        print('Scraping page content...')
        html = driver.page_source
        return html
    except WebDriverException as e:
        print(f"WebDriver error: {e}")
        print(traceback.format_exc())
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        print(traceback.format_exc())
        return None
    finally:
        if 'driver' in locals():
            driver.quit()

def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""

def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")
    
    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()
        
    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )
    
    return cleaned_content

def split_dom_content(dom_content, max_length=6000):
    return [
        dom_content[i: i + max_length] for i in range(0, len(dom_content), max_length)
    ]
