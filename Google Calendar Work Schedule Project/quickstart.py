##!/usr/bin/env python2
## -*- coding: utf-8 -*-
#"""
#Created on Wed Mar  7 12:30:39 2018
#
#@author: soundpipe
#"""
#
## follow this video to create the GUI to run a windows like interface for adrianna: https://www.youtube.com/watch?v=0hN6vSSHT0I
## to read the excel spreadsheets that she is gonna load to the application: https://stackoverflow.com/questions/22169325/read-excel-file-in-python
## for learning the API for google Calendar: https://developers.google.com/google-apps/calendar/create-events
#
#
#from __future__ import print_function
#import httplib2
#import os
#
#from apiclient import discovery
#from oauth2client import client
#from oauth2client import tools
#from oauth2client.file import Storage
#
#import datetime
#
#try:
#    import argparse
#    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
#except ImportError:
#    flags = None


#
#def __init__(self):
#    super(Window, self).__init__()
#    self.setGeometry(50, 50, 500, 300)
#    self.setWindowTitle("Google Schedule Pusher")
#    self.setWindowIcon(QtGui.QIcon("SchedulerLogo.png"))
#
#    openFile = QtGui.QAction("&Open FIle", self)
#    openfile.setShortcut("Ctrl+O")
#    openFile.setStatusTip('open excel file to extract')
#    openFile.triggered.connect(self.file_open)
#
#def create_gui():
#    return
#
#
## If modifying these scopes, delete your previously saved credentials
## at ~/.credentials/calendar-python-quickstart.json
#SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
#CLIENT_SECRET_FILE = 'client_secret.json'
#APPLICATION_NAME = 'Google Calendar API Python Quickstart'
#
#
#def get_schedule_from_spreadsheet(Spreadsheetname):
#    return
#def get_credentials():
#    """Gets valid user credentials from storage.
#
#    If nothing has been stored, or if the stored credentials are invalid,
#    the OAuth2 flow is completed to obtain the new credentials.
#
#    Returns:
#        Credentials, the obtained credential.
#    """
#    home_dir = os.path.expanduser('~')
#    credential_dir = os.path.join(home_dir, '.credentials')
#    if not os.path.exists(credential_dir):
#        os.makedirs(credential_dir)
#    credential_path = os.path.join(credential_dir,
#                                   'calendar-python-quickstart.json')
#
#    store = Storage(credential_path)
#    credentials = store.get()
#    if not credentials or credentials.invalid:
#        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
#        flow.user_agent = APPLICATION_NAME
#        if flags:
#            credentials = tools.run_flow(flow, store, flags)
#        else: # Needed only for compatibility with Python 2.6
#            credentials = tools.run(flow, store)
#        print('Storing credentials to ' + credential_path)
#    return credentials
#
#def main():
#    
#    """Shows basic usage of the Google Calendar API.
#
#    Creates a Google Calendar API service object and outputs a list of the next
#    10 events on the user's calendar.
#    """
#    credentials = get_credentials()
#    http = credentials.authorize(httplib2.Http())
#    service = discovery.build('calendar', 'v3', http=http)
#
#    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
#    print('Getting the upcoming 10 events')
#    eventsResult = service.events().list(
#        calendarId='primary', timeMin=now, maxResults=10, singleEvents=True,
#        orderBy='startTime').execute()
#    events = eventsResult.get('items', [])
#
#    if not events:
#        print('No upcoming events found.')
#    for event in events:
#        start = event['start'].get('dateTime', event['start'].get('date'))
#        print(start, event['summary'])
#
#
#if __name__ == '__main__':
#    main()