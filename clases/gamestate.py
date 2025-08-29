import pygame
from clases.snake import Snake
from clases.food import Food

class GameState:
    def __init__(self, screen, width, height, cell_size):
        self.screen = screen
        self.width = width
        self.height = height
        self.cell_size = cell_size

        # Crear objetos.
        self.snake = Snake(width, height, cell_size)
        self.food = Food(width, height, cell_size)

    def draw_text(self, surface, text, size, x, y): 
        font_obj = pygame.font.SysFont("comicsansms", size)
        text_surface = font_obj.render(text, True, "white") 
        text_rect = text_surface.get_rect(center=(x, y)) 
        surface.blit(text_surface, text_rect)

    def draw_state(self, logic):
        if not logic.game_over:
            # Dibujar la serpiente y la comida.
            logic.snake.draw_snack(self.screen)
            logic.food.draw_food(self.screen)

            self.draw_text(
                self.screen,
                f"Puntuación Inicial: {logic.score}",
                (self.width // 100) * 6,
                self.width // 2, 20
            )
        else:
            self.draw_text(
                self.screen,
                "GRACIAS POR JUGAR",
                (self.width // 100) * 6,
                self.width // 2,
                self.height // 2 - 30
            )
            self.draw_text(
                self.screen,
                f"Puntuación final: {logic.score}",
                (self.width // 100) * 6,
                self.width // 2,
                self.height // 2 + 20
            )