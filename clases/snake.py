import pygame

class Snake:
    def __init__(self, width, height, cell_size):
        self.width = width
        self.height = height
        self.cell_size = cell_size

        self.directions = [
            (0, -cell_size), # UP.
            (0, cell_size),  # DOWN.
            (-cell_size, 0), # LEFT.
            (cell_size, 0)   # RIGHT.
        ]
        
        self.body = [(width // 2, height // 2)]
        self.direction = 3  # Empieza a la derecha.
        self.grow = False

    def move_snack(self):
        head = (
                self.body[0][0] + self.directions[self.direction][0],
                self.body[0][1] + self.directions[self.direction][1]
               )
        self.body.insert(0, head)

        if not self.grow:
            self.body.pop()
        else:
            self.grow = False

    def change_direction(self, new_direction):
        # Evitar giro de 180°.
        if (self.direction == 0 and new_direction != 1) or \
           (self.direction == 1 and new_direction != 0) or \
           (self.direction == 2 and new_direction != 3) or \
           (self.direction == 3 and new_direction != 2):
            self.direction = new_direction

    def check_collision(self):
        head = self.body[0]
        return (
                head[0] < 0 or head[0] >= self.width or
                head[1] < 0 or head[1] >= self.height or
                head in self.body[1:]
               )

    def draw_snack(self, screen):
        for i, segment in enumerate(self.body):
            if i == 0:  
                # Cabeza.
                pygame.draw.rect(screen, "forestgreen", (*segment, self.cell_size, self.cell_size))
            else:  
                # Cuerpo.
                pygame.draw.rect(screen, "lawngreen", (*segment, self.cell_size, self.cell_size))