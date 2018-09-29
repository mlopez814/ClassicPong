class Settings:

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (0, 200, 200)
        self.black = (0, 0, 0)

        self.paddle_speed = 10
        self.ball_speed = 10.75
        self.ball_speedV = 0
        self.ball_speedH = 0
        self.ball_directionH = 1
        self.ball_directionV = -1

        self.score_limit = 15
