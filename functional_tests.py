from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
  def setUp(self):
      self.browser = webdriver.Firefox()
      self.browser.implicitly_wait(3)

  def tearDown(self):
    self.browser.quit()

  def test_can_start_a_list_and_retrieve_it_later(self):
    #Open a browser to our homepage
    self.browser.get('http://localhost:3333')

    #Check out how the title mentions to-do lists
    self.assertIn('To-Do', self.browser.title)
    self.fail('Finish the test!')
    # Enter a to-do

    # Type "Buy Peacock Feathers"

    # On enter, the page updates and lists 
    # "1: Buy Peacock Feathers" as a new to-do list item

    # There is still a box to add another item
    # Enter "Use Peacock Feathers to make a fly"

    # The page updates and shows both items

    # The should be a unique url to revisit to-do list

    # Visit that url see to-do list


if __name__ == '__main__':
  unittest.main(warnings='ignore')