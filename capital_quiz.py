# Capital Quiz
# Description:
'''
A dictionary of states and their associated capitals is used by this Python program to test the
user's knowledge of US state capitals. The user is prompted to input the capital of the state
after the program randomly chooses one from the list. The program shows a message confirming
whether the user's answer is correct or incorrect. If the user's response is incorrect, the
message indicates that. The user's score is recorded by the program, which shows it at the
conclusion.
'''

import random

# This is the directory of states' names and their captial cities

each_state_capitals = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "California": "Sacramento",
    "Colorado": "Denver",
    "Connecticut": "Hartford",
    "Delaware": "Dover",
    "Florida": "Tallahassee",
    "Georgia": "Atlanta",
    "Hawaii": "Honolulu",
    "Idaho": "Boise",
    "Illinois": "Springfield",
    "Indiana": "Indianapolis",
    "Iowa": "Des Moines",
    "Kansas": "Topeka",
    "Kentucky": "Frankfort",
    "Louisiana": "Baton Rouge",
    "Maine": "Augusta",
    "Maryland": "Annapolis",
    "Massachusetts": "Boston",
    "Michigan": "Lansing",
    "Minnesota": "Saint Paul",
    "Mississippi": "Jackson",
    "Missouri": "Jefferson City",
    "Montana": "Helena",
    "Nebraska": "Lincoln",
    "Nevada": "Carson City",
    "New Hampshire": "Concord",
    "New Jersey": "Trenton",
    "New Mexico": "Santa Fe",
    "New York": "Albany",
    "North Carolina": "Raleigh",
    "North Dakota": "Bismarck",
    "Ohio": "Columbus",
    "Oklahoma": "Oklahoma City",
    "Oregon": "Salem",
    "Pennsylvania": "Harrisburg",
    "Rhode Island": "Providence",
    "South Carolina": "Columbia",
    "South Dakota": "Pierre",
    "Tennessee": "Nashville",
    "Texas": "Austin",
    "Utah": "Salt Lake City",
    "Vermont": "Montpelier",
    "Virginia": "Richmond",
    "Washington": "Olympia",
    "West Virginia": "Charleston",
    "Wisconsin": "Madison",
    "Wyoming": "Cheyenne"
}

# Now here we convert the dictionary into a list for random.
each_state_list = list(each_state_capitals.keys())

# This remembers how many you answered correct and incorrect. 
number_of_correct = 0
number_of_incorrect = 0

# loop
while True:
    # It picks a state at random from the  list. 
    each_state = random.choice(each_state_list)
    
    # This asks the user to input capital of the state asked
    capitals_guess = input("What is the capital of {}? (or enter q to quit): ".format(each_state))
    
    # Verify the user's desire to stop using
    if capitals_guess.lower() == "q":
        break
    
    # Verify the correctness of the user's answer.
    if capitals_guess == each_state_capitals[each_state]:
        print("That is correct.")
        number_of_correct += 1
    else:
        print("That is incorrect.")
        number_of_incorrect += 1

# Print the result.
print("You had {} correct responses and {} incorrect responses.".format(number_of_correct, number_of_incorrect))
