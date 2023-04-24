import pandas as pd
from assets.config import *
from create_dummies import *

df = pd.read_csv('C:\AUA\Capstone\code\data\df_test.csv')
#df = pd.read_excel('C:\AUA\Capstone\code\data\df_rent1.xlsx')
#df2 = pd.read_excel('C:\AUA\Capstone\code\data\df2.xlsx')
try:
    df = df.drop(['Unnamed: 0'], axis=1)
#    df2 = df2.drop(['Unnamed: 0'], axis=1)
except:
    pass

df['sqm'] = df['sqm'].astype(str)
df[['Sqm', 'sqm']] = df.sqm.str.split("SQ. M.Room", expand=True)
df[['rooms', 'floor']] = df.sqm.str.split("Floor/Storeys", expand=True)
df['Sqm'] = df['Sqm'].str.replace('Area', '')
df.sqm = df.sqm.str.replace('SQ. M.', '')
df = df.drop(['sqm'], axis=1)
df = df.drop(['sqm0'], axis = 1)
df.rooms = df.rooms.astype(str)
df.rooms = df.rooms.str[:2]
df.rooms = df.rooms.str.replace('No', 'nan')
df[['price', 'pricebysqm']] = df.price.str.split('/', expand=True)
df.additional = df.additional.str.replace('\n', '')
df.facilities = df.facilities.str.replace('\n', '')
df.adddate = df.adddate.str.slice(start=-12).replace(' ', '')
df.editdate = df.editdate.str.slice(start=-12).replace(' ', '')
df.adddate = df.adddate.str.replace('FOR SALE', '')
df.editdate = df.editdate.str.replace('FOR SALE', '')
df['addyear'] = pd.DatetimeIndex(df['adddate']).year
df['edityear'] = pd.DatetimeIndex(df['editdate']).year
df['addmonth'] = pd.DatetimeIndex(df['adddate']).month
df['editmonth'] = pd.DatetimeIndex(df['editdate']).month
df['addday'] = pd.DatetimeIndex(df['adddate']).day
df['editday'] = pd.DatetimeIndex(df['editdate']).day
df['addquarter'] = pd.DatetimeIndex(df['adddate']).quarter
df['editquarter'] = pd.DatetimeIndex(df['editdate']).quarter
df['adddate'] = pd.to_datetime(df['adddate'])
df['editdate'] = pd.to_datetime(df['editdate'])
df.price = df.price.str.replace(',', '')
df['platform'] = 'MyRealty.am'
df['housetype'] = np.where(df['info'].str.contains('property'), 'property',
                   np.where(df['info'].str.contains('house'), 'house',
                    np.where(df['info'].str.contains('land'), 'land', 'apartment')))
df['type'] = np.where(df['info'].str.contains('rent'), 'rent', 'sale')
df[['City', 'District', 'Street']] = df.address.str.split(',', expand=True)
#df2['sqm'] = df2['sqm'].str.replace(' m 2', '')
#df2['rooms'] = df2['rooms'].str.replace(' ROOM                  ', '')
#df2['price'] = df2['price'].str.replace('$ ', '')
#df2['additional0'] = df2['additional0'].str.replace('\n', '')
#df2['facilities'] = df2['facilities'].str.replace('\n', '')


create_columns(df)
#create_columns(df2)
create_dummy_columns(df, info_dict, 'additional')
#create_dummy_columns(df2, info_dict2, 'additional0')
df['pricebysqm'] = df['pricebysqm'].str.replace(' SQ. M. ', '')
df = df.drop(['more', 'additional', 'facilities'], axis=1)
#df2 = df2.drop(['additional0', 'facilities'], axis=1)

df.to_csv('C:\AUA\Capstone\code\data\df_clean_test_rent.csv')
#df2.to_excel('C:\AUA\Capstone\code\data\df2_clean.xlsx')
