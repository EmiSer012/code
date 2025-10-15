import pygame
import sys

# Initialiser pygame
pygame.init()

# Constantes
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GRAY = (200, 200, 200)

# Créer la grille
grid = [[WHITE for _ in range(GRID_HEIGHT)] for _ in range(GRID_WIDTH)]

# Définir la display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flood Fill Algorithm")

# Définir les outils
current_tool = "draw"
draw_color = BLACK
fill_color = RED

# Remplir avec la couleur
def flood_fill_queue(x, y, fill_color):
    
    if x < 0 or x >= GRID_WIDTH or y < 0 or y >= GRID_HEIGHT :
        return

    if grid[x][y] != WHITE:
        return
    
    grid[x][y] = fill_color

    flood_fill_queue(x, y-1, fill_color)
    flood_fill_queue(x, y+1, fill_color)
    flood_fill_queue(x-1, y, fill_color)
    flood_fill_queue(x+1, y, fill_color)

# Dessiner la grille
def draw_grid():
    screen.fill(WHITE)
    
    # Dessiner les cellules
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            color = grid[x][y]
            pygame.draw.rect(screen, color, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))
    
    # Dessiner les lignes de la grille
    for x in range(0, WIDTH, GRID_SIZE):
        pygame.draw.line(screen, GRAY, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, GRAY, (0, y), (WIDTH, y))
    
    # Draw UI info
    font = pygame.font.SysFont('Arial', 16)
    tool_text = font.render(f"Current Tool: {current_tool.capitalize()}", True, BLACK)
    instructions_text = font.render("D: Draw, F: Fill, SPACE: Clear Grid", True, BLACK)
    
    screen.blit(tool_text, (10, 10))
    screen.blit(instructions_text, (10, HEIGHT - 30))

# Boucle principale
def main():
    global current_tool, grid
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # Changements d'outils
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    current_tool = "draw"
                elif event.key == pygame.K_f:
                    current_tool = "fill"
                elif event.key == pygame.K_SPACE:
                    # Effacer les dessins
                    grid = [[WHITE for _ in range(GRID_HEIGHT)] for _ in range(GRID_WIDTH)]
            
            # Glissements et pressions de la souris
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                grid_x, grid_y = x // GRID_SIZE, y // GRID_SIZE
                
                # Vérifier que le clique est dans la grille
                if 0 <= grid_x < GRID_WIDTH and 0 <= grid_y < GRID_HEIGHT:
                    if current_tool == "draw":
                        grid[grid_x][grid_y] = draw_color
                    elif current_tool == "fill":
                        # Remplir avec la couleur
                        flood_fill_queue(grid_x, grid_y, fill_color)
            
            elif event.type == pygame.MOUSEMOTION:
                # Dessiner quand on glisse la souris en la pressant
                if pygame.mouse.get_pressed()[0] and current_tool == "draw":
                    x, y = event.pos
                    grid_x, grid_y = x // GRID_SIZE, y // GRID_SIZE
                    if 0 <= grid_x < GRID_WIDTH and 0 <= grid_y < GRID_HEIGHT:
                        grid[grid_x][grid_y] = draw_color
        
        # Dessiner le tout
        draw_grid()
        
        # Mettre à jour la display
        pygame.display.flip()
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()