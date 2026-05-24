import pygame as pg
import sys
import math  # Explicitly importing math for pi
from object_3d import *
from camera import *
from projection import *


class SoftwareRender:
    def __init__(self):
        pg.init()
        self.RES = self.WIDTH, self.HEIGHT = 800, 700
        self.H_WIDTH, self.H_HEIGHT = self.WIDTH // 2, self.HEIGHT // 2
        self.FPS = 60
        self.screen = pg.display.set_mode(self.RES)
        self.clock = pg.time.Clock()
        self.create_objects()  # FIXED: Added () to actually invoke the method

    def create_objects(self):
        self.camera = Camera(self, [0.5, 1, -4])
        self.projection = Projection(self)
        self.object = Object3D(self)  
        self.object.translate([0.2, 0.4, 0.2])
        self.object.rotate_y(math.pi / 6)

    def draw(self):
        self.screen.fill(pg.Color('darkgray'))  # Using darkgray for better wireframe contrast
        self.object.draw()

    def run(self):
        while True:
            self.draw()
            
            # Clean exit handling instead of list comprehension side-effects
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                    
            pg.display.set_caption(f"FPS: {self.clock.get_fps():.2f}")
            pg.display.flip()
            self.clock.tick(self.FPS)


    if __name__ == '__main__':
    app = SoftwareRender()
    app.run()