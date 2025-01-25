import pygame

class Paddle:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speedy = 6
        self.score = 0

    def update(self, up, height):
        if up:
            self.y -= self.speedy
        else:
            self.y += self.speedy
        
        if self.y < 0:
            self.y = 0
        elif self.y + self.height > height:
            self.y = height - self.height
            
    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))

    def reset(self, x, y):
        self.x = x
        self.y = y
        self.score = 0