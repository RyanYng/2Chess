import pygame 

pygame.init()

size = (640,640)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My test")


board_dimension = 600
board = pygame.Surface((board_dimension,board_dimension))
board.fill((255,206,158))

square_size = board_dimension/8

# draw the board
for x in range(0, 8, 2):
    for y in range(0, 8, 2):
        pygame.draw.rect(board, (210, 180, 140), (x*square_size, y*square_size, square_size, square_size))
        pygame.draw.rect(board, (210, 180, 140), ((x+1)*square_size, (y+1)*square_size, square_size, square_size))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw shapes
    screen.fill((255, 255, 255))

    screen.blit(board,(20, 20))

    pygame.display.flip()



pygame.quit()


