""""
Create a to-do list, it should have the following features:
1. add tasks
2. remove tasks
3. complete tasks
4. view tasks

"""
task_list = []


class task_options: 
    def adding_tasks(self):
        add_task = input("What task would you like to add? ")
        task_list.append(add_task)
        print(f"Awesome! {add_task} has been added to your To-Do list!")
        print("-----------------------------------------------------------------------")
        main_menu()
        #Next feature is to add the ability to add another task or to exit into the main menu
        

    def deleting_tasks(self):
#       delete_task = input("What task would you like to remove? ")
#       task_list.append(delete_task)
#       print(f"Awesome! {delete_task} has been added removed your To-Do list!")
        pass

    def completing_tasks(self):
#       complete_task = input("What task would you like to complete? ")
#       task_list.append(add_task)
#       print(f"Awesome! {add_task} has been completed from your To-Do list!")
        pass
    def viewing_tasks(self):
        

        pass


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
            options.adding_tasks()
            break
        if choice == '3':
            print("-----------------------------------------------------------------------")
            options.adding_tasks()
            break
        if choice == '4':
            print("-----------------------------------------------------------------------")
            options.adding_tasks()
            break
        if choice == '5':
            print("-----------------------------------------------------------------------")
            print("Have a great day, see you next time!")
            exit
            break
    
name = input("Welcome to your to-do list! What should I call you? ")
print(f"Nice to meet you, {name}!")
main_menu()