# Business Search      URL -- 'https://api.yelp.com/v3/businesses/search'
# Business Match       URL -- 'https://api.yelp.com/v3/businesses/matches'
# Phone Search         URL -- 'https://api.yelp.com/v3/businesses/search/phone'

# Business Details     URL -- 'https://api.yelp.com/v3/businesses/{id}'
# Business Reviews     URL -- 'https://api.yelp.com/v3/businesses/{id}/reviews'

import requests


# Define a business ID
business_id = '4AErMBEoNzbk7Q8g45kKaQ'


# Define my API Key and My Header
API_KEY = 'j0z9jMgY48RfaiFmgMOCBbnZToQFG6yk2IK8wYrf7nkKGCFSCJWUMOn1hwTs58h9k5CkbDcMevd9lC12hQkuIBj9iYDJiiasUcUOll6GX1foN5fPzzrT-qboZEeFYnYx'

ENDPOINT = 'https://api.yelp.com/v3/businesses/search'

HEADERS = {'Authorization': 'bearer %s' % API_KEY}


# Define my parameters of the search
# BUSINESS SEARCH PARAMETERS - EXAMPLE
# PARAMETERS = {'term': 'food',
#               'limit': 10,
#               'offset': 5,
#               'radius': 8000,
#               'price': '1',
#               'location': '33132'}


# Make a request to the Yelp API
# response = requests.get(url=ENDPOINT,
#                         params=PARAMETERS,
#                         headers=HEADERS)


# # Convert the JSON String
# business_data = response.json()


# # print the response
# print(business_data)
def convert_miles(miles):
    """converts miles to meters

        >>> convert_miles(2)
        3218

        >>> convert_miles(5)
        8046
    """
    meters = int(miles * 1609.344)
    return meters


def get_business_data(zip, category, radius):

    parameters = {'term': 'food',
                  'limit': 20,
                  'radius': convert_miles(radius),
                  'categories': category,
                  'location': zip}
    resp = requests.get(url=ENDPOINT, params=parameters, headers=HEADERS)
    business_json = resp.json()
    return business_json


def user_get_business_data(zip, category, radius, price):

    parameters = {'term': 'food',
                  'limit': 20,
                  'radius': convert_miles(radius),
                  'categories': category,
                  'price':price,
                  'location': zip}
    resp = requests.get(url=ENDPOINT, params=parameters, headers=HEADERS)
    business_json = resp.json()
    return business_json
 ########Yelp API TESTS################
        # test for get_biz
######################################