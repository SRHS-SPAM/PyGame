import pygame

class MyPageScreen:
    def __init__(self, screen):
        self.screen = screen
        self.background_color = (0, 128, 255)  # 파란색 배경

    def handle_event(self, event):
        # 이 화면에서는 별도 이벤트 처리를 하지 않음
        return None

    def display(self):
        self.screen.fill(self.background_color)
