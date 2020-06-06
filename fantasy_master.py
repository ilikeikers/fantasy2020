#This will be the master file for my fantasy data collector

#Will Call: fantasy_parse to parse the website and collect it
#Then: fantasy_clean to clean the data for the team
#Set up a database to store the info for each player and position type

#Repeats for every team
import pandas as pd
from fantasy_parse_stats import parseStats
from fantasy_parse_roster import parseRoster
from fantasy_parse_depth import parseDepth
from fantasy_clean_stats import cleanStats
from fantasy_clean_roster import cleanRoster
from fantasy_clean_depth import cleanDepth
from fantasy_combine import combine

teams = ['ari','atl','bal','buf','car','chi','cin','cle','dal','den','det','gb','hou','ind','jax','kc','lac','lv','mia','min','ne','no','nyg','nyj','phi','pit','sea','sf','tb','ten','wsh']
pages = ['stats', 'roster', 'depth']
table_titles_stats= ['Defense', 'Kicking', 'Passing', 'Punting', 'Receiving', 'Returning', 'Rushing', 'Scoring']
table_titles = ['Offense', 'Defense', 'SpecialTeams']
poss = ['all','qb','rb','wr','te','def','off','st']

#Makes sure master lists are created
df = pd.DataFrame(columns=['POS'])
for pos in poss:
    df.to_csv('~/extra/fantasy/fantasy2020/master/master_' + pos)


for team in teams:
    for page in pages:
        if page == 'stats':
            parseStats(team,page)
            for table_title_stats in table_titles_stats:
                cleanStats(team,table_title_stats,page)

        elif page == 'roster': 
            parseRoster(team,page)
            for table_title in table_titles: 
                cleanRoster(team,table_title,page)

        else: 
            parseDepth(team,page='depth')
            for table_title in table_titles:
              cleanDepth(team,table_title,page='depth')
        print(team + ' ' + page + ' done')
    combine(team)
    print(team + ' done :)')

    #TODO make a working algorithm for ranking players by stats
    #TODO make master draft list for both rookies and vets
    #TODO make depth a working part. Right now, it parses but doesn't clean or combine at all. 
    #TODO combine all 'parse', 'clean' and 'combine' functions into one file to not import so many things
    








