import pygame

class Ship():
    def __init__(self,screen):
        """init ship + set start position"""
        self.screen = screen

        # load image and get its rect
        self.image = pygame.image.load("C:/Users/aris123/Desktop/python_practice/python projects/alien invasion game project/image files/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #start each new ship at the bottom center of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """draws ship at current location"""
        self.screen.blit(self.image,self.rect)