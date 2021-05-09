import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import json
from messege_sets import AllDms


class FBLOGIN():

    # todo : FIRST A FUNCTION THAT ILL LOGIN FACEBOOK and at the end make instace varibles output with input function
    def __init__(self, email='melodiesceo@gmail.com', pw='iamahero', url='https://www.facebook.com/groups/dropifyhsd',
                 path="./geckodriver", saved='https://www.facebook.com/saved/?list_id=188792389611581'):
        self.driver = webdriver.Firefox(executable_path=path)
        self.email = email
        self.password = pw
        self.url = url
        self.saved = saved
        self.maximum_text = 0
        self.login()

    def login(self):
        # todo : login facebook
        self.driver.get(url=self.url)
        sleep(5)
        email = self.driver.find_element_by_css_selector('.ipjc6fyt:nth-child(1) .ei4baabg')

        email.click()
        email.send_keys(self.email)
        sleep(3)
        password = self.driver.find_element_by_css_selector('.ipjc6fyt+ .ipjc6fyt .ei4baabg')
        password.click()
        password.send_keys(self.password)
        password.submit()
        # call the afterlogin class from here
        sleep(5)
        self.intosaved()

    def intosaved(self):

        self.driver.get(url=self.saved)
        sleep(3)
        print(
            " ..................................................................RUNNING...................................................................")
        self.savedforlater()

    def savedforlater(self):
        # TODO : OPEN THE POST INTO NEW TAB AND DELETE THE POST
        try:
            sleep(3)
            post = self.driver.find_element_by_css_selector('div.knvmm38d:nth-child(2) > a:nth-child(1)')
            post_link = post.get_attribute('href')
            # todo : after getting the link just delete that first post
            sleep(1)
            moreooption = self.driver.find_element_by_xpath(
                '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div/div/div/div[1]/div[3]/div')
            moreooption.click()
            sleep(4)
            self.driver.find_element_by_xpath(
                '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div/div[1]/div/div[1]/div[2]/div/div/span').click()
            sleep(1)
            self.driver.get(post_link)
        except Exception as e:
            print('no saved post found')
            sleep(3000)
            self.savedforlater()

        self.likechecker()

    def likechecker(self):
        # TODO : OPEN THE likes
        sleep(4)
        self.driver.find_element_by_css_selector('.ja2t1vim .pcp91wgn').click()
        sleep(3)
        self.down_scroller()

    def down_scroller(self):
        # todo : scroll down to the fullest
        t_end = time.time() + 30 * 1
        while time.time() < t_end:
            action = ActionChains(self.driver)
            action.send_keys(Keys.PAGE_DOWN).perform()
            sleep(2)
        self.id_scrapeer()

    def id_scrapeer(self):
        link = self.driver.find_elements_by_css_selector('.gpro0wi8.lrazzd5p')
        self.total_links = 0
        self.list_of_links = []
        for element in link:
            href_link = element.get_attribute('href')  # its a instance variable
            if href_link != None:
                if href_link not in self.list_of_links:
                    self.list_of_links.append(href_link)
                    self.total_links += 1

        print('total links found :', self.total_links)
        self.save_the_list()

    def save_the_list(self):
        # todo : save the list as list
        with open('listofurl.txt', 'w') as p:
            p.write(json.dumps(self.list_of_links))
            print('\n data saved ')
        self.get_to_profiles()

    def get_to_profiles(self):
        sleep(5)
        # todo : get into the profiles of peoples
        print('getting into profiles')
        with open('listofurl.txt', 'r') as e:
            list_of_links = json.loads(e.read())

        for link in list_of_links:
            if list_of_links.index(link) == self.total_links - 1:
                self.intosaved()
            sleep(1)
            self.driver.get(link)
            print('getting the url of index ', list_of_links.index(link))
            sleep(5)
            self.username = self.driver.find_element_by_css_selector('.ipjc6fyt .ihqw7lf3').text
            sleep(1)
            self.messege_click()

    def add_account(self):
        sleep(5)
        try:
            add_friend = self.driver.find_elements_by_css_selector('.a57itxjd .g0qnabr5')
            if add_friend[3].text == 'Add Friend':
                add_friend[3].click()
                print('added as friend')
                sleep(2)
                self.messege_click()


        except (Exception, NoSuchElementException) as e:
            print('going on to next account', e)

        # finally after error arrives go here :
        finally:
            try:
                add_ = self.driver.find_element_by_css_selector('.a57itxjd .g0qnabr5')
                if add_.text == 'Add Friend':
                    add_.click()
                    print('added as friend')
                    self.messege_click()

            except (Exception, NoSuchElementException) as e:
                print('going on to next account', e)

    def messege_click(self):
        # TODO : DM IF youve not texted them
        sleep(3)
        self.firstname = (self.username.split(' '))[0]
        try:
            self.message_button = self.driver.find_elements_by_css_selector('.bwm1u5wc .g0qnabr5')
            self.message_button[3].click()
            sleep(3)
            self.messege_analyser()


        except Exception as e:
            print(' ')

        finally:
            message_button = self.driver.find_element_by_css_selector('.bwm1u5wc .g0qnabr5')
            message_button.click()
            sleep(1)
            self.messege_analyser()

    def messege_analyser(self):
        # Todo : analyses if i have already sent the messege if not then sents one
        sleep(7)
        try:
            if self.driver.find_elements_by_css_selector('.odn2s2vf .ljqsnud1'):
                pass
            else:
                self.sent_the_mesege()

        except Exception as e:
            self.sent_the_mesege()

    def sent_the_mesege(self):
        try:
            sleep(8)
            text = ActionChains(self.driver)
            text.send_keys(AllDms.list_of_first_msg[AllDms.list_index], self.firstname, Keys.ENTER,
                           AllDms.list_of_dms[AllDms.list_index], Keys.ENTER).perform()

            AllDms.list_index += 1
            self.maximum_text += 1
            if AllDms.list_index == 6:
                AllDms.list_index = 0

            if self.maximum_text == AllDms.total_dms_in_an_hour:
                AllDms.total_dms_in_an_hour += AllDms.total_dms_in_an_hour
                print('...........Maximum dms completed , waiting...........')
                sleep(3350)
        except Exception as p:
            pass
        sleep(15)


# TODO : MAKE IT SLOW JUST SENT 6 MESSEGS IN AN HOUR ....AND TAKE IT TO AUTO DELETE SAVED POST WHICH HAS BEEN SCRAPED


obj = FBLOGIN()
