user_input = "random"

data = []

option_list = ["Add an item",
               "Mark as done",
               "View items",
               "Exit"]

def show_menu(list):
    for number,item in enumerate(list):
        print("{}) {}".format(number+1,item))
    print("")


show_menu(option_list)
user_input = int(input ("Enter your choice: "))

while user_input != option_list.index(option_list[-1])+1:

    if user_input == 1:
        item = input("What item do you want to add to the to-do list ?\n")
        data.append(item)
        print("added",item,"to the list\n")
    
    elif user_input == 2:
        if data:
            print("Your list is:")
            show_menu(data)
            item = int(input("What number to remove from list?\n"))
            print("Removed",data[item-1],"\n")
            data.remove(data[item-1])
        else:
            print("Try adding some items first.\n")

    elif user_input == 3:
        print("Your list is:")
        show_menu(data)
        print("")

    elif user_input == 4:
        print("Goodbye")

    else:
        print("Enter 1,2,3 or 4")
    
    show_menu(option_list)
    user_input = int(input ("Enter your choice: "))

print("Hello"[0])