def oldest_person(people: list):
    def get_birth_year(person):
        return person[1]
    oldest = min(people, key=get_birth_year)
    return oldest[0]  


p1 = ("Adam", 1977)
p2 = ("Ellen", 1985)
p3 = ("Mary", 1953)
p4 = ("Ernest", 1997)
people = [p1, p2, p3, p4]

print(oldest_person(people))