import pandas as pd

df = pd.read_csv('MergedData_dateTime.csv', usecols=['Time','Open','High','Low','Close','Volume','Timestamp','Year','Month','Day','Hour','Min','weekofYear','DayinWeek'])

# index,Time,Open,High,Low,Close,Volume,Timestamp,Year,Month,Day,Hour,Min,weekofYear,DayinWeek,FutureOpen,FutureHigh,FutureLow,FutureClose,FutureVolume,FutureTimestamp,FutureYear,FutureMonth,FutureDay,FutureHour,FutureMin,FutureWeekofYear,FutureDayinWeek

df['FutureOpen'] = df['Open'].shift(-1).astype(float)
df['FutureHigh'] = df['High'].shift(-1).astype(float)
df['FutureLow'] = df['Low'].shift(-1).astype(float)
df['FutureClose'] = df['Close'].shift(-1).astype(float)
df['FutureVolume'] = df['Volume'].shift(-1).astype(float)
df['FutureTimestamp'] = df['Timestamp'].shift(-1).astype(pd.Timestamp)
df['FutureYear'] = df['Year'].shift(-1).astype(int)
df['FutureMonth'] = df['Month'].shift(-1).astype(int)
df['FutureDay'] = df['Day'].shift(-1).astype(int)
df['FutureHour'] = df['Hour'].shift(-1).astype(int)
df['FutureMin'] = df['Min'].shift(-1).astype(int)
df['FutureDayinWeek'] = df['DayinWeek'].shift(-1).astype(int)


df.to_csv('MergedDataFuture.csv', header=True, index=False, index_label=None)
# df.drop(['index'], axis=1)
print(df.head())