################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

#Local scope

def drink_potion():
  potion_strength = 2
  #potion_strength solo es valido dentro de la funcion
  print(potion_strength)
drink_potion()

#Global scope
player_heath =  10

def drink_potion():
  potion_strenght =2
  print(player_heath)

drink_potion()

#there is no block scope
#el if no cuenta como local scope

game_level = 3
enemies = ["skeleton","zombie","alien"]
if game_level <5:
  new_enemy =enemies [0]

#Modifying Global Scope

enemies = 1

def increase_enemies():
  global enemies
  enemies += 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

#podes hacerlo asi 

enemies =1

def increase_enemies():
  print(f"enemies inside function:{enemies}")
  return enemies + 1

enemies = increase_enemies()
print(f"enemies outside function:{enemies}")

#Global constants

PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "@YU_ANGELA"

def calc():
  TWITTER_HANDLE