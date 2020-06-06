import pandas as pd 



def combine(team):
    tables_titles= ['Defense', 'Kicking', 'Passing', 'Punting', 'Receiving', 'Returning', 'Rushing', 'Scoring']
    tabler_titles=['Defense','Offense','SpecialTeams']
    pages = 'stats'
    pager = 'roster'
    poss = ['all','qb','rb','wr','te','def','off','st']
    
    #Makes a stats data frame
    dfs0 = pd.read_csv('~/extra/fantasy/fantasy2020/' + team + '/' + team + '_' + tables_titles[0] + '_' + pages, dtype={'NAME':str,'POS':str})
    dfs1 = pd.read_csv('~/extra/fantasy/fantasy2020/' + team + '/' + team + '_' + tables_titles[1] + '_' + pages, dtype={'NAME':str,'POS':str})
    dfstemp = pd.merge(dfs0,dfs1, left_index=True, how='outer', on=['NAME','POS'])
    s=2
    while s < len(tables_titles):
        dfsi = pd.read_csv('~/extra/fantasy/fantasy2020/' + team + '/' + team + '_' + tables_titles[s] + '_' + pages, dtype={'NAME':str,'POS':str})
        dfstemp = pd.merge(dfstemp,dfsi, left_index=True, how='outer', on=['NAME','POS'])
        s+=1
    dfstats = dfstemp
    dfstats.to_csv('~/extra/fantasy/fantasy2020/' + team + '/' + team + '_' + 'stats')

    #Makes a roster data frame
    dfr0 = pd.read_csv('~/extra/fantasy/fantasy2020/' + team + '/' + team + '_' + tabler_titles[0] + '_' + pager)
    dfr1 = pd.read_csv('~/extra/fantasy/fantasy2020/' + team + '/' + team + '_' + tabler_titles[1] + '_' + pager)
    dfr2 = pd.read_csv('~/extra/fantasy/fantasy2020/' + team + '/' + team + '_' + tabler_titles[2] + '_' + pager)
    dfroster = pd.concat([dfr0, dfr1, dfr2], ignore_index=True, join='outer')
    dfroster.to_csv('~/extra/fantasy/fantasy2020/' + team + '/' + team + '_' + 'roster')

    #Makes sure the name strings match
    dfstats['name']=dfstats['NAME'].str.replace(' ','')
    dfroster['name']=dfroster['NAME'].str.replace(' ','')

    #Merges roster and stats
    dftemprs = pd.merge(dfroster,dfstats, on=['name','POS'], how='left')
    dftemprs = dftemprs.loc[:,~dftemprs.columns.duplicated()]
    dftemprs.to_csv('~/extra/fantasy/fantasy2020/' + team + '/' + team + '_' + 'rs')

    #Adds all positions to master list
    #Needs to happen to the right once to make sure list is populated
    dftempma = pd.read_csv('~/extra/fantasy/fantasy2020/master/master_' + poss[0])
    dfmaster = pd.concat([dftemprs,dftempma], ignore_index=True, join='outer')
    dfmaster = dfmaster.loc[:,~dfmaster.columns.duplicated()]
    cols_keepmaster =['POS','Age','HTIN','WT','Exp','College','name','NAME_x','DefGP','DefSOLO','DefAST','DefTOT','DefSACK','DefTFL','DefPD','DefINT','DefYDS','DefLNG','DefTD','DefFF','DefFR','DefFTD','DefKB','PasGP','PasCMP','PasATT','PasCMP%','PasYDS','PasAVG','PasYDS/G','PasLNG','PasTD','PasINT','PasSACK','PasSYL','Pas QBR ','RecGP','RecTGTS','RecYDS','RecAVG','RecTD','RecLNG','RecBIG','RecYDS/G','RecFUM','RecLST','RecYAC','RecFD','RetATT','RetYDS','RetAVG','RetLNG','RetTD','RetATT.1','RetYDS.1','RetAVG.1','RetLNG.1','RetTD.1','RetFC','RusATT','RusYDS','RusAVG','RusLNG','RusBIG','RusTD','RusYDS/G','RusFUM','RusLST','RusFD','ScoRUSH','ScoRET','ScoTD','ScoPAT','Sco2PT','ScoPTS']
    dfmaster[cols_keepmaster].to_csv('~/extra/fantasy/fantasy2020/master/master_' + poss[0])

    #Finds all the qbs
    dftempqb = pd.read_csv('~/extra/fantasy/fantasy2020/master/master_' + poss[1])
    dfloc = dftemprs.loc[dftemprs['POS'] == 'QB']
    dfmasterqb = pd.concat([dftempqb,dfloc], ignore_index=True, join='outer')
    cols_keepqb = ['POS','Age','HTIN','WT','Exp','College','name','NAME_x','PasGP','PasCMP','PasATT','PasCMP%','PasYDS','PasAVG','PasYDS/G','PasLNG','PasTD','PasINT','PasSACK','PasSYL','Pas QBR ','PasRTG','RusATT','RusYDS','RusAVG','RusLNG','RusBIG','RusTD','RusYDS/G','RusFUM','RusLST','RusFD','ScoRUSH','ScoRET','ScoTD','ScoPAT','Sco2PT','ScoPTS']
    dfmasterqb[cols_keepqb].to_csv('~/extra/fantasy/fantasy2020/master/master_' + poss[1])

    #Finds all the rbs
    dftemprb = pd.read_csv('~/extra/fantasy/fantasy2020/master/master_' + poss[2])
    dfloc = dftemprs[(dftemprs.POS.isin(['RB','FB']))]
    dfmasterrb = pd.concat([dftemprb,dfloc], ignore_index=True, join='outer')
    cols_keeprb = ['POS','Age','HTIN','WT','Exp','College','name','NAME_x','RecGP','RecTGTS','RecYDS','RecAVG','RecTD','RecLNG','RecBIG','RecYDS/G','RecFUM','RecLST','RecYAC','RecFD','RetATT','RetYDS','RetAVG','RetLNG','RetTD','RetATT.1','RetYDS.1','RetAVG.1','RetLNG.1','RetTD.1','RetFC','RusATT','RusYDS','RusAVG','RusLNG','RusBIG','RusTD','RusYDS/G','RusFUM','RusLST','RusFD','ScoRUSH','ScoRET','ScoTD','ScoPAT','Sco2PT','ScoPTS']
    dfmasterrb[cols_keeprb].to_csv('~/extra/fantasy/fantasy2020/master/master_' + poss[2])

    #Finds all the wrs
    dftempwr = pd.read_csv('~/extra/fantasy/fantasy2020/master/master_' + poss[3])
    dfloc = dftemprs.loc[dftemprs['POS'] == 'WR']
    dfmasterwr = pd.concat([dftempwr,dfloc], ignore_index=True, join='outer')
    cols_keepwr = ['POS','Age','HTIN','WT','Exp','College','name','NAME_x','RecGP','RecTGTS','RecYDS','RecAVG','RecTD','RecLNG','RecBIG','RecYDS/G','RecFUM','RecLST','RecYAC','RecFD','RetATT','RetYDS','RetAVG','RetLNG','RetTD','RetATT.1','RetYDS.1','RetAVG.1','RetLNG.1','RetTD.1','RetFC','RusGP','RusATT','RusYDS','RusAVG','RusLNG','RusBIG','RusTD','RusYDS/G','RusFUM','RusLST','RusFD','ScoGP','ScoRUSH','ScoRET','ScoTD','ScoPAT','Sco2PT','ScoPTS']
    dfmasterwr[cols_keepwr].to_csv('~/extra/fantasy/fantasy2020/master/master_' + poss[3])

    #Finds all the tes
    dftempte = pd.read_csv('~/extra/fantasy/fantasy2020/master/master_' + poss[4])
    dfloc = dftemprs.loc[dftemprs['POS'] == 'TE']
    dfmasterte = pd.concat([dftempte,dfloc], ignore_index=True, join='outer')
    cols_keepte = ['POS','Age','HTIN','WT','Exp','College','name','NAME_x','RecGP','RecTGTS','RecYDS','RecAVG','RecTD','RecLNG','RecBIG','RecYDS/G','RecFUM','RecLST','RecYAC','RecFD','RetATT','RetYDS','RetAVG','RetLNG','RetTD','RetATT.1','RetYDS.1','RetAVG.1','RetLNG.1','RetTD.1','RetFC','RusGP','RusATT','RusYDS','RusAVG','RusLNG','RusBIG','RusTD','RusYDS/G','RusFUM','RusLST','RusFD','ScoGP','ScoRUSH','ScoRET','ScoTD','ScoPAT','Sco2PT','ScoPTS']
    dfmasterte[cols_keepte].to_csv('~/extra/fantasy/fantasy2020/master/master_' + poss[4])

    #Finds all the def
    dftempdef = pd.read_csv('~/extra/fantasy/fantasy2020/master/master_' + poss[5])
    dfloc = dftemprs[(dftemprs.POS.isin(['DE','DT','LB','CB','S']))]
    dfmasterdef = pd.concat([dftempdef,dfloc], ignore_index=True, join='outer')
    cols_keepdef = ['POS','Age','HTIN','WT','Exp','College','name','NAME_x','DefGP','DefSOLO','DefAST','DefTOT','DefSACK','DefTFL','DefPD','DefINT','DefYDS','DefLNG','DefTD','DefFF','DefFR','DefFTD','DefKB']
    dfmasterdef[cols_keepdef].to_csv('~/extra/fantasy/fantasy2020/master/master_' + poss[5])

    #Finds all the off
    dftempoff = pd.read_csv('~/extra/fantasy/fantasy2020/master/master_' + poss[6])
    dfloc = dftemprs[(dftemprs.POS.isin(['C','OG','OT']))]
    dfmasteroff = pd.concat([dftempoff,dfloc], ignore_index=True, join='outer')
    cols_keepoff = ['POS','Age','HTIN','WT','Exp','College','name','NAME_x','PasGP']
    dfmasteroff[cols_keepoff].to_csv('~/extra/fantasy/fantasy2020/master/master_' + poss[6])

    #Finds all the sts
    dftempst = pd.read_csv('~/extra/fantasy/fantasy2020/master/master_' + poss[7])
    dfloc = dftemprs[(dftemprs.POS.isin(['LS','K','PK']))]
    dfmasterst = pd.concat([dftempst,dfloc], ignore_index=True, join='outer')
    cols_keepst = ['POS','Age','HTIN','WT','Exp','College','name','NAME_x','RecGP','RecTGTS','RecYDS','RecAVG','RecTD','RecLNG','RecBIG','RecYDS/G','RecFUM','RecLST','RecYAC','RecFD','RetATT','RetYDS','RetAVG','RetLNG','RetTD','RetATT.1','RetYDS.1','RetAVG.1','RetLNG.1','RetTD.1','RetFC','RusATT','RusYDS','RusAVG','RusLNG','RusBIG','RusTD','RusYDS/G','RusFUM','RusLST','RusFD','ScoRUSH','ScoRET','ScoTD','ScoPAT','Sco2PT','ScoPTS']
    dfmasterst[cols_keepst].to_csv('~/extra/fantasy/fantasy2020/master/master_' + poss[7])
    
    print(team + ' combined') 
    #TODO find a way to merge depth
    #TODO clean up Unnamed and extra NAME_y columns
    #TODO clean up code with a loop


