from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=4000)
    page = browser.new_page()
    page.goto("https://playwright.dev/python/")
    # locate a link on button
    docs_button = page.get_by_role('link', name='Docs')
    docs_button.click()
    # get url
    print('Docs:', page.url)
    browser.close()