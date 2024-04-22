import pygame


player_speed = 1
player_width = 50
player_height = 50
window_width = 800
window_height = 600
player_x = window_width // 2 - 25
player_y = window_height - 150
window = pygame.display.set_mode((window_width, window_height))
running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    window.fill((135, 206, 250))
    pygame.draw.rect(window, (139, 69, 19), (0, window_height - 100, window_width, 100))
    pygame.draw.rect(window, (0, 128, 0), (0, window_height - 100, window_width, 20))
    pygame.draw.rect(window, (139, 69, 19), (200, window_height - 200, 400, 100))
    pygame.draw.polygon(window, (255, 0, 0), [(200, window_height - 200), (400, window_height - 200), (300, window_height - 300)])
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed
    pygame.draw.rect(window, (255, 255, 255), (player_x, player_y, player_width, player_height))
    pygame.display.flip()
pygame.quit()