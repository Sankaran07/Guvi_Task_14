# first we need to import the libary
import requests
import json

# create a class for breweries
class Breweries:
    #__init__funtion
    def __init__(self, url):
        self.state1 = url
        # Send a GET request to the API
        self.request = requests.get(self.state1)
        self.response = self.request.json()
    def brewery_details(self):
        # Check if the request was successful (status code 200)
        if self.request.status_code == 200:
            # to get all brewery names and counts
            count_no_breweries =0
            list_box_1 =[]
            for breweries_content in (self.response):
                count_no_breweries += 1
                name_of_breweries = breweries_content['name']
                data = {
                    'name':name_of_breweries
                }
                list_box_1.append(data)
            print(f'Name of Breweries are in {state} are: {list_box_1}')
            print(f'total count of breweries in {state} is: {count_no_breweries}')
        else:
            print("failed to retrive data from api webpage")

    # count and list how many breweries have webpage in state of Alaska, Maine, New-york.
    def list_brewery_website(self):
            list_website_brewery_alaska = []
            count_web = 0
            
            for count_website in self.response:
                if count_website['website_url']:
                    list_website_brewery_alaska.append(count_website['name'])
                    count_web += 1
            print(f'total counts of breweries have website in {state} :{count_web}')
            print(f'list of city have website in {state} states are:{list_website_brewery_alaska}')


    # count number of types of breweries present in individual cities in states
    def count_individual_brewery(self):
        # create a dict
            city_brewery_count = {}
            
            # Iterate through each brewery in given state name
            for brewery in self.response:
                city = brewery.get('city')
                brewery_type = brewery.get('brewery_type')
                # Count the types of breweries in each city
                if city in city_brewery_count:
                    if brewery_type not in city_brewery_count[city]:
                        city_brewery_count[city].append(brewery_type)
                    else:
                        city_brewery_count[city] = [brewery_type]
                # Print the counts of brewery types in each city
                print(f"City:{city}")
                print(f"Number of Brewery Types: {len(brewery_type)}")




state = input("enter a state name: ")

Url = Breweries(f"https://api.openbrewerydb.org/v1/breweries?by_state={state}")
Url.brewery_details()
Url.list_brewery_website()
Url.count_individual_brewery()

