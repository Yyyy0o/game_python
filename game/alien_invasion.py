import imp
from re import A
import sys
import pygame

from setting import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    
    def __init__(self):
        pygame.init()
        
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_hight))
        # 设置全屏
        # self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        # self.settings.screen_hight = self.screen.get_rect().height
        # self.settings.screen_width = self.screen.get_rect().width
        pygame.display.set_caption(self.settings.name)
        
        self.bullets = pygame.sprite.Group()
        self.ship = Ship(self)
        

    
    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_screen()
            
            
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_key_down(event)
            elif event.type == pygame.KEYUP:
                self._check_key_up(event)
                    
    def _check_key_down(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.move_right = True
        if event.key == pygame.K_LEFT:
            self.ship.move_left = True
        if event.key == pygame.K_q:
            sys.exit()
        if event.key == pygame.K_SPACE:
            self._fire_bullet()
            
    def _check_key_up(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.move_right = False
        if event.key == pygame.K_LEFT:
            self.ship.move_left = False
        
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()    
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()      
        
    def _fire_bullet(self): 
        print('11111111111111111111111')
        print(self.bullets)
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)
            
            
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

        
        