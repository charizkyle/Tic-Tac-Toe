import pygame

pygame.init()
pygame.mixer.init() # Initialize Pygame mixer for sound

# Set up the display
screen = pygame.display.set_mode((450,450))
pygame.display.set_caption("Tic Tac Toe")

# Load start screen images
start_bg = pygame.image.load("START BG.png")
start_button = pygame.image.load("start button.png")
start_bg = pygame.transform.scale(start_bg, (450, 450))
start_button = pygame.transform.scale(start_button, (200, 160))

# Load game images
background = pygame.image.load("BACKGROUND.png")
heart = pygame.image.load("HEART.png")
star = pygame.image.load("STAR.png")
draw_img = pygame.image.load("draw.png")
heart_wins_img = pygame.image.load("heart wins.png")
star_wins_img = pygame.image.load("star wins.png")

# Resize images to fit the game
background = pygame.transform.scale(background, (450, 450))
heart = pygame.transform.scale(heart, (125, 125))
star = pygame.transform.scale(star, (125, 125))
draw_img = pygame.transform.scale(draw_img, (450, 450))
heart_wins_img = pygame.transform.scale(heart_wins_img, (450, 450))
star_wins_img = pygame.transform.scale(star_wins_img, (450, 450))


# Load sounds
pygame.mixer.music.load("BG MUSIC.mp3")  # Background music
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)


# Function to display the start screen
def show_start_screen():
    screen.blit(start_bg, (0, 0))
    screen.blit(start_button, (125, 300))
    pygame.display.update()
   
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = event.pos
                if 125 <= mouseX <= 325 and 300 <= mouseY <= 380:
                    return  # Exit function and start game


# Show the start screen before the game begins
show_start_screen()


# Grid coordinates
coor = [[(40, 50), (165, 50), (290, 50)],
        [(40, 175), (165, 175), (290, 175)],
        [(40, 300), (165, 300), (290, 300)]]


# Tic-tac-toe board state
def reset_game():
    global table, shift, game_over
    table = [['', '', ''], ['', '', ''], ['', '', '']]
    shift = "heart"
    game_over = False


def graphic_board():
    screen.blit(background, (0, 0))
    for row in range(3):
        for col in range(3):
            if table[row][col] == "heart":
                draw_heart(row, col)
            elif table[row][col] == "star":
                draw_star(row, col)


def draw_heart(row, col):
    screen.blit(heart, coor[row][col])


def draw_star(row, col):
    screen.blit(star, coor[row][col])


def check_winner():
    for row in range(3):
        if table[row][0] == table[row][1] == table[row][2] != "":
            return table[row][0]
        if table[0][row] == table[1][row] == table[2][row] != "":
            return table[0][row]
    if table[0][0] == table[1][1] == table[2][2] != "":
        return table[0][0]
    if table[0][2] == table[1][1] == table[2][0] != "":
        return table[0][2]
    return None


def is_draw():
    for row in table:
        for cell in row:
            if cell == "":
                return False
    return True


# Game loop
reset_game()
clock = pygame.time.Clock()
while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX, mouseY = event.pos
            if (40 <= mouseX < 415) and (50 <= mouseY < 425):
                row = (mouseY - 50) // 125
                col = (mouseX - 40) // 125
                if table[row][col] == "":
                    table[row][col] = shift                  
                    winner = check_winner()
                    if winner:
                        game_over = True
                        if winner == "heart":
                            screen.blit(heart_wins_img, (0, 0))
                        else:
                            screen.blit(star_wins_img, (0, 0))
                        pygame.display.update()
                        pygame.time.delay(2000)
                        reset_game()
                    elif is_draw():
                        screen.blit(draw_img, (0, 0))
                        pygame.display.update()
                        pygame.time.delay(2000)
                        reset_game()
                    else:
                        shift = "star" if shift == "heart" else "heart"
   
    graphic_board()
    pygame.display.update()