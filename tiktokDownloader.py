from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
class TikTok():
    def __init__(self):
        self.options = webdriver.FirefoxOptions()
        self.options.add_argument('--headless')
        self.options.headless = False
        self.driver = webdriver.Firefox(options=self.options)
        self.driver.get('https://www.tiktok.com/')
    def account_parse(self, account):
        print('Скрипт успішно запущено! Скачування почнеться через 300 секунд(5 хв.).')
        with open('links.txt', 'w') as file:
                file.write('')
        url = 'https://www.tiktok.com/' + '@' + account
        self.driver.get(url)
        html = self.driver.find_element(By.TAG_NAME, 'html')
        for i in range(100):
            html.send_keys(Keys.END)
            time.sleep(3)
        soup = BeautifulSoup(self.driver.page_source, 'lxml')
        links_div = soup.find_all(class_='tiktok-yz6ijl-DivWrapper e1cg0wnj1')
        for link_div in links_div:
            link = link_div.find('a')
            url = link.get('href')
            print(url)
            with open('links.txt', 'a') as file:
                file.write(url + f'\n')
    def download(self):
        with open('links.txt', 'r') as file:
            urls = file.readlines()
            print('Скачування почалося! Всі відео будуть скачані в папку "Завантаження".')
        for url in urls:
            try:
                self.driver.get('https://snaptik.app/en')
                input_tik_tok_url = self.driver.find_element(By.ID, 'url')
                input_tik_tok_url.click()
                time.sleep(1)
                input_tik_tok_url.send_keys(url)
                time.sleep(1)
                download1 = self.driver.find_element(By.XPATH, '/html/body/main/div[1]/div/div[2]/form/div/div[4]/button')
                download1.click()
                time.sleep(4)
                download = self.driver.find_element(By.XPATH, '/html/body/main/div[2]/div/div/div[2]/div/a[1]')
                download.click()
                time.sleep(5)
            except Exception as ex:
                print(ex)
    def exit(self):
        time.sleep(10)
        self.driver.close()
        self.driver.quit()
def main():
    try:
        print("Дякую за покупку софта, покищо це рання версія, тому можуть бути баги. Мій телеграм для зв'язку: @wztpw")
        account = input("Введіть ім'я аккаунта: ")
        driver = TikTok()
        driver.account_parse(account=account)
        driver.download()
        driver.exit()
    except Exception as ex:
        print(ex)
        driver.exit()
if __name__ == '__main__':
    main()
