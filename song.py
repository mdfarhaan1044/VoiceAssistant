from selenium import webdriver

class music():
    def __init__(self):
        self.driver=webdriver.Firefox()

    def playing(self,query):
        self.query = query 
        # self.driver.get(url="https://www.saregama.com/search/song?s=" + query)
        # s = self.driver.find_element("xpath",'//*[@id="liDataLi0"]/div[1]/a/img')
        self.driver.get(url="https://www.jiosaavn.com/search/song/" + query)
        s = self.driver.find_element("xpath",'//*[@id="root"]/div[2]/div[1]/div/main/div/div/section/ol/li[1]/div/article/div[2]/figure/figcaption/h4/a')
        s.click()
   
        song=self.driver.find_element("xpath",'/html/body/div[1]/div[2]/div[1]/div/main/div[2]/figure')
        song.click()
        
        

assist=music()
assist.playing('kesariya')