import logging

from playwright.sync_api import sync_playwright

from .utils import start_chrome

# Set up logging configuration
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def google_search_and_signout(page):
    # Navigate to Google
    page.goto("https://www.google.com")

    # Locate the search box and perform search
    search_box = page.locator('textarea[name="q"]')
    search_box.fill("what is computer")
    search_box.press("Enter")

    # Wait for search results
    page.wait_for_selector("#search")

    account_button = page.locator('a.gb_B.gb_Za')
    account_button.click()

    signout_button = page.locator('button#signout.sign-out[name="signout"]')
    signout_button.click()
    print("Logging out ...")
    page.wait_for_timeout(2000)
    page.close()

def login_to_gmail(page, email, password):
    print("Logging in...")

    page.goto("https://accounts.google.com/v3/signin/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin")
    # Enter email
    page.fill("input[type='email']", email)
    page.click("#identifierNext")

    # Enter password
    page.fill("input[type='password']", password)
    page.click("#passwordNext")
    page.wait_for_timeout(3000)
    return page


def main(email: str, password: str, ) -> None:

    try:
        with sync_playwright() as p:
            # start_chrome()
            browser = p.chromium.connect_over_cdp("http://127.0.0.1:9223")
            page = browser.contexts[0].pages[0]
            page=login_to_gmail(page, email, password)

            google_search_and_signout(page)
            page.close()
            browser.close()

    except Exception as e:
        logger.error(e)
