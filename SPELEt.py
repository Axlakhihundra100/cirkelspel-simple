import pygame
import math

# startar pygame
pygame.init()

# skärm aspect ratio
skärmbredd = 1280
skärmhöjd = 720

# startar skärmen
skärmen = pygame.display.set_mode((skärmbredd, skärmhöjd))
# dehär funkar inte, vet inte varför eller hur de skulle funka
pygame.display.set_caption("AXls SPel")

# har någonting att göra med fps helt ärligt ingen aning
clock = pygame.time.Clock()

# sätter state till meny
skärm = "meny"

# hur stor bollen är/spelaren
radie = 50

# var spelarna starar
pos1 = pygame.Vector2(skärmbredd / 4, skärmhöjd / 2)
pos2 = pygame.Vector2(3 * skärmbredd / 4, skärmhöjd / 2)


# kollar kollision
def kollision(player1, player2):
    längd = math.sqrt((player1.x - player2.x) ** 2 + (player1.y - player2.y) ** 2)
    return längd < (2 * radie)


# meny funktionen
def display_meny():
    skärmen.fill((255, 255, 255))

    font = pygame.font.Font(None, 36)
    text = font.render("Space för att starta", True, (0, 0, 0))
    text_rekt = text.get_rect(center=(skärmbredd / 2, skärmhöjd / 2))

    skärmen.blit(text, text_rekt)


# slutskärmen press esc to quit funkar inte tror jag glömde att skriva den koden
def display_slut():
    skärmen.fill((255, 255, 255))  # White background

    font = pygame.font.Font(None, 36)
    text = font.render("du torska, synd. ESC för att stänga av", True, (0, 0, 0))
    text_rekt = text.get_rect(center=(skärmbredd / 2, skärmhöjd / 2))

    skärmen.blit(text, text_rekt)


running = True
dt = 0
# startar spelet från menyen
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif skärm == "meny" and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            skärm = "spelet"
        elif skärm == "spelet" and event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            skärm = "slut"

    # hämtar spelplanen
    skärmen.fill((255, 255, 255))  # bakgrund

    if skärm == "meny":
        display_meny()
    elif skärm == "spelet":
        keys = pygame.key.get_pressed()

        # kontroller player1
        if keys[pygame.K_w]:
            pos1.y -= 600 * dt
        if keys[pygame.K_s]:
            pos1.y += 600 * dt
        if keys[pygame.K_a]:
            pos1.x -= 600 * dt
        if keys[pygame.K_d]:
            pos1.x += 600 * dt

        # om spelaren går över spelkanten kommer de hamna på andra sidan om
        # exempelvis om de går upp över övre kanten kommer den upp från undre
        pos1.x %= skärmbredd
        pos1.y %= skärmhöjd

        # player1 är blå
        pygame.draw.circle(skärmen, "blue", pos1, radie)

        if keys[pygame.K_UP]:
            pos2.y -= 600 * dt
        if keys[pygame.K_DOWN]:
            pos2.y += 600 * dt
        if keys[pygame.K_LEFT]:
            pos2.x -= 600 * dt
        if keys[pygame.K_RIGHT]:
            pos2.x += 600 * dt

        pos2.x %= skärmbredd
        pos2.y %= skärmhöjd

        pygame.draw.circle(skärmen, "red", pos2, radie)

        # kollar efter  kollision om de kolliderar slutar spelet
        if kollision(pos1, pos2):
            skärm = "slut"
    elif skärm == "slut":
        display_slut()

    pygame.display.flip()
    # fps
    dt = clock.tick(60) / 1000

pygame.quit()
