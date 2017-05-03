import json
import unittest

from Response_from_API import Response_from_API
from RestClient import RestClient
from ConfigManager import ConfigManager


class TestNLU_OsUsbconfig(unittest.TestCase):
    """"
        To Test the 'USBConfig' intent
    """
    restClient = RestClient()
    expectedIntent = "OS-USBCONFIG"
    expectedEntity = "AccessType"
    url = ConfigManager.nlu_url
    resposne_instance = Response_from_API()
    input_request = ["Please provide USB read and write access.",
                     "I want to connect USB in my laptop, please provide access.",
                     "Write access required for my usb.",
                     "Configure usb in my system.",
                     "Provide read and write access for my pendrive"]
    accuracy = []
    failure_message = []
    testcase_result = []

    def test_NLUBot_OS_USBCONFIG1(self):
        failureException = ""
        try:

            data = json.dumps(self.resposne_instance.input_value_json_nlu(self.input_request[0], "OS"))
            expectedEntityValue = "read/write"
            actual_response = self.restClient.post(self.url, data)
            self.assertEquals(actual_response["intent"], self.expectedIntent,"Expecting Intent is OS-USBCONFIG")
            self.assertEquals(actual_response["entities"][0]['entity'], self.expectedEntity,"Expecting Entity is AccessType")
            self.assertEquals(actual_response["entities"][0]['value'], expectedEntityValue,"Expecting Entity Value is read and write")
        except AssertionError as error:
            failureException = error.args[0]
        finally:
            if failureException is None:
                self.testcase_result.append("Pass")
                self.failure_message.append("None")
            else:
                self.testcase_result.append("Fail")
                self.failure_message.append(failureException)

    def test_NLUBot_OS_USBCONFIG2(self):
        failureException = ""
        try:

            data = json.dumps(self.resposne_instance.input_value_json_nlu(self.input_request[1], "OS"))
            actual_response = self.restClient.post(self.url, data)
            self.assertEquals(actual_response["intent"], self.expectedIntent,"Expecting intent is OS-USBCONFIG")
            self.assertEquals(actual_response["entities"][0]['entity'], self.expectedEntity,"Expecting Entity is AccessType")
        except AssertionError as error:
            failureException = error.args[0]
        finally:
            if failureException is None:
                self.testcase_result.append("Pass")
                self.failure_message.append("None")
            else:
                self.testcase_result.append("Fail")
                self.failure_message.append(failureException)
    def test_NLUBot_OS_USBCONFIG3(self):
        failureException = ""
        try:

            data = json.dumps(self.resposne_instance.input_value_json_nlu(self.input_request[2], "OS"))
            actual_response = self.restClient.post(self.url, data)
            self.assertEquals(actual_response["intent"], self.expectedIntent,"Expecting Intent is OS-USBCONFIG")
        except AssertionError as error:
            failureException = error.args[0]
        finally:
            if failureException is None:
                self.testcase_result.append("Pass")
                self.failure_message.append("None")
            else:
                self.testcase_result.append("Fail")
                self.failure_message.append(failureException)
    def test_NLUBot_OS_USBCONFIG4(self):
        failureException = ""
        try :

            data = json.dumps(self.resposne_instance.input_value_json_nlu(self.input_request[3], "OS"))
            actual_response = self.restClient.post(self.url, data)
            self.assertEquals(actual_response["intent"], self.expectedIntent,"Expecting Intent is OS-USBCONFIG")
            self.assertEquals(actual_response["entities"][0]['entity'], self.expectedEntity,"Expecting Entity is AccessType")
        except AssertionError as error:
            failureException = error.args[0]
        finally:
            if failureException is None:
                self.testcase_result.append("Pass")
                self.failure_message.append("None")
            else:
                self.testcase_result.append("Fail")
                self.failure_message.append(failureException)

    def test_NLUBot_OS_USBCONFIG5(self):
        failureException = ""
        try:

            data = json.dumps(self.resposne_instance.input_value_json_nlu(self.input_request[4], "OS"))
            expectedEntityValue = "read/write"
            actual_response = self.restClient.post(self.url, data)
            self.assertEquals(actual_response["intent"], self.expectedIntent,"Expecting Intent is OS-USBCONFIG")
            self.assertEquals(actual_response["entities"][0]['entity'], self.expectedEntity,"Expecting Entity  is AccessType")
            self.assertEquals(actual_response["entities"][0]['value'], expectedEntityValue,"Expecting Entity Value is read and write")
        except AssertionError as error:
            failureException = error.args[0]
        finally:
            if failureException is None:
                self.testcase_result.append("Pass")
                self.failure_message.append("None")
            else:
                self.testcase_result.append("Fail")
                self.failure_message.append(failureException)

    @staticmethod
    def metadata_INTERNETOTAGE():
        return TestNLU_OsUsbconfig.expectedIntent

    @staticmethod
    def metadata_description():
        return TestNLU_OsUsbconfig.input_request

    @staticmethod
    def metadata_accuracy():
        return TestNLU_OsUsbconfig.accuracy

    @staticmethod
    def metadata_failure_message():
        return TestNLU_OsUsbconfig.failure_message

    @staticmethod
    def metadata_testcase_result():
        return TestNLU_OsUsbconfig.testcase_result

    @staticmethod
    def suite():
        return unittest.TestLoader().loadTestsFromTestCase(TestNLU_OsUsbconfig)
suite = unittest.TestLoader().loadTestsFromTestCase(TestNLU_OsUsbconfig)
unittest.TextTestRunner(verbosity=2).run(suite)