from playwright.sync_api import Page, expect

def test_get_home(page, test_web_address):
    page.goto(f"http://{test_web_address}")
    h1_tags = page.locator("h1")
    expect(h1_tags).to_have_text("Christmas Website")

    # response = web_client.get("/")
    # assert response.status_code == 200
    # assert response.data.decode("utf-8") == "I am a CI-CD hero"
