from utilities.customLogger import LogGen
from utilities.outlookUtilis import *

from pywinauto.application import Application
import win32com.client
#other libraries to be used in this script
import os
from datetime import datetime, timedelta


class TestOutlook:

    def test_100_outlook_test(self):
        outlook = win32com.client.Dispatch('outlook.application')
        # mapi = outlook.GetNamespace("MAPI")
        # for account in mapi.Accounts:
        #     print(account.DeliveryStore.DisplayName)
        #
        # inbox = mapi.GetDefaultFolder(6)
        # messages = inbox.Items
        # mail = messages.getLast()
        # print(mail)
        # launch_outlook()
        # subject = "Jenkins Bot"
        # duration = 0
        # found = False
        # outlook = win32com.client.Dispatch("Outlook.Application").GetNameSpace("MAPI")
        # inbox = outlook.GetDefaultFolder(6)
        # duration += 1
        # messages = inbox.Items
        # print(messages)
        # messages.Sort("[ReceivedTime]", True)
        # for message in messages:
        #     actual_subject = message.Subject
        #     if subject == actual_subject:
        #         found = True
        #         print(message)
        #         message.UnRead = False
        #         # message.Delete()
        #         break
        # return found

    #outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")


        #inbox = outlook.GetDefaultFolder(6)  # "6" refers to the index of a folder - in this case,
        # the inbox. You can change that number to reference
        # any other folder

        # messages = inbox.Items
        # received_dt = datetime.now() - timedelta(days=1)
        # received_dt = received_dt.strftime('%m/%d/%Y %H:%M %p')
        # messages = messages.Restrict("[ReceivedTime] >= '" + received_dt + "'")
        # messages = messages.Restrict("[SenderEmailAddress] = 'venugopal.venkatesha@daimler.com'")
        # messages = messages.Restrict("[Subject] = 'Jenkins Bot'")
        # message = messages.GetLast()
        # body_content = message.body
        # print(body_content)
#         launch_outlook()
# #         to = "venugopal.venkatesha@daimler.com"
# #         subject = "Outlook Automation Test"
# #         body = "Automation Test Pass"
# #
#         mail = check_for_v7_email_in_outlook("V7_Test_Automation ")
#         print(mail)

        #app = Application().start("notepad.exe")