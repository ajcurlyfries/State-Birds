#Lab 3
#File name: States.py
#Author:Andora Zuniga
#Date: September 7th, 2019
#Purpose: allows a user to display, sort and update as needed a List of U.S States
#containing the State Capital and State Bird

import sys

#Start of program 
#welcome message
print("********* Welcome to the State Capital and Bird List Application *********")
choice = 0
#Dictionary of states capitals and birds
stateInfo = {'Alabama': ['Montgomery', 'Yellowhammer'],
                'Alaska': ['Juneau', 'Willow Ptarmigan'], 
                'Arizona': ['Phoenix', 'Cactus Wren'], 
                'Arkansas': ['Little Rock', 'Mockingbird'], 
                'California': ['Sacramento', 'California Valley Quail'], 
                'Colorado': ['Denver', 'Lark Bunting'], 
                'Connecticut': ['Hartford', 'Robin'],
                'Delaware': ['Dover', 'Blue Hen'],
                'Florida': ['Tallahassee', 'Mockingbird'], 
                'Georgia': ['Atlanta', 'Brown Thrasher'], 
                'Hawaii': ['Honolulu', 'Nene'], 
                'Idaho': ['Boise', 'Mountain Bluebird'], 
                'Illinois': ['Springfield', 'Cardinal'],
                'Indiana': ['Indianapolis', 'Cardinal'], 
                'Iowa': ['Des Moines', 'Eastern Goldfinch'], 
                'Kansas': ['Topeka', 'Western Meadowlark'], 
                'Kentucky': ['Frankfort', 'Cardinal'], 
                'Louisiana': ['Baton Rouge', 'Eastern Brown Pelican'], 
                'Maine': ['Augusta', 'Chickadee'], 
                'Maryland': ['Annapolis', 'Baltimore Oriole'], 
                'Massachusetts': ['Boston', 'Chickadee'], 
                'Michigan': ['Lansing', 'Robin'],
                'Minnesota': ['Saint Paul', 'Common Loon'],
                'Mississippi': ['Jackson', 'Mockingbird'],
                'Missouri': ['Jefferson City', 'Bluebird'],
                'Montana': ['Helena', 'Western Meadowlark'],
                'Nebraska': ['Lincoln', 'Western Meadowlark'],
                'Nevada': ['Carson City', 'Mountain Bluebird'],
                'New Hampshire': ['Concord', 'Purple Finch'],
                'New Jersey': ['Trenton', 'Eastern Goldfinch'],
                'New Mexico': ['Santa Fe', 'Roadrunner'],
                'New York': ['Albany', 'Bluebird'],
                'North Carolina': ['Raleigh', 'Cardinal'],
                'North Dakota': ['Bismarck', 'Western Meadowlark'],
                'Ohio': ['Columbus', 'Cardinal'],
                'Oklahoma': ['Oklahoma City', 'Scissor-Tailed Flycatcher'],
                'Oregon': ['Salem', 'Western Meadowlark'],
                'Pennsylvania': ['Harrisburg', 'Ruffed Grouse'],
                'Rhode Island': ['Providence', 'Rhode Island Red'],
                'South Carolina': ['Columbia', 'Great Carolina Wren'],
                'South Dakota': ['Pierre', 'Ring-Necked Pheasant'],
                'Tennessee': ['Nashville', 'Mockingbird'],
                'Texas': ['Austin', 'Mockingbird'],
                'Utah': ['Salt Lake City', 'California Seagull'],
                'Vermont': ['Montpelier', 'Hermit Thrush'],
                'Virginia': ['Richmond', 'Cardinal'],
                'Washington': ['Olympia', 'Willow Goldfinch'],
                'West Virginia': ['Charleston', 'Cardinal'], 
                'Wisconsin': ['Madison', 'Robin'], 
                'Wyoming': ['Cheyenne', 'Western Meadowlark']}
#loop 
while choice != 4:
    #ask for choice
    print("\nChoose an option:")
    print("1. Display all U.S. States in Alphabetical order along with Capital and bird")
    print("2. Search for a specific state and display the appropriate Capital and Bird")
    print("3. Update a Bird for a specific state")
    print("4. Exit the program")
    #store input
    choice = int(input("\n"))
    
    if choice == 1:
        print("\nYou selected 1:")
        for key in sorted(stateInfo.keys()) :
            print(f'{key:<16}Capital: {stateInfo[key][0]:<16} Bird: {stateInfo[key][1]:<14}')
    
    if choice == 2:
        print("\nYou selected 2:")
        state = ""
        print("Which state would you like to look up?")
        for key in stateInfo.keys():
            state = input("\n")
            if state not in stateInfo:
                print("State not found, try again")
                break
            else:
                print(f'Capital: {stateInfo[state][0]:<16} Bird: {stateInfo[state][1]:<14}')
            break
    if choice == 3:
        print("\nYou selected 3:")
        state = ""
        newBird = ""
        print("Which state would you like to update?")
        for key in stateInfo.keys():
            state = input("\n")
            if state not in stateInfo:
                print("State not found, try again")
                break
            else:
                newBird = input("Please type the new state bird: ")
                stateInfo[state][1] = newBird
                print(f'\nThank you! \nThe state bird of {state} is {stateInfo[state][1]}')
            break
    
    if choice == 4:
        print("\nYou selected 4:\nThanks for trying out the State Capital and Bird List Application")
        print("\n\n***************************************Goodbye!******************************************")
        
        
        