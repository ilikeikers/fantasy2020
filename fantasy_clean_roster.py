import pandas as pd 
import re

def cleanRoster(team,table_title,page):
    #Imports CSV file 
    df = pd.read_csv('~/extra/fantasy/fantasy2020/' + team + '/' + team + '_' + table_title + '_' + page , header=[1])
    
    #Sets up and makes coulmn for height in inches
    df['ht_clean'] = df['HT'].apply(lambda x: x.replace("'",",").replace('"',''))
    df['feet'] = df['ht_clean'].apply(lambda x: int(x.split(",")[0]))
    df['inches'] = df['ht_clean'].apply(lambda x: int(x.split(",")[1]))
    df['ftin'] = df['feet'].apply(lambda x: int(x*12))
    df['HTIN'] = df.apply(lambda x: (x.ftin + x.inches), axis=1)
    
    #What 're' is needed for. Removes numbers and renames ['NAME']
    pattern = '[0-9]'
    df['NAME'] = df['Name'].apply(lambda x: re.sub(pattern, '', x))

    
    #Drop unndeeded columns
    df = df.drop('ht_clean', axis=1)
    df = df.drop('feet', axis=1)
    df = df.drop('inches', axis=1)
    df = df.drop('ftin', axis=1)
    df = df.drop('Name', axis=1)
    #df = df.drop('Unnamed: 0', axis=1)
    #df = df.drop('Unnamed: 7', axis=1)
    
    #Removes lbs from WT
    df['WT'] = df.apply(lambda x: x['WT'][:-4], axis=1)

    #print(df)
    df.to_csv('~/extra/fantasy/fantasy2020/' + team + '/' + team + '_' + table_title + '_' + page)



