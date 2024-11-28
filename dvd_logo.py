"""
Animated ASCII art of a DVD logo bouncing around the screen.

This program was created from the project 5 of the book "The Big Book of Small Python Projects"
"""

import sys, random, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext')
    sys.exit()

WIDTH, HEIGHT = bext.size()
HEIGHT -= 1
NUMBER_OF_LOGOS = 5
PAUSE_AMOUNT = 0.2
COLORS = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

UP_RIGHT = 'ur'
UP_LEFT = 'ul'
DOWN_RIGHT = 'dr'
DOWN_LEFT = 'dl'
DIRECTIONS = (UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT)
COLOR = 'color'
X = 'x'
Y = 'y'
DIR = 'direction'

def main():
    """
    Run the animated ASCII art of the DVD logo bouncing around the
    screen.
    """
    bext.clear()

    logos = []
    for i in range(NUMBER_OF_LOGOS):
        logos.append({COLOR: random.choice(COLORS), X: random.randint(1, WIDTH - 3), Y: random.randint(1, HEIGHT - 3), DIR: random.choice(DIRECTIONS)})
        if logos[-1][X] % 2 == 1:
            logos[-1][X] -= 1

    cornerBounces = 0
    while True:
        # Move and draw all the logos
        for logo in logos:
            bext.goto(logo[X], logo[Y])
            print(' ', end='')

            originalDirection = logo[DIR]

            # Corner bounce detection
            if logo[X] == 0 and logo[Y] == 0:
                logo[DIR] = DOWN_RIGHT
                cornerBounces += 1
            elif logo[X] == 0 and logo[Y] == HEIGHT:
                logo[DIR] = UP_RIGHT
                cornerBounces += 1
            elif logo[X] == WIDTH - 3 and logo[Y] == 0:
                logo[DIR] = DOWN_LEFT
                cornerBounces += 1
            elif logo[X] == WIDTH - 3 and logo[Y] == HEIGHT:
                logo[DIR] = UP_LEFT
                cornerBounces += 1
            # Boundary bounce detection
            elif logo[X] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] = UP_RIGHT
            elif logo[X] == 0 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = DOWN_RIGHT
            elif logo[X] == WIDTH - 3 and logo[DIR] == UP_RIGHT:
                logo[DIR] = UP_LEFT
            elif logo[X] == WIDTH - 3 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = DOWN_LEFT
            elif logo[Y] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] = DOWN_LEFT
            elif logo[Y] == 0 and logo[DIR] == UP_RIGHT:
                logo[DIR] = DOWN_RIGHT
            elif logo[Y] == HEIGHT and logo[DIR] == DOWN_LEFT:
                logo[DIR] = UP_LEFT
            elif logo[Y] == HEIGHT and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = UP_RIGHT

            # Change color when direction changes
            if logo[DIR] != originalDirection:
                logo[COLOR] = random.choice(COLORS)

            # Move the logo
            if logo[DIR] == UP_RIGHT:
                logo[X] += 2
                logo[Y] -= 1
            elif logo[DIR] == UP_LEFT:
                logo[X] -= 2
                logo[Y] -= 1
            elif logo[DIR] == DOWN_RIGHT:
                logo[X] += 2
                logo[Y] += 1
            elif logo[DIR] == DOWN_LEFT:
                logo[X] -= 2
                logo[Y] += 1

            # Ensure the logo stays within bounds
            logo[X] = max(0, min(logo[X], WIDTH - 3))
            logo[Y] = max(0, min(logo[Y], HEIGHT))

        # Print the number of corner bounces
        bext.goto(4, 0)
        bext.fg('white')
        print('Corner bounces: ', cornerBounces, end='')

        # Redraw all the logos
        for logo in logos:
            bext.goto(logo[X], logo[Y])
            bext.fg(logo[COLOR])
            print('DVD', end='')

        # Update the screen
        bext.goto(0, 0)
        sys.stdout.flush()
        time.sleep(PAUSE_AMOUNT)

# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Gracefully exiting")
        sys.exit()

