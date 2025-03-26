def search_by_name(filename: str, word: str):
    found_lines = []
    word_lower = word.lower()
    with open("recipes1.txt") as new_file:
        for line in new_file:
            if word_lower in line.lower():
                found_lines.append(line)
    return found_lines


found_recipes = search_by_name("recipes1.txt", "cake")

for recipe in found_recipes:
    print(recipe)

