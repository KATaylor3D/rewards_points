from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from time import sleep
from stringgenerator import random_string


enter = '\n'
wait = lambda: sleep(3)
backspace = '\b'

def get_credentials():
    with open('creds.txt', 'r') as file:
        content = file.read()
        email, password = content.split(',')
    return email, password


class PointsBot:

    def __init__(self):
        self.email, self.password = get_credentials()
        self.bot = webdriver.Edge(EdgeChromiumDriverManager().install())

        # Login
        self.bot.get('https://login.live.com/login.srf')
        wait()
        self.bot.find_element_by_id('i0116').send_keys(self.email + enter)
        wait()
        self.bot.find_element_by_id('i0118').send_keys(self.password + enter)
        wait()

        # Set points
        self.bot.get('https://account.microsoft.com/rewards/')
        self.points = self.bot.find_element_by_xpath('//*[@id="userBanner"]/mee-banner/div/div/div/div[2]/div[1]/mee-banner-slot-2/mee-rewards-user-status-item/mee-rewards-user-status-balance/div/div/div/div/div/p[1]/mee-rewards-counter-animation/span').text

    def updatePoints(self):
        self.bot.get('https://account.microsoft.com/rewards/')
        self.points = self.bot.find_element_by_xpath('//*[@id="userBanner"]/mee-banner/div/div/div/div[2]/div[1]/mee-banner-slot-2/mee-rewards-user-status-item/mee-rewards-user-status-balance/div/div/div/div/div/p[1]/mee-rewards-counter-animation/span').text
        return self.points

    def pcSearchPoints(self):
        previous_points = -1
        current_points = self.points
        while previous_points != current_points:
            self.bot.get('https://www.bing.com/')
            wait()
            print(current_points)
            previous_points = current_points
            active = self.bot.find_element_by_id('id_s').get_attribute('aria-hidden')
            if not active:
                self.bot.find_element_by_id('id_s').click()
            self.bot.find_element_by_id('sb_form_q').send_keys((backspace * 14) + random_string(14) + enter)
            current_points = self.updatePoints()

    def dailySet(self):
        pass

        
def main():
    alfred = PointsBot()
    alfred.pcSearchPoints()

if __name__ == '__main__':
    main()