from playwright.sync_api import sync_playwright
from time import perf_counter

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=4000)
    page = browser.new_page()
    print("page loading...")
    start = perf_counter()

    page.goto("https://bootswatch.com/default", 
        #wait until='load',    // load all image resources
        # wait_until='commit', // html response from server(HTML parsed and <script> executed)
        # wait_until='domcontentloaded',   //just load page not image or rest things
        # wait_until='networkidle',  // network in or out
        wait_until='commit',
    ) 
    time_taken = perf_counter() - start
    print(f"...Page loaded in {round(time_taken, 2)}s")

    browser.close()