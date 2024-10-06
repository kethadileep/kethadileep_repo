import unittest
from unittest.mock import patch, Mock
from devicedata import DeviceDataProcessor

class TestDeviceDataProcessor(unittest.TestCase):

    @patch('devicedata.requests.post')
    def test_login_success(self, mock_post):
        """Test successful login and token retrieval."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"Token": "sample_token"}
        mock_post.return_value = mock_response

        processor = DeviceDataProcessor('sandboxdnac.cisco.com', 'devnetuser', 'Cisco123!', {})
        processor.login()

        self.assertEqual(processor.token, "sample_token")
        mock_post.assert_called_once()

    @patch('devicedata.requests.post')
    def test_login_failure(self, mock_post):
        """Test login failure scenario."""
        mock_response = Mock()
        mock_response.status_code = 401
        mock_post.return_value = mock_response

        processor = DeviceDataProcessor('sandboxdnac.cisco.com', 'devnetuser', 'wrongpassword', {})
        
        with self.assertRaises(Exception):
            processor.login()

        mock_post.assert_called_once()

    @patch('devicedata.requests.get')
    @patch('devicedata.DeviceDataProcessor.login')
    def test_get_device_data_success(self, mock_login, mock_get):
        """Test successful retrieval of device data."""
        mock_login.return_value = None  # Mock successful login

        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "response": [
                {"hostname": "device1", "macAddress": "00:1A:2B:3C:4D:5E", "managementIpAddress": "10.10.20.1"},
                {"hostname": "device2", "macAddress": "00:1A:2B:3C:4D:5F", "managementIpAddress": "10.10.20.2"}
            ]
        }
        mock_get.return_value = mock_response

        processor = DeviceDataProcessor('sandboxdnac.cisco.com', 'devnetuser', 'Cisco123!', {})
        processor.token = 'sample_token'
        device_data = processor.get_device_data()

        self.assertEqual(len(device_data["response"]), 2)
        self.assertEqual(device_data["response"][0]["hostname"], "device1")
        mock_get.assert_called_once()

    @patch('devicedata.requests.get')
    def test_get_device_data_failure(self, mock_get):
        """Test failure to retrieve device data."""
        mock_response = Mock()
        mock_response.status_code = 500
        mock_get.return_value = mock_response

        processor = DeviceDataProcessor('sandboxdnac.cisco.com', 'devnetuser', 'Cisco123!', {})
        processor.token = 'sample_token'
        
        with self.assertRaises(Exception):
            processor.get_device_data()

        mock_get.assert_called_once()

    def test_process_data(self):
        """Test the process_data function (dummy test for now)."""
        processor = DeviceDataProcessor('sandboxdnac.cisco.com', 'devnetuser', 'Cisco123!', {})
        processor.token = 'sample_token'

        # Since process_data() is not yet implemented, you can test this later.
        processor.process_data()
        self.assertTrue(True)  # Dummy assert

if __name__ == '__main__':
    unittest.main()
