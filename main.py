print('You got just caught cheating on your midterms\n and your teacher is very angry, hurry and run!')
print()
print('Pick a door to answer a question, \n if you get the question wrong, the teacher will catch up to you!')
print()


correctanswer = True

if correctanswer == True:
#level 1
  doornumber = input('Choose a number for the three doors: ')

  if doornumber == "1":
    print('How many classes are in a semester?')
    answer = input("enter your answer: ")
    if answer == "5":
      print('Correct!')
    else:
      print("Wrong answer! Oh no, the teacher caught you! time for detention :-(") 
      correctanswer = False
  elif doornumber == "2":
    print('Which Jamaican runner is an 11-time world champion and holds the record in the 100 and 200-meter race?')
    answer = input("enter your answer: ")
    if answer == "Usain Bolt":
      print('Correct!')
    else:
      print("Wrong Answer! Oh no, the teacher caught you! time for detention :-(")
      correctanswer = False
  elif doornumber == "3":
    print('What year was the very first model of the iPhone released?')
    answer = input("enter your answer: ")
    if answer == "2007":
      print('Correct!')
    else:
      print("Wrong answer! Oh no, the teacher caught you! time for detention :-(")
      correctanswer = False

if correctanswer == True:
  print('You made it to the cafeteria! Now go through the double doors so you can get to the main hall!')

  doornumber = input('Choose a number for the three doors: ')

  if doornumber == "1":
    print('Google Chrome, Safari, Firefox, and Explorer are different types of what?')
    answer = input("enter your answer: ")
    if answer == "Web browsers":
      print('Correct!')
    else:
      print("Wrong answer! Oh no, the teacher caught you! time for detention :-(") 
      correctanswer = False

  elif doornumber == "2":
    print('Who discovered penicillin?')
    answer = input("enter your answer: ")
    if answer == "Alexander Fleming":
      print('Correct!')
    else:
      print("Wrong Answer! Oh no, the teacher caught you! time for detention :-(")
      correctanswer = False

  elif doornumber == "3":
    print('What part of the atom has no electric charge?')
    answer = input("enter your answer: ")
    if answer == "Neutron":
      print('Correct!')
    else:
      print("Wrong answer! Oh no, the teacher caught you! time for detention :-(")
      correctanswer = False

  print('Whew! You made it out! Now hurry up and get back home!')
