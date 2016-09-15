from selenium import webdriver
import unittest

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
    header_text = self.browser.find_element_by_tag_name('h1')
    self.asserIn('To-Do', header_text)

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

    table = self.browser.find_element_by_id('id_list_table')
    rows = table.find_elements_by_tag_name('tr')
    self.assertTrue(
      any(row.text == '1: Learn Linux' for row in rows)
    )
    self.fail('Finish the test!')

    #There is a box to enter anothr to-do item
    #Enter: "Figure out what DevOps is"

    #Page updates, shows both items
    #site generates unique url

    #visit url see your list

if __name__ == '__main__':
  unittest.main(warnings='ignore')