import json
import unittest
from RestClient import RestClient
from ConfigManager import ConfigManager
from Response_from_API import Response_from_API


class TestNLU_ConfigureOutlook(unittest.TestCase):
    """"
        To Test the 'ConfigureOutlook' intent
    """
    restClient = RestClient()
    expectedIntent = "OUTLOOK-CONFIGURE"
    expectedEntity = "configtype"
    url = ConfigManager.nlu_url
    resposne_instance = Response_from_API()

    def test_NLUBot_CONFIGURE_OUTLOOOK1(self):
        input_request = "Please configure outlook in my laptop remotely"
        data = json.dumps(self.resposne_instance.input_value_json_nlu(input_request,"Outlook"))
        actual_response = TestNLU_ConfigureOutlook.restClient.post(self.url, data)
        self.assertEquals(actual_response["intent"], TestNLU_ConfigureOutlook.expectedIntent)
        self.assertEquals(actual_response["entities"][0]['entity'],TestNLU_ConfigureOutlook.expectedEntity)

    def test_NLUBot_CONFIGURE_OUTLOOOK2(self):
        input_request = "Configure Microsoft Outlook"
        data = json.dumps(self.resposne_instance.input_value_json_nlu(input_request,"Outlook"))
        actual_response = TestNLU_ConfigureOutlook.restClient.post(self.url, data)
        self.assertEquals(actual_response["intent"], TestNLU_ConfigureOutlook.expectedIntent)
        self.assertEquals(actual_response["entities"][0]['entity'],TestNLU_ConfigureOutlook.expectedEntity)

    def test_NLUBot_CONFIGURE_OUTLOOOK3(self):
        input_request = "Need to add PST in my outlook account"
        data = json.dumps(self.resposne_instance.input_value_json_nlu(input_request, "Outlook"))
        expectedEntityValue = "PST"
        actual_response = TestNLU_ConfigureOutlook.restClient.post(self.url, data)
        self.assertEquals(actual_response["intent"], TestNLU_ConfigureOutlook.expectedIntent)
        self.assertEquals(actual_response["entities"][0]['entity'], TestNLU_ConfigureOutlook.expectedEntity)
        self.assertEquals(actual_response["entities"][0]['value'], expectedEntityValue)

    def test_NLUBot_CONFIGURE_OUTLOOOK4(self):
        input_request = "Configure new PST in my outlook"
        data = json.dumps(self.resposne_instance.input_value_json_nlu(input_request, "Outlook"))
        expectedEntityValue = "PST"
        actual_response = TestNLU_ConfigureOutlook.restClient.post(self.url, data)
        self.assertEquals(actual_response["intent"], TestNLU_ConfigureOutlook.expectedIntent)
        self.assertEquals(actual_response["entities"][0]['entity'], TestNLU_ConfigureOutlook.expectedEntity)
        self.assertEquals(actual_response["entities"][0]['value'], expectedEntityValue)

    def test_NLUBot_CONFIGURE_OUTLOOOK5(self):
        input_request = "I need to get the outlook configured in my machine"
        data = json.dumps(self.resposne_instance.input_value_json_nlu(input_request, "Outlook"))
        actual_response = TestNLU_ConfigureOutlook.restClient.post(self.url, data)
        self.assertEquals(actual_response["intent"], TestNLU_ConfigureOutlook.expectedIntent)
        self.assertEquals(actual_response["entities"][0]['entity'], TestNLU_ConfigureOutlook.expectedEntity)

suite = unittest.TestLoader().loadTestsFromTestCase(TestNLU_ConfigureOutlook)
unittest.TextTestRunner(verbosity=2).run(suite)