from selenium import webdriver

class video():
    def __init__(self):
        self.driver=webdriver.Firefox()

    def play(self,query):
        self.query = query 
        self.driver.get(url="https://www.youtube.com/results?search_query=" + query)
        vid = self.driver.find_element("xpath",'//*[@id="video-title"]/yt-formatted-string')
        vid.click()


# assist=video()
# assist.play('beleiver')