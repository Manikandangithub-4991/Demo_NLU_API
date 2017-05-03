import json
import unittest

from Response_from_API import Response_from_API
from RestClient import RestClient
from ConfigManager import ConfigManager


class TestNLU_OsDiskCleanup(unittest.TestCase):
    """"
        To Test the 'OSDiskCleanup' intent
    """
    restClient = RestClient()
    expectedIntent = "OS-DISKCLEANUP"
    url = ConfigManager.nlu_url
    resposne_instance = Response_from_API()

    def test_NLUBot_OS_DISKCLEANUP1(self):
        input_request = "My Disk space showing as full. Please help to fix this."
        data = json.dumps(self.resposne_instance.input_value_json_nlu(input_request,"OS"))
        actual_response = TestNLU_OsDiskCleanup.restClient.post(self.url, data)
        self.assertEquals(actual_response["intent"], TestNLU_OsDiskCleanup.expectedIntent)

    def test_NLUBot_OS_DISKCLEANUP2(self):
        input_request = "My computer runs out of space."
        data = json.dumps(self.resposne_instance.input_value_json_nlu(input_request, "OS"))
        actual_response = TestNLU_OsDiskCleanup.restClient.post(self.url, data)
        self.assertEquals(actual_response["intent"], TestNLU_OsDiskCleanup.expectedIntent)

    def test_NLUBot_OS_DISKCLEANUP3(self):
        input_request = "My system is very slow due to low disk space. Please help."
        data = json.dumps(self.resposne_instance.input_value_json_nlu(input_request, "OS"))
        actual_response = TestNLU_OsDiskCleanup.restClient.post(self.url, data)
        self.assertEquals(actual_response["intent"], TestNLU_OsDiskCleanup.expectedIntent)

    def test_NLUBot_OS_DISKCLEANUP4(self):
        input_request = "Please help to clean my system."
        data = json.dumps(self.resposne_instance.input_value_json_nlu(input_request, "OS"))
        actual_response = TestNLU_OsDiskCleanup.restClient.post(self.url, data)
        self.assertEquals(actual_response["intent"], TestNLU_OsDiskCleanup.expectedIntent)

    def test_NLUBot_OS_DISKCLEANUP5(self):
        input_request = "I am getting low disk space warning. Please help"
        data = json.dumps(self.resposne_instance.input_value_json_nlu(input_request, "OS"))
        actual_response = TestNLU_OsDiskCleanup.restClient.post(self.url, data)
        self.assertEquals(actual_response["intent"], TestNLU_OsDiskCleanup.expectedIntent)

suite = unittest.TestLoader().loadTestsFromTestCase(TestNLU_OsDiskCleanup)
unittest.TextTestRunner(verbosity=2).run(suite)
