import pygame
from ball import Ball
from paddle import Paddle
from tkinter import messagebox
import tkinter as tk

WIDTH = 700
HEIGHT = 500
BLACK = '#000000'
WHITE = '#FFFFFF'
FPS = 144
x = 0

def reset_game():
    ball.reset(WIDTH//2, HEIGHT//2)
    paddle_left.reset(10, HEIGHT//2-50)
    paddle_right.reset(WIDTH-25, HEIGHT//2-50)
    

root = tk.Tk()#創建TKINTER視窗
root.withdraw() #隱藏主視窗

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT)) # 創建視窗寬和高
pygame.display.set_caption('乒乓球')# 創標題
clock = pygame.time.Clock()

ball = Ball(WIDTH//2, HEIGHT//2, 10, WHITE)
paddle_left = Paddle(10, HEIGHT//2-50, 15, 100, WHITE)
paddle_right = Paddle(WIDTH-25, HEIGHT//2-50, 15, 100, WHITE)

font = pygame.font.Font('微軟正黑體.ttf', 40) #字型檔案 文字大小

player_1 = font.render("Player 1", True, WHITE)
player_2 = font.render("Player 2", True, WHITE)

running = True
while running:
    clock.tick(FPS) # limits FPS to 144
    # 取得輸入
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # elif event.type == pygame.KEYDOWN: #偵測鍵盤 (按一下)
        #     if event.key == pygame.K_UP:
        #         print('上')
        #     elif event.key == pygame.K_DOWN:
        #         print('下')
    # 遊戲更新
    ball.update(WIDTH, HEIGHT, paddle_left, paddle_right)
    ball.check_collide(paddle_left, paddle_right)

    if paddle_left.score >= 11:
        final_score = f"Final Score: {paddle_left.score} - {paddle_right.score}"
        replay = messagebox.askyesno("Game Over", f"Player 1 Win!\n{final_score}\nDo you want to play again?")
        if replay:
            reset_game()
        else:
            running = False

    elif paddle_right.score >= 11:
        final_score = f"Final Score: {paddle_left.score} - {paddle_right.score}"
        replay = messagebox.askyesno("Game Over", f"Player 2 Win!\n{final_score}\nDo you want to play again?")
        if replay:
            reset_game()
        else:
            running = False

    point_left = font.render(f"{paddle_left.score}", True, WHITE) #要寫的字 是否要抗鋸齒 文字顏色
    point_right = font.render(f'{paddle_right.score}', True, WHITE)
    keys = pygame.key.get_pressed()#偵測是否一直按著
    if keys[pygame.K_w]:
        paddle_left.update(True, HEIGHT)
    if keys[pygame.K_s]:
        paddle_left.update(False, HEIGHT)
    if keys[pygame.K_UP]:
        paddle_right.update(True, HEIGHT)
    if keys[pygame.K_DOWN]:
        paddle_right.update(False, HEIGHT)


    # 畫面顯示
    window.fill(BLACK)# 畫面顏色 
    window.blit(point_left, (100, 50))# 顯示字
    window.blit(point_right, (WIDTH-100-point_right.get_width(), 50))
    window.blit(player_1, (43, 0))
    window.blit(player_2, (WIDTH-32-player_2.get_width(), 0))
    ball.draw(window)
    paddle_left.draw(window)
    paddle_right.draw(window)
    pygame.display.flip()# flip() the display to put your work on screen

pygame.quit()
root.destroy()