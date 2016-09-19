from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest, time

class NewVisitorTest(unittest.TestCase):
  def setUp(self):
    self.browser = webdriver.Firefox()
    self.browser.implicitly_wait(3)

  def tearDown(self):
    self.browser.quit()

  def test_can_start_list_and_retreive_later(self):


    # Go to the homepage
    self.browser.get('http://localhost:8000')

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

    #after hitting enter the page lists
    # "1: Learn Linux"
    #time.sleep(10)

    table = self.browser.find_element_by_id('id_list_table')
    rows = table.find_elements_by_tag_name('tr')
    self.assertIn('1: Learn Linux',[row.text for row in rows])
    

    #There is a box to enter anothr to-do item
    #Enter: "Figure out what DevOps is"
    #Type "Learn Linux"
    #inputbox = self.browser.find_element_by_id('id_new_item')
    inputbox.send_keys('Figure out what DevOps is')
    inputbox.send_keys(Keys.ENTER)
    self.fail('Finish the test!')
    #Page updates, shows both items
    #table = self.browser.find_element_by_id('id_list_table')
    rows = table.find_elements_by_tag_name('tr')
    self.assertIn('1: Learn Linux',[row.text for row in rows])
    self.assertIn('2: Figure out what DevOps is',[row.text for row in rows])

    #site generates unique url

    #visit url see your list

if __name__ == '__main__':
  unittest.main(warnings='ignore')