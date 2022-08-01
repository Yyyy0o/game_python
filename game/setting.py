class Settings:

    def __init__(self):
        self.name = 'Alien Invasion'
        # screen设置
        self.screen_width = 1200
        self.screen_hight = 800
        self.bg_color = (230, 230, 230)
        # ship设置
        self.ship_speed = 1.5
        # bullet设置
        self.bullet_speed = 1.0
        self.bullet_with = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        # alien设置
        self.alien_speed = 1.0
        self.alien_drop_speed = 10
        self.alien_direction = 1
