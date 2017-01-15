# -*- coding: utf-8 -*-
from dataapi import Client

token = '3207956af0aa3427e75a0ae1b294d990870373905df065302ae2311b7b3a8d07'

if __name__ == "__main__":
    try:
        client = Client()
        client.init(token)
        url = '/api/equity/getEquMainshFCCXE.csv?field=&secID=&ticker=300371&shRank=&exchangeCD=&endDateStart=20160101&endDateEnd=&shareCharType='
        
        code, result = client.getData(url)
        if code==200:
            print(result)
        else:
            print(code)
            print(result)
#        url2='/api/subject/getThemesContent.csv?field=&themeID=&themeName=&isMain=1&themeSource='
#        code, result = client.getData(url2)
#        if(code==200):
#            file_object = open('thefile.csv', 'w')
#            file_object.write(result)
#            file_object.close( )
#        else:
#            print(code)
#            print(result)
    except:
        traceback.print_exc()
#        raise e
