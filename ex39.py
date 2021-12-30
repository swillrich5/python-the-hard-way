# create a mapping of state abbreviations

states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'Texas': 'TX',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI',
    'Colorado': 'CO'
}

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Florida',
    'TX': 'Austin',
    'CO': 'Denver',
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'
cities['FL'] = 'Orlando'

# print out some cities
print('-' * 10)
print('NY State has: ', cities['NY'])
print('OR State has: ', cities['OR'])

# print some states
print('-' * 10)
print("Michigan's abbreviation is:", states['Michigan'])
print("Texas' abbreviation is:", states['Texas'])

# print all state abbreviations
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

# print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# now do both at the same time
print('-' * 10)

for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 10)
# safely get an abbreviation by state that might not be there
state = states.get('Arkansas')

if not state:
    print("Sorry, no Arkansas.")

# get a cty with a default value
city = cities.get('AR', 'Does Not Exist')
print(f"The city for the state AR is: {city}")
