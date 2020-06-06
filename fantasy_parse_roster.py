from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

team = 'det'
page = 'roster'

def parseRoster(team,page):
    #URL for stats
    my_url = 'https://www.espn.com/nfl/team/' + page + '/_/name/' + team
    #Opens up connection and grabs the page
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    #html Parser
    page_soup = soup(page_html, 'html.parser')
    page_container = page_soup.findAll('div',{'page-container cf'})
    pages = page_container[0]
    tables_container = pages.div.div.section.div.section
    tables = tables_container.findAll('section')

    for table in tables:
        
        table_titles = table.div.text
        table_title = table_titles.replace(' ','')
        filename = team + '_' + table_title + '_' + page
        f = open('/home/ike/extra/fantasy/fantasy2020/' + team + '/' + filename, 'w')
        f.write(team + ',' + table_title + '\n')
        #Gets the headers (saved to second row) 
        table_headers = table.findAll('th',{'colspan':False, 'class':'Table__TH'})
        for table_header in table_headers:
            table_col_title = table_header.text
            if len(table_col_title) > 0: f.write(table_col_title + ',')
        f.write('\n') 
    
        #TODO Need to clean number out of name
        table_rows = table.findAll('tr',{'data-idx':True})
        for table_row in table_rows:
            table_data_container = table_row.findAll('td')
            for table_data_cell in table_data_container:
                table_data = table_data_cell.text
                if len(table_data) > 0: f.write(table_data + ',')
            f.write('\n')
        f.close()

parseRoster(team,page)
      

















