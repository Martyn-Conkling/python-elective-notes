 #! python3
   # randomQuizGenerator.py - Creates quizzes with questions and answers in
   # random order, along with the answer key.


from pathlib import Path
from datetime import datetime
import random

# The quiz data. Keys are states and values are their capitals.
capitals = {
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
    'Michigan':'Lansing', 
    'Minnesota': 'Saint Paul',
    'Mississippi': 'Jackson', 
    'Missouri':'Jefferson City', 
    'Montana': 'Helena', 
    'Nebraska': 'Lincoln', 
    'Nevada':'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhode Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakota': 'Pierre',
    'Tennessee':'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont':'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia', 
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne'}

# getting the current date and time
now = datetime.now()

dir_name = now.strftime("%Y-%m-%d_%H-%M-%S")
new_quiz_dir = Path('quizFolder') / dir_name
new_quiz_dir.mkdir(exist_ok=True)


# Generate 35 quiz files.
for quizNum in range(35):
    print(f'Creating quiz {quizNum + 1}')


    questions_file_path = new_quiz_dir/ f'capitalsquiz{quizNum + 1}.txt'
    quizFile = open(questions_file_path, 'w')
    # open(f'capitalsquiz{quizNum + 1}.txt', 'w')

    
    answers_file_path = new_quiz_dir / f'capitalsquiz_answers{quizNum + 1}.txt'
    answerKeyFile = open(answers_file_path, 'w')
    
    # Alternatively could use a 'with' statement to automatically take care of closing the file once the
    # code block is exited
    
    # with open(questions_file_path, 'w') as quizFile, open(answers_file_path, 'w') as answerKeyFile:

    # Write out the header for the quiz.
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + f'State Capitals Quiz (Form{quizNum + 1})')
    quizFile.write('\n\n')

    # Shuffle the order of the states.
    states = list(capitals.keys())
    random.shuffle(states)

    # Create all of the 50 quiz questions
    for questionNum in range(50):
        # get the correct answer
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        # Deletes the correct answer from the wrongAnswers list
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
         # Picks a random sample of 3 wrong answers
        wrongAnswers = random.sample(wrongAnswers,3)

        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)
       
        # Write the question and answer options to the quiz file.
        quizFile.write(f'{questionNum + 1}. What is the capital of {states[questionNum]}?\n')

        for i in range(4):
            quizFile.write(f"   {'ABCD'[i]}. {answerOptions[i]}\n")
        
        # Creates a newline space before the next question is printed
        quizFile.write('\n')
            
        answerKeyFile.write(f"{questionNum + 1}. {'ABCD'[answerOptions.index(correctAnswer)]}\n")

    quizFile.close()
    answerKeyFile.close()







    # todo: Create the quiz and answer key files.
        # done

    # todo: Write out the header for the quiz.
        # done

    # todo: Shuffle the order of the states.
        # done

    # todo: Loop through all 50 states, making a question for each
        # done

    # todo: Write the question and answer options to the quiz file.

    # todo: Write the answer key to a file.