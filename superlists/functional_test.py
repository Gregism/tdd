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
    self.fail('Finish the test!')
    #Invitation to enter a to-do item

    #Type "Learn Linux"

    #after hitting enter the page lists
    # "1: Learn Linux"

    #There is a box to enter anothr to-do item
    #Enter: "Figure out what DevOps is"

    #Page updates, shows both items
    #site generates unique url

    #visit url see your list

if __name__ == '__main__':
  unittest.main(warnings='ignore')