from playwright.sync_api import Page, expect

def test_get_home(page, test_web_address):
    page.goto(f"http://{test_web_address}")
    h1_tags = page.locator("h1")
    expect(h1_tags).to_have_text("It's almost Christmas!")
    checklist_tags = page.locator(".t-checklist")
    expect(checklist_tags).to_have_text([
        "Put up the decorations",
        "Write a letter to Father Christmas",
        "Buy presents",
        "Wrap presents",
        "Write Christmas Cards",
        "Watch some Christmas Films",
        "Listen to Christmas Music",
        "Leave a mince pie and carrot out for Father Christmas and Ruldolph"
    ])
    food_heading_tags = page.locator("h3")
    expect(food_heading_tags).to_have_text([
        'Starters:',
        'Center Piece:',
        'Side Dishes:'
    ])
    starters_tags = page.locator('.t-starters')
    expect(starters_tags).to_have_text([
        'Soup',
        'Prawn Cocktail',
        'Salmon Blinis',
        'Pate or Parfait'
    ]

    )

    # response = web_client.get("/")
    # assert response.status_code == 200
    # assert response.data.decode("utf-8") == "I am a CI-CD hero"
