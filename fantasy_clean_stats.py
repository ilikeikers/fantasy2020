import pandas as pd 

def cleanStats(team,table_title,page):
#Imports CSV file 
    df = pd.read_csv('~/extra/fantasy/fantasy2020/' + team + '/' + team + '_' + table_title + '_' + page , header=[1])

    #Deletes the 'Total' row
    df = df.drop(df.index[-1:])
    #Parses 'Name' and separates out the position of the player
    df['POS'] = df.apply(lambda x: x['Name'][-2:], axis =1)
    df['NAME'] = df.apply(lambda x: x['Name'][:-2], axis =1)
    #Deletes the original 'Name' Column
    df = df.drop('Name', axis=1)
    #print(df)
    df.to_csv('~/extra/fantasy/fantasy2020/' + team + '/' + team + '_' + table_title + '_' + page)

    #TODO Need to move the created columns to the front two positons.
    #Should be fun.
