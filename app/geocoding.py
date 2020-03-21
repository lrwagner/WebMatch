import requests

def get_gps(address):
    # Set up your Geocoding url
    with open('api/apikey', 'r') as key:
        api_key = key.read()
    geocode_url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}"
 
    # Ping google for the reuslts:
    results = requests.get(geocode_url)
    # Results will be in JSON format - convert to dict using requests functionality
    results =  results.json()

    # if there's no results or an error, return empty results.
    if len(results['results']) == 0:    
        output = {
            "formatted_address" : None,
            "latitude": None,
            "longitude": None,
            "accuracy": None,
            "google_place_id": None,
            "type": None,
            "postcode": None
        }
    else:    
        answer = results['results'][0]
        output = {
            "formatted_address" : answer.get('formatted_address'),
            "latitude": answer.get('geometry').get('location').get('lat'),
            "longitude": answer.get('geometry').get('location').get('lng'),
            "accuracy": answer.get('geometry').get('location_type'),
            "google_place_id": answer.get("place_id"),
            "type": ",".join(answer.get('types')),
            "postcode": ",".join([x['long_name'] for x in answer.get('address_components') 
                                  if 'postal_code' in x.get('types')])
        }

    return output

# runs only if you run geocoding.py
if __name__ == "__main__":
    q = get_gps(address='Harzbachstraße 16, Illingen, Germany')
    print(q)