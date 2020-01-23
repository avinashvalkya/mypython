import datetime
import pandas as pd
import time

df=pd.read_csv("C:\\Users\\avina\\Desktop\\Backtesting\\INFY.csv") 

# print df['date']
df['date']=pd.to_datetime(df['date'])
# print df
df['date_new'] = df['date'].dt.date
# df['month'] = df['date'].dt.month
# df['year'] = df['date'].dt.year
# df['hour'] = df['date'].dt.hour
# df['minute'] = df['date'].dt.minute
df['time'] = df['date'].dt.time
# print df

IB_Date=datetime.date(2019,9,19)
IB_Start_Time=datetime.time(9,15,0)
IB_End_Time=datetime.time(9,30,0)
df_IB=df.query('date_new == @IB_Date & time >= @IB_Start_Time & time<=@IB_End_Time' )
# print df_IB


High=df_IB['high'].max()
Low=df_IB['low'].min()

# print High
# print Low

Trade_Start_Time=datetime.time(9,31,0)
Trade_End_Time=datetime.time(15,15,0)

df_Trade=df.query('date_new == @IB_Date & time >= @Trade_Start_Time & time<=@Trade_End_Time' )
# print df_Trade

Long_Entry_Candle=0
Short_Entry_Candle=0
Long_SL_Candle=0
Short_SL_Candle=0	
Exit_Time=datetime.time(15,15,0)

for i in df_Trade.index:
	v_High=df.loc[i,'high']
	v_Low=df.loc[i,'low']
	while v_High>High and Long_Entry_Candle==0:
		# print df.loc[i,'time']
		Long_Entry_Candle=i
	while v_Low<Low and Short_Entry_Candle==0:
		# print df.loc[i,'time']
		Short_Entry_Candle=i

Long_Entry_Time=df.loc[Long_Entry_Candle,'time']		
Short_Entry_Time=df.loc[Short_Entry_Candle,'time']	

# print Long_Entry_Time
# print Short_Entry_Time

df_Long=df.query('date_new == @IB_Date & time > @Long_Entry_Time & time<@Exit_Time' )	

for i in df_Long.index:
	v_Low_Long=df.loc[i,'low']
	while v_Low_Long<Low and Long_SL_Candle==0:
		# print df.loc[i,'time']
		Long_SL_Candle=i
		
Long_SL_Time=df.loc[Long_SL_Candle,'time']	

df_Short=df.query('date_new == @IB_Date & time > @Short_Entry_Time & time<@Exit_Time' )	

for i in df_Short.index:
	v_High_Short=df.loc[i,'high']
	while v_High_Short>High and Short_SL_Candle==0:
		# print df.loc[i,'time']
		Short_SL_Candle=i

		
Short_SL_Time=df.loc[Short_SL_Candle,'time']	

df_Exit=df.query('date_new == @IB_Date & time==@Exit_Time' )

# print df_Exit	

# print df_Exit['close'].values[0]

Long_Entry_Price=High
Long_SL_Price=Low
Long_Exit_Price=df_Exit['close'].values[0]
Short_Entry_Price=Low
Short_SL_Price=High
Short_Exit_Price=df_Exit['close'].values[0]

print "Long Entry: "+str(Long_Entry_Time)+" Long SL:"+str(Long_SL_Time)
print "Short Entry: "+str(Short_Entry_Time)+" Short SL:"+str(Short_SL_Time)

if Long_SL_Time>Long_Entry_Time:
	Long_Exit_Price=Long_SL_Price
if Short_SL_Time>Short_Entry_Time:
	Short_Exit_Price=Short_SL_Price
	
print "Side,Buy,Sell,SL"
if Long_Entry_Time!=datetime.time(9,15,0):
	print "Long"+","+str(Long_Entry_Price)+","+str(Long_Exit_Price)+","+str(Long_SL_Price)
if Short_Entry_Time!=datetime.time(9,15,0):
	print "Short"+","+str(Short_Exit_Price)+","+str(Short_Entry_Price)+","+str(Short_SL_Price)
