task = []

while True: # Main loop, makes the program run until the user decides to exit
    file = open("todo.txt", "a+") # Open the file in append and read mode
    action = input("Would you like to add a task or view tasks? (add/view/exit): ").strip().lower() # Get user action
    if action == "add": 
        new_task = input("Enter the task you want to add: ").strip() # Get the new task from the user
        file.write(new_task + "\n") # Write the new task to the file
        print(f'Task "{new_task}" added.') 
    
    elif action == "view": # View existing tasks
        file.seek(0) # Move the cursor to the beginning of the file
        tasks = file.readlines() # Read all tasks from the file
        if not tasks:   # Check if there are no tasks
            print("No tasks found.")    
        else: # Display the tasks   
            print("Your tasks:")    
            for idx, task in enumerate(tasks, start=1):   # Enumerate tasks for numbering
                print(str(idx) + ". " + task.strip()) # Print each task with its number
                
    elif action == "exit": # Exit the program
        print("Exiting the To-Do application.")
        file.close()
        break
