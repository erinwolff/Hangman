# First version of hangman
'''import random
import pygame

hangman_stages = [
    pygame.image.load("hangman_stage1.png"),
    pygame.image.load("hangman_stage2.png"),
    pygame.image.load("hangman_stage3.png"),
    pygame.image.load("hangman_stage4.png"),
    pygame.image.load("hangman_stage5.png"),
    pygame.image.load("hangman_stage6.png"),
]

pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hangman Game")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    def select_word():
        """Selects a random word from the hangman_words.txt file"""
        with open('hangman_words.txt', 'r') as file:
            word_list = [line.strip() for line in file.readlines()]
        return random.choice(word_list)

    def play_hangman():
        word = select_word().lower()
        guessed_letters = []
        tries = 6  # Number of tries before the game ends

        while tries > 0:
            # Display the current state of the word with blanks for unguessed letters
            display_word = ""
            for letter in word:
                if letter in guessed_letters:
                    display_word += letter
                else:
                    display_word += "_"
            print(display_word)

            guess = input("Guess a letter: ").lower()

            # Check if the guessed letter is in the word (case-sensitive)
            if guess in word:
                if guess in guessed_letters:
                    print("You already guessed that letter!")
                else:
                    print("Correct!")
                    guessed_letters.append(guess)
            else:
                print("Wrong guess!")
                tries -= 1
                
            # Check if the player has guessed all the letters
            if all(letter in guessed_letters for letter in word):
                print("Congratulations! You guessed the word:", word)
                break

        # Update graphical elements based on game logic
        hangman_image = hangman_stages[incorrect_guesses]
        word_surface = font.render(partially_revealed_word, True, (255, 255, 255))

        # Draw the graphical elements on the screen
        screen.blit(hangman_image, (x, y))
        screen.blit(word_surface, (x, y))

        if tries == 0:
            print("Out of tries. The word was:", word)

    pygame.display.flip()

pygame.quit()

# Start the game
play_hangman()''' 

# Second version of hangman without button    
'''import random
import pygame
import string

# Mapping of key constants to corresponding letters
key_mapping = {getattr(pygame, "K_" + letter): letter for letter in string.ascii_lowercase}

hangman_stages = [
    pygame.image.load("hangman_stage1.png"),
    pygame.image.load("hangman_stage2.png"),
    pygame.image.load("hangman_stage3.png"),
    pygame.image.load("hangman_stage4.png"),
    pygame.image.load("hangman_stage5.png"),
    pygame.image.load("hangman_stage6.png"),
    pygame.image.load("hangman_stage7.png"),
]

pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Super Cool & Fun Hangman Game")

def select_word():
    """Selects a random word from the hangman_words.txt file"""
    with open('hangman_words.txt', 'r') as file:
        word_list = [line.strip() for line in file.readlines()]
    return random.choice(word_list)

def play_hangman():
    word = select_word().lower()
    guessed_letters = []
    tries = 6  # Number of tries before the game ends

    # Define initial display_word
    display_word = "_" * len(word)

    while tries > 0:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:
                if event.key in key_mapping:
                    guess = key_mapping[event.key]
                    # Check if the guessed letter is in the word (case-insensitive)
                    if guess in guessed_letters:
                        print("You already guessed that letter!")
                    else:
                        if guess in word:
                            print("Correct!")
                            guessed_letters.append(guess)
                        else:
                            if guess not in guessed_letters:
                                print("Wrong guess!")
                                tries -= 1
                                guessed_letters.append(guess)

        # Check if there are any events in the queue before displaying the word
        for index, letter in enumerate(word):
            if letter in guessed_letters:
                display_word = display_word[:index] + letter + display_word[index+1:]

        # Print the current state of the word
        print(display_word)

        # Clear the screen
        screen.fill((0, 0, 0))

        # Update graphical elements based on game logic
        hangman_image = hangman_stages[6 - tries]  # Adjusted index to match tries count
        word_surface = font.render(display_word, True, (255, 255, 255))

        # Draw the graphical elements on the screen
        screen.blit(hangman_image, (x, y))
        screen.blit(word_surface, (new_x, new_y))

        pygame.display.flip()  # Update the display

        # Check if the player has guessed all the letters
        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You guessed the word:", word)
            break

        # Wait for a short time to avoid high CPU usage
        pygame.time.delay(100)

    if tries == 0:
        print("Out of tries. The word was:", word)

# Set up font and coordinates
font = pygame.font.Font(None, 36)
x, y = 325, 150
new_x, new_y = 330, 350

# Start the game
play_hangman()

pygame.quit()'''

