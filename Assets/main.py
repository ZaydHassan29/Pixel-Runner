from cgi import test
from re import I
from time import time
from tkinter import TRUE
from tracemalloc import start
import pygame
from sys import exit
from random import randint
def display_score():
    current_time= int(pygame.time.get_ticks() /1000) - startime
    score_surf = test_font.render(f'Score :  {current_time}',False,(64,64,64))
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit(score_surf,score_rect)
    return current_time

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 6
            if obstacle_rect.bottom == 300:
                screen.blit(snail_surface,obstacle_rect)
            else:
                screen.blit(fly_surf,obstacle_rect)


            

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

        return obstacle_list
    else: return []

def collisions(player,obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect): return False 
    return True
                

def player_animation():
    global player_surface, player_index
    if player_rectangle.bottom < 300:
        player_surface = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk):player_index=0
        player_surface=player_walk[int(player_index)]






pygame.init()

screen= pygame.display.set_mode((800,400))
pygame.display.set_caption("Game")
clock = pygame.time.Clock()
test_font = pygame.font.Font("Assets/font/Pixeltype.ttf", 50)
game_active = False
startime=0
score= 0
bg_Music = pygame.mixer.Sound ('Assets/audio/bg_music.wav')
bg_Music.play(loops = -1)
bg_Music.set_volume(0.1)
oh_no = pygame.mixer.Sound ("Assets/audio/Oh no.mp3")

sky_surface = pygame.image.load('Assets/graphics/Sky.png').convert_alpha()
ground_surface = pygame.image.load('Assets/graphics/ground.png').convert_alpha()
#score_surf = test_font.render("My game", False, (64,64,64)).convert_alpha()
#score_rect=score_surf.get_rect(center = (400, 50))

#Obstacles

#snail
snail_frame_1 = pygame.image.load("Assets/graphics/snail/snail1.png").convert_alpha()
snail_frame_2 = pygame.image.load("Assets/graphics/snail/snail2.png").convert_alpha()
snail_frames= [snail_frame_1,snail_frame_2]
snail_frame_index = 0
snail_surface = snail_frames[snail_frame_index]

#Fly
fly_frame_1 = pygame.image.load("Assets/graphics/fly/fly1.png").convert_alpha()
fly_frame_2 = pygame.image.load("Assets/graphics/fly/fly2.png").convert_alpha()
fly_frames = [fly_frame_1,fly_frame_2]
fly_frame_index = 0
fly_surf = fly_frames[fly_frame_index]

obstacle_rect_list = []

player_walk_1 = pygame.image.load("Assets/graphics/player/player_walk_1.png").convert_alpha()
player_walk_2 = pygame.image.load("Assets/graphics/player/player_walk_2.png").convert_alpha()
player_walk = [player_walk_1 , player_walk_2]
player_index = 0
player_jump = pygame.image.load("Assets/graphics/player/jump.png").convert_alpha()
player_surface = player_walk [player_index]
player_rectangle = player_surface.get_rect(midbottom = (80,300))
player_gravity = 0
player_stand = pygame.image.load("Assets/graphics/player/player_stand.png").convert_alpha()
player_stand_scaled= pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect= player_stand_scaled.get_rect(center = (400, 200))
jump_sound = pygame.mixer.Sound('Assets/audio/jump.mp3')
jump_sound.set_volume(0.2)


game_name=test_font.render("Pixel runner" , False, (111,196,169))
game_name_rect=game_name.get_rect(center=(400,80))

game_message= test_font.render("Press space to run",False, (111,196,169))
game_message_rectangle=game_message.get_rect(center =(400,340))

Level_switch = test_font.render("Good job you got more than 10 score",False, (255,0,0))
Level_switch_rect = Level_switch.get_rect(center = (500,300))

#timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,1500)


snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer,500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer,200)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rectangle.collidepoint(event.pos) and player_rectangle.bottom >=300:
                    player_gravity = -20
                    jump_sound.play()


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rectangle.bottom >=300:
                    player_gravity = -20
                    jump_sound.play()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and player_rectangle.bottom >=300:
                    player_gravity = -20
                    jump_sound.play()
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                startime= int (pygame.time.get_ticks() / 1000)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                game_active = True
                startime= int (pygame.time.get_ticks() / 1000)

            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                game_active = True
                startime= int (pygame.time.get_ticks() / 1000)




            

                

            
        if game_active:
            if event.type == obstacle_timer:
                if randint(0,2):
                
                    obstacle_rect_list.append(snail_surface.get_rect(bottomright=(randint(900,1100),300)))
                else:
                    obstacle_rect_list.append(fly_surf.get_rect(bottomright=(randint(900,1100),210)))

            if event.type == snail_animation_timer:
                if snail_frame_index == 0:
                    snail_frame_index=1
                else: snail_frame_index = 0
                snail_surface = snail_frames[snail_frame_index]
            
            if event.type == fly_animation_timer:
                if fly_frame_index == 0:
                    fly_frame_index=1
                else: fly_frame_index = 0
                fly_surf = fly_frames[fly_frame_index]
        
        

        


    
    if game_active:
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))
       # pygame.draw.rect(screen, "#FFAA33",score_rect)
        #pygame.draw.rect(screen, "#FFAA33",score_rect,10)
        #screen.blit(score_surf,score_rect)
        score = display_score()
        
        #snail_rectangle.x -= 6
        #if snail_rectangle.right <=0: snail_rectangle.left = 800
        #screen.blit(snail_surface,snail_rectangle)


        player_gravity +=+1
        player_rectangle.y += player_gravity
        if player_rectangle.bottom >= 300:
            player_rectangle.bottom=300
        screen.blit(player_surface,player_rectangle)
        player_animation()


        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        game_active = collisions(player_rectangle,obstacle_rect_list)
    else:
        screen.fill((94,129,162))
        screen.blit (player_stand_scaled,player_stand_rect)
        obstacle_rect_list.clear()
        player_rectangle.midbottom = (80,300)
        player_gravity=0

        score_message = test_font.render(f'You score: {score}',False,(111,196,169))
        score_message_rect= score_message.get_rect (center = (400,330))
        screen.blit (game_name,game_name_rect)
        if score == 0:
            screen.blit (game_message,game_message_rectangle)
        else:
            oh_no.play()
            screen.blit (score_message, score_message_rect)


    
    

        


    
    
        
            
        

        
        


        

        


    pygame.display.update()
    clock.tick(60)


