import turtle
import random
import time             #win_game and lose_game functions, time.sleep(seconds) used here to create simple animations

### Player field: 10x10 grid ###
#Define the screen and setup size. (e.g., 600x600 pixels)
grid_size = 5
screen_size =600
#Calculate the size of each grid cell
cell_size = screen_size // grid_size
screen = turtle.Screen()
screen.setup(screen_size+400, screen_size+400)    #sets size of entire window
screen.title("The Nightmare Crawl")
screen.bgcolor("black")    # changed to dark background

#Draw horizontal and vertical lines for grid (create new turtle)
grid_drawer = turtle.Turtle()
grid_drawer.speed(0)
grid_drawer.color ("gray")    # changed from black to gray for visibility
grid_drawer.penup()     #to move without drawing
grid_drawer.hideturtle()    #hides the turtle cursor

#columns
for c in range(grid_size+1):    #loop runs once for each column line
    x = -screen_size // 2 + c*cell_size    #starts form bottom left edge of screen, calculates the x-coordinate where the vertical line should be drawn. starts at the far left edge of the screen.moves the position to the right by one cell each loop.
    grid_drawer.goto(x,-screen_size//2)    #(x,y)
    grid_drawer.pendown()
    grid_drawer.goto(x,screen_size//2)     #(x,y)
    grid_drawer.penup()

#rows
for r in range (grid_size+1):
    y = -screen_size // 2 + r*cell_size    #starts from bottom left edge of screen, exactly like x
    grid_drawer.goto(-screen_size//2,y)    #(x,y) starts writing from exact point as the columns
    grid_drawer.pendown()
    grid_drawer.goto(screen_size//2,y)     #(x,y)
    grid_drawer.penup()

#Intro message in terminal
print("It is dark, Find the flashlight! Move with (w/a/s/d) or arrow keys on keyboard")

#Intro message on screen
intro_writer = turtle.Turtle()
intro_writer.hideturtle()
intro_writer.penup()
intro_writer.color("white")
intro_writer.goto(0, screen_size // 2 - 40)  # near the top center
intro_writer.write("It is dark, Find the flashlight!", align="center", font=("Arial", 20, "bold"))

### Player pink dot ###
#Create a pink dot Turtle that can move from cell to cell (Allow keyboard movement (WASD or arrow keys))
player = turtle.Turtle()
player.shape("circle")
player.color("pink")    # pink works well on black background
player.penup()
player.speed(0)

#start player and flashlight at a random cell
player_pos = [random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)]

# Text display turtle for move counter and messages
text_writer = turtle.Turtle()
text_writer.hideturtle()
text_writer.penup()
text_writer.color("white")
text_writer.goto(-450,200)  # moved far left outside grid

# New turtle for centered win/lose messages
center_writer = turtle.Turtle()
center_writer.hideturtle()
center_writer.penup()
center_writer.color("white")

while True:     #flashlight position can´t be same as player position
    flashlight_pos = [random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)]
    if flashlight_pos != player_pos:
        break

#counter for number of tries
moves_left = 10

# Flag to stop movement after game ends
game_over = False

#Move the  dot to the center of the current grid cell.
def move_player():
    x = -screen_size//2 + cell_size//2 + player_pos[0]*cell_size
    y = -screen_size//2 + cell_size//2 + player_pos[1]*cell_size
    player.goto(x,y)

# Movement feedback for terminal hints
def give_feedback():
    dx = flashlight_pos[0] - player_pos[0]      #x coordinate of flashligt and player, horisontal difference in number of cells
    dy = flashlight_pos[1] - player_pos[1]      #y coordinate of flashlight and player, vertical difference in number of cells
    distance = abs(dx) + abs(dy)                # calculates total number of grid moves needed to get from one cell to another if you can only move up/down/left/right


    if player_pos == flashlight_pos:        #stop the function from giving feedback once the player has found the flashlight
        return

    if distance == 1:
        print("I can hear something, you are close!")
    elif distance >= 3:
        print("You are too far away!")
    else:
        direction_str = "The flashlight is "
        if dx > 0:
            direction_str += "east "
        elif dx < 0:
            direction_str += "west "

        if dy > 0:
            direction_str += "north "
        elif dy < 0:
            direction_str += "south "

        print(direction_str + "from you!")

# Will update text display of moves
def update_moves_display():
    text_writer.clear()
    text_writer.goto(-450, 200)  # move before writing every time!
    text_writer.write(f"Moves left:\n{moves_left}", align="left", font=("Arial", 20, "normal"))

# Win animation: Pink dot grows and message displayed
def win_game():
    global game_over
    game_over = True
    print("You found the flashlight!")
    center_writer.clear()
    center_writer.goto(0, 0)
    center_writer.write("YOU WON!", align="center", font=("Arial", 48, "bold"))

    # Grow the player dot until it covers the whole screen
    max_size = (screen_size + 400) // 20  # scale factor based on window size
    for size in range(10, max_size + 1, 2):
        player.shapesize(size)
        time.sleep(0.03)
    # Window remains open until manually closed

# Lose animation: screen turns dark and message displayed
def lose_game():
    global game_over
    game_over = True
    print("The dark is taking over... you lost!")
    screen.bgcolor("black")
    player.hideturtle()
    center_writer.clear()
    center_writer.goto(0, 0)
    center_writer.write("YOU LOST", align="center", font=("Arial", 48, "bold"))
    time.sleep(2)
    # Window remains open until manually closed

#checks if flashlight is found and updates moves
def handle_move():
    global moves_left       #global function defined from outside
    moves_left -= 1
    update_moves_display()      #keeps moves counted on screen
    move_player()
    give_feedback()

    if player_pos == flashlight_pos:
        win_game()
    elif moves_left == 0:
        lose_game()

#Movement controls
def move_up():
    global game_over
    if game_over:
        return
    if player_pos[1] < grid_size-1:
        player_pos[1] += 1
        handle_move()

def move_down():
    global game_over
    if game_over:
        return
    if player_pos[1] > 0:
        player_pos[1] -= 1
        handle_move()

def move_left():
    global game_over
    if game_over:
        return
    if player_pos[0] > 0:
        player_pos[0] -= 1
        handle_move()

def move_right():
    global game_over
    if game_over:
        return
    if player_pos[0] < grid_size-1:
        player_pos[0] += 1
        handle_move()

#Move player initially on screen
move_player()
update_moves_display()

#Key bindings = the way you connect (bind) certain keyboard keys to specific functions or actions in your program. Use the arrows on keyboard (by name) or wsad
screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

# Also WASD controls
screen.onkey(move_up, "w")
screen.onkey(move_down, "s")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")

screen.mainloop()

