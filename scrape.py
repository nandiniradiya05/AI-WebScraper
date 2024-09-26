from selenium.webdriver import Remote, ChromeOptions
from selenium import webdriver
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from bs4 import BeautifulSoup

# def scrape_website(website):
#     print("Launching Chrome...")
    
#     chrome_driver_path = './chromedriver'
#     options = webdriver.ChromeOptions()
#     driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)
    
#     try:
#         print(f"Scraping {website}...")
#         driver.get(website)
#         html = driver.page_source
#         time.sleep(10)
        
#         return html
    
#     finally:
#         driver.quit()
        
        

AUTH = 'brd-customer-hl_063a0a56-zone-ai_scraper:2xto5vgmay7g'
SBR_WEBDRIVER = f'http://api.scrapingbrowser.com/api/v1/webdriver?auth={AUTH}'
def main(website):
    print('Connecting to Scraping Browser...')
    chrome_driver_path = './chromedriver'
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)
    
    print(f"Scraping {website}...")
    driver.get(website)
    html = driver.page_source
    # time.sleep(10)
    
    return html
    # sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, 'goog', 'chrome')
    # with Remote(sbr_connection, options=ChromeOptions()) as driver:
    #     print('Connected! Navigating...')
    #     driver.get(website)
    #     print('Taking page screenshot to file page.png')
    #     driver.get_screenshot_as_file('./page.png')
    #     print('Navigated! Scraping page content...')
    #     html = driver.page_source
        
    #     return html
    
    
def extract_html(html_content):
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
        cleaned_content = "\n".join([line.strip() for line in cleaned_content.splitlines() if line.strip()])
        
        return cleaned_content
    
    
def split_dom_content(dom_content, max_length=6000):
    return [dom_content[i:i+max_length] for i in range(0, len(dom_content), max_length)]