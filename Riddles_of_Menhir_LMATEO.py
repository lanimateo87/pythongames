# Python 3.7
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 09:16:22 2018

@author: Lani L. Mateo

Working directory:
/Users/Dell/OneDrive - Education First/Desktop/PyCourses


Purpose:
To test student's creativity and ability in applying Python essentials
including but not limited to:
    a) strings and string manipulation,
    b) user-defined functions and variables,
    c) conditional statements and
    d) loops

About the Game - "Riddles of Menhir"

Menhir - n. huge stones set into the ground vertically
This game was inspired by the Netflix series Outlander.

Claire Randall, a British army nurse, unexpectedly travelled back in time while
on her second honeymoon trip in Invernes, Scotland. Her husband, Frank Randall,
a history professor, has been looking for her and thought that Claire left him
for another man because he is infertile.

The only way back is if Claire can twist the turn of events by answering 3
riddles secretly engraved in huge standing stones on the hill of Craig Dah Nun
correctly or she will forever be stuck in 1745.

The Jacobite rebellion is at its peak and she needs the player's help
to bring her back before the armies start questioning her identity.

The player lives at present and is gifted with telepathy and ability to see
places from the past. There are only 2 chances to solve a riddle. The player
may opt to play the game again right from the start until player solves all
3 riddles.

    Stone 1: The Enigma of Spacetime
    Stone 2: The Eye of Ra
    Stone 3: The Way Out

B. Known Bugs and/or Errors:
   None
"""
# Riddles of Menhir Code Starts Here
from sys import exit
import time

# Introduction
def start():
    global name
    global country
    global datetime_player

    datetime_player = time.strftime("%c")

    name = input("""
           Hello! Welcome to Riddles of Menhir!
           What is your name?

           >>> """).capitalize()

    country = input("""
           And which country are you from?

           >>> """).capitalize()

    print (f"""
           Hey {name} of {country}! I'm Claire Randall.
           I'm a British army nurse married to a history professor,
           Frank Randall.""")
    input ('\nPress enter to continue...')

    print (f"""
           
           Hmmmm... It's {datetime_player} where you are from.
           It sounds odd that I am 273 years behind you.

           But this mystery is as mindboggling as your ability to communicate
           through the mind and to even see where I am now.

           Here's my story...""")
    input ('\nPress enter to continue...')
    print ("""

           On October 2018, I was gathering herbal plants near the
           standing stones on the hill of Craigh na Dun in Scotland
           when I heard a buzzing noise near the stones.""")
    input ('\nPress enter to continue...')
    print ("""

           I followed the noise and that is all I remember
           before I fainted.""")
    input ('\nPress enter to continue...')
    print ("""

           When I woke up, I am already surrounded by the armies
           of Clan Mackenzie. And it's year 1745!
           
           The Jacobite rebellions is at its peak.
           Oh no! The armies might mistaken me as a spy!""")
    input ('\nPress enter to continue...')
    print (f"""

           I need to go back to the present and find my husband!
           The clock is ticking!
           
           The only way back is if I can move all 3 standing stones.
           Please help me {name} of {country}!""")
    input ('\nPress enter to continue...')
    print ("""

           The huge stones will move only if the correct answer to a secretly
           engraved riddle is chosen. You have 2 chances to answer it correctly.
           Remember, only by moving a stone can the next riddle be revealed.""")
    input ('\nPress enter to continue...')
    print (f"""

           One more thing. Read what is engraved on the stone carefully.
           If you fail to do so, you will need to read more than what
           is required before you get your chance to answer again.

           This will waste not only a chance but also time.
           Take heed {name} of {country}.""")
    input ('\nPress enter to continue...')
    starting_path()

# Acceptance of Challenge
def starting_path():
    print ("""

           Will you help me move the stones now? (Yes/No)""")
    answer = input(">>> ").upper()

    if answer == 'YES':
        print (f"""

           Great! Brace yourself {name} of {country}.
           The Riddles of Menhir is about to be revealed.""")
        input ('\nPress enter to reveal the first riddle...')
        stone_1 ()

    elif answer == 'NO':
        print (f"""

           Oh my! I might be stuck here forever.""")
        input (f"""
           I'm sorry to see you go {name} of {country}.
           I will try to assimilate with the Clan of Mackenzie while I wait
           for someone to succesfully help me move all the 3 stones.

           I hope the Jackobites don't attack anytime soon or this place
           will be my bloody grave!

           oooooooooooooooooooooo END OF GAME oooooooooooooooooooooo

           Press enter to exit.""")
        exit (0)

    else:
        print (f"""

            Sorry {name} of {country}.
            Let your yes be yes and your no be no.""")
        input ('\nPress enter to answer again.')
        starting_path ()

