import os
from utils.selenium_utils import get_webdriver
from src.downloader import download_pdfs

def main():
    base_url = 'https://www.leadingindia.ai/projects'
    download_directory = os.path.join(os.getcwd(), 'data')
    
    driver = get_webdriver(headless = False,
                           download_directory = download_directory)
    download_pdfs(driver, base_url)

if __name__ == "__main__":
    main()
