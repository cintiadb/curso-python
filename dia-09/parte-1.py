programming_dictionary = {
 "Bug": "An error in a program that prevents the program from running as expected.", 
 "Function": "A piece of code that you can easily call over and over again.",
}

print(programming_dictionary["Bug"])


#Adding new items to dictionary.
programming_dictionary["Loop"]="The action of doing something over and over again"
print(programming_dictionary)

#Create an empty dictionary
empty_dictionary = {}

#Wipe and existing dictionary
programming_dictionary={}
print(programming_dictionary)

#Edit and item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary)

#Loop trought in dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

#Nesting

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

#Nesting a list in a Dictionary
#Nesting dictionary in a dictionary

travel_log = {
    "France":{"cities_visited":["Paris","Lille","Dijon"], "total_visits" :12}, 
    "Germany": ["Berlin","Hamburg","Stuttgart"],
}


#Nesting dictionary in a list
travel_log = [
    {
    {"country":"France",
     "cities_visited":["Paris","Lille","Dijon"], 
     "total_visits" :12
     }, 
    {"country":"Germany",
     "cities_visited": ["Berlin","Hamburg","Stuttgart"],
     "total_visits":5}
    }
]

