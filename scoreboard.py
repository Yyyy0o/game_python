import pygame.font


class Scoreboard():

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        # 设置属性
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.pre_score()
        self.pre_high_score()

    def pre_score(self):
        score_str = "{:,}".format(round(self.stats.score, -1))
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
        # 展示score
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)

    def pre_high_score(self):
        score_str = "{:,}".format(round(self.stats.high_score, -1))
        self.high_score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
        # 展示score
        self.high_score_rect = self.score_image.get_rect()
        self.high_score_rect.right = self.screen_rect.centerx
        self.high_score_rect.top = 20

    def check_high_score(self):
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.pre_high_score()