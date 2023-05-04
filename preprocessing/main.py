import pandas as pd
import preprocessing


df1 = pd.read_csv("C:\AUA\Capstone\code\data\data_new1.csv")
# df2 = pd.read_csv("C:\AUA\Capstone\code\data\data_new2.csv")

preprocessing.preprocess_myrealty(df1)
# preprocessing.preprocess_besthouse(df2)
