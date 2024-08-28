import pygame
from mypage import MyPageScreen

class StartScreen:
    def __init__(self, screen, button_width=100, button_height=50, button_x_ratio=0.5, button_y_ratio=0.5):
        self.screen = screen
        self.background = pygame.image.load("background.png")

        # 버튼 설정 (비율에 따른 위치 조정)
        screen_width = screen.get_width()
        screen_height = screen.get_height()
        button_x = screen_width * button_x_ratio - button_width // 2
        button_y = screen_height * button_y_ratio - button_height // 2

        self.button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
        self.button_color = (255, 0, 0)  # 빨간색 버튼

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button_rect.collidepoint(event.pos):
                return MyPageScreen(self.screen)  # 화면 전환
        return None

    def display(self):
        self.screen.blit(self.background, (0, 0))
        pygame.draw.rect(self.screen, self.button_color, self.button_rect)
