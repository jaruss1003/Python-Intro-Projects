italian_food = ["Pasta Bolognese", "Pepperoni Pizza", "Margherita pizza", "Lasagna"]

indian_food = ["Curry", "Chutney", "Samosa", "Naan"]

def find_meal(name, menu):
  return name if name in menu else None

def select_meal(name, food_type):
  if food_type == "Italian": 
    return find_meal(name, italian_food)
  elif food_type == "Indian":
    return find_meal(name, indian_food)
  else: 
    return None
  
  
def display_available_meals(food_type):
  if food_type == "Italian":
    print("Available Italian Meals:")
    for meal in italian_food: 
      print(meal)
  elif food_type == "Indian":
    print("Available Indian Meals:")
    for meal in indian_food:
      print(meal)
  else: 
    print("Invalid food type")

def create_summary(name, amount, type_input):
  order = select_meal(name, type_input)
  if order == name:
    return(f"{amount} {name} found")
  else: 
    return ("Meal not found")
  

print("Welcome to the Food Order System!")
type_input = input("What type of food would you like? ")
display_available_meals(type_input)


name_input = input("Enter the name of the meal you want to order: ")
amount_input = int(input("Enter the amount you would like: "))
create_summary(name_input, amount_input, type_input)
result = create_summary(name_input, amount_input, type_input)
print(result)