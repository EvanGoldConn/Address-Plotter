'''

cleaning the address' in the 909 dataset so the lat/long grabber works 

'''

import pandas as pd
import csv
import address_plotter
import re






file = "/Users/evangoldsmith/Documents/GitHub/Email-Scraper/saved_directory/909_FIXED_DATASET.csv"

data_909 = pd.read_csv(file, delimiter=',')
data_909['Latitude'] = ""
data_909['Longitude'] = ""
data_909['Zipcode'] = ""
pd.set_option('display.max_columns', None)





'''updating street names from first -> 1st'''


data_909['Address'] = data_909['Address'].str.replace("FIRST", "1st")
data_909['Address'] = data_909['Address'].str.replace("SECOND", "2nd")
data_909['Address'] = data_909['Address'].str.replace("THIRD", "3rd")
data_909['Address'] = data_909['Address'].str.replace("FOURTH", "4th")
data_909['Address'] = data_909['Address'].str.replace("FIFTH", "5th")
data_909['Address'] = data_909['Address'].str.replace("SIXTH", "6th")
data_909['Address'] = data_909['Address'].str.replace("SEVENTH", "7th")
data_909['Address'] = data_909['Address'].str.replace("EIGHTH", "8th")
data_909['Address'] = data_909['Address'].str.replace("NINTH", "9th")
data_909['Address'] = data_909['Address'].str.replace("TENTH", "10th")
data_909['Address'] = data_909['Address'].str.replace("ELEVENTH", "11th")
data_909['Address'] = data_909['Address'].str.replace("TWELFTH", "12th")
data_909['Address'] = data_909['Address'].str.replace("THIRTEENTH", "13th")
data_909['Address'] = data_909['Address'].str.replace("FOURTEENTH", "14th")
data_909['Address'] = data_909['Address'].str.replace("FIFTEENTH", "15th")
data_909['Address'] = data_909['Address'].str.replace("SIXTEENTH", "16th")
data_909['Address'] = data_909['Address'].str.replace("SEVENTEENTH", "17th")
data_909['Address'] = data_909['Address'].str.replace("EIGHTEENTH", "18th")
data_909['Address'] = data_909['Address'].str.replace("NINETEENTH", "19th")
data_909['Address'] = data_909['Address'].str.replace("TWENTIETH", "20th")
data_909['Address'] = data_909['Address'].str.replace("TWENTY-FIRST", "21st")


''' -------------------------- END UPDATING STREET NAMES --------------------------'''


#implementing street end cases from random stack answer that doesnt rlly work
##obj = data_909['Address'].copy()
##for k,v in add_map.items():
##    obj = obj.str.replace(r"(\W)(%s)(\W?)" % k, r"\1%s\3" % v, regex=True, flags=re.IGNORECASE)
##data_909['Address_n'] = obj


'''fixing street end abbreviations '''


add_map = dict([
    ("AV", "Avenue"),
    ("BV", "Boulevard"),
    ("BP", "Bypass"), 
    ("BY", "Bypass"),
    ("CL", "Circle"),
    ("DR", "Drive"),
    ("LA", "Lane"),
    ("LN", "Lane"),
    ("PY", "Parkway"),
    ("RD", "Road"),
    ("ST", "Street"),
    ("WY", "Way"),
    ("PL", "Place"),
    ("TR", "Trail"),
    ("TE", "Terrace"),
    ("CT", "Court"),
    ("RT130", "US-130"),
    ("RT295", "US-295"),
    
      
])

#COOL REGEX IMPLEMENTATION
data_909['Address_new'] = data_909['Address']
#print(data_909['Address_new'])

obj = data_909['Address'].copy()
for k,v in add_map.items():
    rule1 = (r"(\b)(%s)(\b)" % k)
    rule2 = (lambda m: add_map.get(m.group(), m.group()))
    obj = obj.str.replace(rule1, rule2, regex=True, flags=re.IGNORECASE)
data_909['Address_New'] = obj


''' -------------------------- END STREET ABBREVIATION REPLACING --------------------------'''


''' ADDING ZIPCODES '''


for i in range(len(data_909.Address)):
    curCity = data_909.City[i]

    #adding zipcodes except for florence (there are 3) and springfield (like 10)

    if(curCity == "Edgewater Park" or curCity == "Beverly City"):
        data_909.Zipcode[i] = '08010'
    elif(curCity == "Burlington City" or curCity == "Burlington Township"):
        data_909.Zipcode[i] = '08016'
    elif(curCity == "Willingboro Township"):
        data_909.Zipcode[i] = '08046'
    elif(curCity == "Florence Township"):
        data_909.Zipcode[i] = "Florence Township"
    elif(curCity == "Springfield Township"):
        data_909.Zipcode[i] = "Springfield Township"
    else:
        print('wtf?', data_909.Date[i], curAddress, curCity)



''' ------------------------------------- END ADDING ZIPCODES --------------------------------'''







'''testing geocoding with all address' '''


brokeAddress = []
with open('/Users/evangoldsmith/Documents/GitHub/Address-Plotter/NON_GEOCODEABLE.csv', mode='w') as file1: #creating the file we are writing to 
    fileWriter1 = csv.writer(file1, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    fileWriter1.writerow(['', 'Date', 'Address'])
    for i in range(len(data_909.Address)):
        curNewAddy = data_909.Address_New[i]
        curCity = data_909.City[i]
        curZipCode = data_909.Zipcode[i]
        curState = "New Jersey"


        geoLocation = address_plotter.returnCoordinates(curNewAddy, curZipCode, curState)

        if (i%4500 == 0):
            print(data_909.Date[i], curNewAddy)

        x = 1
        
        if(geoLocation == None):
            #print('didnt work', data_909.Date[i], curNewAddy, curZipCode)

            if(curNewAddy not in brokeAddress):
                fileWriter1.writerow(['', str(data_909.Date[i]), curNewAddy])
                brokeAddress.append((str(data_909.Date[i]), curNewAddy))

    ##    elif(geoLocation != None):
    ##        print('it worked!', geoLocation)
        #fixing address

with open("NON_GEOCODEABLE_ADDRESS.txt", "w") as file:
    for item in brokeAddress:
        file.write("%s\n" % item)
    
#data_909.to_csv("/Users/evangoldsmith/Documents/GitHub/Address-Plotter/TRYING_DATASET.csv")

    
