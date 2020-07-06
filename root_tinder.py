from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import time
import datetime
import random


class tindabot:

    def __init__(self, total_swipes_desired=0):
        self.browser = webdriver.Chrome()
        self.total_swipes_desired = total_swipes_desired
        # self.email = email
        # self.password = password

    def log_in(self):
        self.browser.get("https://www.tinder.com")
        # WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="content"]/div/div[2]/div/div/div[1]/button')))
        self.browser.implicitly_wait(10)

        self.browser.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button').click()
        print('accepted cookies')
        self.browser.implicitly_wait(10)
        sleep(3)
        try:
            self.browser.find_element_by_xpath("//button[contains(.,'More Options')]").click()
        except:
            pass
        print('clicking to go to fb login window')
        sleep(3)
        self.browser.find_element_by_xpath("//button[@aria-label='Log in with Facebook']").click()
        print('clicked login with facebook')
        sleep(15)

    def perform_swipes(self):
        #name says it all
        t0 = time.time()
        self.browser.refresh()
        WebDriverWait(self.browser, 25).until(EC.presence_of_element_located(
            (By.XPATH, "//button[@aria-label='Like']")))
        print('probs found like button')
        count = 0
        while count < self.total_swipes_desired:
            try:
                while count < self.total_swipes_desired:
                    WebDriverWait(self.browser, 10).until(
                        EC.presence_of_element_located((By.XPATH, "//button[@aria-label='Like']")))
                    self.browser.find_element_by_xpath("//button[@aria-label='Like']").click()
                    count += 1
                    print(f'swiped: {count}')
                    rand_nums = random.uniform(1, 5)
                    sleep(rand_nums)
                    print(rand_nums)
                print(f'Totals = {count}')
            except:
                try:
                    self.browser.find_element_by_xpath('''//*[@id="modal-manager"]/div/div/div[2]/button[2]''').click()
                except:
                    sleep(8)
                    self.browser.refresh()
                    time.sleep(5)
                    WebDriverWait(self.browser, 15).until(
                        EC.presence_of_element_located((By.XPATH, "//button[@aria-label='Like']")))
        print('_' * 80)
        print('Tinder Report:>')
        print(f'Total Swipes done = {count}')

        t1 = 'Hours elapsed = ' + str((time.time() - t0) / 3600)
        print(t1)
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    def scroll_through_messages(self):
        # just scrolls through messages does nothing else. it could if you want it to
        self.browser.find_element_by_xpath("//button[@id='messages-tab']").click()
        print('clicked message')
        count = 0
        for i in range(2, 61):
            self.browser.find_element_by_xpath(f"//a[{i}]").click()
            count += 1
            print(f'clicked on message {count}')
            sleep(4)
        sleep(5)

    def derive_replied_and_non_replied_ones(self):
        # name says it all
        try:
            self.browser.find_element_by_xpath("//button[@id='messages-tab']").click()
            print('clicked message tab')
            sleep(2)
            left_box_counter = 0
            list_of_those_who_replied = []
            not_replied_names_list = []
            all_names = []
            for i in range(2, 600):
                # individual message box opening
                sleep(2)
                left_box_counter += 1
                click_scroll_through_left_box = self.browser.find_element_by_xpath(f"//a[{i}]")
                click_scroll_through_left_box.click()
                print(f'clicked on the left box= {left_box_counter}')
                sleep(2)
                try:  # her message strings if detected, her name appends to list_of_those_who_replied
                    all_her_replies = self.browser.find_element_by_xpath(
                        "//*[@class='msg BreakWord D(ib) Ta(start) Us(t) Pos(r) Whs(pw) Va(m) Maw(100%) C(#000) msg--received Op(1) Trsp($opacity) Trsdu($fast) Trsde($normal) Px(12px) Py(10px)']")
                    try:
                        all_her_replies = self.browser.find_element_by_xpath(
                            "//*[@class='msg BreakWord D(ib) Ta(start) Us(t) Pos(r) Whs(pw) Va(m) Maw(100%) C(#000) msg--received Op(1) Trsp($opacity) Trsdu($fast) Trsde($normal) Px(12px) Py(10px)']")
                        # left incomplete to work on future to extract her texts
                    except:
                        pass
                    name = self.browser.find_element_by_xpath(
                        "//a[@class='messageListItem D(f) Ai(c) Pos(r)--s BdB--s Bdbc($c-divider) focus-background-style messageListItem--active']//div[2]//div[1]//div[1]//h3[1]")
                    her_name_from_left_active_box = name.get_attribute('textContent')
                    list_of_those_who_replied.append(her_name_from_left_active_box)
                    print(f'{her_name_from_left_active_box} is appended to ones who replied')
                    print(f'replied ones in list:{list_of_those_who_replied}')
                    sleep(1)
                except:  # her message strings when not detected, her name appends to not_replied_ones_list
                    try:
                        name = self.browser.find_element_by_xpath(
                            "//a[@class='messageListItem D(f) Ai(c) Pos(r)--s BdB--s Bdbc($c-divider) focus-background-style messageListItem--active']//div[2]//div[1]//div[1]//h3[1]")
                        her_name_from_left_active_box = name.get_attribute('textContent')
                        not_replied_names_list.append(her_name_from_left_active_box)
                        print(f'name of non replied person:{her_name_from_left_active_box}')
                        print(f'non replied ones in list form:{not_replied_names_list}')
                        sleep(1)
                    except:
                        print('Error zXCES')

                name = self.browser.find_element_by_xpath(
                    "//a[@class='messageListItem D(f) Ai(c) Pos(r)--s BdB--s Bdbc($c-divider) focus-background-style messageListItem--active']//div[2]//div[1]//div[1]//h3[1]")
                her_name_from_left_active_box = name.get_attribute('textContent')
                all_names.append(her_name_from_left_active_box)
                print(f'all_names in list= {all_names}')
                sleep(1)
        except:
            pass

        print(f'final_all_names_list = {all_names}')
        print(f'final_list_of_those_who_replied {list_of_those_who_replied}')
        print(f'final_not_replied_names_list{not_replied_names_list}')
        sleep(4)

    def send_new_message_to_new_matches(self):
        count = 0
        all_message_greets = ['hello you there!, how are you doing today?', 'hello there! how you doin today?',
                              'hey you! how are you doing today?', 'ey hey!how are you doin today?']
        self.browser.get("https://www.tinder.com")
        sleep(4)
        for i in range(1, 150):
            try:
                count += 1
                try:
                    self.browser.find_element_by_xpath(
                        "//body[@class='M(0) Pos(f) Ov(h) P(0) Expand Fz($s) C($c-base) Ovsby(n)']/div[@id='content']/div[@class='App Expand Ovy(a) Ovx(h) animation-fade-in-out-enter-done']/div[@class='App__body H(100%) Pos(r) Z(0)']/div[@class='D(f) Fld(r) Flx($flx1) H(100%) desktop Ov(h)']/aside[@class='H(100%) Fld(c) Pos(r) Fxg(0) Fxs(0) Flxb(25%) Miw(325px) Maw(375px)']/nav[@class='Pos(r) NetHeight(100%,$desktop-navbar-height) NetHeight(100%,$tablet-navbar-height)--m']/div[@class='H(100%)']/div[@class='H(100%)']/div[@class='D(f) Flx($flx1) Fld(c) H(100%) Z(0) Bgc(#fff)']/div[@class='D(f)']/div[@id='matchListNoMessages']/div[1]/div[1]/a[1]/div[1]").click()
                except:
                    self.browser.find_element_by_xpath(
                        "//body[@class='M(0) Pos(f) Ov(h) P(0) Expand Fz($s) C($c-base) Ovsby(n)']/div[@id='content']/div[@class='App Expand Ovy(a) Ovx(h) animation-fade-in-out-enter-done']/div[@class='App__body H(100%) Pos(r) Z(0)']/div[@class='D(f) Fld(r) Flx($flx1) H(100%) desktop Ov(h) desktop--recs']/aside[@class='H(100%) Fld(c) Pos(r) Fxg(0) Fxs(0) Flxb(25%) Miw(325px) Maw(375px)']/nav[@class='Pos(r) NetHeight(100%,$desktop-navbar-height) NetHeight(100%,$tablet-navbar-height)--m']/div[@class='H(100%)']/div[@class='H(100%)']/div[@class='D(f) Flx($flx1) Fld(c) H(100%) Z(0) Bgc(#fff)']/div[@class='D(f)']/div[@id='matchListNoMessages']/div[1]/div[1]/a[1]/div[1]").click()
                print(f'counter = {count}')
                sleep(1)
                r_num = random.randint(0, 3)
                self.browser.find_element_by_id('chat-text-area').send_keys(all_message_greets[r_num])
                self.browser.find_element_by_id('chat-text-area').send_keys(Keys.ENTER)
                print('sent message')
                sleep(5)
                self.browser.find_element_by_xpath("//button[@id='match-tab']").click()
                sleep(5)
            except:
                print(f'something wrong or run out of matches card. Totals done = {count}')
                break


