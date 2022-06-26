import curses
from hashlib import new 
import random 
import curses

s = curses.initscr() # initialize a screen
curses.curs_set(0) #ensure cursor does not show up on screen
s_height,s_width = s.getmaxyx() # get height and width of screen
s_height = int(s_height)
s_width = int(s_width)

w = curses.newwin(s_height,s_width,0,0) #new window with height and width ; 0,0 is for initial window position 
w.keypad(1) #to accept keypad input
w.timeout(100) #refreshes screen every 100 miliseconds

snake_init_x = s_width / 4 #starting x,y position of snake head
snake_init_x = int(snake_init_x)
snake_init_y = s_height / 2
snake_init_y = int(snake_init_y)

snake = [ #body of snake ; 1 x 3 snake
    [snake_init_y,snake_init_x],
    [snake_init_y,snake_init_x-1],
    [snake_init_y,snake_init_x-2]
]

fruit = [int(s_height/2),int(s_width/2)] # first fruit at centre of screen
w.addch(fruit[0],fruit[1],curses.ACS_DIAMOND) #Adds fruit to screen , input fruit positions

key = curses.KEY_RIGHT#inital direction of snake

while True: # game runs infinitely
    next_key = w.getch() #wait for next key input, in this case change direction input
    key = key if next_key == -1 else next_key # key input is either nothing or the next key ; -1 is an impossbile input

    #game ends if snake head ends up at border of screen
    #lose game if y position at bottom or top of screen
    #lose game if x position at left or right of screen
    #lose game if snake in itself

    if snake[0][0] in [0,s_height] or snake[0][1] in [0,s_width] or snake[0] in snake[1:]:
        curses.endwin()
        quit()



#Direction movement input, eg. if key = down, add 1 to y position
    new_head = [snake[0][0] , snake[0][1]]

    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_DOWN:
        new_head[0] += 1

    snake.insert(0,new_head) # now to check whether snake ran into fruit

    if snake[0] == fruit:
        fruit = None
        while fruit is None:
            new_fruit = [random.randint(1,s_height-1),random.randint(1,s_width-1)]
            fruit = new_fruit if new_fruit not in snake else None #this will generate new fruit if snake eats fruit
        w.addch(fruit[0],fruit[1],curses.ACS_DIAMOND) #add fruit 
    else:
        tail = snake.pop()
        w.addch(tail[0],tail[1]," ") #add space where tail was

    w.addch(snake[0][0],snake[0][1],curses.ACS_CKBOARD) #add to screen








    







