import pygame
import random
from paddle import Paddle 
import math

class Ball:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed = 3
        self.reset(x, y)

    def update(self, width:int , height:int, paddle_left:Paddle, paddle_right:Paddle):
        self.x += self.speedx
        self.y += self.speedy
        ball_top = self.y - self.radius
        ball_bottom = self.y + self.radius
        ball_left = self.x - self.radius
        ball_right = self.x + self.radius
        if ball_top < 0 or ball_bottom > height:
            self.speedy *= -1

        if ball_left < 0 :
            paddle_right.score += 1
            self.reset(width/2, height/2)
        elif ball_right > width:
            paddle_left.score += 1
            self.reset(width/2, height/2)
                

    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)

    def reset(self, x, y):
        self.x = x
        self.y = y
    
        # 定義允許的角度範圍
        allowed_ranges = [
            (21.0, 69.0),   
            (111.0, 159.0),
            (201.0, 249.0),  
            (291.0, 339.0)   
        ]
    
        # 直接從允許的範圍中選擇
        # 從這個列表中隨機選擇一個元組 如果選到 (21.0, 69.0)，則 start 會得到 21.0，end 會得到 69.0
        start, end = random.choice(allowed_ranges)
        # 在指定的範圍內隨機生成一個浮點數
        angle_degrees = random.uniform(start, end)
        # 將角度（degrees）轉換為弧度（radians）
        angle = math.radians(angle_degrees)
        
        self.speedx = self.speed * math.cos(angle)
        self.speedy = self.speed * math.sin(angle)

    
    def check_collide(self, paddle_left:Paddle, paddle_right:Paddle):
        paddle_left_top = paddle_left.y
        paddle_left_bottom = paddle_left.y + paddle_left.height
        paddle_left_left = paddle_left.x
        paddle_left_right = paddle_left.x + paddle_left.width

        paddle_right_top = paddle_right.y
        paddle_right_bottom = paddle_right.y + paddle_right.height
        paddle_right_left = paddle_right.x
        paddle_right_right = paddle_right.x + paddle_right.width

        if self.speedx < 0 and self.speedy < 0:
            ball_left_x = self.x - self.radius
            ball_left_y = self.y

            if paddle_left_top <= ball_left_y and\
                paddle_left_bottom >= ball_left_y and\
                paddle_left_left <= ball_left_x and\
                paddle_left_right >= ball_left_x:

                self.speedx *= -1
                self.speedy += random.randint(-3, -1)
        
        elif self.speedx < 0 and self.speedy > 0:
            ball_left_x = self.x - self.radius
            ball_left_y = self.y

            if paddle_left_top <= ball_left_y and\
                paddle_left_bottom >= ball_left_y and\
                paddle_left_left <= ball_left_x and\
                paddle_left_right >= ball_left_x:

                self.speedx *= -1
                self.speedy += random.randint(1, 3)

        elif self.speedx > 0 and self.speedy < 0 :
            ball_right_x = self.x + self.radius
            ball_right_y = self.y

            if paddle_right_top <= ball_right_y and\
                paddle_right_bottom >= ball_right_y and\
                paddle_right_left <= ball_right_x and\
                paddle_right_right >= ball_right_x:

                self.speedx *= -1
                self.speedy += random.randint(-3, -1)

        else:
            ball_right_x = self.x + self.radius
            ball_right_y = self.y

            if paddle_right_top <= ball_right_y and\
                paddle_right_bottom >= ball_right_y and\
                paddle_right_left <= ball_right_x and\
                paddle_right_right >= ball_right_x:

                self.speedx *= -1
                self.speedy += random.randint(1, 3)