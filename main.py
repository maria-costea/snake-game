import pygame
from pygame.locals import *
import time
import random

SIZE = 20

SPEED = 0.4

ORANGE = pygame.image.load("resources/block.jpg")
RED = pygame.image.load("resources/block1.jpg")
BLUE = pygame.image.load("resources/block2.jpg")
PINK = pygame.image.load("resources/block3.jpg")
PURPLE = pygame.image.load("resources/block4.jpg")
YELLOW = pygame.image.load("resources/block5.jpg")

class Apple:
    def __init__(self, parent_screen):
        self.image = pygame.image.load("resources/apple.png").convert()
        self.parent_screen = parent_screen
        self.x = 3 * SIZE
        self.y = 3 * SIZE

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(0, 25) * SIZE
        self.y = random.randint(0, 20) * SIZE

class Snake:
    def __init__(self, parent_screen, length):
        self.parent_screen = parent_screen;
        self.block = ORANGE.convert()
        self.x = [SIZE]*length
        self.y = [SIZE]*length
        self.direction = 'úp'
        self.length = length

    def draw(self):
        self.parent_screen.fill((0, 200, 0))
        for i in range(self.length):
            self.parent_screen.blit(self.block,(self.x[i], self.y[i]))
        pygame.display.flip()

    def increase_lenght(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)
    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def change_color_orange(self):
        self.block = ORANGE

    def change_color_red(self):
        self.block = RED

    def change_color_blue(self):
        self.block = BLUE
    
    def change_color_pink(self):
        self.block = PINK
    
    def change_color_purple(self):
        self.block = PURPLE

    def change_color_yellow(self):
        self.block = YELLOW

    def walk(self):

        for i in range(self.length-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        if self.direction == 'up':
            self.y[0] -= SIZE

        if self.direction == 'down':
            self.y[0] += SIZE

        if self.direction == 'left':
            self.x[0] -= SIZE

        if self.direction == 'right':
            self.x[0] += SIZE

        self.draw()

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000, 800))
        self.surface.fill((0,200,0))
        self.snake = Snake(self.surface, 1)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw
        # self.speed = speed

    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        return False

    def play(self):
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.snake.increase_lenght()
            self.apple.move()

    def display_score(self):
        font = pygame.font.SysFont('arial', 30)
        score = font.render(f"Score: {self.snake.length}", True, (255, 255, 255))
        speed = font.render(f"Score: {self.snake.length}", True, (255, 255, 255))
        self.surface.blit(score, (800, 10))
    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
				#verifica daca se apasa alta tasta in afara de esc
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_UP:
                        self.snake.move_up()
                        
                    if event.key == K_DOWN:
                        self.snake.move_down()

                    if event.key == K_LEFT:
                        self.snake.move_left()

                    if event.key == K_RIGHT:
                        self.snake.move_right()

                    if event.key == K_1:
                        self.snake.change_color_orange()

                    if event.key == K_2:
                        self.snake.change_color_red()

                    if event.key == K_3:
                        self.snake.change_color_blue()

                    if event.key == K_4:
                        self.snake.change_color_pink()
                    if event.key == K_5:
                        self.snake.change_color_purple()

                    if event.key == K_6:
                        self.snake.change_color_yellow()

                elif event.type == QUIT:
                    running = False

            self.play()
            if self.snake.length < 25:
                time.sleep(SPEED - 0.144 * (self.snake.length / 10))
            else:
                time.sleep(0.04)    
            

if __name__ == "__main__":
    game = Game()
    game.run()
