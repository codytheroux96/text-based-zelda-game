# Cody Theroux


def show_instructions(): # Function to show the instructions to the user
    print("Text-Based Zelda Adventure Game")
    print("The evil Ganondorf has taken over Hyrule and it is up to Link, the Hero of Time, to save the kingdom!")
    print("In order to move Link, you must enter the commands: 'go north', 'go south', 'go east', 'go west', in order to navigate the map")
    print("The room you will start in is Hyrule Field")
    print("When you enter a room, you will be shown an item if you have not collected it yet. You can collect this item by typing 'get [item name]'")
    print("In order to view your inventory and current location, type: 'show status'")
    print("In order to win, you must collect all items from every room BEFORE you encounter Ganondorf. If you encounter Gananondorf before collecting all items, you lose!")
    print("There are 6 rooms that you must collect items from before you reach the room, where Ganondorf is located! The starting room and the room with Ganondorf do not have items in them!")
    print("At any point you can show the instructions again by typing 'show instructions'")
    print("Type 'quit' to exit the game")
    print("Good luck!")
    print("------------------------------------------------------------------------------------------------------------------------")

def main():
    global current_room  # Declare current_room as a global variable

    rooms = { # Create a dictionary of rooms, their available exits, and the items in each room
        'Hyrule Field': {'North': 'Temple of Time', 'South': 'Lost Woods', 'East': 'Zoras Domain', 'West': 'Gerudo Desert', 'item': None}, #Starting room
        'Temple of Time': {'South': 'Hyrule Field', 'East': 'Hyrule Castle', 'item': 'Master Sword'},
        'Lake Hylia': {'North': 'Zoras Domain', 'West': 'Lost Woods', 'item': 'Hookshot'},
        'Goron City': {'South': 'Zoras Domain', 'item': 'Hylian Shield'},
        'Gerudo Desert': {'East': 'Hyrule Field', 'item': 'Silver Gauntlets'},
        'Lost Woods': {'North': 'Hyrule Field', 'East': 'Lake Hylia', 'item': 'Fairy Bow'},
        'Zoras Domain': {'North': 'Goron City', 'West': 'Hyrule Field', 'South': 'Lake Hylia', 'item': 'Magic'},
        'Hyrule Castle': {'item': None}, # Ganondorf (the villain) is in this room
    }

    inventory = [] # Create an empty list to store the user's inventory
    current_room = 'Hyrule Field' # Set the starting room


    def show_status(): # Function to show the user's current location, inventory, and available items in the room
        print("You are in the", current_room)
        print("Inventory:", inventory)
        if rooms[current_room]['item']: print("Items in this room:", rooms[current_room].get('item')) # Check if there is an item in the room
        else: print("There is no item in this room!") # If there is no item in the room, print that there are no items in the room
    
    show_instructions() # Call the show_instructions function
    show_status() # Call the show_status function

    def add_to_inventory(item_name): # Function to add an item to the user's inventory
        if item_name in inventory: # Check if the user has already collected the item
            print("You have already collected this item!")
            show_status()
        elif 'item' in rooms[current_room] and rooms[current_room]['item'] is not None: # Check if there is an item in the room
            if item_name.lower() == rooms[current_room]['item'].lower():  # Compare item names
                inventory.append(item_name)
                print(f"You have now collected the {item_name} in this room! Enter a new command!")
                rooms[current_room]['item'] = None
                show_status()
            else: # If the item name is valid but is not the item that belongs in that room, print that the item is not in the room
                print(f"That item is not in the {current_room}! Enter another command!")
                show_status()
        else:
            print("There are no items to collect in this room.")
            show_status()


    while True: # While loop to keep the game running until the user enters 'quit'

        move = input("Enter your move: ").lower()  # Convert input to lowercase for consistency
        
        if move == 'show status': # If the user enters 'show status', call the show_status function
            show_status()
        
        if move == 'show instructions': # If the user enters 'show instructions', call the show_instructions function
            show_instructions()
        
        if move == 'go north': # If the user enters 'go north', check if there is a room to the north
            if 'North' in rooms[current_room]: 
                new_room = rooms[current_room]['North'] 
                current_room = new_room
                show_status()
            else:
                print("You cannot go that way!")
        
        if move == 'go south': # If the user enters 'go south', check if there is a room to the south
            if 'South' in rooms[current_room]: 
                new_room = rooms[current_room]['South']
                current_room = new_room
                show_status()
            else:
                print("You cannot go that way!")

        if move == 'go east': # If the user enters 'go east', check if there is a room to the east
            if 'East' in rooms[current_room]:
                new_room = rooms[current_room]['East']
                current_room = new_room
                show_status()
            else:
                print("You cannot go that way!")
        
        if move == 'go west': # If the user enters 'go west', check if there is a room to the west
            if 'West' in rooms[current_room]:
                new_room = rooms[current_room]['West']  
                current_room = new_room
                show_status()
            else:
                print("You cannot go that way!")
        
        if move.startswith('get '):  # Check if the input starts with 'get '
            item_name = move[4:].lower()  # Extract the item name from the input
            if item_name in ["magic", "master sword", "hookshot", "hylian shield", "silver gauntlets", "fairy bow", "iron boots"]: # Check if the item name is valid
                add_to_inventory(item_name)
            else:
                print("Invalid item name, try again!") # If the item name is invalid, print that the item name is invalid
        else: # Check if the user enters a valid command
            if (
                move != 'show status'
                and move != 'show instructions'
                and move != 'go north'
                and move != 'go south'
                and move != 'go east'
                and move != 'go west'
                and move != 'quit'
            ): # If the user enters an invalid command, print that the command is invalid
                print("Invalid command, try again!")
        
                
        if current_room == 'Hyrule Castle': # If the user enters the room with Ganondorf, check if they have all items
            if len(inventory) == len(rooms) - 2: # Check to see if the user has all of the items
                print("You have found Ganondorf in Hyrule Castle!! ")
                print("You have collected all of the items and have defeated Ganondorf! YOU WIN!")
                break
            else:
                print("You have found Ganondorf in Hyrule Castle!! ")
                print("You have not collected all items and Ganondorf has defeated you! GAME OVER!") # If the user enters the room with Ganondorf without all items, they lose
                break

        elif move == 'quit': # If the user enters 'quit', end the game
            print("Thanks for playing, I hope you had fun!")
            break


if __name__ == "__main__": # Call the main function
    main() 