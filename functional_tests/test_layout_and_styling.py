from .base import FunctionalTest

class LayoutAndStylingTest(FunctionalTest):
  def test_layout_and_styling(self):
    # Head to the homepage
    self.browser.get(self.server_url)
    self.browser.set_window_size(1024,768)

    # Notice a nice centered input bx
    inputbox = self.browser.find_element_by_id('id_new_item')
    self.assertAlmostEqual(
      inputbox.location['x'] + inputbox.size['width'] / 2,
      512,
      delta=5
    )
    # Start a new list input should be centered there as well
    inputbox.send_keys('testing\n')
    inputbox = self.browser.find_element_by_id('id_new_item')
    self.assertAlmostEqual(
      inputbox.location['x'] + inputbox.size['width'] / 2,
      512,
      delta=5
    )