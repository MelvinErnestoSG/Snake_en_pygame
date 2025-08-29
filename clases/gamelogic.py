import pygame
from clases.snake import Snake
from clases.food import Food

# Cargar sonido.
pygame.mixer.init()
move_sound = pygame.mixer.Sound("sound/collision.mp3") 

class GameLogic:
    def __init__(self, width, height, cell_size):
        self.width = width
        self.height = height
        self.cell_size = cell_size

        # Crear objetos.
        self.snake = Snake(width, height, cell_size)
        self.food = Food(width, height, cell_size)

        # Variables del juego.
        self.score = 0
        self.game_over = False

    # Controles del juego ⬆️ ⬇️ ⬅️ ➡️
    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.snake.change_direction(0)
            elif event.key == pygame.K_DOWN:
                self.snake.change_direction(1)
            elif event.key == pygame.K_LEFT:
                self.snake.change_direction(2)
            elif event.key == pygame.K_RIGHT:
                self.snake.change_direction(3)

    def update_game(self):
        # Lógica del juego si no ha terminado.
        if not self.game_over:
            # Mover la serpiente.
            self.snake.move_snack()

            # Verificar si comió.
            if self.snake.body[0] == self.food.position:
                self.score += 1
                self.snake.grow = True
                self.food.change_color()
                self.food.respawn(self.snake.body)
                move_sound.play()

            # Verificar colisiones.
            if self.snake.check_collision():
                move_sound.play()
                self.game_over = True 