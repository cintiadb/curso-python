

def search_by_time(filename: str, prep_time: int):
    recipes_dict = {}
    current_recipe = []
    with open("recipes1.txt") as new_file:
        for line in new_file:
            if line == "\n":
                # print("nex recipe incoming!!")
                # Create dictionary structrure for ease of use
                recipes_dict[current_recipe[0]] = {}
                recipes_dict[current_recipe[0]]["name"] = current_recipe[0]
                recipes_dict[current_recipe[0]]["time"] = int(current_recipe[1])
                recipes_dict[current_recipe[0]]["ingredients"] = current_recipe[2:]

                # reset uurent list
                current_recipe = []
                # print(recipes_dict)
                # print(current_recipe)
            else:
                current_recipe.append(line.replace("\n", ""))

        # add last item of the file

        recipes_dict[current_recipe[0]] = {}
        recipes_dict[current_recipe[0]]["name"] = current_recipe[0]
        recipes_dict[current_recipe[0]]["time"] = int(current_recipe[1])
        recipes_dict[current_recipe[0]]["ingredients"] = current_recipe[2:]
        
        recipes_found_by_time = []
        for key, value in recipes_dict.items():
            if value["time"] == prep_time:
                # print(f"{key}, preparation time {value["time"]} min")
                recipes_found_by_time.append(f"{key}, preparation time {value["time"]} min")
        
        return recipes_found_by_time


# ------------------------------------------------------

# with open("recipes1.txt") as new_file:
#    for line in new_file:
#        print(repr(line))


found_recipes = search_by_time("recipes1.txt", 60)


for recipe in found_recipes:
    print(recipe)