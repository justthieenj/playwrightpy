from playwright.sync_api import expect


def test_playwright_homepage(playwright):
    chromium = playwright.chromium  # or "firefox" or "webkit".
    browser = chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://playwright.dev/python/")
    expect(page).to_have_title("Fast and reliable end-to-end testing for modern web apps | Playwright Python")
    browser.close()
