#sito https://blog.coupler.io/python-to-google-sheets/
from __future__ import print_function
from auth import spreadsheet_service
from auth import drive_service

def create():
    spreadsheet_details = {
    'properties': {
        'title': 'Python-google-sheets-demo'
        }
    }
    sheet = spreadsheet_service.spreadsheets().create(body=spreadsheet_details,
                                    fields='spreadsheetId').execute()
    sheetId = sheet.get('spreadsheetId')
    print('Spreadsheet ID: {0}'.format(sheetId))
    permission1 = {
    'type': 'user',
    'role': 'writer',
    'emailAddress': 'godwinekuma@gmail.com'
    }
    drive_service.permissions().create(fileId=sheetId, body=permission1).execute()
    return sheetId

def read_range(range_name):
    #range_name = 'Sheet1!A2:D30'
    spreadsheet_id = '1z3wT8rCdvpG7fu67E3ROYmH0_FoLl4WD9qo2vqNMIIc'
    result = spreadsheet_service.spreadsheets().values().get(
    spreadsheetId=spreadsheet_id, range=range_name).execute()
    rows = result.get('values', [])
    #print('{0} rows retrieved.'.format(len(rows)))
    #print('{0} rows retrieved.'.format(rows))
    return rows

def write_range(range_name,values):
    spreadsheet_id = '1z3wT8rCdvpG7fu67E3ROYmH0_FoLl4WD9qo2vqNMIIc'
    #range_name = 'Sheet1!E1:F1'
    #values = read_range()
    #values=[["1","2"]]
    value_input_option = 'USER_ENTERED'
    body = {
        'values': values
    }
    result = spreadsheet_service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id, range=range_name,
        valueInputOption=value_input_option, body=body).execute()
    #print('{0} cells updated.'.format(result.get('updatedCells')))

#write_range()
#read_range()