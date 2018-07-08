#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.

import random

# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama':'Montgomery','Alaska':'Juneau','Arizona':'Phoenix',
'Arkansas':'LittleRock','California':'Sacramento','Colorado':'Denver',
'Connecticut':'Hartford','Delaware':'Dover','Florida':'Tallahassee','Georgia':
'Atlanta','Hawaii':'Honolulu','Idaho':'Boise','lllinois':'Springfield',
'Indiana':'Indianapolis','Iowa':'DesMoines','Kansas':'Topeka','Kentucky':
'Frankfort','Louisiana':'BatonRouge','Maine':'Augusta','Maryland':
'Annapolis','에assachusetts':'Boston','Michigan':'Lansing','Minnesota':'SaintPaul',
'Mississippi':'Jackson','Missouri':'JeffersonCity','Montana':'Helena',
'Nebraska':'Lincoln','Nevada':'CarsonCity','NewHampshire':'Concord',
'NewJersey':'Trenton','NewMexico':'SantaFe','NewYork':'Albany','North Carolina':'Raleigh',
'NorthDakota':'Bismarck','Ohio':'Columbus','Oklahoma':'OklahomaCity',
'Oregon':'Salem','Pennsylvania':'Harrisburg','RhodeIsland':'Providence',
'SouthCarolina':'Columbia','SouthDakota':'Pierre','Tennessee':'Nashville',
'Texas':'Austin','Utah':'SaltLakeCity','Vermont':'Montpelier',
'Virginia':'Richmond','Washington':'0lympia','씨estVirginia':'Charleston',
'Wisconsin':'Madison','Wyoming':'Cheyenne'}

# Generate 32 quiz files.
for quizNum in range(35):
    # Create the quiz and answer key files.
    quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')
    answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum +1), 'w')

    # Write out the header for the quiz.
    quizFile.write('Name:\n\nData:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')

    # Shuffle the order of the states.
    states = list(capitals.keys())
    random.shuffle(states)

    # Loop through all 50 states, making a question for each.
    for questionNum in range(50):

        # Get right and wrong answers.
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        # Write the question and answer options to the quiz file.
        quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1, states[questionNum]))
        for i in range(4):
            quizFile.write('    %s. %s\n' % ('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')

        # Write the answer key to a file.
        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
    quizFile.close()
    answerKeyFile.close()

