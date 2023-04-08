import pygame
import sys

pygame.init()

width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Paddle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.width, self.height = 10, 60
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def move(self, dy):
        if self.rect.y + dy >= 0 and self.rect.y + dy <= height - self.height:
            self.rect.y += dy

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width, self.height = 10, 10
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.reset()

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

        if self.rect.y <= 0 or self.rect.y >= height - self.height:
            self.dy = -self.dy

    def reset(self):
        self.rect.center = (width // 2, height // 2)
        self.dx, self.dy = 3, 3

paddle1 = Paddle(10, height // 2 - 30)
paddle2 = Paddle(width - 20, height // 2 - 30)
ball = Ball()

all_sprites = pygame.sprite.Group()
all_sprites.add(paddle1)
all_sprites.add(paddle2)
all_sprites.add(ball)

clock = pygame.time.Clock()

score1, score2 = 0, 0
font = pygame.font.Font(None, 36)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                ball.reset()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        paddle2.move(-5)
    if keys[pygame.K_DOWN]:
        paddle2.move(5)
    if keys[pygame.K_w]:
        paddle1.move(-5)
    if keys[pygame.K_s]:
        paddle1.move(5)

    ball.update()

    if ball.rect.colliderect(paddle1.rect) or ball.rect.colliderect(paddle2.rect):
        ball.dx = -ball.dx

    if ball.rect.x < 0:
        score2 += 1
        ball.reset()
    elif ball.rect.x > width:
        score1 += 1
        ball.reset()

    screen.fill(BLACK)
    all_sprites.draw(screen)
    
    score_text = font.render(f"{score1} - {score2}", True, WHITE)
    screen.blit(score_text, (width // 2 - score_text.get_width() // 2, 10))
    
    pygame.display.flip()
    clock.tick(60)
