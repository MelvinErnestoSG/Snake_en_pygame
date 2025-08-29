import pygame
from clases.gamelogic import GameLogic
from clases.gamestate import GameState

# Configuración.
WIDTH = HEIGHT = 600
CELL_SIZE = WIDTH // 100 * 5

# Inicializar Pygame.
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_icon(pygame.image.load("imagen/snake.png"))
pygame.display.set_caption("Snake")

# Las instancias de la clase logica y estado.
logic = GameLogic(WIDTH, HEIGHT, CELL_SIZE)
state = GameState(screen, WIDTH, HEIGHT, CELL_SIZE)

# Limpiar la consola cuando se termina el juego.
print("\033c", end="")

# Bucle principal del juego.
running = True
while running:
    # Eventos.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        logic.handle_input(event)

    screen.fill("black")

    logic.update_game()
    
    state.draw_state(logic)

    if logic.game_over:
        pygame.display.update()
        # Espera 1000 ms antes de salir.
        pygame.time.wait(1000)  
        running = False

    # Actualizar pantalla.
    pygame.display.flip()

    # Controlar FPS.
    pygame.time.Clock().tick(10)

pygame.quit()