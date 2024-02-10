import pygame  # importing pygame
from player import Player  # importing the Player class from player.py
from plat import Platform  # importing the Platform class from plat.py
from coin import Coin  # importing the Coin class from coin.py

# initialize pygame
pygame.init()

# set window
window = pygame.display.set_mode((1200, 800))
ground = pygame.Rect(0, 720, 1200, 100)

version = "v0.3"

yellow = (255, 217, 3)
black = (0, 0, 0)

# the x and y position for scoreboard
scoreboard_x = 950
scoreboard_y = 16

# the x and y position for win 
win_x = 580
win_y = 400

# the x and y position for version
Version_x = 560
Version_y = 790

platforms = []
plat = Platform()
p = Player()
coins = []
coins_collected = 0
score = 0

# fonts for all the texts
scoreboard_font = pygame.font.Font('freesansbold.ttf', 20)
win_font = pygame.font.Font('freesansbold.ttf', 100)
version_font = pygame.font.Font('freesansbold.ttf', 9)


platforms.append(plat)

for i in range(25):
    platforms.append(Platform())
    coins.append(Coin())


# draw window
def draw():
    global run
    global coins_collected
    global score

    window.fill((3, 235, 252))  # fill in window with color

    pygame.draw.rect(window, (3, 252, 15), ground)  # draw ground
    p.draw(window, platforms)  # draw player

    scoreboard = scoreboard_font.render(f"Coins collected: {coins_collected}/25 Score: {score} Time: {timer}s", True, yellow)

    win = win_font.render("You win!!!", True, yellow)

    Version = version_font.render(version, True, black)

    scoreboard_textRect = scoreboard.get_rect()
    scoreboard_textRect.center = (scoreboard_x, scoreboard_y)

    win_textRect = win.get_rect()
    win_textRect.center = (win_x, win_y)

    Version_textRect = Version.get_rect()
    Version_textRect.center = (Version_x, Version_y)

    window.blit(scoreboard, scoreboard_textRect)  # displaying the scoreboard
    window.blit(Version, Version_textRect)  # displaying the version
    if coins_collected >= 25:  # checking if the player collects all 25 coins then display win
        window.blit(win, win_textRect)
    for platform in platforms:
        platform.draw(window)
    for coin in coins:
        coin.draw(window)
        if p.hit_box.colliderect(coin.hit_box):  # check if the player's hit box collides with the coin
            # check the time to know how many points to add to
            if timer <= 10:
                score += 5
            elif 10 <= timer <= 20:
                score += 3
            elif 20 <= timer <= 30:
                score += 2
            else:
                score += 1
            coins_collected += 1
            coins.remove(coin)  # remove the coin after collided with player


# game loop
run = True  # creating a variable to control runtime
frame_rate = pygame.time.Clock()  # creating a variable to set framerate

while run:
    timer = pygame.time.get_ticks() / 1000  # set timer
    frame_rate.tick(47)  # setting framerate to 47
    for event in pygame.event.get():  # checking events happening
        if event.type == pygame.QUIT:  # if user hits exit button on window
            run = False  # change the boolean for game runtime and end loop
    draw()  # calling the draw function
    pygame.display.update()  # refreshing display for next frame
