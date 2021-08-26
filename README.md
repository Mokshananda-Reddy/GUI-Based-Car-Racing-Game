### Hi there 👋

Description:
This python program is basically a racing game which works on pygame platform.
It is based on Graphical User Interface. The game focuses on the concept of player
dodging the obstacles rather than racing with other players.

Our Requirements
We have designed the code that is suitable with python3. We also need to install
pygame module before running this game.

External Packages used:
1. Pygame – It is an open source python library that is used to design game and
multimedia applications.
2. Time - The python time module provides many ways of representing time in
code, such as objects, numbers, and strings. It also provides functionality other
than representing time, like waiting during code execution and measuring the
efficiency of your code.
3. Random - Python offers random module that can generate random numbers.
These are pseudo-random number as the sequence of number generated depends
on the seed. We use it in our game for generation of random obstacles.
4. Math - The Python Math Library provides us access to some common math
functions and constants in Python, which we can use throughout our code for more complex mathematical computations. The library is a built-in Python module;
therefore, you don't have to do any installation to use it.

Design of the program:
So, here we describe the setup of the game in following points:
1. Set up of environment.
2. Setting of controls and position of players.
3. Setting up obstacles and hurdles along the way.
4. Calculation of score and saving it.
Initially there is a pop-up menu asking regarding the start or quit of the game.
Then when the game begins, there is a score board at the top left corner
calculating the number of obstacles passed through the user without any damage
to the car.
The screen is divided into two parts one is background and playground. The
background is a field of grass where the player cannot go, and the playground is
the path where the player can move his car clearing the obstacles in the path. At
the end of the game the score of users is displayed.
The player will be positioned at the bottom most center of the path initially. So,
using the direction keys the player can move his vehicle with due number of
coordinates in the respected direction.
(the arrow keys: - left, right, up, down are to be used).
The obstacles are other vehicles generated using random module which comes
during certain time intervals provided by the time module.The score of the player is stored in a file using file handling, where one can check
the current score of the player.
