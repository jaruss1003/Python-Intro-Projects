todo_list = []
while True:
  if not todo_list:
    print("Your ToDo list is empty")
  else:
   index = 1
  for item in todo_list:
    print(f"{index}. {item}")
    index += 1 

  print("Options:")
  print("1) Add Task")
  print("2) Remove Task")
  print("3) Quit")

  choice = input("Enter your choice (1,2,or 3): ")

  if choice == "1": 
    print("Adding Task")
    new_task = input("Enter the task you want to add: ")
    todo_list.append(new_task)
    print(f"The task '{new_task}' has been added to the list")
  elif choice == "2":
   if len(todo_list) == 0:
    print("The ToDo list is empty")
   if len(todo_list) != 0:
    todo_list.pop()
  elif choice == "3":
    print("Quitting")
    break
    