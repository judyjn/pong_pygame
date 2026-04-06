import pygame
import random 
#import os

#import operator
pygame.init()
players = {'Player 1': 0,  'Player 2': 0}
W, H = 1000, 600
wn = pygame.display.set_mode((W,H))

run = True
direction = [0, 1]
angle = [0, 1, 2]

#ball
green = (0,255,0)
rad = 15
b_x, b_y = W/2 - rad, H/2 - rad
b_vel_x, b_vel_y = 0.6, 0.6

#paddle
pink = (255, 0, 127)
pad_w, pad_h = 20, 120
left_pad_y = right_pad_y = H/2 - pad_h/2
left_pad_x, right_pad_x = 100 - pad_w/2, W - (100 - pad_w/2)
left_pad_vel = right_pad_vel = 0

#gadget
left_gadget = right_gadget = 0
left_gad_rem = right_gad_rem = 5

while run:
    #players = {'Player 1': 0,  'Player 2': 0}
    wn.fill((0, 0, 0))
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False 
        elif i.type == pygame.KEYDOWN:
            if i.type == pygame.K_y:
                run = True
            if i.type == pygame.K_n:
                run = False
            if i.key == pygame.K_UP:
                right_pad_vel = -0.9
            if i.key == pygame.K_DOWN:
                right_pad_vel = 0.9
            if i.key == pygame.K_RIGHT and right_gad_rem > 0:
                right_gadget = 1
            if i.key == pygame.K_LEFT and right_gad_rem > 0:
                right_gadget = 2
            if i.key == pygame.K_w:
                left_pad_vel = -0.9
            if i.key == pygame.K_s:
                left_pad_vel = 0.9
            if i.key == pygame.K_a and left_gad_rem > 0:
                left_gadget = 1
            if i.key == pygame.K_d and left_gad_rem > 0:
                left_gadget = 2
        if i.type == pygame.KEYUP:
            left_pad_vel = 0
            right_pad_vel = 0  
            
    #ball movement
    if b_y <= 0 + rad or b_y >= H - rad:
        b_vel_y *= -1
    if b_x >= W - rad:
        players['Player 1'] += 1
        b_x, b_y = W/2 - rad, H/2 - rad
        dir = random.choice(direction)
        ang = random.choice(angle)
        if dir == 0:
            if ang == 0:
                b_vel_x, b_vel_y = 0.6, -1.2
            if ang == 1:
                b_vel_x, b_vel_y = 0.6, -0.6
            if ang == 2:
                b_vel_x, b_vel_y = 1.2, -0.6
        if dir == 1:
            if ang == 0:
                b_vel_x, b_vel_y = 0.6, 1.2
            if ang == 1:
                b_vel_x, b_vel_y = 0.6, 0.6
            if ang == 2:
                b_vel_x, b_vel_y = 1.2, 0.6
        #b_vel_x *= -1
        #b_vel_y *= -1
    if b_x <= 0:
        players['Player 2'] += 1
        b_x, b_y = W/2 - rad, H/2 - rad  
        dir = random.choice(direction)
        ang = random.choice(angle)
        if dir == 0:
            if ang == 0:
                b_vel_x, b_vel_y = 0.6, -1.2
            if ang == 1:
                b_vel_x, b_vel_y = 0.6, -0.6
            if ang == 2:
                b_vel_x, b_vel_y = 1.2, -0.6
        if dir == 1:
            if ang == 0:
                b_vel_x, b_vel_y = 0.6, 1.2
            if ang == 1:
                b_vel_x, b_vel_y = 0.6, 0.6
            if ang == 2:
                b_vel_x, b_vel_y = 1.2, 0.6

    #paddle movements
    if left_pad_y >= H - pad_h:
        left_pad_y = H - pad_h
    if left_pad_y <= 0:
        left_pad_y = 0
    if right_pad_y >= H - pad_h:
        right_pad_y = H - pad_h
    if right_pad_y <= 0:
        right_pad_y = 0
    
    #collisions
    if left_pad_x <= b_x <= left_pad_x + pad_w:
        if left_pad_y <= b_y <= left_pad_y + pad_h:
            b_x = left_pad_x + pad_w 
            b_vel_x *= -1
    if right_pad_x <= b_x <= right_pad_x + pad_w:
        if right_pad_y <= b_y <= right_pad_y + pad_h:
            b_x = right_pad_x
            b_vel_x *= -1

    #gadget actions
    if left_gadget == 1:
        if left_pad_x <= b_x <= left_pad_x + pad_w:
            if left_pad_y <= b_y <= left_pad_y + pad_h:
                b_x = left_pad_x + pad_w 
                b_vel_x *= -3.5
                leftt_gadget = 0
                left_gad_rem -= 1
    elif left_gadget == 2:
        left_pad_y = b_y
        left_gadget = 0 
        left_gad_rem -= 1

    if right_gadget == 1:
        if right_pad_x <= b_y <= right_pad_x + pad_w:
            if right_pad_y <= b_y <= right_pad_y + pad_h:
                b_y = right_pad_x + pad_w
                b_vel_x *= -3.5 
                right_gadget = 0
                right_gadget -= 1
    elif right_gadget == 2:
        right_pad_y = b_y
        right_gadget = 0 
        right_gad_rem -= 1

    #movements
    b_x += b_vel_x
    b_y += b_vel_y
    right_pad_y += right_pad_vel
    left_pad_y += left_pad_vel

    #scoreboard
    font = pygame.font.SysFont('comicsansms', 30 )
    score1 = font.render(f'Player 1: {players["Player 1"]}', True, (255, 255, 255) )
    wn.blit(score1, (25, 25))
    score2 = font.render(f'Player 2: {players["Player 2"]}', True, (255, 255, 255) )
    wn.blit(score2, (825, 25))

    pygame.draw.circle(wn, green, (b_x, b_y), rad)
    pygame.draw.rect(wn, pink, pygame.Rect(left_pad_x, left_pad_y, pad_w, pad_h))
    pygame.draw.rect(wn, pink, pygame.Rect(right_pad_x, right_pad_y, pad_w, pad_h))
    if left_gadget == 1:
        pygame.draw.circle(wn, (255,255,255), (left_pad_x + 10, left_pad_y + 10), 4)
    if right_gadget == 1:
        pygame.draw.circle(wn, (255,255,255), (right_pad_x + 10, right_pad_y + 10), 4)
    
    #endgame screen
    winning_font = pygame.font.SysFont('comicsansms', 100)
    if players['Player 1'] == 1 or players['Player 2'] == 1:
        wn.fill((0,0,0))
        winner = font.render(f'{max(players, key = players.get)} WINS!!!!', True, (255,255,255))
        wn.blit(winner, (350, 250)) 
      
    pygame.display.update()
