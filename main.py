task_list = []
status_list = []

def load_my_tasks():
    try:
        file = open("tasks.txt", "r")
        for line in file:
            clean_line = line.replace("\n", "")
            
            parts = clean_line.split(",")
            
            if len(parts) == 2:
                task_list.append(parts[0])
                status_list.append(parts[1])
        file.close()
    except:
        pass

def save_my_tasks():
    file = open("tasks.txt", "w")
    for i in range(len(task_list)):
        file.write(task_list[i] + "," + status_list[i] + "\n")
    file.close()

def add_task():
    name = input("Enter task name: ")
    task_list.append(name)
    status_list.append("Not Done")
    save_my_tasks()
    print("Task added successfully!")

def view_tasks():
    if len(task_list) == 0:
        print("Your list is empty!")
        return
        
    print("\n--- Current Tasks ---")
    for i in range(len(task_list)):
        print(str(i + 1) + ". [" + status_list[i] + "] " + task_list[i])
    print("--------------------")

def mark_done():
    view_tasks()
    if len(task_list) == 0:
        return
        
    choice = input("Enter the number of the task you finished: ")
    index = int(choice) - 1
    
    if index >= 0 and index < len(task_list):
        status_list[index] = "Done"
        save_my_tasks()
        print("Task marked as Done!")
    else:
        print("That number is not on the list!")

def delete_task():
    view_tasks()
    if len(task_list) == 0:
        return
        
    choice = input("Enter the number of the task to delete: ")
    index = int(choice) - 1
    
    if index >= 0 and index < len(task_list):
        del task_list[index]
        del status_list[index]
        save_my_tasks()
        print("Task removed!")
    else:
        print("Invalid number layout selection!")

# --- MAIN LOOP RUNNER ---
load_my_tasks()
while True:
    print("\n=== MENU ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Finish Task")
    print("4. Delete Task")
    print("5. Exit")
    
    user_choice = input("Select an option (1-5): ")
    
    if user_choice == "1":
        add_task()
    elif user_choice == "2":
        view_tasks()
    elif user_choice == "3":
        mark_done()
    elif user_choice == "4":
        delete_task()
    elif user_choice == "5":
        print("Goodbye!")
        break
    else:
        print("Wrong input. Select from 1 to 5.")
