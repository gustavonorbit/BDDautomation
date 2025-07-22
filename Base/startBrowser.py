from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def start_browser():
    options = ChromeOptions()
    #options.add_argument("")  # Run in headless mode
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Initialize the Chrome driver with the specified options
    driver = Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    return driver