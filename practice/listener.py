from playwright.sync_api import sync_playwright

def on_filechooser(filechooser):
    print("filechooser opened")
    filechooser.set_files("file.txt")
    
with sync_playwright() as playwright:

    browser= playwright.chromium.launch(headless=False , slow_mo=1000)

    page= browser.new_page()

    page.on("filechooser", on_filechooser)

    page.goto("https://bootswatch.com/default")

    file_input= page.get_by_label("default file input example")
    file_input.click()
    
    browser.close()