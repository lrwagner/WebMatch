import requests


def get_gps(address):
    # Set up your Geocoding url
    with open('api/apikey', 'r') as key:
        api_key = key.read()
    print(api_key)
    geocode_url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}"

        
    # Ping google for the reuslts:
    results = requests.get(geocode_url)
    # Results will be in JSON format - convert to dict using requests functionality
    return results.json()


q = get_gps(address='Brauerstraße 17, Saarbrücken, Germany')
print(q)