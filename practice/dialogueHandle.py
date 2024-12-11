from playwright.sync_api import sync_playwright
 
def on_dialog(dialog):
   print("dialog opened",dialog)
   dialog.accept("cool")
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=3000)
    page = browser.new_page()
    page.goto("https://testpages.eviltester.com/styled/alerts/alert-test.html")

    page.on("dialog", on_dialog) 
    
    alert_btn = page.get_by_text("show prompt box")
    alert_btn.click()
    browser.close()