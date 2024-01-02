""""
Create a to-do list, it should have the following features:
1. add tasks
2. remove tasks
3. complete tasks
4. view tasks

"""
task_list = []
completed_task_list = []


class task_options: 
#Allows you to add tasks to your task_list
    def adding_tasks(self):
        while True:
            add_task = input("What task would you like to add? Type 'menu' to return to the main menu. \n")
            

            if add_task.lower().strip() == 'menu':
                print("-----------------------------------------------------------------------")
                main_menu()
            else:
                task_list.append(add_task)
                print("-----------------------------------------------------------------------")
                print(f"Awesome! {add_task} has been added to your To-Do list!")
                print("-----------------------------------------------------------------------")
                self.adding_tasks()
                
#Allows you to delete tasks from your task_list
#Will add feature eventually to delete from your Completed Tasks List if user wants
    def deleting_tasks(self):
        while True:   
            print(f"Here are your current tasks: ")
            for index, task in enumerate(task_list, start = 1):
                print(f"\n{index}.{task}")
            print("\nType 'menu' to return back to the main menu")

            delete_choice = input("\nWhich task number would you like to delete? ")
            

            if delete_choice.lower() == 'menu':
                print("-----------------------------------------------------------------------")
                main_menu()

            try :
                delete_choice =int(delete_choice)
                deleted_task = task_list.pop(delete_choice - 1)
                print("-----------------------------------------------------------------------")
                print(f"Task {deleted_task} has been deleted successfully!")
                print("-----------------------------------------------------------------------")
                self.deleting_tasks()

            except(ValueError, IndexError) :
                print("\nPlease select a proper number or 'menu' to return to the main menu: \n")

#Allows you to transfer current tasks from your task_list to completed_task_list
    def completing_tasks(self):
        while True:   
            print(f"Here are your current tasks: ")
            for index, task in enumerate(task_list, start = 1):
                print(f"\n{index}.{task}")
            print("\nType 'menu' to return back to the main menu")

            complete_task = input("What task number would you like to complete? ")
            

            if complete_task.lower() == 'menu':
                print("-----------------------------------------------------------------------")
                main_menu()

            try :
                complete_task =int(complete_task)
                complete_task = task_list.pop(complete_task - 1)
                completed_task_list.append(complete_task)
                print("-----------------------------------------------------------------------")
                print(f"Task {complete_task} has been completed successfully!")
                print("-----------------------------------------------------------------------")

            except(ValueError, IndexError) :
                print("\nPlease select a proper number or 'menu' to return to the main menu: \n")


#Allows you to choose to view your current tasks and your completed tasks
    def viewing_tasks(self):
        print("\nWhich tasks would you like to see? Type 'menu' to return to the main menu.")
        print("\n1. Current Active Tasks")
        print("\n2. Completed Task List")
        task_list_options = input("\nEnter Decision Here: ")
        print("-----------------------------------------------------------------------")

        if task_list_options == '1':
            print("-----------------------------------------------------------------------")
            print("Here are your current tasks: ")
            for index, task in enumerate(task_list, start=1):
                print(f" {index}.{task}")
                self.viewing_tasks()

        elif task_list_options == '2':
            print("Here are your completed tasks: ")
            for index, task in enumerate(completed_task_list, start=1):
                print(f" {index}.{task}")
                print("-----------------------------------------------------------------------")
                self.viewing_tasks()

        elif task_list_options.lower().strip() =='menu':
            print("-----------------------------------------------------------------------")
            main_menu()

        else:
            print("-----------------------------------------------------------------------")
            print("\nPlease select a proper option.\n")
            print("-----------------------------------------------------------------------")
            self.viewing_tasks()


        

#contains all the options available
def main_menu():
    
    print("How can I help you today?")

    options = task_options()

    while True:
        print("\nWe have a few options for you.")
        print("\n1. Add a task to your list")
        print("\n2. Remove a task to your list")
        print("\n3. Complete a task on your list")
        print("\n4. View tasks in your list")
        print("\n5. I\'m all done for now")
        print("-----------------------------------------------------------------------")
        choice = input("\nEnter your choice here:  ")
        

        if choice == '1':
            print("-----------------------------------------------------------------------")
            options.adding_tasks()
            break
        if choice == '2':
            print("-----------------------------------------------------------------------")
            options.deleting_tasks()
            break
        if choice == '3':
            print("-----------------------------------------------------------------------")
            options.completing_tasks()
            break
        if choice == '4':
            print("-----------------------------------------------------------------------")
            options.viewing_tasks()
            break
        if choice == '5':
            print("-----------------------------------------------------------------------")
            print("Have a great day, see you next time!")
            exit()
        else :
            print("-----------------------------------------------------------------------")
            print("\nPlease select a proper option.\n")
            print("-----------------------------------------------------------------------")
            main_menu()
            
    
name = input("Welcome to your to-do list! What should I call you? ")
print(f"Nice to meet you, {name.title()}!")
print("-----------------------------------------------------------------------")
main_menu()
