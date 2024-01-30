import pygame
import time
import random
pygame.font.init()
pygame.init()

pygame.display.set_caption("Catcher")
WIDTH,HEIGHT = 1100, 700
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
BG = pygame.transform.scale(pygame.image.load("appleforest.jpg"),(WIDTH,HEIGHT))
FONT = pygame.font.SysFont("comicsans", 30)
FPS = 60
VEL = 10


BASKET_IMAGE = pygame.image.load("basket.png")
BASKET_WIDTH =170
BASKET_HEIGHT =100
BASKET = pygame.transform.scale(BASKET_IMAGE, (BASKET_WIDTH,BASKET_HEIGHT))


APPLE_IMAGE = pygame.image.load("apple.png")
APPLE_WIDTH =80
APPLE_HEIGHT =80
APPLEE = pygame.transform.scale(APPLE_IMAGE, (APPLE_WIDTH, APPLE_HEIGHT))

def draw_window(basket_player, apple_enemy, score):
    WIN.blit(BG,(0,0))
    WIN.blit(BASKET, (basket_player.x , basket_player.y))
    WIN.blit(APPLEE, (apple_enemy.x ,apple_enemy.y))
    score_text = FONT.render(f"Score: {round(score)}",1,"white")
    WIN.blit(score_text,(10,10))
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    score = 0

    apple_enemy = pygame.Rect(1, 1, APPLE_WIDTH, APPLE_HEIGHT)
    basket_player = pygame.Rect(400, 550, BASKET_WIDTH, BASKET_HEIGHT)

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_a] and basket_player.x - VEL >= 0:
            basket_player.x -= VEL
        if keys_pressed[pygame.K_d] and basket_player.x + VEL + BASKET_WIDTH <= WIDTH:
            basket_player.x += VEL


        draw_window(basket_player, apple_enemy, score)

    pygame.quit()


if __name__ == "__main__":
    main()