import json
import unittest
from RestClient import RestClient
from ConfigManager import ConfigManager
from Response_from_API import Response_from_API


class TestNLU_BrowserInternetoutage(unittest.TestCase):
    """"
        To Test the 'BrowserInternetoutrange' intent
    """
    restClient = RestClient()
    expectedIntent = "BROWSER-INTERNETOUTAGE"
    input_request = ["Internet is not working in my laptop.","Internet is very slow.","I do not have internet access. Please help",
                     "LAN cable is connected, but there is no internet access","I am unable to connect to google or myWipro, please help to fix this issue."]
    url = ConfigManager.nlu_url
    resposne_instance = Response_from_API()

    def test_NLUBot_BROWSER_INTERNETOUTAGE1(self):
        data = json.dumps(self.resposne_instance.input_value_json_nlu(self.input_request[0],"Browser"))
        actual_response = TestNLU_BrowserInternetoutage.restClient.post(self.url, data)
        self.assertEquals(actual_response["intent"], TestNLU_BrowserInternetoutage.expectedIntent)

    def test_NLUBot_BROWSER_INTERNETOUTAGE2(self):
        data = json.dumps(self.resposne_instance.input_value_json_nlu(self.input_request[1],"Browser"))
        actual_response = TestNLU_BrowserInternetoutage.restClient.post(self.url, data)
        self.assertEquals(actual_response["intent"], TestNLU_BrowserInternetoutage.expectedIntent)

    def test_NLUBot_BROWSER_INTERNETOUTAGE3(self):
        data = json.dumps(self.resposne_instance.input_value_json_nlu(self.input_request[2],"Browser"))
        actual_response = TestNLU_BrowserInternetoutage.restClient.post(self.url, data)
        self.assertEquals(actual_response["intent"], TestNLU_BrowserInternetoutage.expectedIntent)

    def test_NLUBot_BROWSER_INTERNETOUTAGE4(self):
        data = json.dumps(self.resposne_instance.input_value_json_nlu(self.input_request[3],"Browser"))
        actual_response = TestNLU_BrowserInternetoutage.restClient.post(self.url, data)
        self.assertEquals(actual_response["intent"], TestNLU_BrowserInternetoutage.expectedIntent)

    def test_NLUBot_BROWSER_INTERNETOUTAGE5(self):
        data = json.dumps(self.resposne_instance.input_value_json_nlu(self.input_request[4],"Browser"))
        actual_response = TestNLU_BrowserInternetoutage.restClient.post(self.url, data)
        self.assertEquals(actual_response["intent"], TestNLU_BrowserInternetoutage.expectedIntent)
suite = unittest.TestLoader().loadTestsFromTestCase(TestNLU_BrowserInternetoutage)
unittest.TextTestRunner(verbosity=2).run(suite)