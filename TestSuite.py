# coding=utf-8
"""
Author : TH316641
Created on : 4/5/2017 5:01 PM
"""
import unittest

from TestNLU_BrowserInternetoutage import TestNLU_BrowserInternetoutage
from TestNLU_ConfigureOutlook import TestNLU_ConfigureOutlook
from TestNLU_OsDiskcleanup import TestNLU_OsDiskCleanup
from TestNLU_OsSoftwareInstall import TestNLU_OsSoftwareInstall
from TestNLU_OsUsbconifg import TestNLU_OsUsbconfig


class TestSuite(unittest.TestCase):

    if __name__ == "__main__":
        loader = unittest.TestLoader
        module1 = TestNLU_BrowserInternetoutage.suite()
        module2 = TestNLU_ConfigureOutlook.suite()
        module3 = TestNLU_OsDiskCleanup.suite()
        module4 = TestNLU_OsSoftwareInstall.suite()
        module5 = TestNLU_OsUsbconfig.suite()
        suite = unittest.TestSuite([module1, module2,module3,module4,module5])
        unittest.TextTestRunner(verbosity=2).run(suite)

