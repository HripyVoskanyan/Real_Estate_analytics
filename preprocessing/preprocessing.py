import pandas as pd
from assets.config import *
from create_dummies import *

df = pd.read_excel('C:\AUA\Capstone\code\data\df.xlsx')
df2 = pd.read_excel('C:\AUA\Capstone\code\data\df2.xlsx')
try:
    df = df.drop(['Unnamed: 0'], axis=1)
    df2 = df2.drop(['Unnamed: 0'], axis=1)
except:
    pass

df[['Sqm', 'sqm']] = df.sqm.str.split("SQ. M.Room", expand=True)
df[['rooms', 'floor']] = df.sqm.str.split("Floor/Storeys", expand=True)
df['Sqm'] = df['Sqm'].str.replace('Area', '')
df = df.drop(['sqm'], axis=1)
df[['price', 'pricebysqm']] = df.price.str.split('/', expand=True)
df.additional = df.additional.str.replace('\n', '')
df.facilities = df.facilities.str.replace('\n', '')
df2['sqm'] = df2['sqm'].str.replace(' m 2', '')
df2['rooms'] = df2['rooms'].str.replace(' ROOM                  ', '')
df2['price'] = df2['price'].str.replace('$ ', '')
df2['additional0'] = df2['additional0'].str.replace('\n', '')
df2['facilities'] = df2['facilities'].str.replace('\n', '')


create_columns(df)
create_columns(df2)
create_dummy_columns(df, info_dict, 'additional')
create_dummy_columns(df2, info_dict2, 'additional0')
df['pricebysqm'] = df['pricebysqm'].str.replace(' SQ. M. ', '')
df = df.drop(['more', 'additional', 'facilities'], axis=1)
df2 = df2.drop(['additional0', 'facilities'], axis=1)

df.to_excel('C:\AUA\Capstone\code\data\df_clean.xlsx')
df2.to_excel('C:\AUA\Capstone\code\data\df2_clean.xlsx')
