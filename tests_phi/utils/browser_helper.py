from selenpy.support import browser


def get_page_title():
    return browser.get_driver().title
    
    
def get_alert_text():
    return browser.get_alert().text
    
    
def dismiss_alert():
    browser.close_alert()
