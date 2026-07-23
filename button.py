import pygame

class Button:
    def __init__(self, img_path, position, scale = 0.5):
        self.image = pygame.image.load(img_path).convert_alpha()
        new_width = int(self.image.get_width() * scale)
        new_height = int(self.image.get_height() * scale)
        self.image = pygame.transform.smoothscale(self.image, (new_width, new_height))
        self.pressed = False
        self.rect = self.image.get_rect(topleft = position)
    
    def draw(self, wn):
        wn.blit(self.image, self.rect)


    def is_pressed(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()[0]

        if self.rect.collidepoint(mouse_pos):
            if mouse_pressed and not self.pressed:
                self.pressed = True
                return True
        if not mouse_pressed:
            self.pressed = False
            return False
        return False
                


