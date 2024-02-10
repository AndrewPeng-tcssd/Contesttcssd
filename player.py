import pygame  # importing pygame

class Player:
    def __init__(self):
        self.x = 500  # player's initial x position
        self.y = 670  # player's initial y position
        self.hit_box = pygame.Rect(self.x, self.y, 20, 20)  # player's hitbox for collisions
        self.sprite = None  # placeholder for player sprite, if any
        self.speed = 5  # player's movement speed
        self.g = 10  # gravity variable affecting player
        self.inAir = [False, False, False]  # array tracking jump states
        self.release = False  # flag to check if jump button is released
        self.t = 0  # timer for handling jump button release

    def draw(self, window, platforms):
        self.move(platforms)  # updating player's position based on movement and collisions
        pygame.draw.rect(window, (255, 0, 0), self.hit_box)  # drawing player hitbox

    def gravity(self, col_bottom, col_up, jumping):
        if not col_bottom:  # apply gravity if player is not on solid ground/platform
            self.y += self.g
            self.g += 1.3  # gravity increases to simulate acceleration
        else:
            self.g = 10  # reset gravity when player lands
            self.y += self.speed / 2
        if col_up:
            self.y -= 10

        if self.y >= 700:  # check for ground collision
            self.y = 700  # reset player position to ground
            self.inAir = [False, False, False]  # reset jump states
            self.g = 10  # reset gravity

    def move(self, platforms):
        col_up = False  # flag for collision above player
        col_bottom = False  # flag for collision below player
        for platform in platforms:
            if self.hit_box.colliderect(platform.up):  # check for collision with bottom of platform
                col_up = True
                self.y = platform.y - 20  # adjust player position to stand on platform
                self.g = 10  # reset gravity
                self.inAir = [False, False, False]  # reset jump states
            elif self.hit_box.colliderect(platform.bottom) and self.g < 0:  # collision while moving up
                col_up = True
                self.g = 1  # minimal gravity to stop upward movement

            if self.hit_box.colliderect(platform.bottom):  # collision with top of platform
                col_bottom = True

        user_input = pygame.key.get_pressed()  # capture keyboard input
        jumping = False
        if user_input[pygame.K_UP] and not self.inAir[2] and not self.release:  # initiate jump if conditions met
            self.release = True
            jumping = True
            if not self.inAir[0]:  # first jump
                self.y -= 10
                self.g = -15
                self.inAir[0] = True
            elif not self.inAir[1]:  # second jump
                self.inAir[1] = True
                self.g -= 20
            else:  # third jump
                self.inAir[2] = True
                self.g -= 21
            self.t = 0
        elif self.release and self.t > 10:  # allow for jump reinitiation after release
            self.release = False
        else:
            self.t += 1  # increment timer for jump release
            jumping = False
        if user_input[pygame.K_LEFT]:  # move left
            self.x -= self.speed
        if user_input[pygame.K_RIGHT]:  # move right
            self.x += self.speed
        self.gravity(col_bottom, col_up, jumping)  # apply gravity based on collision states
        self.hit_box = pygame.Rect(self.x, self.y, 20, 20)  # update hitbox position
