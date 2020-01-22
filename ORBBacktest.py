import datetime
import pandas as pd
import time

df=pd.read_csv("C:\\Users\\avina\\Desktop\\Backtesting\\INFY.csv") 

# print df['date']
df['date']=pd.to_datetime(df['date'])
# print df
df['date_new'] = df['date'].dt.date
df['month'] = df['date'].dt.month
df['year'] = df['date'].dt.year
df['hour'] = df['date'].dt.hour
df['minute'] = df['date'].dt.minute
# print df

IB_Start_Hour=9
IB_End_Hour=9
IB_Start_Minute=15
IB_End_Minute=30
IB_Date=datetime.date(2019,11,01)
df=df.query('date_new == @IB_Date & hour == @IB_Start_Hour & minute<=@IB_End_Minute' )
print df
