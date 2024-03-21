 #! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in random order, along with the answer key.

import random


   # The quiz data. Keys are states and values are their capitals.
usa_state_capitals = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinois':'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Moines', 
    'Kansas':'Topeka', 
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine':'Augusta', 
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan':'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany',
   'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}




def createQuizes(numberOfQuizzes=35):
   # This for loop will determine how many quizzes we wish to create.  This number should likely be determined by the number of students in your class
   for quizNum in range(numberOfQuizzes):
    # For each quiz we need to do the following
      # Create the quiz file
         # needs to have a unique dilename and should have a standard header for students to fill out their name and the date and class period
      
      # Create the unique quiz question order, with 1 correct answer and 3 incorrect answers
         # 
      # Create the answer key for the unique quiz


      #Todo: Write out the header for the quiz
      # Todo: Shuffle the order of the states.
      # Todo: Loop through all 50 states, making a question for each.





      #Create the quiz questions and answers files 
      quizFile = open(f'usa_state_capitals_quiz{quizNum+1}.txt', 'w')
      answerKeyFile = open(f'usa_state_capitals_quiz_answers{quizNum + 1}.txt', 'w')
      
      # Write out the header for the quiz
      quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
      quizFile.write((' ' * 20) + f'State Capitals Quiz (Form{quizNum + 1})')
      quizFile.write('\n\n')

      # Shuffle the order of the states
      # Creates a list of all the keys in the usa_state_capitals dictionary
      states = list(usa_state_capitals.keys()) 
      random.shuffle(states)


    