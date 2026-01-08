import time

from playwright.sync_api import expect


def test_validate_login(page):
    page.goto("https://www.zenclass.in/login")
    page.locator("//input[@placeholder='Enter your mail']").fill("vidhyasarjun@gmail.com")
    page.locator("//input[@type='password']").fill("Guvi!2Plat")
    page.locator("//button[@type='submit']").click()
    page.locator("//button[@aria-label='Close popup']").click()
    url = page.url
    title = page.title()
    print(title)

    assert url == "https://www.zenclass.in/dashboard" , "Login process has failed"


def test_invalidate_login(page):
    page.goto("https://www.zenclass.in/login")
    page.locator("//input[@placeholder='Enter your mail']").fill("vidhyasarjun@gmail.com")
    page.locator("//input[@type='password']").fill("Guvi!")
    page.locator("//button[@type='submit']").click()

    print(page.url)
    title = page.title()
    print(title)

    assert page.url == "https://www.zenclass.in/login" ,"User shoud not get into home page"

def test_input_field_validation(page):

    page.goto("https://www.zenclass.in/login")
    emailfield =  page.locator("//input[@placeholder='Enter your mail']")
    passwordfield = page.locator("//input[@type='password']")
    login_button = page.locator("//button[@type='submit']")

    expect(emailfield).to_be_enabled(),"Username field not visible"
    expect(passwordfield).to_be_enabled(),"Password field not visible"
    expect(login_button).to_be_enabled(),"login button not visible"

def test_logout_button_validation(page):

    page.goto("https://www.zenclass.in/login")
    page.locator("//input[@placeholder='Enter your mail']").fill("vidhyasarjun@gmail.com")
    page.locator("//input[@type='password']").fill("Guvi!2Plat")
    login = page.locator("//button[@type='submit']").click()
    page.locator("//button[@aria-label='Close popup']").click()
    page.locator("//img[@id='profile-click-icon']").click()
    page.locator("//div[contains(text(),'Log out')]").click()



    expect(login).to_be_visible(), "Login button not visible"

    assert page.url=="https://www.zenclass.in/login", "Logout button validation failed"



