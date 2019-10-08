"""
Created on Wed Oct  2 13:03:11 2019

@author: MatthewOliver
"""

import pandas as pd
import matplotlib.pyplot as plt
import csv
import datetime

#create inflation table
#with open('inflation_data.csv') as csvfile:
#    inflated={}
#    readCSV = csv.reader(csvfile, delimiter=',')
#    for row in readCSV:
#        if row[0]!='year':
#            inflated[int(row[0])]=(30.9106/float(row[1]))

inflated=[[1900, 30.542616666666667], [1901, 30.183291764705885], [1902, 29.832323255813957], [1903, 29.154315909090904],
[1904, 28.826739325842695], [1905, 29.154315909090904], [1906, 28.506442222222223], [1907, 27.293402127659576],
[1908, 27.886736956521744], [1909, 28.193184615384617], [1910, 27.006103157894742], [1911, 27.006103157894742],
[1912, 26.449276288659796], [1913, 25.914947474747475], [1914, 25.655798], [1915, 25.401780198019804],
[1916, 23.537429357798167], [1917, 20.0435921875], [1918, 16.99059470198676], [1919, 14.82994104046243],
[1920, 12.827899], [1921, 14.332848044692739], [1922, 15.271308333333334], [1923, 15.003390643274853],
[1924, 15.003390643274853], [1925, 14.660456], [1926, 14.494801129943504], [1927, 14.744711494252874],
[1928, 15.003390643274853], [1929, 15.003390643274853], [1930, 15.362753293413176], [1931, 16.878814473684212],
[1932, 18.7268598540146], [1933, 19.73522923076923], [1934, 19.146117910447764], [1935, 18.7268598540146],
[1936, 18.457408633093525], [1937, 17.81652638888889], [1938, 18.19560141843972], [1939, 18.457408633093525],
[1940, 18.32557], [1941, 17.45292380952381], [1942, 15.739753374233128], [1943, 14.82994104046243],
[1944, 14.577157954545452], [1945, 14.253221111111111], [1946, 13.156819487179487], [1947, 11.504842152466368],
[1948, 10.645559336099584], [1949, 10.77974705882353], [1950, 10.645559336099584], [1951, 9.867614615384616],
[1952, 9.68143320754717], [1953, 9.608913108614233], [1954, 9.537471375464685], [1955, 9.573058955223882],
[1956, 9.43227867647059], [1957, 9.130177224199288], [1958, 8.877438754325262], [1959, 8.816425429553265],
[1960, 8.667499324324325], [1961, 8.580534448160536], [1962, 8.49529735099338], [1963, 8.3842477124183],
[1964, 8.276063870967741], [1965, 8.144697777777779], [1966, 7.918456172839506], [1967, 7.681376646706588],
[1968, 7.372355747126437], [1969, 6.990680653950953], [1970, 6.612319072164949], [1971, 6.334764938271605],
[1972, 6.13775071770335], [1973, 5.778332882882884], [1974, 5.204015821501015], [1975, 4.768735687732343],
[1976, 4.508927592267136], [1977, 4.2336300330033], [1978, 3.934938343558282], [1979, 3.5338564738292013],
[1980, 3.113567718446602], [1981, 2.8224200220022], [1982, 2.658631917098446], [1983, 2.5758833333333335],
[1984, 2.469277959576516], [1985, 2.3843678438661713], [1986, 2.340857481751825], [1987, 2.2584329225352113],
[1988, 2.16870650887574], [1989, 2.0690159677419353], [1990, 1.962953175210406], [1991, 1.8836856093979444],
[1992, 1.8286384889522453], [1993, 1.775487750865052], [1994, 1.7311604588394063], [1995, 1.6834513123359582],
[1996, 1.6351687699171447], [1997, 1.5984920872274144], [1998, 1.573975337423313], [1999, 1.5399638655462187],
[2000, 1.4898837398373983], [2001, 1.4486616600790516], [2002, 1.4261143968871597], [2003, 1.394336847826087],
[2004, 1.3581682371625199], [2005, 1.3136609318996415], [2006, 1.272609027777778], [2007, 1.2373661872654842],
[2008, 1.1916135864340025], [2009, 1.1958682185357303], [2010, 1.1765692299225887], [2011, 1.1405669092509525],
[2012, 1.117442006324207], [2013, 1.1013104564361664], [2014, 1.0837303156258449], [2015, 1.0824454785943625],
[2016, 1.0689604053215114], [2017, 1.0466627774151436], [2018, 1.0217084760072377], [2019, 0.9999999220449178]]
            
inflatedict={}
for i,row in enumerate(inflated):
    inflatedict[int(row[0])]=(row[1])

def inflate_adj(df, years, prices):
    '''
    Function should be passed a dataframe and strings of the names of the dates/prices columns
    Returns the data frame with new a new 'adj_price' column.
    '''
    
    new_price=[]
    for i,row in df.iterrows():
        get_year=str(row[years])
        year=int(get_year[:4])
        new_price.append(inflatedict[year]*float(row[prices]))
    name='adj_'+ prices
    df[name]=new_price
    return df

def inflate_adj_db(df, years, col_names):
    '''
    Function should be passed a dataframe, name of years column, and a list of column names
    Returns a new data frame with with adjusted prices.
    '''
    data={}
    for name in col_names:
        new_price=[]
        for i,row in df.iterrows():
            get_year=str(row[name])
            year=int(get_year[:4])
            new_price.append(inflatedict[year]*float(row[name]))
        
        data[name]=new_price
    new_df=pd.DataFrame(data)
    new_df['Year']=df[years]
    return new_df