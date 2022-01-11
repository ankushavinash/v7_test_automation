from utilities.customLogger import LogGen
from utilities.outlookUtilis import *

from pywinauto.application import Application
import win32com.client
#other libraries to be used in this script
import os
from datetime import datetime, timedelta


class TestOutlook:

    def test_099_outlook_test(self):
        outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

        inbox = outlook.GetDefaultFolder(6)  # "6" refers to the index of a folder - in this case,
        # the inbox. You can change that number to reference
        # any other folder
        messages = inbox.Items
        message = messages.GetLast()
        body_content = message.body
        print(body_content)
#         launch_outlook()
# #         to = "venugopal.venkatesha@daimler.com"
# #         subject = "Outlook Automation Test"
# #         body = "Automation Test Pass"
# #
#         mail = check_for_v7_email_in_outlook("V7_Test_Automation ")
#         print(mail)

        #app = Application().start("notepad.exe")