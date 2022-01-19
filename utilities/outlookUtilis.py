import time

import win32com.client
import psutil
import os


def check_for_dmp_email_in_outlook(subject):
    duration = 0
    found = False
    outlook = win32com.client.Dispatch("Outlook.Application").GetNameSpace("MAPI")
    inbox = outlook.GetDefaultFolder(6)
    duration += 1
    messages = inbox.Items
    messages.Sort("[ReceivedTime]", True)
    for message in messages:
        actual_subject = message.Subject
        if subject == actual_subject:
            found = True
            message.UnRead = False
            message.Delete()
            break
    return found


def launch_outlook():
    for p in psutil.process_iter(attrs=['pid', 'name']):
        if "OUTLOOK.EXE" in p.info['name']:
            break
    else:
        os.startfile("outlook")


def send_email_from_outlook(to, subject, body):
    outlook = win32com.client.Dispatch("Outlook.Application")
    mail = outlook.CreateItem(0)
    mail.To = to
    mail.Subject = subject
    mail.Body = body
    mail.Send()
    time.sleep(240)
