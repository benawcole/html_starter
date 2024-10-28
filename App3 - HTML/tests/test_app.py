from playwright.sync_api import Page, expect

# Tests for your routes go here

def test_albums(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f'http://{test_web_address}/albums')
    expect(page.locator("h1")).to_have_text("Albums")
