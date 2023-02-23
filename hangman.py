import pygame
import random

pygame.init()

ecran = pygame.display.set_mode((600, 500))
image = pygame.image.load("image/pendu_0.png").convert()
image_size = (600, 380)

def words():
    f = open('mots.txt')
    result = f.read().splitlines()
    f.close()
    return random.choice(result)

word = words()
frame = True
error = 0
font = pygame.font.Font(None, 50)
lose = font.render(f'you lose, your word was:{word}', True, "black")
letters = []

def hanged_man():
    global image, error
    if error == 1:
        image = pygame.image.load("image/pendu_1.png").convert()
    elif error == 2:
        image = pygame.image.load("image/pendu_2.png").convert()
    elif error == 3:
        image = pygame.image.load("image/pendu_3.png").convert()
    elif error == 4:
        image = pygame.image.load("image/pendu_4.png").convert()
    elif error == 5:
        image = pygame.image.load("image/pendu_5.png").convert()
    elif error == 6:
        image = pygame.image.load("image/pendu_6.png").convert()
    elif error == 7:
        image = pygame.image.load("image/pendu_7.png").convert()
        image = pygame.transform.scale(image, image_size)
        ecran.blit(image, (0, 0))
        ecran.blit(lose, (0, 400))
        pygame.display.update()
        pygame.time.delay(10000)
        pygame.quit()
        quit()

    image = pygame.transform.scale(image, image_size)
    ecran.blit(image, (0, 0))

def victory():
    for i in word:
        if i.lower() not in letters:
            return False
    return True

while frame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            frame = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                frame = False
            elif event.unicode.isalpha() and event.unicode.lower() not in letters:
                letters.append(event.unicode.lower())
                if event.unicode.lower() not in word.lower():
                    error += 1

    ecran.fill((255, 255, 255))
    hanged_man()

    display_word = ""
    for letter in word:
        if letter.lower() in letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    word_found = font.render(display_word, True, (0, 0, 0))
    ecran.blit(word_found, (100, 400))

    letters_text = font.render("Letters: " + ", ".join(letters), True, (0, 0, 0))
    ecran.blit(letters_text, (0, 450))

    if victory():
        win_message = font.render("You win!", True, (0, 255, 0))
        ecran.blit(win_message, (200, 360))
        pygame.display.update()
        pygame.time.delay(10000)
        pygame.quit()
        quit()

    pygame.display.update()

pygame.quit()
