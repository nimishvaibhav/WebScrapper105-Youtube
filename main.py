from selenium import webdriver

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    browser = webdriver.Chrome('chromedriver')
    #browser.get('https://www.youtube.com/watch?v=UpolBSznWp0')
    browser.get('https://www.youtube.com/user/Apple/videos')
    browser.find_element_by_xpath('//*[@id="dismissible"]/ytd-thumbnail').click()
