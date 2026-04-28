from playwright.sync_api import sync_playwright

def search_and_add(product):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.amazon.in")

        page.fill("input[name='field-keywords']", product)
        page.press("input[name='field-keywords']", "Enter")

        page.click("div.s-main-slot h2 a")

        new_page = page.context.pages[-1]

        price = new_page.locator("span.a-price-whole").first.text_content()
        print(product, "Price:", price)

        new_page.click("#add-to-cart-button")

        browser.close()

def test_iphone():
    search_and_add("iPhone")

def test_galaxy():
    search_and_add("Samsung Galaxy")