"""

# use it without class
totals_desired = 0

t0 = time.time()


total_swipes_desired = random.randint(totals_desired -2,totals_desired + 2)

browser = webdriver.Chrome()
go_to_tinder_url = "https://www.tinder.com"

browser.get(go_to_tinder_url)
print('Accessing URL...')

time.sleep(3)
# accept cookies
browser.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button').click()

print('Accepted cookies, now clicking more options')
time.sleep(3)

t1 = time.time() - t0
print(t1)
#click more options
try:
    browser.find_element_by_xpath("//button[contains(.,'More Options')]").click()
except:
    pass
print('clicking to go to fb login window')
time.sleep(3)
WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@aria-label='Log in with Facebook']")))
browser.find_element_by_xpath("//button[@aria-label='Log in with Facebook']").click()

time.sleep(15)

WebDriverWait(browser, 25).until(EC.presence_of_element_located((By.XPATH, "//button[@aria-label='Like']")))
print('probs found like button')
count = 0
while count < total_swipes_desired:
    try:
        while count < total_swipes_desired:
            WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@aria-label='Like']")))
            browser.find_element_by_xpath("//button[@aria-label='Like']").click()
            count += 1
            print(f'swiped: {count}')
            rand_nums = random.uniform(1, 5)
            time.sleep(rand_nums)
            print(rand_nums)
        print(f'Totals = {count}')
    except:
        try:
            browser.find_element_by_xpath('''//*[@id="modal-manager"]/div/div/div[2]/button[2]''').click()
        except:
            time.sleep(8)
            browser.refresh()
            time.sleep(5)
            WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, "//button[@aria-label='Like']")))

print('_' * 80)
print('Tinder Report:>')
print(f'Total Swipes done = {count}')

t2 = 'Hours elapsed = '+ str((time.time() - t0) / 3600)

print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

print(t2)
"""
