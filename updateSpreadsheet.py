import gspread
from google.oauth2.service_account import Credentials

def authenticate_google_sheets():
      scopes = [ "https://www.googleapis.com/auth/spreadsheets" ]

      creds = Credentials.from_service_account_file("credentials.json", scopes = scopes)
      client = gspread.authorize(creds)

      sheet_id = "1QatVAVCSdSd4_im0cquljX3RjwriWKeJ3oPbb9X6cVw"
      workbook = client.open_by_key(sheet_id)
      return workbook

def UpdateLCnum(input_val):
      workbook = authenticate_google_sheets()
      sheet = workbook.get_worksheet(0)

      row = 1
      while(sheet.cell(row, 1).value!= None):
            row+=1

      sheet.update_cell(row, 1, input_val)


def UpdateLCname(input_val):
      workbook = authenticate_google_sheets()
      sheet = workbook.get_worksheet(0)

      row = 1
      while(sheet.cell(row, 2).value!= None):
            row+=1

      sheet.update_cell(row, 2, input_val)


def UpdateLCtime(inp, input_val):
      workbook = authenticate_google_sheets()
      sheet = workbook.get_worksheet(0)


      if(inp == "E" or inp == "e"):
            row = 1
            while(sheet.cell(row, 3).value!= None or sheet.cell(row, 4).value!= None or sheet.cell(row, 5).value!= None):
                  row+=1

            sheet.update_cell(row, 3, input_val)

      if(inp == "M" or inp == "m"):
            row = 1
            while(sheet.cell(row, 3).value!= None or sheet.cell(row, 4).value!= None or sheet.cell(row, 5).value!= None):
                  row+=1

            sheet.update_cell(row, 4, input_val)

      if(inp == "H" or inp == "h"):
            row = 1
            while(sheet.cell(row, 3).value != None or sheet.cell(row, 4).value!= None or sheet.cell(row, 5).value!= None):
                  row+=1
            sheet.update_cell(row, 5, input_val)


