from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=4000)
    page = browser.new_page()
    page.goto("https://bootswatch.com/default")
    #auto waiting 
    #link = page.locator("a.dropdown-item").first
    #link.click(force=True)
    link = page.locator("a.dropdown-toggle").first
    link.click()
    link = page.locator("a.dropdown-item").first
    link.click(force=True)
    browser.close()