# Stone 1: The Enigma of Spacetime
def stone_1():
    """This function will direct player to the first stone/riddle."""
    print (f"""

          Stone 1: The Enigma of Spacetime

          "The beginning of eternity,
           The end of time and space,
           The beginning of every end,
           And the end of every place."
             -The Guess Book (c. 1820) """)

    input ('\nPress enter to continue...')

    chances = 2

    while chances > 0:
        print (f"""

           What could this be {name} of {country}?
           Select from the options below.
             A) God
             B) Infinity
             C) Letter e""")
        riddle_1 = input(">>> ").upper()

        if riddle_1 == "C" or riddle_1 == "LETTER E" or riddle_1 == "E":
            print(f"""

            Brilliant! {riddle_1} is right {name} of {country}!

            (the earth started grumbling and the sound of a huge stone moving
            is echoing in the background...)""")
            input ('\nPress enter to continue...')
            print("""

            Time and space is such an enigma.
            And I have a life to live!

            I need to travel forward to the present times.
            You're on your way to help me do this by solving 2 more riddles.""")
            input('\nPress enter to reveal the second riddle.')
            stone_2()
            break

        elif riddle_1 == "A" or riddle_1 == "GOD" or riddle_1 == "B" or riddle_1 == "INFINITY":
           print(f"""

           Oh, this makes me sad. The stone won't move.
           {riddle_1} is not the right answer.""")

           input(f"""
           If you still have a chance
           please think harder {name} of {country}.""")
           chances -= 1

        else:
           print(f"""

           {name} of {country}, did you even read?!
           {riddle_1} is not among the options given by the stone.
           You wasted a chance! Read what the stone wants
           to remind you of and gain wisdom.""")

           input("\nPress enter to continue.")

           print("""

           “A reader lives a thousand lives before he dies
           The man who never reads lives only one.”
                                  – George R.R. Martin""")
           print("\nPress enter to continue.")
           input(f"""
           If you still have a chance
           please read more carefully {name} of {country}.""")
           chances -= 1

    fail()

# Stone 2: The Eye of Ra
def stone_2():
    """This function will direct player to the second stone/riddle."""
    print (f"""\n
          Stone 2: The Eye of Ra

          "There is one that has a head without an eye,
           And there’s one that has an eye without a head.
           You may find the answer if you try;
           And when all is said,
           Half the answer hangs upon a thread."
                                      -Christina Rossetti""")
    input ('\nPress enter to continue...')

    chances = 2

    while chances > 0:
        print (f"""\n
           What could this be {name} of {country}?
           Select from the options below.
             A) Pins and needles
             B) Pencil
             C) Book""")
        riddle_2 = input(">>> ").upper()

        if riddle_2 == "A" or riddle_2 == "PINS AND NEEDLES" or riddle_2 == "PINS & NEEDLES":
           print(f"""

           Magnificent! {riddle_2} is right {name} of {country}!

           (the earth started grumbling and the sound of a huge stone moving
            is echoing in the background...)""")
           input ('\nPress enter to continue...')
           print(f"""

           Time is running. I heard the Jacobites are on their way for war.
           Oh! This place will be a bloodbath in no time.
           We need to think quick!
           Help me move the last stone {name} of {country}.""")
           input('\nPress enter to reveal the third riddle.\n')
           stone_3()
           break

        elif riddle_2 == "B" or riddle_2 == "PENCIL" or riddle_2 == "C" or riddle_2 == "BOOK":
           print(f"""

           Oh, I'm sorry, the stone won't move.
           {riddle_2} is incorrect.""")

           input(f"""
           If you still have a chance
           please think harder {name} of {country}.""")
           print("\nPress enter to continue.")
           chances -= 1

        else:
           print(f"""

           {name} of {country}, did you even read?!
           {riddle_2} is not among the options given by the stone.
           You wasted a chance! Read what the stone wants
           to remind you of and gain wisdom.""")

           input("\nPress enter to continue.")

           print("""

          “Reading is essential for those who seek
           to rise above the ordinary.”
                                          – Jim Rohn""")
           print("\nPress enter to continue.")
           input(f"""
           If you still have a chance
           please read more carefully {name} of {country}.""")
           chances -= 1

    fail()

