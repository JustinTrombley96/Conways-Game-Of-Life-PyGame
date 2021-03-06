import pygame
import sys
import random
import webbrowser
from game_window_class import *
from button_class  import *

width, height = 800, 800
background = (50, 50, 200)
FPS = 60

#---------------------------------Setting

def get_events():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if mouse_on_grid(mouse_pos):
                click_cell(mouse_pos)
            else:
                for button in buttons:
                    button.click()

def update():
    game_window.update()
    for button in buttons:
        button.update(mouse_pos, game_state=state)

def draw():
    window.fill(background)
    for button in buttons:
        button.draw()
    game_window.draw()

#----------------------------------Running

def running_get_events():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if mouse_on_grid(mouse_pos):
                click_cell(mouse_pos)
            else:
                for button in buttons:
                    button.click()

def running_update():
    game_window.update()
    for button in buttons:
        button.update(mouse_pos, game_state=state)
    if frame_count%(FPS//10) == 0:
        game_window.evaluate()

def running_draw():
    window.fill(background)
    for button in buttons:
        button.draw()
    game_window.draw()


#--------------------------------------------------------Paused

def paused_get_events():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if mouse_on_grid(mouse_pos):
                click_cell(mouse_pos)
            else:
                for button in buttons:
                    button.click()

def paused_update():
    game_window.update()
    for button in buttons:
        button.update(mouse_pos, game_state=state)

def paused_draw():
    window.fill(background)
    for button in buttons:
        button.draw()
    game_window.draw()


def mouse_on_grid(pos):
    if pos[0] > 100 and pos[0] < width-100:
        if pos[1] > 180 and pos[1] < height-20:
            return True
    return False

def click_cell(pos):
    grid_pos = [pos[0]-100, pos[1]-180]
    grid_pos[0] = grid_pos[0]//20
    grid_pos[1] = grid_pos[1]//20
    if game_window.grid[grid_pos[1]][grid_pos[0]].alive:
        game_window.grid[grid_pos[1]][grid_pos[0]].alive = False
    else:
        game_window.grid[grid_pos[1]][grid_pos[0]].alive = True

def make_buttons():
    buttons = []
    buttons.append(Button(window, width//2-50, 50, 100, 30, text='Run', color=(100,50,200), hover_color=(20,140,10), bold_text=True, function=run_game, state='setting' ))
    buttons.append(Button(window, width//1.25-50, 50, 100, 30, text='Speed?', color=(255,50,100), hover_color=(20,140,10), bold_text=True, function=random_game, state='setting' ))
    buttons.append(Button(window, width//2-50, 50, 100, 30, text='Pause', color=(20,20,200), hover_color=(20,140,10), bold_text=True, function=pause_game, state='running' ))
    buttons.append(Button(window, width//4-50, 50, 100, 30, text='Reset', color=(255,50,100), hover_color=(20,140,10), bold_text=True, function=reset_grid, state='paused' ))
    buttons.append(Button(window, width//1.25-50, 50, 100, 30, text='Resume', color=(255,50,100), hover_color=(20,140,10), bold_text=True, function=run_game, state='paused' ))
    buttons.append(Button(window, width//5-50, 100, 100, 30, text='Info', color=(255,50,100), hover_color=(20,140,10), bold_text=True, function=about_game))

    return buttons

def about_game():
    url="https://github.com/JustinTrombley96/Conways-Game-Of-Life-PyGame/blob/master/README.md"
    webbrowser.open(url)

def run_game():
    global state 
    state = 'running'
    FPS = 60
    print(FPS)
    return FPS

def random_game():
    global state
    state = 'running'
    FPS = random.randint(20, 100)
    print(FPS)
    return FPS

def pause_game():
    global state 
    state = 'paused'

def reset_grid():
    global state 
    state = 'setting'
    game_window.reset_grid()
    pygame.mixer.music.load('victory_fanfare.mp3')
    pygame.mixer.music.play(0)  


pygame.init()
pygame.font.init()
window = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
game_window = Game_window(window, 100, 180)
buttons = make_buttons()
state = 'setting'
frame_count = 0


running = True
while running:
    frame_count += 1
    mouse_pos = pygame.mouse.get_pos()
    if state == 'setting':
        get_events()
        update()
        draw()
    if state == 'running':
        running_get_events()
        running_update()
        running_draw()
    if state == 'paused':
        paused_get_events()
        paused_update()
        paused_draw()
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()