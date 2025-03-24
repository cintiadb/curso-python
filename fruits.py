def read_fruits():
    fruits_dict = {}

    with open("fruits.csv") as new_file:
        for line in new_file:
            print(line)
            line = line.replace('\n', '')  
            fruit, price = line.split(';')
            fruits_dict[fruit] = float(price)
    return fruits_dict

read_fruits()
    
 



