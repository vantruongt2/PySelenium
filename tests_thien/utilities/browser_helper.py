from selenpy.support import browser

def dismiss_alert():
    browser.close_alert()

def get_alert_text():
    return browser.get_alert().text

def accept_alert():
    browser.get_alert().accept()

def get_title():
    return browser.get_driver().title
