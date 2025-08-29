import pygame
import random

class Food:
    def __init__(self, width, height, cell_size, colors="red"):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.colors = colors
        self.position = self.generate_position()

    def generate_position(self):
        return (
                random.randrange(0, self.width, self.cell_size),
                random.randrange(0, self.height, self.cell_size)
               )

    def respawn(self, snake_body):
        while True:
            position = self.generate_position()
            # Evitar que la comida aparezca dentro de la serpiente.
            if position not in snake_body:
                self.position = position
                break

    def change_color(self):
        all_colors = [
            "aliceblue", "antiquewhite", "aqua", "aquamarine", "azure",
            "beige", "bisque", "blanchedalmond", "blue", "blueviolet",
            "brown", "burlywood", "cadetblue", "chartreuse", "chocolate",
            "coral", "cornflowerblue", "cornsilk", "crimson", "cyan",
            "darkblue", "darkcyan", "darkgoldenrod", "darkgray", "darkgreen",
            "darkgrey", "darkkhaki", "darkmagenta", "darkolivegreen",
            "darkorange", "darkorchid", "darkred", "darksalmon", "darkseagreen",
            "darkslateblue", "darkslategray", "darkslategrey", "darkturquoise",
            "darkviolet", "deeppink", "deepskyblue", "dimgray", "dimgrey",
            "dodgerblue", "firebrick", "floralwhite", "forestgreen",
            "fuchsia", "gainsboro", "ghostwhite", "gold", "goldenrod",
            "gray", "green", "greenyellow", "honeydew", "hotpink", 
            "indianred", "indigo", "ivory", "khaki", "lavender", "lavenderblush",
            "lawngreen", "lemonchiffon", "lightblue", "lightcoral", "lightcyan",
            "lightgoldenrod", "lightgoldenrodyellow", "lightgray", "lightgreen",
            "lightgrey", "lightpink", "lightsalmon", "lightseagreen", "lightskyblue",
            "lightsteelblue", "lightyellow", "lightslategray", "lightslategrey",
            "lime", "limegreen", "linen", "magenta", "maroon", "mediumaquamarine", 
            "mediumblue", "mediumorchid", "mediumpurple", "mediumseagreen", 
            "mediumslateblue", "mediumspringgreen", "mediumturquoise", "mediumvioletred",
            "midnightblue", "mintcream", "mistyrose", "moccasin", "navy", "navajowhite",
            "oldlace", "olive", "olivedrab", "orange", "orangered","orchid", 
            "palegoldenrod", "palegreen", "paleturquoise", "palevioletred", 
            "papayawhip", "peachpuff", "peru", "pink", "plum", "powderblue", "purple", 
            "red", "rosybrown", "royalblue", "saddlebrown", "salmon", "sandybrown", 
            "seagreen", "seashell", "sienna", "silver", "skyblue", "slateblue",
            "slategray", "slategrey", "snow", "springgreen", "steelblue",
            "tan", "tan1", "teal", "thistle", "tomato", "turquoise",
            "violet", "wheat", "white", "whitesmoke", "yellow", "yellowgreen"
        ]
        # Lista de comprensión.
        self.colors = random.choice([i for i in all_colors if i != self.colors])

    def draw_food(self, screen):
        pygame.draw.rect(screen, self.colors, (*self.position, self.cell_size, self.cell_size))