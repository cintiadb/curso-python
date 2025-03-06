def most_common_character(s):
    return max(s, key=s.count)

first_string = "abcdbde"
print(most_common_character(first_string))

second_string = "exemplaryelementary"
print(most_common_character(second_string))

