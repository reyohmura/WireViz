import gspread
from oauth2client.service_account import ServiceAccountCredentials 

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('get-bom-han-key.json', scope)
gc = gspread.authorize(credentials) 
SPREADSHEET_KEY = '12vwBbMYRTrVfD1Q_CP6MRMQIh_HHHl5F8UzsLQuYaJc'
wb = gc.open_by_key(SPREADSHEET_KEY)
 
ws = wb.get_worksheet(2)
print(ws)
val = ws.acell('F4')
print(val)
lst=ws.col_values(6)
print(lst)
print(len(lst))