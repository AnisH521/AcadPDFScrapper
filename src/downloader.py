import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException
from utils.selenium_utils import wait_for_element

def download_pdfs(driver, base_url):
    driver.get(base_url)
    time.sleep(3)

    try:
        ol_element = wait_for_element(driver, By.CLASS_NAME, 'resgrouplist')
        anchor_tags = ol_element.find_elements(By.TAG_NAME, 'a')

        for anchor in anchor_tags:
            href = anchor.get_attribute('href')
            
            if href:
                try:
                    driver.get(href)

                    # Wait for the page to load
                    time.sleep(3)
                    # Re-locate the ol element and anchor tags since we navigated back
                    ol_element = wait_for_element(driver, By.CLASS_NAME, 'resgrouplist')
                    anchor_tags = ol_element.find_elements(By.TAG_NAME, 'a')
                
                except (NoSuchElementException, TimeoutException, WebDriverException) as e:
                    print(f"An error occurred while handling the link {href}: {e}")

    except (NoSuchElementException, TimeoutException, WebDriverException) as e:
        print(f"An error occurred while locating the ol element or anchor tags: {e}")
    
    finally:
        driver.quit()
