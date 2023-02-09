import datetime as dt
import pandas as pd
stockdata = input('\n\t\t\t\t*/\*/\*/\*/\*/\*/\***Select the Company Name***/\*/\*/\*/\*/\*/\* \n\t\tDIS\n\t\tTATASTEEL\n\t\tRELIANCE\n\t\tTSLA\n\t\tGOOG\n')
ts1 = str(int(dt.datetime(2023,2,1).timestamp()))
ts2 = str(int(dt.datetime(2023,2,8).timestamp()))
interval = input('Enter the interval from 1d to 1mo :\n\t daywise = 1d\n\t weekwise = 1wk\n\t monthwise = 1mo\n')
#interval = '1d' , '1wk' ,'1mo'
events = input('Do you want me to print history or div data ? \n')
#events = 'div','split'
Stockurl = 'https://finance.yahoo.com/quote/'+stockdata+'/history?p='+stockdata+''
Stock_downurl = 'https://query1.finance.yahoo.com/v7/finance/download/' + stockdata + '?period1='+ ts1 + '&period2=' + ts2 + '&interval=' + interval + '&events'+ events
company_data = pd.read_csv(Stock_downurl)
print(company_data)
print('\n\nThe Download link is here :')
print(Stock_downurl)
print('\n//***Hence you Can change the "date interval" at line no.4 and 5 in code and try***//\n')