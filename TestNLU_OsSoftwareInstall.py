import json
import unittest

from Response_from_API import Response_from_API
from RestClient import RestClient
from ConfigManager import ConfigManager


class TestNLU_OsSoftwareInstall(unittest.TestCase):
    """"
        To Test the 'OsSoftwareInstall' intent
    """
    restClient = RestClient()
    expectedIntent = "SOFTWARE-INSTALL"
    expectedEntity = "softwareName"
    url = ConfigManager.nlu_url
    resposne_instance = Response_from_API()


    def test_NLUBot_OS_SOFTWAREINSTALL1(self):
        input_request = "Install 7zip Software in my laptop."
        data = json.dumps(self.resposne_instance.input_value_json_nlu(input_request, "Software"))
        expectedEntityValue = "7zip"
        actual_response = TestNLU_OsSoftwareInstall.restClient.post(self.url, data)
        self.assertEquals(actual_response["intent"], TestNLU_OsSoftwareInstall.expectedIntent)
        self.assertEquals(actual_response["entities"][0]['entity'], TestNLU_OsSoftwareInstall.expectedEntity)
        self.assertEquals(actual_response["entities"][0]['value'], expectedEntityValue)

    def test_NLUBot_OS_SOFTWAREINSTALL2(self):
        input_request = "I need a software to compress files."
        data = json.dumps(self.resposne_instance.input_value_json_nlu(input_request, "Software"))
        expectedEntityValue = "7zip"
        actual_response = TestNLU_OsSoftwareInstall.restClient.post(self.url, data)
        self.assertEquals(actual_response["intent"], TestNLU_OsSoftwareInstall.expectedIntent)
        self.assertEquals(actual_response["entities"][0]['entity'], TestNLU_OsSoftwareInstall.expectedEntity)
        self.assertEquals(actual_response["entities"][0]['value'], expectedEntityValue)

    def test_NLUBot_OS_SOFTWAREINSTALL3(self):
        input_request = "Configure 7zip Software on my machine."
        data = json.dumps(self.resposne_instance.input_value_json_nlu(input_request, "Software"))
        expectedEntityValue = "7zip"
        actual_response = TestNLU_OsSoftwareInstall.restClient.post(self.url, data)
        self.assertEquals(actual_response["intent"], TestNLU_OsSoftwareInstall.expectedIntent)
        self.assertEquals(actual_response["entities"][0]['entity'], TestNLU_OsSoftwareInstall.expectedEntity)
        self.assertEquals(actual_response["entities"][0]['value'], expectedEntityValue)

    def test_NLUBot_OS_SOFTWAREINSTALL4(self):
        input_request = "I want to install Microsoft office software."
        data = json.dumps(self.resposne_instance.input_value_json_nlu(input_request, "Software"))
        expectedEntityValue = "msoffice"
        actual_response = TestNLU_OsSoftwareInstall.restClient.post(self.url, data)
        self.assertEquals(actual_response["intent"], TestNLU_OsSoftwareInstall.expectedIntent)
        self.assertEquals(actual_response["entities"][0]['entity'], TestNLU_OsSoftwareInstall.expectedEntity)
        self.assertEquals(actual_response["entities"][0]['value'], expectedEntityValue)

    def test_NLUBot_OS_SOFTWAREINSTALL5(self):
        input_request = "Please install a software to decompress files."
        data = json.dumps(self.resposne_instance.input_value_json_nlu(input_request, "Software"))
        expectedEntityValue = "7zip"
        actual_response = TestNLU_OsSoftwareInstall.restClient.post(self.url, data)
        self.assertEquals(actual_response["intent"], TestNLU_OsSoftwareInstall.expectedIntent)
        self.assertEquals(actual_response["entities"][0]['entity'], TestNLU_OsSoftwareInstall.expectedEntity)
        self.assertEquals(actual_response["entities"][0]['value'], expectedEntityValue)

suite = unittest.TestLoader().loadTestsFromTestCase(TestNLU_OsSoftwareInstall)
unittest.TextTestRunner(verbosity=2).run(suite)
