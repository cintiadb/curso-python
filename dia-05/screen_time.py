filename = input("Filename: ")
starting_date = input("Starting date: ")

num_days = int(input("How many days: "))

with open(filename, "w") as file:
    file.write(f"Starting date: {starting_date}\n")
    file.write(f"How many days: {num_days}\n")
    current_date = starting_date

    for i in range(num_days):
        screen_time = input(f"Screen time {current_date}: ")
   
        file.write(f"Screen time {current_date}: {screen_time}\n")
        
        day, month, year = map(int, current_date.split('.'))
        if day < 31:  
            day += 1
        else:
            day = 1
            if month < 12:
                month += 1
            else:
                month = 1
                year += 1
        current_date = f"{day:02d}.{month:02d}.{year}"

print(f"Data stored in file {filename}")