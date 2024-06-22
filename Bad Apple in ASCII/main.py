"""
Bad Apple ASCII Art Renderer with PyGame

This lil script processes and renders an MP4 of Bad Apple frame-by-frame
as ASCII art using PyGame as the display output (I really like PyGame).

Requirements:
- Python 3
- PyGame (install with: pip install pygame)
- opencv-python (install with: pip install opencv-python)

Usage:
1. Replace 'bad_apple.mp4' in VIDEO_PATH with the path to your video file.
2. Run the script: python main.py
"""

import pygame
import cv2

# Video config stuff (feel free to mess around with it)
VIDEO_PATH = "bad_apple.mp4"
OUTPUT_WIDTH = 120
OUTPUT_HEIGHT = 80
FONT_SIZE = 10 
CHAR_SET = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

# PyGame init
pygame.init()
screen = pygame.display.set_mode((OUTPUT_WIDTH * FONT_SIZE, OUTPUT_HEIGHT * FONT_SIZE))
pygame.display.set_caption("Bad Apple")
font = pygame.font.Font(None, FONT_SIZE)

def render_ascii_frame(frame):
    """Converts a video frame to an ASCII art surface."""
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    resized_frame = cv2.resize(gray_frame, (OUTPUT_WIDTH, OUTPUT_HEIGHT))

    surface = pygame.Surface((OUTPUT_WIDTH * FONT_SIZE, OUTPUT_HEIGHT * FONT_SIZE))
    surface.fill((0, 0, 0)) # Black background

    for y, row in enumerate(resized_frame):
        for x, pixel_value in enumerate(row):
            char_index = int(pixel_value / 255 * (len(CHAR_SET) - 1))
            char = CHAR_SET[char_index]
            text_surface = font.render(char, True, (255, 255, 255))
            surface.blit(text_surface, (x * FONT_SIZE, y * FONT_SIZE))

    return surface

def main():
    """Main function to handle video processing and PyGame display."""
    video = cv2.VideoCapture(VIDEO_PATH)
    if not video.isOpened():
        print(f"Error: Could not open video file at '{VIDEO_PATH}'")
        exit(1)

    fps = video.get(cv2.CAP_PROP_FPS)
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        ret, frame = video.read()
        if not ret:
            break

        ascii_surface = render_ascii_frame(frame)
        screen.blit(ascii_surface, (0, 0)) 

        pygame.display.flip()
        clock.tick(fps)
    video.release()
    pygame.quit() 

if __name__ == "__main__":
    main() 