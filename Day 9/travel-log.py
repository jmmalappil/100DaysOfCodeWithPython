country = input("Please provide the country name:") # Add country name
visits = int(input("Please provide the number of visits to the country:")) # Number of visits
list_of_cities = eval(input("Please provide the cities visited in the country:")) # create list from formatted string

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]
# Do NOT change the code above 👆

# TODO: Write the function that will allow new countries
# to be added to the travel_log.
def add_new_country(country, visits, list_of_cities):
    temp_dict={}
    temp_dict["country"]=country
    temp_dict["visits"]=visits
    temp_dict["cities"]=list_of_cities
    travel_log.append(temp_dict)


# Do not change the code below 👇
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")