import sys
from time import sleep

import pygame

from alien import Alien
from bullet import Bullet
from button import Button
from game_stats import GameStats
from setting import Settings
from ship import Ship


class AlienInvasion:

    def __init__(self):
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # 设置全屏
        # self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        # self.settings.screen_hight = self.screen.get_rect().height
        # self.settings.screen_width = self.screen.get_rect().width
        pygame.display.set_caption(self.settings.name)

        self.stats = GameStats(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.ship = Ship(self)
        self.button = Button(self, 'play')

        self._crete_fleet()

    def run_game(self):
        while True:
            self._check_events()

            if self.stats.game_stats:
                self.ship.update()
                self._update_aliens()
                self._update_bullets()
                self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_key_down(event)
            elif event.type == pygame.KEYUP:
                self._check_key_up(event)

    def _check_key_down(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.move_right = True
        if event.key == pygame.K_LEFT:
            self.ship.move_left = True
        if event.key == pygame.K_q:
            sys.exit()
        if event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_key_up(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.move_right = False
        if event.key == pygame.K_LEFT:
            self.ship.move_left = False

        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)

        if not self.stats.game_stats:
            self.button.draw_button()

    def _update_screen(self):
        pygame.display.flip()

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        # 更新子弹位置
        self.bullets.update()
        # 删除消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)
        # 射杀alien
        groupcollide = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        # 创建fleet
        if not self.aliens:
            self.bullets.empty()
            self._crete_fleet()

    def _crete_fleet(self):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        # alien列数
        available_space_x = self.settings.screen_width - 2 * alien_width
        number_columns = available_space_x // (2 * alien_width)
        # alien行数
        available_space_y = self.settings.screen_height - 4 * alien_height - self.ship.rect.height
        number_rows = available_space_y // (2 * alien_height)

        for row in range(number_rows):
            for column in range(number_columns):
                self._create_alien(column, row)

    def _create_alien(self, column, row):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * column
        alien.rect.y = alien_height + 2 * alien_height * row
        alien.rect.x = alien.x
        self.aliens.add(alien)

    def _update_aliens(self):
        self._check_fleet_edge()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        self._check_alien_bottom()

    def _ship_hit(self):
        if self.stats.ship_left > 0:
            self.stats.ship_left -= 1
            self.aliens.empty()
            self.bullets.empty()
            self._crete_fleet()
            self.ship.center_ship()
            sleep(0.5)
        else:
            self.stats.game_stats = False

    def _check_fleet_edge(self):
        for alien in self.aliens.sprites():
            if alien.check_edge():
                self._change_fleet_direction()
                break

    def _check_alien_bottom(self):
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    def _change_fleet_direction(self):
        self.settings.alien_direction *= -1
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.alien_drop_speed


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
