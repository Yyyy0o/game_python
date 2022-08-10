class Settings:

    def __init__(self):
        self.name = 'Alien Invasion'
        # screen设置
        self.screen_width = 1200
        self.screen_height = 1000
        self.bg_color = (230, 230, 230)
        # ship设置
        self.ship_limit = 1
        # bullet设置
        self.bullet_with = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        # alien设置
        self.alien_drop_speed = 10
        self.speedup_scale = 1.1
        # 动态设置
        self.init_dynamic_settings()

    def init_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        self.alien_direction = 1
        self.alien_points = 10

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.speedup_scale)