# Third version of Hangman with messages displayed
'''import random
import pygame
import string

# Mapping of key constants to corresponding letters
key_mapping = {getattr(pygame, "K_" + letter): letter for letter in string.ascii_lowercase}

hangman_stages = [
    pygame.image.load("hangman_stage0.png"),
    pygame.image.load("hangman_stage1.png"),
    pygame.image.load("hangman_stage2.png"),
    pygame.image.load("hangman_stage3.png"),
    pygame.image.load("hangman_stage4.png"),
    pygame.image.load("hangman_stage5.png"),
    pygame.image.load("hangman_stage6.png"),
]

pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Super Cool & Fun Hangman Game")

def select_word():
    """Selects a random word from the hangman_words.txt file"""
    with open('hangman_words.txt', 'r') as file:
        word_list = [line.strip() for line in file.readlines()]
    return random.choice(word_list)

def display_message(message, font):
    """Display a message on the screen"""
    text_surface = font.render(message, True, (255, 255, 255))
    screen.blit(text_surface, (150, 450))
    pygame.display.flip()

    # Wait for a key press
    key_pressed = False
    while not key_pressed:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                key_pressed = True

def play_hangman():
    word = select_word().lower()
    guessed_letters = []
    tries = 6  # Number of tries before the game ends

    # Define initial display_word
    display_word = "_" * len(word)

    # Set up font
    font = pygame.font.Font(None, 36)

    while tries > 0:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:
                if event.key in key_mapping:
                    guess = key_mapping[event.key]
                    # Check if the guessed letter is in the word (case-insensitive)
                    if guess in guessed_letters:
                        display_message("You already guessed that letter!", font)
                    else:
                        if guess in word:
                            display_message("Correct!", font)
                            guessed_letters.append(guess)
                        else:
                            if guess not in guessed_letters:
                                display_message("Wrong guess!", font)
                                tries -= 1
                                guessed_letters.append(guess)

        # Check if there are any events in the queue before displaying the word
        for index, letter in enumerate(word):
            if letter in guessed_letters:
                display_word = display_word[:index] + letter + display_word[index+1:]

        # Clear the screen
        screen.fill((0, 0, 0))

        # Update graphical elements based on game logic
        hangman_image = hangman_stages[6 - tries]  # Adjusted index to match tries count
        word_surface = font.render(display_word, True, (255, 255, 255))

        # Draw the graphical elements on the screen
        screen.blit(hangman_image, (325, 150))
        screen.blit(word_surface, (330, 350))

        pygame.display.flip()  # Update the display

        # Check if the player has guessed all the letters
        if all(letter in guessed_letters for letter in word):
            display_message("~Congratulations!~ You guessed the word: " + word, font)
            break

        # Wait for a short time to avoid high CPU usage
        pygame.time.delay(100)

    if tries == 0:
        display_message("Out of tries :( The word was: " + word, font)

# Start the game
play_hangman()

pygame.quit() '''

# Fourth version displaying letters already guessed
import random
import pygame
import string

# Mapping of key constants to corresponding letters
key_mapping = {getattr(pygame, "K_" + letter): letter for letter in string.ascii_lowercase}

hangman_stages = [
    pygame.image.load("hangman_stage0.png"),
    pygame.image.load("hangman_stage1.png"),
    pygame.image.load("hangman_stage2.png"),
    pygame.image.load("hangman_stage3.png"),
    pygame.image.load("hangman_stage4.png"),
    pygame.image.load("hangman_stage5.png"),
    pygame.image.load("hangman_stage6.png"),
]

pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Super Cool & Fun Hangman Game")

def select_word():
    """Selects a random word from the hangman_words.txt file"""
    with open('hangman_words.txt', 'r') as file:
        word_list = [line.strip() for line in file.readlines()]
    return random.choice(word_list)

def display_message(message, font):
    """Display a message on the screen"""
    text_surface = font.render(message, True, (255, 255, 255))
    screen.blit(text_surface, (150, 450))
    pygame.display.flip()

    # Wait for a key press
    key_pressed = False
    while not key_pressed:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                key_pressed = True

def play_hangman():
    word = select_word().lower()
    guessed_letters = []
    tries = 6  # Number of tries before the game ends

    # Define initial display_word
    display_word = "_" * len(word)

    # Set up font
    font = pygame.font.Font("Pixellettersfull-BnJ5.ttf", 36)

    while tries > 0:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:
                if event.key in key_mapping:
                    guess = key_mapping[event.key]
                    # Check if the guessed letter is in the word (case-insensitive)
                    if guess in guessed_letters:
                        display_message("You already guessed that letter!", font)
                    else:
                        if guess in word:
                            display_message("Correct!", font)
                            guessed_letters.append(guess)
                        else:
                            if guess not in guessed_letters:
                                display_message("Wrong guess!", font)
                                tries -= 1
                                guessed_letters.append(guess)

        # Check if there are any events in the queue before displaying the word
        for index, letter in enumerate(word):
            if letter in guessed_letters:
                display_word = display_word[:index] + letter + display_word[index+1:]

        # Clear the screen
        screen.fill((0, 0, 0))

        # Update graphical elements based on game logic
        hangman_image = hangman_stages[6 - tries]  # Adjusted index to match tries count
        word_surface = font.render(display_word, True, (255, 255, 255))

        # Draw the graphical elements on the screen
        screen.blit(hangman_image, (325, 150))
        screen.blit(word_surface, (330, 350))

        # Show the guessed letters
        guessed_letters_surface = font.render("Guessed letters: " + ', '.join(guessed_letters), True, (255, 255, 255))
        screen.blit(guessed_letters_surface, (150, 400))

        pygame.display.flip()  # Update the display

        # Check if the player has guessed all the letters
        if all(letter in guessed_letters for letter in word):
            display_message("~Congratulations!~ You guessed the word: " + word, font)
            break

        # Wait for a short time to avoid high CPU usage
        pygame.time.delay(100)

    if tries == 0:
        display_message("Out of tries :( The word was: " + word, font)

# Start the game
play_hangman()

pygame.quit()













































