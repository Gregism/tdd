from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(LiveServerTestCase):
  def setUp(self):
    self.browser = webdriver.Firefox()
    self.browser.implicitly_wait(3)

  def tearDown(self):
    self.browser.quit()

  def check_for_row_in_list(self, row_text):
    table = self.browser.find_element_by_id('id_list_table')
    rows = table.find_elements_by_tag_name('tr')
    self.assertIn(row_text,[row.text for row in rows])

  def test_can_start_list_and_retreive_later(self):


    # Go to the homepage
    self.browser.get(self.live_server_url)

    self.assertIn('To-Do',self.browser.title)
    header_text = self.browser.find_element_by_tag_name('h1').text
    self.assertIn('To-Do', header_text)

    #Invitation to enter a to-do item
    inputbox = self.browser.find_element_by_id('id_new_item')
    self.assertEqual(
      inputbox.get_attribute('placeholder'),
      'Enter a to-do item'
    )

    #Type "Learn Linux"
    inputbox.send_keys('Learn Linux')
    inputbox.send_keys(Keys.ENTER)

    gregs_list_url = self.browser.current_url
    self.assertRegex(gregs_list_url, '/lists/.+')
    #after hitting enter the page lists
    # "1: Learn Linux"
    #time.sleep(10)
    self.check_for_row_in_list('1: Learn Linux')
    
    

    #There is a box to enter anothr to-do item
    #Enter: "Figure out what DevOps is"
    #Type "Learn Linux"
    #inputbox = self.browser.find_element_by_id('id_new_item')
    inputbox = self.browser.find_element_by_id('id_new_item')
    inputbox.send_keys('Figure out what DevOps is')
    inputbox.send_keys(Keys.ENTER)
    
    
    #Page updates, shows both items
    #table = self.browser.find_element_by_id('id_list_table')
    self.check_for_row_in_list('1: Learn Linux')
    self.check_for_row_in_list('2: Figure out what DevOps is')
    self.browser.quit()
    self.browser = webdriver.Firefox()
    
    self.browser.get(self.live_server_url)
    page_text = self.browser.find_element_by_tag_name('body').text
    self.assertNotIn('Learn Linux', page_text)
    self.assertNotIn('Figure out what DevOps is', page_text)

    inputbox = self.browser.find_element_by_id('id_new_item')
    inputbox.send_keys('Learn more')
    inputbox.send_keys(Keys.ENTER)

    self.assertNotIn('Learn Linux', page_text)
    self.assertIn('Learn more', page_text)

