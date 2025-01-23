"""
print("Welcome to the tip calculator")
total = float(input("What was the total bill?$"))
tip = int(input("What percentage tip would you like to give? 10,12,or 15?"))
people = int(input("How many people to split the bill?"))
tip_as_porcentage = tip / 100
total_tip_amount = total * tip_as_porcentage
total_bill = total + total_tip_amount
bill_per_person = total_bill / people
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay {final_amount}")
"""
"""
number = int(input("Which number do you want to know if it is even or odd?"))
if number % 2 == 0 :
 print("even")
if number % 2 != 0 :
 print("odd")
 """
"""
height = float(input("enter your height in m:"))
weight = float(input("enter your weight in kg:"))
bmi = round(weight / height ** 2)
print(bmi)
if bmi < 18.5:
  print("Your BMI is {bmi} and you are underweight")
elif bmi < 25:
  print("Your BMI is {bmi} and you are normal weight")
elif bmi > 25:
  print("you are overweight")
elif bmi > 30:
  print("you are obese")
else:
    print("clinically obese")
    """

"""
year = int(input("Which year do you want to check?"))
if year %4 == 0:
  if year % 100 == 0:
    if year %400 == 0:
      print("leap year")
    else:
      print("not leap year")
  else:
    print("leap year")   
else:
  print("not leap")


""""""print("Welcome yto the rollercoaster")
height = int(input("what is yout height in cm"))

if height >=120:
  print("You can ride the rollercoaster")
  age = int(input("What is your age?"))
  if age < 12:
    bill =5
    print("Plase pay $5")
  elif age <= 18:
    bill = 7
    print("Please pay $7")
  else:
    bill = 12
    print("Please pay $12")

  wants_photo = input("Do yoy want a photo taken) Y or N")
  if want_photo == "y"
    bill += 3
  print (f"Your final bill is {bill}")
  
else:
  print:("Sorry you have to grow taller before you can ride")
  """


"""
print("Welcome yo Phyton Pizza Deliveries")
size = input("What size pizza do you Want? S, M ,L  ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input ("Do you want extra cheese? Y or N ")
bill = 0

if size == "S":  
  bill += 15
  if add_pepperoni == "Y":
    bill += 2 
    
elif size == "M":
  bill += 20
  if add_pepperoni == "Y":
    bill +=3   
    
elif size == "L":
  bill += 25
  if add_pepperoni == "Y":
    bill +=3

else:
  print("we do not have this size available")
  
if extra_cheese == "Y":
  bill += 1
  print(f"Your final bill is {bill}")
  
else:
  print(f"Your final bill is {bill}")
  """
"""
print("Welcome yto the rollercoaster")
height = int(input("what is yout height in cm"))

if height >=120:
  print("You can ride the rollercoaster")
  age = int(input("What is your age?"))
  if age < 12:
    bill =5
    print("Plase pay $5")
  elif age <= 18:
    bill = 7
    print("Please pay $7")
  elif age >= 45 and age <= 55:
    bill = 0
    print("Please pay $0")
  else:
    bill = 12
    print("Please pay $12")

  wants_photo = input("Do you want a photo taken) Y or N")
  if wants_photo == "y":
    bill += 3
  print (f"Your final bill is {bill}")

else:
  print:("Sorry you have to grow taller before you can ride")

"""
"""
print("Welcome to the love calculator")
name1 = input("What is your name?\n")
name2 = input("What is their name?\n")

lower_case_name1 =name1.lower()
lower_case_name2 =name2.lower()

T =lower_case_name1.count("t") 
R =lower_case_name1.count("r")
U =lower_case_name1.count("u")
E =lower_case_name1.count("e")
L =lower_case_name1.count("l")
O =lower_case_name1.count("o")
V =lower_case_name1.count("v")
E =lower_case_name1.count("e")
T2 =lower_case_name2.count("t") 
R2 =lower_case_name2.count("r")
U2 =lower_case_name2.count("u")
E2 =lower_case_name2.count("e")
L2 =lower_case_name2.count("l")
O2 =lower_case_name2.count("o")
V2 =lower_case_name2.count("v")
E2 =lower_case_name2.count("e")


score = T+R+U+E+L+O+V+E+T2+R2+U2+E2+L2+O2+V2+E2

if score <10 or score >90 :
  print(f"Your score is {score} you go together like coke and mentos")
elif score >40 and score <50:
  print(f"Your score is {score}, you are alright together")
else:
  print(f"Your score is {score}")

"""
"""

print("Welcome to the love calculator")
name1 = input("What is your name?\n")
name2 = input("What is their name?\n")

lower_case_name1 =name1.lower()
lower_case_name2 =name2.lower()

names_together = name1.lower() + name2.lower()

T =names_together.count("t") 
R =names_together.count("r")
U =names_together.count("u")
E =names_together.count("e")
L =names_together.count("l")
O =names_together.count("o")
V =names_together.count("v")
E =names_together.count("e")


score1 = (T+R+U+E)
score2 =L+O+V+E
score3= str(score1)+str(score2)

if int(score3) <10 or int(score3) >90 :
  print(f"Your score is {score3} you go together like coke and mentos")
elif int(score3) >40 and int(score3) <50:
  print(f"Your score is {score3}, you are alright together")
else:
  print(f"Your score is {score3}")




"""
"""print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
question1 = input("Would you chose go right or left?\n")
question1=question1.lower()

if question1 == "left":
  question2=input("Would you prefer swim or wait?")
  if question2 == "wait":
    question3= input("Which door would you like to open? red, blue or yellow")
    if question3 == "red":
      print("Burned by fire. Game over")
    elif question3 == "blue":
      print("Eaten by beasts. Game over")
    elif question3 == "yellow":
      print("You win!")
    else:
      print("Game over")
  else:
    print("Attack by trout. Game over") 
    
else: 
  "Game over"

question2 = "wait"
question2= question2.lower()

question3="yellow"
question3 = question3.lower()
"""
"""
import random

random_integer = random.randint(1,10)
print(random_integer)

random_float = random.random() *5
print(random_float)

"""
#import random

