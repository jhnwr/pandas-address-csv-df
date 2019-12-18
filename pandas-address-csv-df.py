import pandas as pd 

#read the csv file into a dataframe
df = pd.read_csv('address-data.csv')

#tidy up the column names
df.columns =[column.replace(" ", "_") for column in df.columns]

#create new dataframes for different shipping_type columns
shipping_1day = df[(df['Shipping_Type'] == '1 Day')]
shipping_2day = df[(df['Shipping_Type'] == '2 Day')]
shipping_5day = df[(df['Shipping_Type'] == '5 Day')]

#
# df.drop(shipping_1day.index, inplace=True)

#see how many orders we have for each
print(len(shipping_1day))
print(len(shipping_2day))
print(len(shipping_5day))
print(len(df))

#create new dataframes for matching criteria
shipping_1day_china = df[(df['Shipping_Type'] == '1 Day') & (df['Shipping_Country'] == 'China')]

#print(shipping_1day_china.head())

#create new  DF with 3 criteria
hatorders = df[(df['item'] == 'Hat') & (df['Shipping_Country'] == 'China') & (df['Shipping_Type'] == '1 Day')]

#remove from original DF
df.drop(hatorders.index, inplace=True)

#create same as above but using tidier "df.query()". this only works with column names with no spaces - shows 0 as we dropped them in the line above
hatorders_query = df.query('item == "Hat" & Shipping_Country == "China" & Shipping_Type == "1 Day"')


print(len(hatorders))
print(len(hatorders_query))

#save to new csv files ready for purpose
#shipping_1day.to_csv('1-day-shipping.csv')

print(len(df))