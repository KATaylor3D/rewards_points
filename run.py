from selenium import webdriver
from selenium.webdriver import ChromeOptions
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
        self.bot = webdriver.Edge(EdgeChromiumDriverManager().install())
        self.email, self.password = get_credentials()

    def pcSearchPoints(self):
        bot = self.bot
        login_url = 'https://login.live.com/login.srf'
        search_url = 'https://www.bing.com/'
        bot.get(login_url)
        wait()
        bot.find_element_by_id('i0116').send_keys(self.email + enter)
        wait()
        bot.find_element_by_id('i0118').send_keys(self.password)
        wait()
        bot.find_element_by_id('idChkBx_PWD_KMSI0Pwd').click()
        wait()
        bot.find_element_by_id('idSIButton9').click()
        wait()
        bot.get(search_url)
        wait()
        bot.find_element_by_id('id_s').click()
        for i in range(0,35):
            wait()
            bot.find_element_by_id('sb_form_q').send_keys((backspace * 14) + random_string(14) + enter)

    def dailySet(self):
        pass

        
def main():
    alfred = PointsBot()
    alfred.pcSearchPoints()

if __name__ == '__main__':
    main()