# Stone 3: The Way Out
def stone_3():
    """This function will direct player to the third stone/riddle."""
    print (f"""
           Stone 3: The Way Out

          "Voiceless it cries,
           Wingless flutters,
           Toothless bites,
           Mouthless mutters."
             -J.R.R. Tolkien """)
    input ('\nPress enter to continue...')

    chances = 2

    while chances > 0:
        print (f"""

           What could this be {name} of {country}?
           Select from the options below.
             A) Nightingale
             B) Time
             C) Wind""")
        riddle_3 = input(">>> ").upper()

        if riddle_3 == "C" or riddle_3 == "WIND":
           print(f"""\n
           Excellent! {riddle_3} is right {name} of {country}!
           I couldn't thank you more!


           (the earth started grumbling and the sound of huge stones moving
            is echoing in the background...) """)
           input ('\nPress enter to continue...')
           print("""\n
           (An army of horsemen approaching...)


           Oh! The Jacobites are here. Bloody war is coming!
           You helped me move all 3 stones just in time.""")
           input('\nPress enter to initiate time travel for Claire Randall.\n')
           success()
           break

        elif riddle_3 == "B" or riddle_3 == "A" or riddle_3 == "NIGHTINGALE" or riddle_3 == "TIME":
           print(f"""

           Oh, I'm sorry, the stone won't move.
           {riddle_3} is incorrect.""")
           input(f"""
           If you still have a chance
           please think harder {name} of {country}.""")
           chances -= 1

        else:
           print(f"""

           {name} of {country}, did you even read?!
           {riddle_3} is not among the options given by the stone.
           You wasted a chance! Read what the stone wants
           to remind you of and gain wisdom.""")

           input("\nPress enter to continue.")

           print("""

           “Today a reader, tomorrow a leader.”
                             – Margaret Fuller""")
           print("\nPress enter to continue.")
           input(f"""
           If you still have a chance
           please read more carefully {name} of {country}.""")
           chances -= 1

    fail()

def fail():
    """This function will prompt player to either play from the beginning
    of the game or not after using up 2 chances to answer correctly."""
    print(f"""

           Oh no! You've used up the chances to answer the riddle.
           The stone won't reveal the next one.

           Would you like to go back and play from the beginning? (Yes/No)""")
    replay = input(">>> ")
    replay = replay.upper()

    if replay == 'YES':
        stone_1()

    elif replay == 'NO':
        print(f"""

          You tried to release me from this bondage of time
          {name} of {country} but you failed.
          Oh my! I might be stuck here forever.

          I will try to assimilate with the Clan of Mackenzie while I wait
          for someone to succesfully help me move the 3 stones.

          I hope the Jackobites don't attack anytime soon or this place
          will be my bloody grave!"

          oooooooooooooooooooooo GAME OVER oooooooooooooooooooooo""")

        input("Press enter to exit.")

        exit(0)

    else:
        print (f"""\n
            Sorry {name} of {country}.
            Let your yes be yes and your no be no.""")
        input ('\nPress enter to answer again.')
        starting_path ()

def success():
    """This function will execute countdown from 5"""
    count = 5

    while count > 0:
        print(count)
        count -= 1
        input("Time traveling to 2018...\n")

    print(f"""
          It's {datetime_player}! I am indeed back!
          Thank you for helping me {name} of {country}.

          I should rush to tell Frank about what happened.
          History will never be the same again. Thank you!

          ooooooooooooooooooo THE STONES HAVE BEEN MOVED ooooooooooooooooooo

          "Permanence, perseverance and persistence
          in spite of all obstacles, discouragements and impossibilities:
          It is this, that in all things distinguishes the strong soul
          from the weak."
                                                           -Thomas Carlyle

          """)

    input("Press enter to exit.")

    exit(0)
start()