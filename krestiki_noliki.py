import pygame
import sys

pygame.init()
size_block = 100
otstup = 15
width = heigth = size_block*3 + otstup*4

size_window = (width,heigth)
screen = pygame.display.set_mode(size_window)
pygame.display.set_caption("Крестики-нолики")

black = (0,0,0)
red = (255, 0, 0)
green = (0, 255, 0)
white = (255,255,255)
mass = [[0]*3 for i in range(3)]
subseq = 0
game_over = False

def check_win(mass,sign):
    zeroes = 0
    for row in mass:
        zeroes += row.count(0)
        if row.count(sign) == 3:
            return sign
    for col in range(3):
        if mass[0][0] == sign and mass[1][1] == sign and mass[2][2] == sign:
            return sign
        if mass[0][2] == sign and mass[1][1] == sign and mass[2][0] == sign:
            return sign
        if mass[0][0] == sign and mass[0][1] == sign and mass[0][2] == sign:
            return sign
        if mass[2][0] == sign and mass[1][0] == sign and mass[0][0] == sign:
            return sign
        if mass[0][1] == sign and mass[0][2] == sign and mass[0][3] == sign:
            return sign
        if mass[1][0] == sign and mass[1][1] == sign and mass[1][2] == sign:
            return sign
        if zeroes == 0:
            return 'Ничья, Tab'
        return False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            col = x_mouse // (size_block + otstup)
            row = y_mouse // (size_block + otstup)
            if mass[row][col] == 0:
                if subseq%2 == 0:
                    mass[row][col] = 'x'
                else:
                    mass[row][col] = 'o'
                subseq +=1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_TAB:
            game_over = False
            mass = [[0]*3 for i in range(3)]
            subseq = 0
            screen.fill(black)
    if not game_over:
        for row in range(3):
            for col in range(3):
                if mass[row][col] == 'x':
                    color = red
                elif mass[row][col] == 'o':
                    color = green
                else:
                    color = white
                x = col*size_block + (col + 1) * otstup
                y = row*size_block + (row + 1) * otstup
                pygame.draw.rect(screen,color, (x,y,size_block,size_block))
                if color == red:
                    pygame.draw.line(screen,white, (x+5,y+5), (x+size_block-5,y+size_block-5),5)
                    pygame.draw.line(screen,white, (x+size_block-5,y+5), (x+5,y+size_block-5),5)
                elif color == green:
                    pygame.draw.circle(screen, white, (x+size_block//2, y+size_block//2),size_block//2-3,5)
        if (subseq - 1)%2 == 0:
            game_over = check_win(mass,'x')
        else:
            game_over = check_win(mass,'o')

        if game_over:
            screen.fill(black)
            font = pygame.font.SysFont('stxinqkai', 80)
            text1 = font.render(game_over,True, white)
            text_rect = text1.get_rect()
            text_x = screen.get_width() / 2 - text_rect.width / 2
            text_y = screen.get_height() / 2 - text_rect.height / 2
            screen.blit(text1, [text_x,text_y])
    pygame.display.update()
