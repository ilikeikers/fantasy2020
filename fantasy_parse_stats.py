from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

#team = 'det' 
#page = 'stats'

def parseStats(team,page):
    #URL for stats
    my_url = 'https://www.espn.com/nfl/team/' + page + '/_/name/' + team
    #Opens up connection and grabs the page
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    #html Parser
    page_soup = soup(page_html, 'html.parser')

    #Begins to parse the data
    #Finds the data tables on the stats page
    tables = page_soup.findAll('section',{'class':'ResponsiveTable ResponsiveTable--fixed-left mt5 remove_capitalize'})
    number_of_tables = len(tables)
    table_number = 0
    #Cycles through the tables
    while table_number < number_of_tables:
      for table in tables:
          #Gets the title of the table (Passing, Running, etc.)
          table_title = table.div.text.title()
          table_title_abbr = table_title[0:3]
          #Creates the ending filename
          filename = team + '_' + table_title + '_' + page
          #Saves each team's stats in their own directory
          f = open('/home/ike/extra/fantasy/fantasy2020/' + team + '/' + filename, 'w')
          f.write(team + ',' + table_title + '\n')
          
          #Get the column titles
          table_headers = table.findAll('th',{'colspan':False})
          #Creates label for all of the column titles (Name, Completion, etc.)
          for table_header in table_headers:
              table_col_title = table_header.text
              #Ignores blank th tags
              if len(table_col_title) > 0:
                  if table_col_title == 'Name': 
                      f.write(table_col_title + ',')
                  else:
                      f.write(table_title_abbr + table_col_title + ',')
          f.write('\n') 
      
          #Gets all the rows in the table
          table_rows = table.findAll('tr',{'class':'Table__TR Table__TR--sm Table__even','data-idx':True})
          number_rows = int(len(table_rows) / 2)
          i = 0
          #Loops through every row to find data in the table
          while i < number_rows:
              #Needed for the next .findAll
              index_input = str(i)
              table_row = table.findAll('tr',{'class':'Table__TR Table__TR--sm Table__even', 'data-idx':index_input})
              #Cycles through the two containers that contain data per row
              for table_data_container in table_row:
                  table_data_cells = table_data_container.findAll('td',{'class':'Table__TD'})
                  #Cycles through every cell for data
                  for table_data_cell in table_data_cells:
                      table_data = table_data_cell.text
                      f.write(table_data.replace(',','') + ',')
              f.write('\n') 
              i += 1
      table_number +=1
      f.close()



      

















