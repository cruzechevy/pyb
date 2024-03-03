import unittest

def check_standard_categories(predicted_value):
    """
    Check if a predicted value falls within three standard categories.

    Args:
        predicted_value: The predicted value to check.

    Returns:
        str: The category ('low', 'medium', 'high') the value falls into.
    """
    if predicted_value < 0.25:
        return 'low'
    elif predicted_value >= 0.25 and predicted_value < 0.75:
        return 'medium'
    else:
        return 'high'

class TestStandardCategories(unittest.TestCase):

    def test_low_category(self):
        # Test value below 1
        self.assertEqual(check_standard_categories(0.25), 'low')

    def test_medium_category(self):
        # Test value between 1 and 2
        self.assertEqual(check_standard_categories(0.5), 'medium')

    def test_high_category(self):
        # Test value above or equal to 2
        self.assertEqual(check_standard_categories(0.75), 'high')

    def test_boundary_values(self):
        # Test boundary values
        self.assertEqual(check_standard_categories(1), 'medium')
        self.assertEqual(check_standard_categories(2), 'high')

if __name__ == '__main__':
    unittest.main()