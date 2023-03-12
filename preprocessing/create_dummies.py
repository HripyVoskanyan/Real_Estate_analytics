import numpy as np


def create_columns(df):
    df['eurowindows'] = np.nan
    df['irondoor'] = np.nan
    df['openbalcony'] = np.nan
    df['securitysystem'] = np.nan
    df['sunny'] = np.nan
    df['view'] = np.nan
    df['roadside'] = np.nan
    df['closetothebusstation'] = np.nan
    df['parking'] = np.nan
    df['park'] = np.nan
    df['elevator'] = np.nan
    df['furniture'] = np.nan
    df['equipment'] = np.nan
    df['balcony'] = np.nan
    df['storageroom'] = np.nan
    df['playground'] = np.nan
    df['parquet'] = np.nan
    df['tile'] = np.nan
    df['laminateflooring'] = np.nan
    df['heating'] = np.nan
    df['hotwater'] = np.nan
    df['electricity'] = np.nan
    df['centralheating'] = np.nan
    df['water'] = np.nan
    df['water247'] = np.nan
    df['gas'] = np.nan
    df['airconditioner'] = np.nan
    df['sewerage'] = np.nan
    df['logha'] = np.nan
    df['garage'] = np.nan
    df['internet'] = np.nan


def create_dummy_columns(df, dt, name):
    for key in dt.keys():
        rn = 0
        value = dt[key]
        for row in df[name].str.split('--') + df.facilities.str.split('--'):
            try:
                for i in row:
                    if i == key:
                        df[value][rn] = 1
                        break
                    else:
                        df[value][rn] = 0
            except:
                df[value][rn] = 0
            rn += 1
