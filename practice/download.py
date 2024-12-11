from playwright.sync_api import sync_playwright
 
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=3000)
    page = browser.new_page()
    page.goto("https://unsplash.com/photos/a-woman-standing-in-front-of-a-flat-screen-tv-20A4KOtqmEI")
    btn = page.get_by_role("link", name="Download free")
    with page.expect_download() as download_info:
        btn.click()
        download = download_info.value
        download.save_as("woman.jpg")
   
    browser.close()