from pygame import *
from time import sleep

window = display.set_mode((700, 500))


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (60, 60))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def change_sprite(self, new_sprite):
        self.image = transform.scale(image.load(new_sprite), (65, 65))


class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_s] and self.rect.y < 495:
            self.rect.y += self.speed
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_d] and self.rect.x < 695:
            self.rect.x += self.speed
        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed


class Enemy(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_x2, direction):
        super().__init__(player_image, player_x, player_y, player_speed)
        self.direction = direction
        self.player_x1 = player_x
        self.player_x2 = player_x2

    def update(self):
        if self.direction == 'right':
            self.rect.x += self.speed
            if self.rect.x > self.player_x2:
                self.direction = 'left'
        else:
            self.rect.x -= self.speed
            if self.rect.x < self.player_x1:
                self.direction = 'right'


class Wall(sprite.Sprite):
    def __init__(self, x, y, height, width, color_tuple):
        super().__init__()
        self.height = height
        self.width = width
        self.color_tuple = color_tuple
        self.image = Surface((width, height))
        self.image.fill(color_tuple)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


def reset_game():
    global player
    player = Player('strawberry.png', 60, 320, 2)
    global counter
    counter = 0
    global final_flag1
    global final_flag2
    global final_flag3
    global final_flag4
    final_flag1 = True
    final_flag2 = True
    final_flag3 = True
    final_flag4 = True
    final1.change_sprite('rubin.png')
    final2.change_sprite('diamond.png')
    final3.change_sprite('izumrud.png')
    final4.change_sprite('diamond2.png')


counter = 0
heart_amount = 3

display.set_caption('StrawRun')
background = transform.scale(image.load('background2.jpg'), (700, 500))
mixer.init()
kick = mixer.Sound('kick.ogg')
money = mixer.Sound('money.ogg')

player = Player('strawberry.png', 60, 320, 2)
heart1 = GameSprite('heart.png', 430, 400, 0)
heart2 = GameSprite('heart.png', 505, 400, 0)
heart3 = GameSprite('heart.png', 580, 400, 0)
enemy1 = Enemy('ponchik.png', 450, 300, 1, 600, 'right')
enemy2 = Enemy('watermelon.png', 50, 150, 1, 170, 'right')
final1 = GameSprite('rubin.png', 580, 50, 0)
final2 = GameSprite('diamond.png', 160, 340, 0)
final3 = GameSprite('izumrud.png', 70, 50, 0)
final4 = GameSprite('diamond2.png', 580, 200, 0)
walls = []
walls.append(Wall(42, 30, 455, 10, (5, 77, 24)))
walls.append(Wall(235, 130, 360, 10, (5, 77, 24)))
walls.append(Wall(140, 300, 10, 100, (5, 77, 24)))
walls.append(Wall(140, 300, 100, 10, (5, 77, 24)))
walls.append(Wall(50, 130, 10, 90, (5, 77, 24)))
walls.append(Wall(50, 30, 10, 380, (5, 77, 24)))
walls.append(Wall(240, 130, 10, 90, (5, 77, 24)))
walls.append(Wall(420, 40, 200, 10, (5, 77, 24)))
walls.append(Wall(340, 240, 10, 90, (5, 77, 24)))
walls.append(Wall(240, 350, 10, 90, (5, 77, 24)))
walls.append(Wall(420, 250, 110, 10, (5, 77, 24)))
walls.append(Wall(670, 30, 455, 10, (5, 77, 24)))
walls.append(Wall(400, 30, 10, 150, (5, 77, 24)))
walls.append(Wall(550, 150, 10, 130, (5, 77, 24)))
walls.append(Wall(41, 480, 10, 640, (5, 77, 24)))
walls.append(Wall(550, 150, 140, 10, (5, 77, 24)))

player.reset()
clock = time.Clock()
FPS = 165
game = True
finish = False

final_flag1 = True
final_flag2 = True
final_flag3 = True
final_flag4 = True

heart_flag1 = True
heart_flag2 = True
heart_flag3 = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.blit(background, (0, 0))
        player.reset()
        player.update()
        heart1.reset()
        heart2.reset()
        heart3.reset()
        enemy1.reset()
        enemy1.update()
        enemy2.reset()
        enemy2.update()
        final1.reset()
        final1.update()
        final2.reset()
        final2.update()
        final3.reset()
        final3.update()
        final4.reset()
        final4.update()
        for wall in walls:
            wall.reset()
        if sprite.collide_rect(player, enemy1):
            heart_amount -= 1
            if heart_amount == 2:
                heart3.change_sprite('edited_heart.png')
            elif heart_amount == 1:
                heart2.change_sprite('edited_heart.png')
            elif heart_amount == 0:
                heart1.change_sprite('edited_heart.png')
                heart1.reset()
            reset_game()
            sleep(2)
        if sprite.collide_rect(player, enemy2):
            heart_amount -= 1
            if heart_amount == 2:
                heart3.change_sprite('edited_heart.png')
            elif heart_amount == 1:
                heart2.change_sprite('edited_heart.png')
            elif heart_amount == 0:
                heart1.change_sprite('edited_heart.png')
                heart1.reset()
            reset_game()
            sleep(2)
        for wall in walls:
            if sprite.collide_rect(player, wall):
                heart_amount -= 1
                if heart_amount == 2:
                    heart3.change_sprite('edited_heart.png')
                elif heart_amount == 1:
                    heart2.change_sprite('edited_heart.png')
                elif heart_amount == 0:
                    heart1.change_sprite('edited_heart.png')
                    heart1.reset()
                reset_game()
                sleep(2)
                break
        if sprite.collide_rect(player, final1) and final_flag1:
            money.play()
            counter += 1
            final_flag1 = False
            final1.change_sprite('DungeonSpider.png')
        if sprite.collide_rect(player, final2) and final_flag2:
            money.play()
            counter += 1
            final_flag2 = False
            final2.change_sprite('DungeonSpider.png')
        if sprite.collide_rect(player, final3) and final_flag3:
            money.play()
            counter += 1
            final_flag3 = False
            final3.change_sprite('DungeonSpider.png')
        if sprite.collide_rect(player, final4) and final_flag4:
            money.play()
            counter += 1
            final_flag4 = False
            final4.change_sprite('DungeonSpider.png')
        if counter == 4:
            finish = True
        if heart_amount == 0:
            finish = True
    display.update()
    clock.tick(FPS)
display.update()
# кайф
