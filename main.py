import pygame
import sys
from start import StartScreen
from mypage import MyPageScreen

# Pygame 초기화
pygame.init()

# 윈도우 크기 설정
screen_width = 1600
screen_height = 900
screen = pygame.display.set_mode((screen_width, screen_height))

# 윈도우 제목 설정
pygame.display.set_caption("Legend of Pie")

# 초기 화면 설정
current_screen = StartScreen(screen)

# 메인 루프
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # 현재 화면에서 이벤트 처리
        next_screen = current_screen.handle_event(event)
        if next_screen:
            current_screen = next_screen

    # 현재 화면 그리기
    current_screen.display()
    
    # 화면 업데이트
    pygame.display.flip()
