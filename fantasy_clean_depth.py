import pandas as pd 

def cleanDepth(team,table_title,page):
    #Imports CSV file 
    df = pd.read_csv('~/extra/fantasy/fantasy2020/' + team + '/' + team + '_' + table_title + '_' + page , header=[1])
    #print(df)
    df.to_csv('~/extra/fantasy/fantasy2020/' + team + '/' + team + '_' + table_title + '_' + page)

