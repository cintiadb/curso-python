def dict_of_numbers():
        d = { 0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five',
          6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten',
          11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen',
          15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen',
          19 : 'nineteen', 20 : 'twenty',
          30 : 'thirty', 40 : 'forty', 50 : 'fifty', 60 : 'sixty',
          70 : 'seventy', 80 : 'eighty', 90 : 'ninety' }
        
        numbers_dict = {}
        for num in range(100):  # Loop from 0 to 99
            if num in d:  
                numbers_dict[num] = d[num]  # Directly store if already in dictionary
            else:
                tens = num // 10 * 10  # Get the tens place (e.g., 45 → 40)
                ones = num % 10  # Get the ones place (e.g., 45 → 5)
                numbers_dict[num] = d[tens] + '-' + d[ones]  # Combine parts
    
        return numbers_dict



numbers = dict_of_numbers()
print(numbers[2])
print(numbers[11])
print(numbers[45])
print(numbers[99])
print(numbers[0])