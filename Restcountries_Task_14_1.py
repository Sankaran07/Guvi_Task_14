# we to import the libry

import requests
import json

# information from json structure
# using https://restcountries.com/v3.1/all url 
# create class constructor for taking input the mentioned above url 
class Countries:
    def __init__(self, rest_api):
        self.all_details = rest_api

    # create a method that will fetch all the json data from url mentioned above
    def fetch_all_details(self):
        
        # to get contents from  requests.get()
        request_get = requests.get(self.all_details)
        
        # to get content in json format by using json() 
        response = request_get.json()
        
        #  if we get 200 status code. its successfull to access the webpage
        status_code = request_get.status_code
        modify_api = json.dumps(response, indent=2)
        print(f' signal_status: {status_code}')
        print(f'total countries are in a Restcountry:{len(response)}')
        #print(response)

    # i created the method,  that will display all name of countries, currency and currency symbols
    def get_name_currencies(self, name_currency):
        request_name = requests.get(name_currency)
        response_name = request_name.json()
        name_list = []
        for api_name in response_name:
            name = api_name["name"]
            currency = api_name['currencies']
            detail = {
                'name': name,
                'curr_name':currency
            }
            name_list.append(detail)
        print("we will get all those names, currency and currency symbol in below list:")
        return name_list
    
    # i created the method, that will display all of those countries which have Dollar as its currency to get and find
    def Dollar_currency(self, url_dollar):
        request_currency = requests.get(url_dollar)
        response_currency = request_currency.json()
        print("These countries are using Dollar as its currency:")
        print(response_currency)
        print(f' total number of countries using Dollar as its currency are:{len(response_currency)}')
        
        
    # i created the method, that will display all of those countries which have Euro as its currency (to find)
    def Euro_currency(self, url_Euro):
        request_Euro = requests.get(url_Euro)
        response_euro = request_Euro.json()
        list_euro = []
        for list in response_euro:
            name = list['name']['common']
            currency = list['currencies']
            data={
                'name':name,
                'currencies':currency
            }
            list_euro.append(data)
            
        print("In below list of countries are using Euro as its currency:")
        print(list_euro)
        print(f'total number of countries using Euro as its currency: {len(list_euro)}')

Url = Countries("https://restcountries.com/v3.1/all")

Url.fetch_all_details()
print(Url.get_name_currencies("https://restcountries.com/v3.1/all?fields=name,currencies"))
Url.Dollar_currency("https://restcountries.com/v3.1/currency/USD")
Url.Euro_currency("https://restcountries.com/v3.1/currency/EUR")
