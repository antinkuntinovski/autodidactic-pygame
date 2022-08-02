
import random
import sys
import pygame
import math
FPS=30

pygame.init()
screen = pygame.display.set_mode((1000, 700))#pencere boyut
icon = pygame.image.load('arka_plan.jpeg')
pygame.display.set_icon(icon)
background=pygame.image.load('arka_plan.jpeg')#background ayarı (1)
title=pygame.display.set_caption("SPACE WAR")
saat=pygame.time.Clock()
class Player(pygame.sprite.Sprite): # player için bir sınıf oluşturuluyor.
    def __init__(self): # Sınıfın ana parametrelerini taşıyacak fonksiyon oluşturuluyor.
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('dost.png') # Karakterin görseli atanıyor.
        self.rect = self.image.get_rect() # Karakterin haraketi ve çarpışması için bir dikdörtgen oluşturuluyor.
        self.rect.centerx =  random.randint(0, 900)# Karakterin  x başlangıç koordinatları atanıyor.
        self.rect.centery= random.randint(0,600)#karakterin y başlangıç koordinatları

    def update(self):  # Aksiyonların ekrana yansıtılması için güncelleyici fonksiyon çağrılıyor.
        self.hizx = 0  # Hız sıfırlanıyor.

        tusdurumu = pygame.key.get_pressed()  # Tuşa basılma olayı bir değişkene çekiliyor.
        if tusdurumu[pygame.K_LEFT]:  # Sol ok tuşuna basıldı ise,
            self.hizx = -6  # Hız verisine gereken değer atanıyor.
        if tusdurumu[pygame.K_RIGHT]:
            self.hizx = 6
        self.rect.x += self.hizx  # Karaktere hız verisi ekleniyor.
        if 900 < self.rect.right:  # Karakterin pencere içinde kalması sağlanıyor.
            self.rect.right = 600
        if self.rect.left < 0:
            self.rect.left = 0


class Enemy(pygame.sprite.Sprite):  # Lazer için bir sınıf oluşturuluyor.
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image =  pygame.image.load('dusman.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(0, 900)  # Karakterin  x başlangıç koordinatları atanıyor.
        self.rect.centery = random.randint(0, 600)  # karakterin y başlangıç koordinatları
        self.hizy =2

    def update(self):
        self.rect.centery += self.hizy
        if self.rect.bottom < 0:  # Enemy pencere dışına çıktı ise,
            self.kill()  # Enemy yok ediliyor.

class Game(object):
    '''def __init__(self):
        self.player=Player()
        self.enemy = Enemy()
        self.enemy1=Enemy()
        self.runway= Runway()
        self.screen = pygame.display.set_mode((1000, 800))
        self.screen.blit(self.player.img, (self.player.x, self.player.y))
        self.screen.blit(self.enemy.img, (self.enemy.x, self.enemy.y))
        self.screen.blit(self.enemy1.img, (self.enemy1.x, self.enemy1.y))
        self.screen.blit(self.runway.img,(self.runway.x,self.runway.y))'''''
class Player():
    def __init__(self):
        self.img = pygame.image.load('dost.png')
        self.x = random.randint(0, 900)
        self.y = random.randint(0, 600)
        self.hız=10
    def temas(self):
        pass
    def hareket(self):
        tus=pygame.key.get_pressed()
        if tus[pygame.K_LEFT]:
            self.player.rect.x-=self.hız
        elif tus[pygame.K_RIGHT]:
            self.player.rect.x+=self.hız
        elif tus[pygame.K_UP]:
            self.player.rect.y-=self.hız
        elif tus[pygame.K_DOWN]:
            self.player.rect.y+=self.hız
'''class Enemy():
    def __init__(self):
        self.img = pygame.image.load('dusman.png')
        self.x = random.randint(0, 900)
        self.y = random.randint(0, 600)'''

class Enemy(pygame.sprite.Sprite):  # Lazer için bir sınıf oluşturuluyor.
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image =  pygame.image.load('dusman.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(0, 900)  # Karakterin  x başlangıç koordinatları atanıyor.
        self.rect.centery = random.randint(0, 600)  # karakterin y başlangıç koordinatları
        self.hizy =2
    def update(self):
        self.rect.centery += self.hizy
        if self.rect.bottom < 0:  # Enemy pencere dışına çıktı ise,
            self.kill()  # Enemy yok ediliyor.
class Runway(pygame.sprite.Sprite):  # Lazer için bir sınıf oluşturuluyor.
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image =  pygame.image.load('dusman.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(0, 900)  # Karakterin  x başlangıç koordinatları atanıyor.
        self.rect.centery = random.randint(0, 600)  # karakterin y başlangıç koordinatları
        self.hizy =2
'''class Runway():
    def __init__(self):
        self.img = pygame.image.load('runway.png')
        self.x = random.randint(0, 900)
        self.y = random.randint(0, 600)'''

game = Game()
while oyun:  # Ana oyun döngüsü oluşturuluyor.

    if oyunBitti:  # Oyun bitmiş ise,
        tumkarakterler = pygame.sprite.Group()  # Karakterler ekrana çizdirmek için "sprite.Group()" olarak tanımlanıyor.
        enemy= pygame.sprite.Group()
        player = Player()
        enemy=Enemy()
        runway=Runway()
        enemy1=Enemy()

        tumkarakterler.add(player)

        oyunBitti = False  # Değişken resetleniyor.

    saat.tick(FPS)  # Saniyede 60 kare çizdiriliyor.

    for event in pygame.event.get():  # Olaylar denetleniyor.

        if event.type == pygame.QUIT:  # Oyundan Çıkma isteği gelirse,
            oyun = False  # Oyun ekranından çıkılıyor.


    tumkarakterler.update()  # Bütün karakterler güncelleniyor.

    screen.blit(background,(0,0))  # Arkaplan siyaha boyanıyor.
    tumkarakterler.draw(screen)  # Bütün karakterler render edilip ekrana çizdiriliyor.
    pygame.display.flip()  # Ekran güncelleniyor.

pygame.quit()
        #step adımını çalıştırır
#dost piste yaklaşacak bunun için adımları belirle(geldiğinde oyun başa alacak)
#düşman dosta yaklaşacak iki durum oluşacak ya sıkışacak veya hedefe ulaşacak
#her iki durumda da oyun baştan başlayacak
game=Game()
asd
