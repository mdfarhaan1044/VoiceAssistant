from selenium import webdriver

class information():
    def __init__(self):
        self.driver=webdriver.Firefox()

    def get_info(self,query):
        self.query=query
        self.driver.get(url="https://www.wikipedia.org")
        search = self.driver.find_element("xpath",'//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)
        enter = self.driver.find_element("xpath",'/html/body/main/div[2]/form/fieldset/button')
        enter.click()

        
        

        # assist=information()
        # assist.get_info('Genshin Impact')


