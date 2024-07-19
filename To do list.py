def main():
  tasks=[]
  while True:
    print("====To-Do List====")
    print("1. Add item")
    print("2. View item")
    print("3. Mark item as Done")
    print("4. Exit")
    choice=input("Enter your choice: ")
    if choice=='1':
      print()
      n_tasks=int(input("How many items do you want to add: "))
      for i in range(n_tasks):
        task=input("Enter item: ")
        tasks.append({"task":task,"done":False})
        print("Items added successfully")
    elif choice=='2':
      print("\nTasks:")
      for index, task in enumerate(tasks):
        status="Done" if task["done"] else "Not Done"
        print(f"{index+1}. {task['task']} ({status})")
    elif choice=='3':
        task_index=int(input("Enter the index of the item to mark as done: "))-1
        if 0<=task_index<len(tasks):
          tasks[task_index]["done"]=True
          print("Item marked as done.")
        else:
          print("Invalid item index.")
    elif choice=='4':
      print("Exiting program.....\n\n~~ Thank you ~~")
      break
    else:
      print("Invalid choice. Please choose from 1 to 4.")
if __name__=="__main__":
  main()