#random_integer = random.randint(0,1)

#if random_integer == 0:
  #print("head")
#if random_integer == 1:
 # print("tail")

#states_of_america = ["Delaware","Pennsylvani","NYC"]
#print(states_of_america[0])

""""names_string= input("Give me everybody's name, separated by a comma.")
names = names_string.split(",")
print(names)

nombres = len(names)

import random
random_choice = random.randint(0,nombres-1)

person_who_will_pay =names [random_choice]

print(f"el que paga la cuenta es {person_who_will_pay}")"""

""""
row1 = ["⬜","⬜","⬜"]
row2 = ["⬜","⬜","⬜"]
row3 = ["⬜","⬜","⬜"]
map = [row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure?")

horizontal = int(position[0])
vertical = int(position[1]) 

map[vertical - 1][horizontal - 1] = "X"
print(f"{row1}\n{row2}\n{row3}")
"""

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
"""
you = input("What do you choose? Type 0 for rock, 1 for Paper or 2 for Scissors.")
your_decision = int(you) 
if your_decision == 0:
  print(rock)
if your_decision == 1:
  print(paper)
if your_decision == 2:
  print(scissors)

import random
computer = print("Computer chose:") 
computer = random.randint (0,2)
print(computer)
computer_decision =int(computer)
if computer_decision == 0:
  print(rock)
if computer_decision == 1:
  print(paper)
if computer_decision == 2:
  print(scissors)

if your_decision >2 or your_decision <0:
  print("You chose an invalid number.You lose")
if your_decision == 0 and computer_decision ==0:
  print("Draw")
if your_decision == 0 and computer_decision ==1:
  print("You lose")
if your_decision ==0 and computer_decision ==2:
  print("You win")
if your_decision == 1 and computer_decision ==0:
  print("You win")
if your_decision == 1 and computer_decision ==1:
  print("Draw")
if your_decision ==1 and computer_decision ==2:
  print("You lose")
if your_decision == 2 and computer_decision ==0:
  print("You lose")
if your_decision == 2 and computer_decision ==1:
  print("You win")
if your_decision ==2 and computer_decision ==2:
  print("Draw")

"""
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
"""
you = input("What do you choose? Type 0 for rock, 1 for Paper or 2 for Scissors.")
your_decision = int(you) 
games_images = [rock,paper,scissors]
if your_decision >2 or your_decision <0:
  print("You chose an invalid number.You lose")
else:
  print(games_images[your_decision])


import random
computer = print("Computer chose:") 
computer = random.randint (0,2)
computer_decision =int(computer)
print(games_images[computer_decision])


if your_decision == 0 and computer_decision ==0:
  print("Draw")
if your_decision == 0 and computer_decision ==1:
  print("You lose")
if your_decision ==0 and computer_decision ==2:
  print("You win")
if your_decision == 1 and computer_decision ==0:
  print("You win")
if your_decision == 1 and computer_decision ==1:
  print("Draw")
if your_decision ==1 and computer_decision ==2:
  print("You lose")
if your_decision == 2 and computer_decision ==0:
  print("You lose")
if your_decision == 2 and computer_decision ==1:
  print("You win")
if your_decision ==2 and computer_decision ==2:
  print("Draw")
"""

#fruits = ["Apple","Peach","Pear"]
#for fruit in fruits:
#  print(fruit)
"""
student_heights = input("input a list of student heights").split()
for n in range(0,len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(student_heights)

total_height =0
for height in student_heights:
  total_height += height
print(total_height)

number_of_student = 0
for student in student_heights:
  number_of_student += 1
print(number_of_student)

average_height = round(total_height / number_of_student)
print(average_height)

"""
"""
#va probando con cada variable si es mayor o no a la anterior!!!
student_scores = input("input a list of student scores").split()
for n in range(0,len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
max_score = 0
for score in student_scores:
  if score > max_score:
    max_score = score 
print(max_score)
"""
"""
total = 0
for number in range (1,101):
  if number % 2 == 0:
    total +=number
print(total)
"""
"""
number = 0

for number in range (1,101):
  if number % 3 == 0 and number %5 ==0 :
    print("FizzBuzz")
  elif number % 5 == 0:
    print("Buzz")
  elif number % 3 == 0:
    print("Fizz")
  else:
    print(number)
    print("hola")

  """









  
  
  





