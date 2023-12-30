""""
Create a to-do list, it should have the following features:
1. add tasks
2. remove tasks
3. complete tasks
4. view tasks

"""
task_list = []


class task_options: 
    #Next feature is to add the ability to add another task
    def adding_tasks(self):
        add_task = input("What task would you like to add? ")
        task_list.append(add_task)
        print(f"Awesome! {add_task} has been added to your To-Do list!")
        print("-----------------------------------------------------------------------")
        main_menu()
                
    #Next feature is to add the ability to delete another task
    def deleting_tasks(self):
        while True:   
            print(f"Here are your current tasks: ")
            for index, task in enumerate(task_list, start = 1):
                print(f"\n{index}.{task}")
            print("\nType 'menu' to return back to the main menu")

            delete_choice = input("\nWhich task would you like to delete? ")

            if delete_choice.lower() == 'menu':
                print("-----------------------------------------------------------------------")
                main_menu()

            try :
                delete_choice =int(delete_choice)
                deleted_task = task_list.pop(delete_choice - 1)
                print("-----------------------------------------------------------------------")
                print(f"Task {deleted_task} has been deleted successfully!")
                print("-----------------------------------------------------------------------")

            except(ValueError, IndexError) :
                print("\nPlease select a proper number or 'menu' to return to the main menu: \n")

    #Next feature to be added, this will probably be a boolean method to transfer tasks that are completed
    #From the task_list [] to completed_task_list[]
    #I'll need to look into how to transfer items from 1 list to another
    def completing_tasks(self):
#       complete_task = input("What task would you like to complete? ")
        pass

    #itemizes all tasks inputted
    def viewing_tasks(self):
        print("Here are your current tasks: ", task_list)
        for index, task in enumerate(task_list, start = 1):
            print(f" {index}.{task}")

        

#contains all the options available, still working on completing tasks option.
#future feature will be to add and delete multiple tasks without going back to the main menu everytime. 
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
            
            pass
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
