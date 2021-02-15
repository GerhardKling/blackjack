# blackjack
Simple version of Blackjack for education and fun.

This project is suitable for students that know lists, loops, branching and classes.

I split the project into 8 Sessions as outlined below.

I am not a Blackjack expert; hence, some adjustments will be needed!

Sessions:

Session 1: start main.py, card.py, and deck.py

Session 2: add tests in folder Tests; introduction to test-driven development

Session 3: adds player.py and game.py

Session 4: build the first game rounds in game.py

Session 5: return scores for each player after first game round; account for the case of two Aces 

Session 6: build display class to show the game in terminal

Session 7: asking for another card; first add deck attribute to Game class as we need to work with the same deck in the next round

Session 8: adding the bank and determining winners; add bank as another player in display.py; the bank needs their own optimal response

Finally, I freeze the application using pyinstaller -c -F main.py, where the -F flag is to bundle everything into one exe file; 
open a console and keep it open using the -c flag; use cmd in folder and execute main.exe directly to keep terminal open.
