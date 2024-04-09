"""
@name: utils.py
@date: 09/04/2024
@author: github.com/chrvstian
"""


from typing import Any, Dict
from playwright.sync_api import sync_playwright


def take_screenshot_from_url(
        url: str,
        session_data: Dict[str, str]
    ) -> bytes:
    """
    Takes a screenshot from a given URL using Playwright.
    
    Parameters:
        url (str): The URL to take a screenshot from.
        session_data (Dict[str, str]): Session data to be used for authentication.
        
    Returns:
        bytes: The screenshot in bytes format.
    """
    with sync_playwright() as playwright:
        webkit = playwright.webkit
        browser = webkit.launch()
        browser_context = browser.new_context(device_scale_factor=2)
        browser_context.add_cookies([session_data])
        page = browser_context.new_page()
        page.goto(url)
        screenshot_bytes: bytes = page.locator(".code").screenshot()
        browser.close()

        return screenshot_bytes

