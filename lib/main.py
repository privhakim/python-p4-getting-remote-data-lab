from GetRequester import GetRequester

# URL of the page you want to fetch data from
URL = 'https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json'

# Create a GetRequester instance
get_requester = GetRequester(URL)

# Fetch and load the JSON data
data = get_requester.load_json()

print(data)
