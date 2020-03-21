import requests


def get_gps(address):
    # Set up your Geocoding url
    geocode_url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}"

        
    # Ping google for the reuslts:
    results = requests.get(geocode_url)
    # Results will be in JSON format - convert to dict using requests functionality
    return results.json()


q = get_gps(address='18 Grafton Street, Dublin, Ireland')
print(q)