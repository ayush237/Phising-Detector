
import re

def URLBreakdown(url):

    regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'''

    phoneNumRegex = re.compile(r'''\b(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\b''')
    mo = phoneNumRegex.search('http:google//110.234.52.124.//google.com ')
    if(mo is not None):
        has_ip = 1
    else:
        has_ip =0





    if(len(url)<54):
        lenurl = 1
    elif(len(url)>=54 and len(url)<=75):
        lenurl = 0
    else:
        lenurl =  -1



    if(url.find("@")):
        atsymbol =1
    else:
        atsymbol = 0


    redirect_index = url.rindex("//")

    if(redirect_index>7):
        redirect_check = 1
    else:
        redirect_check = 0




    if(url.find("-") >=0):
        hyphen = 1
    else:
        hyphen = 0



    afterwwwdot = url.partition("www.")[0]
    count=0
    for i in afterwwwdot:
        if i == '.':
            count=count+1
    if(count==2):
        dotcount=1
    elif(count==2):
        dotcount= 0
    else:
        dotcount=-1

    if(url[4]=='s'):
        https =1
    else:
        https =0


    httpsorhttp = 1 if(url[:5]=='https') or url[:4]=='http' else 0

    return[has_ip,lenurl,atsymbol,redirect_check,hyphen,dotcount,httpsorhttp,https]








