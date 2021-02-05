# sample code for reading data from different sources

# read csv
# use low_memory in case of large files. Do check datatypes in that case.
df_scan = pd.read_csv(filename, sep=';', decimal=",", header=None, low_memory=False, parse_dates=['date column']) 


# read json data into pandas dataframe
import pandas as pd
import urllib.request
import json

with urllib.request.urlopen(url) as file:
    a = json.loads(file.read())
    df = pd.DataFrame.from_dict(a)

    
# read html 
# use sheet_name=None for all sheets
df = pd.read_html('http://url.html',skiprows=4, header=0, decimal=',', thousands='.')

# read excel
def read_data(file, sheet):
    '''
    :param file: filename including path
    :param sheet: sheetname
    :return: dataframe
    '''
    try:
    	xls = pd.ExcelFile(file)
    	df = pd.read_excel(xls, sheet_name=sheet)
    except:
	print(‘file not found’)

    return df

# read SQL
engine="mssql://<server>/<database name>?trusted_connection=yes;driver=SQL+Server"
qry = "select column from table"
df = pd.read_sql_query(qry, con=engine, parse_dates=None)

# read SQL
import pyodbc
import pandas as pd

conn = pyodbc.connect(
    r'DRIVER={SQL Server};'
    r'SERVER=<servername>;'
    r'DATABASE=<databasename>;'
    r'Trusted_Connection=yes;')

sql = "SELECT * FROM <table>"

df = pd.read_sql(sql, conn)

# read XML
# also look at beautiful soup for reading XML!!
from pathlib import Path
import xml.etree.cElementTree as et

file = Path(r'filepath\filename.xml')
fund_data = et.parse(file)
root = fund_data.getroot()
# get all xml tags
list = [elem.tag for elem in root.iter()]
# get unique xml tags
set(list)

# read from clipboard
# copy from excel then ->
pd.read_clipboard()

# read dictionairy from config file
# config file
[GROUP]
dict = {'level_1': {'item1': 'item'}, 'level_2': {'item1': 'item'}}
# python file
import ast  # for parsing string to dictionairy
file_dict = ast.literal_eval(config['GROUP']['dict'])





