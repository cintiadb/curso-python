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


def add_new_country(country_name,num_visit,cities_visited):
    new_country = {
    "country":"Rusia",
    "visits":2,
    "cities":["Moscow","Saint Petersburg"]
    }
    travel_log.append(new_country)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"]) 
print(travel_log)
