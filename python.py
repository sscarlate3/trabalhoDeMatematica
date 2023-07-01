import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from termcolor import colored 


def draw_hexagonal_prism():
    
    vertices = [
        [1, 0, -1],  
        [0.5, 0.87, -1],  
        [-0.5, 0.87, -1],  
        [-1, 0, -1],  
        [-0.5, -0.87, -1],  
        [0.5, -0.87, -1],  
        [1, 0, 1],  
        [0.5, 0.87, 1],  
        [-0.5, 0.87, 1],  
        [-1, 0, 1],  
        [-0.5, -0.87, 1],  
        [0.5, -0.87, 1]  
    ]

    base_edges = [
        (0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0),# Base DOWNhexagonal
        
        (6, 7), (7, 8), (8, 9), (9, 10), (10, 11), (11, 6) # Base Tophexagonal
    ]

    side_edges = [
        (0, 6), (1, 7), (2, 8), (3, 9), (4, 10), (5, 11)  # Lateral hexagonal

    ]

    glBegin(GL_LINES)
    
    
    glColor3f(1.0, 1.0, 0.0)  # Amarelo
    for edge in base_edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])

   
    glColor3f(1.0, 0.0, 0.0)  # Vermelho
    for edge in side_edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    pygame.init()
    
    display_info = pygame.display.Info()
    
    display = (display_info.current_w, display_info.current_h)

    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(40, (display[0] / display[1]), 0.1, 50.0)

    glTranslatef(0.0, 0.0, -5)

    rotatingXU = False
    rotatingXD = False
    rotatingZL = False
    rotatingZR = False
    rotatingY = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    rotatingZL = True
                if event.key == pygame.K_UP:
                    rotatingXU = True
                if event.key == pygame.K_DOWN:
                    rotatingXD = True
                if event.key == pygame.K_RIGHT:
                    rotatingZR = True
                if event.key == pygame.K_SPACE:
                    rotatingY = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    rotatingZL = False
                if event.key == pygame.K_UP:
                    rotatingXU = False
                if event.key == pygame.K_DOWN:
                    rotatingXD = False
                if event.key == pygame.K_RIGHT:
                    rotatingZR = False
                if event.key == pygame.K_SPACE:
                    rotatingY = False
        #up    
        if rotatingXU:
            glRotatef(1, 1, 0, 0) 
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            draw_hexagonal_prism()
            pygame.display.flip()
            pygame.time.wait(10)
        #down
        if rotatingXD:
            glRotatef(1, -1, 0, 0) 
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            draw_hexagonal_prism()
            pygame.display.flip()
            pygame.time.wait(10)
        #left
        if rotatingZL:
            glRotatef(1, 0, 0, -1) 
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            draw_hexagonal_prism()
            pygame.display.flip()
            pygame.time.wait(10)
        #right
        if rotatingZR:
            glRotatef(1, 0, 0, 1) 
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            draw_hexagonal_prism()
            pygame.display.flip()
            pygame.time.wait(10)
        #space
        if rotatingY:
            glRotatef(1, 0, 1, 0) 
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            draw_hexagonal_prism()
            pygame.display.flip()
            pygame.time.wait(10)


if __name__ == '__main__':
    main()