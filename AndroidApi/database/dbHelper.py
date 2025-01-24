import os
import pyodbc, struct
from azure import identity

class dbHelper:
    def __init__(self):
        #self.connectionString = "Driver={ODBC Driver 17 for SQL Server};Server=tcp:bakerstreetcreates-q.database.windows.net,1433;Database=AndroidApp;UID=bakerstreetadmin;PWD=Elijah0504;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30"
        self.connectionString = "Driver={ODBC Driver 17 for SQL Server};Server=tcp:bakerstreetcreates-q.database.windows.net,1433;Database=AndroidApp;UID=bakerstreetadmin;PWD=Elijah0504;Connection Timeout=30"


    def get_conn(self):
        #credential = identity.DefaultAzureCredential(exclude_interactive_browser_credential=False)
        #token_bytes = credential.get_token("https://database.windows.net/.default").token.encode("UTF-16-LE")
        #token_struct = struct.pack(f'<I{len(token_bytes)}s', len(token_bytes), token_bytes)
        #SQL_COPT_SS_ACCESS_TOKEN = 1256  # This connection option is defined by microsoft in msodbcsql.h
        #conn = pyodbc.connect(self.connectionString, attrs_before={SQL_COPT_SS_ACCESS_TOKEN: token_struct})
        conn = pyodbc.connect(self.connectionString)
        return conn