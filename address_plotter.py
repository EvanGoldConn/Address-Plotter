'''

Address in Zone checker
Evan Goldsmith
12/27/2020


'''


from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import pandas as pd


locator = Nominatim(user_agent="myGeocoder")

testdf = pd.read_csv("addresses.csv")

df_909 = pd.read_csv("909_dataset.csv")
newdf = df_909

geocode = RateLimiter(locator.geocode, min_delay_seconds=1)


''' the double # will actiavte the pandas way of converting the entire df. '''


##print(len(df_909))
##df1 = df_909.iloc[:8270]
##df2 = df_909.iloc[8270:16540]
##df3 = df_909.iloc[16540:24810]
##df4 = df_909.iloc[24810:]
##
##
##
##dfs = [df1, df2, df3, df4]
##
##updatedDFs = []
##for curDF in dfs:
##
##    curDF['ADDRESS'] = curDF.Address+', '+curDF.City+', New Jersey, United States of America'
##    curDF['location'] = curDF['ADDRESS'].apply(geocode)
##    curDF['point'] = curDF['location'].apply(lambda loc: tuple(loc.point) if loc else None)
##    curDF[['latitude', 'longitude', 'altitude']] = pd.DataFrame(curDF['point'].tolist(), index=curDF.index)
##
##    updatedDFs.append(curDF)
##
##fullDF = pd.concat(updatedDFs)
##fullDF.to_csv("/Users/evangoldsmith/Documents/GitHub/Email-Scraper/saved_directory/909_dataset_coordinates.csv")


####
####
####
####
####'''testing on test df '''
####
######
######testdf['ADDRESS'] = testdf.Address1+','+testdf.Address3+','+testdf.Address4+','+testdf.Address5+', Sweden'
######testdf['location'] = testdf['ADDRESS'].apply(geocode)
####### 3 - create longitude, laatitude and altitude from location column (returns tuple)
######testdf['point'] = testdf['location'].apply(lambda loc: tuple(loc.point) if loc else None)
####### 4 - split point column into latitude, longitude and altitude columns
######testdf[['latitude', 'longitude', 'altitude']] = pd.DataFrame(testdf['point'].tolist(), index=testdf.index)
####
####
####
####
####
####
####
####
####
######def getCoordinates(Address, City, State):
####print("poop")
####from time import sleep
####def getCoordinates():
####    
####    newdf['latitude'], newdf['longitude'] = "", ""
####    
####    for i in range(len(newdf.Address)):
####        sleep(1)
####        curAddress, curCity = str(newdf.Address[i]), str(newdf.City[i]) #grab add/city, maybe add zipcode?
####        curState = "New Jersey"
####
####        curFullAddress = curAddress+", "+curCity+", "+curState
####        if(i%1000 == 0):
####            print(newdf.Date[i], curFullAddress)
####        curLocation = locator.geocode(curFullAddress)
####
####        try:
####            curLat = curLocation.latitude
####            curLong = curLocation.longitude
####            newdf.latitude[i], newdf.longitude[i] = curLat, curLong
######            return(curLat, curLong)
####        except:
####            print("Unable to get coordinates.", newdf.Date[i], curFullAddress)
####            
####            newdf.latitude[i], newdf.longitude[i] = None, None
######            return None
####    newdf.to_csv("/Users/evangoldsmith/Documents/GitHub/Email-Scraper/saved_directory/909_data_coordsTERMINAL.csv")
####
####
######getCoordinates()
####    
####    

def returnCoordinates(Address, City, State):
    curFullAddress = str(Address)+", "+str(City)+", "+str(State)
    curLocation = locator.geocode(curFullAddress)
    try:
        curLat = curLocation.latitude
        curLong = curLocation.longitude
        return(curLat, curLong)
    except:
##        print("Unable to get coordinates.", curFullAddress)
        return None

    


