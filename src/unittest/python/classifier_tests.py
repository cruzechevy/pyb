import unittest
from unittest.mock import patch
from classifier import user_input_features

class TestClassifier(unittest.TestCase):

    @patch('classifier.st.sidebar.slider', side_effect=lambda name, min_val, max_val, default_val: default_val)
    def test_user_input_features(self, mock_slider):
        # Mocking user input for all parameters to their default values
        expected_features = {
            'sepal_length': 5.4,
            'sepal_width': 5.4,
            'petal_length': 1.4,
            'petal_width': 0.5
        }

        # Call the function
        features = user_input_features()

        # Assert the expected features
        self.assertEqual(
            {k: v[0] if isinstance(v, dict) else v for k, v in features.to_dict().items()},
            expected_features
        )

if __name__ == '__main__':
    unittest.main()