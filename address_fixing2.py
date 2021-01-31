'''

fixing address part 2

1/29/2021
'''

import pandas as pd
import csv
#import address_plotter
import re


file = "/Users/evangoldsmith/Documents/GitHub/Address-Plotter/manipulated_datasets/ALMOST_DONE_2nd.csv"
data_909 = pd.read_csv(file, delimiter=',')
pd.set_option('display.max_columns', None)

print(data_909)



for i in range(len(data_909.Address_New)):
    curZip = data_909.Zipcode[i]
    
    if('8' in curZip):
        data_909.Zipcode[i] = str('0'+str(curZip))

    
    curZip = data_909.Zipcode[i]
    curAdd = data_909.Address_New[i]
data_909.Zipcode.apply('="{}"'.format)
##    if('RIVERBANK' in curAdd):
##        print(data_909.Date[i], curAdd, curZip)
##        if(str(curZip) == '08010'):
##            data_909.Address_New[i] = data_909.Address_New[i].replace("RIVERBANK", "RIVERBANK Avenue")
##        elif(str(curZip) == '08016'):
##            data_909.Address_New[i] = data_909.Address_New[i].replace("RIVERBANK", "RIVERBANK Street")
##        print('new', data_909.Date[i], data_909.Address_New[i], curZip)
##    if("STONE VILLA" in curAdd):
##        print(data_909.Date[i], curAdd, curZip)
##        data_909.Address_New[i] = "98-82 W 3rd St"
##        data_909.City[i] = "Burlington City"
##        data_909.Zipcode[i] = "08016"
##        print('new', data_909.Date[i], data_909.Address_New[i], curZip)
##    if("STEEPLE CHASE" in curAdd):
##        print(data_909.Date[i], curAdd, curZip)
##        data_909.Address_New[i] = data_909.Address_New[i].replace("STEEPLE CHASE", "STEEPLECHASE")
##        data_909.City[i] = "Burlington Township"
##        data_909.Zipcode[i] = "08016"
##        print('new', data_909.Date[i], data_909.Address_New[i], curZip)
##    if("FAWNHOLLOW" in curAdd):
##        print(data_909.Date[i], curAdd, curZip)
##        data_909.Address_New[i] = data_909.Address_New[i].replace("FAWNHOLLOW", "FAWN HOLLOW")
##        print('new', data_909.Date[i], data_909.Address_New[i], curZip)
##    if("VANKIRK" in curAdd): #change to Van Kirk Street
##        print(data_909.Date[i], curAdd, curZip)
##        data_909.Address_New[i] = data_909.Address_New[i].replace("VANKIRK", "VAN KIRK")
##        print('new', data_909.Date[i], data_909.Address_New[i], curZip)  
##    if("VANSCIVER" in curAdd): #change to VAN SCIVER Parkway
##        print(data_909.Date[i], curAdd, curZip)
##        data_909.Address_New[i] = data_909.Address_New[i].replace("VANSCIVER", "VAN SCIVER")
##        print('new', data_909.Date[i], data_909.Address_New[i], curZip)
##    if("BENNETT" in curAdd): #change to Bennet Street (roebling, florence)
##        print(data_909.Date[i], curAdd, curZip)
##        data_909.Address_New[i] = data_909.Address_New[i].replace("BENNETT", "BENNET")
##        data_909.City[i] = "Florence Township"
##        data_909.Zipcode[i] = "Florence Township"
##        print('new', data_909.Date[i], data_909.Address_New[i], curZip)
print(data_909)

data_909.to_csv("/Users/evangoldsmith/Documents/GitHub/Address-Plotter/manipulated_datasets/ziptest.csv")

##string1 = "1701 SALEM Road APT A11 8016"
##string2 = "240 N US-130 UNIT 5 8016"
##string3 = "111 SUNSET Road RM 101 8016"
##strings=[string1, string2, string3]
##
##for curString in strings:
##    new = re.split("APT |UNIT |RM ", curString)
##
##    print(new[0], 'poop', new[1])


##splitrules = "APT |UNIT |SUITE |RM |FLOOR |UNKN|STORE "
##data_909['New_Address_Fixed'] = ""
###data_909[['New_Address_Fixed', 'Trash']] =
##
##fixed = data_909.Address_New.str.split(splitrules, expand=True)
##
##
##
##data_909['New_Address_Fixed'] = fixed[0]
##
##data_909.to_csv("/Users/evangoldsmith/Documents/GitHub/Address-Plotter/manipulated_datasets/ALMOST_DONE_3rd.csv")


        
##i = 0
##for newAddy in data_909.New_Address_Fixed:
##    newAddy = str(newAddy)
##    oldAddy = str(data_909.Address_New[i])
##    curZipCode = data_909.Zipcode[i]
##    curState = "New Jersey"
##
##    geoLocation = address_plotter.returnCoordinates(newAddy, curZipCode, curState)
##
##    
##    if(geoLocation == None):
##        print('didnt work', data_909.Date[i], newAddy)
##    
####    if(newAddy != oldAddy):
####        print(data_909.Date[i], newAddy, oldAddy)
##    i += 1
##
##print(len(data_909.New_Address_Fixed), len(data_909.Address_New))

##for i in range(len(data_909.Address_new)):
##    curNewAddy = data_909.Address_New[i]
##    curCity = data_909.City[i]
##    curZipCode = data_909.Zipcode[i]
##    curState = "New Jersey"
##
##
##    geoLocation = address_plotter.returnCoordinates(curNewAddy, curZipCode, curState)
##
##    
##    if(geoLocation == None):
##        print('didnt work', data_909.Date[i], curNewAddy, curZipCode)

     




