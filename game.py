from pygame import *

win_width = 700
win_height = 500
player = 'rocket.png'

class GameSprite(sprite.Sprite):
    #конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        #вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)

        #каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    #метод, отрисовывающий героя на окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#класс главного игрока
class Player(GameSprite):
    #метод для управления спрайтом стрелками клавиатуры
    def update_1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

    def update_2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed


display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))

window.fill((210, 105, 30))

player_1 = Player(player, 0, win_height/2, 20, 140, 10)
player_2 = Player(player, win_width-20, win_height/2, 20, 140, 10)

run = True

while run:
    window.fill((210, 105, 30))
    for e in event.get():
        if e.type == QUIT:
            run = False

    player_1.reset()
    player_1.update_1()
    player_2.reset()
    player_2.update_2()
    display.update()
    time.delay(50)
