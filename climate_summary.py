
import pandas as pd
import numpy as np
from config import gkey
import numpy as np
import requests
import json
import gmaps
import pymongo


# Configure gmaps
gmaps.configure(api_key = gkey)

# Initialize PyMongo to work with MongoDBs
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

#creates db (climate_change) and collection (anamoly_data) to hold data
db = client.climate_change
collection = db.anamoly_data


def climate_scrape_func():

        print('Starting Python function')

        #url of national capitals        for scraping
        url = 'https://en.wikipedia.org/wiki/List_of_national_capitals_by_latitude'

        #temperaturate anamolies from https://data.giss.nasa.gov/gistemp/
        zonal_temp_anamolies = pd.read_csv('C:/Users/joelb/Documents/Github/ClimateChange/ZonAnn.Ts+dSST.csv')

        # scrape html table from wikipediea
        tables = pd.read_html(url)

        #grabs the 2nd table on the webpage
        city_by_hemisphere = tables[1]

        #give the table column names
        city_by_hemisphere.columns = ['City','Latitude','Country','Notes']

        #drops the first row that is just headers
        city_by_hemisphere = city_by_hemisphere.drop(0,axis=0)

        #converts the latitude column into numeric
        city_by_hemisphere['Latitude'] = city_by_hemisphere['Latitude'].str.replace('−','-')
        city_by_hemisphere['Latitude'] = pd.to_numeric(city_by_hemisphere['Latitude'])

        #if lat is negative its south, if positive its north
        city_by_hemisphere['Hemisphere'] = np.where(city_by_hemisphere['Latitude']<=0, 'south', 'north')


        #determies what zone of the hemisphere the city is in
        city_by_hemisphere['zone'] = np.where(np.logical_and(                                     np.logical_and(city_by_hemisphere['Latitude']>0,city_by_hemisphere['Latitude']<=24),                                             city_by_hemisphere['Hemisphere'] == 'north'),'EQU-24N',                              np.where(np.logical_and(                                     np.logical_and(city_by_hemisphere['Latitude']>24,city_by_hemisphere['Latitude']<=44),                                             city_by_hemisphere['Hemisphere'] == 'north'),'24N-44N',
                                np.where(np.logical_and( \
                                        np.logical_and(city_by_hemisphere['Latitude']>44,city_by_hemisphere['Latitude']<=64), \
                                                city_by_hemisphere['Hemisphere'] == 'north'),'44N-64N',
                                np.where(np.logical_and( \
                                        np.logical_and(city_by_hemisphere['Latitude']>64,city_by_hemisphere['Latitude']<=90), \
                                                city_by_hemisphere['Hemisphere'] == 'north'),'64N-90N', \
                                np.where(np.logical_and( \
                                        np.logical_and(city_by_hemisphere['Latitude']<0,city_by_hemisphere['Latitude']>=-24), \
                                                city_by_hemisphere['Hemisphere'] == 'south'),'24S-EQU', \
                                np.where(np.logical_and( \
                                        np.logical_and(city_by_hemisphere['Latitude']<-24,city_by_hemisphere['Latitude']>=-44), \
                                                city_by_hemisphere['Hemisphere'] == 'south'),'44S-24S', \
                                np.where(np.logical_and( \
                                        np.logical_and(city_by_hemisphere['Latitude']<-44,city_by_hemisphere['Latitude']>=-64), \
                                                city_by_hemisphere['Hemisphere'] == 'south'),'64S-44S', \
                                np.where(np.logical_and( \
                                        np.logical_and(city_by_hemisphere['Latitude']<-64,city_by_hemisphere['Latitude']>=-90), \
                                                city_by_hemisphere['Hemisphere'] == 'south'),'64S-44S', \
                                        ""))))))))                                  
        year_header = []

        #get column headers for the year to be used later
        year_header = list(zonal_temp_anamolies['Year'])

        #transpose the dataframe for merging
        zonal_temp_anamolies = zonal_temp_anamolies.transpose()

        #merge the city capitals with the zonal temperature data
        climate_df =  city_by_hemisphere.merge(zonal_temp_anamolies, how='left', left_on='zone', right_index=True)

        #rename columns to the appropriate year
        climate_df.rename(columns=dict(zip(climate_df.columns[6:],year_header)),inplace=True)

        #drop a notes column that is not needed
        climate_df = climate_df.drop('Notes',axis=1)

        #sums temperature anomalies over a period of years.  will be the layers on the leaflet map
        climate_df['rng_1880_1910'] = climate_df.iloc[:, 5:36].sum(axis='columns')
        climate_df['rng_1911_1940'] = climate_df.iloc[:, 36:66].sum(axis='columns')
        climate_df['rng_1941_1970'] = climate_df.iloc[:, 66:96].sum(axis='columns')
        climate_df['rng_1971_2000'] = climate_df.iloc[:, 96:126].sum(axis='columns')
        climate_df['rng_2001_2017'] = climate_df.iloc[:, 126:143].sum(axis='columns')

        print('Climate Anamolies gathered and cleaned')
        print('Starting geo code api for city lat/lng')

        #create lat and lgn fields for google maps geocode api
        climate_df["Lat"] = ""
        climate_df["Lng"] = ""

        #set parameters to my gkey
        params = {"key": gkey}

        #loop through cities to get lat and lng for leaflet map
        count = 0
        bad_list = []

        for index, row in climate_df.iterrows():

               
                base_url = "https://maps.googleapis.com/maps/api/geocode/json"

                city = row['City']
                country = row['Country']

                # update address key value
                params['address'] = f"{city},{country}"
            

                # make request, print url
                cities_lat_lng = requests.get(base_url, params=params)
                
                # convert to json
                cities_lat_lng = cities_lat_lng.json()
                
                try:

                        climate_df.loc[index, "Lat"] = cities_lat_lng["results"][0]["geometry"]["location"]["lat"]
                        climate_df.loc[index, "Lng"] = cities_lat_lng["results"][0]["geometry"]["location"]["lng"]

                        count +=1
                        print("num records processed" + str(count))
                except:
                        print("didnt copy street: " +  "city: " + city )
                        bad_list.append(city)
        
                        
        print('Done with geo code api for city lat/lng')

        #drop original lat field so it does not conflict with google lat field
        climate_df = climate_df.drop('Latitude',axis=1)

        # convert columns to string.  to_dict will not accept keys that are not strings
        climate_df.columns = [str(i) for i in climate_df.columns.values.tolist()]

        #turn df into a dictionary for processing into mongo
        climate_dict = climate_df.to_dict('list')

        #pair down the data into a dictionary to go in mongo db
        anamoly_dict = { "City" : climate_dict['City'],
                "Country" : climate_dict['Country'],
                "Lat" : climate_dict['Lat'],
                "Lng" : climate_dict['Lng'],
                "rng_1880_1910" : climate_dict['rng_1880_1910'],
                "rng_1911_1940" : climate_dict['rng_1911_1940'],
                "rng_1941_1970": climate_dict['rng_1941_1970'],
                'rng_1971_2000' : climate_dict['rng_1971_2000'],
                'rng_2001_2017' : climate_dict['rng_2001_2017']
            }

        #  Insert climae anamolies into mongo database
        collection.insert_one(anamoly_dict)


climate_scrape_func()