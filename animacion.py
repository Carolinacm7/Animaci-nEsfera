import pygame
import time

# Inicializar Pygame
pygame.init()

# Dimensiones de la ventana
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Animación Esfera - Movimiento con teclas')

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Cargar la imagen del obstáculo (árbol) con la ruta correcta
tree_image = pygame.image.load('resources/img/obstacle_image.png')  # Asegúrate de que esta ruta sea correcta

# Escalar la imagen del árbol para que se ajuste al espacio sin recortarse
tree_width, tree_height = tree_image.get_size()
scale_factor = HEIGHT // 2 / tree_height  # Escalar la altura del árbol para que ocupe la mitad de la pantalla
new_tree_width = int(tree_width * scale_factor)
new_tree_height = int(tree_height * scale_factor)
tree_image = pygame.transform.scale(tree_image, (new_tree_width, new_tree_height))  # Escalado

tree_rect = tree_image.get_rect(center=(WIDTH // 2, HEIGHT - new_tree_height // 2))  # Ajustar la posición

# Puntos A y B
point_a = pygame.Rect(50, HEIGHT - 100, 50, 50)  # Cuadro naranja en el punto A
point_b = pygame.Rect(WIDTH - 100, HEIGHT - 100, 50, 50)  # Cuadro naranja en el punto B

# Esfera
sphere_radius = 20
sphere_x, sphere_y = point_a.center  # Inicializa la esfera en el centro de 'point_a'
sphere_velocity = 5

# Cronómetro
start_time = None
elapsed_time = 0

# Fuente para el texto
font = pygame.font.SysFont('Arial', 24)

# Función para iniciar el cronómetro
def start_timer():
    global start_time, elapsed_time
    start_time = time.time()  # Guardar la hora de inicio
    elapsed_time = 0  # Reiniciar el tiempo transcurrido

# Función para reiniciar el juego
def reset_game():
    global sphere_x, sphere_y, start_time, elapsed_time, game_over, in_transition
    sphere_x, sphere_y = point_a.center  # Reubicar la esfera en el punto A
    start_timer()  # Iniciar el cronómetro nuevamente
    game_over = False  # Restablecer el estado del juego
    in_transition = False  # Restablecer la transición hacia point_b
    elapsed_time = 0  # Asegurar que el tiempo se reinicie correctamente

# Bucle principal
running_game = True
game_over = False  # Variable para saber si el juego terminó
in_transition = False  # Variable para controlar la transición hacia el centro de point_b

# Iniciar el cronómetro al principio
start_timer()

while running_game:
    screen.fill(WHITE)

    # Capturar los eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_game = False
        elif event.type == pygame.MOUSEBUTTONDOWN and game_over:
            # Verificar si el botón "Reiniciar" fue presionado
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if restart_button.collidepoint(mouse_x, mouse_y):
                reset_game()

    # Detectar las teclas presionadas
    keys = pygame.key.get_pressed()

    # Movimiento de la esfera con las teclas de dirección
    if keys[pygame.K_UP]:  # Mover hacia arriba
        if not tree_rect.colliderect(pygame.Rect(sphere_x, sphere_y - sphere_velocity, sphere_radius*2, sphere_radius*2)):
            sphere_y -= sphere_velocity
    if keys[pygame.K_DOWN]:  # Mover hacia abajo
        if not tree_rect.colliderect(pygame.Rect(sphere_x, sphere_y + sphere_velocity, sphere_radius*2, sphere_radius*2)):
            sphere_y += sphere_velocity
    if keys[pygame.K_LEFT]:  # Mover hacia la izquierda
        if not tree_rect.colliderect(pygame.Rect(sphere_x - sphere_velocity, sphere_y, sphere_radius*2, sphere_radius*2)):
            sphere_x -= sphere_velocity
    if keys[pygame.K_RIGHT]:  # Mover hacia la derecha
        if not tree_rect.colliderect(pygame.Rect(sphere_x + sphere_velocity, sphere_y, sphere_radius*2, sphere_radius*2)):
            sphere_x += sphere_velocity

    # Asegurar que la esfera no salga de la pantalla
    if sphere_x < 0:
        sphere_x = 0
    elif sphere_x > WIDTH - sphere_radius * 2:
        sphere_x = WIDTH - sphere_radius * 2
    if sphere_y < 0:
        sphere_y = 0
    elif sphere_y > HEIGHT - sphere_radius * 2:
        sphere_y = HEIGHT - sphere_radius * 2

    # Verificar si la esfera toca el área de point_b
    if point_b.collidepoint(sphere_x + sphere_radius, sphere_y + sphere_radius) and not in_transition:
        in_transition = True  # Iniciar transición
        # Calculamos la diferencia entre la posición actual de la esfera y el centro de point_b
        target_x, target_y = point_b.center
        delta_x = target_x - sphere_x
        delta_y = target_y - sphere_y
        distance = (delta_x**2 + delta_y**2)**0.5
        steps = int(distance / sphere_velocity)  # Cuántos pasos necesitaremos para llegar al centro

        # Control para mover la esfera hacia el centro de point_b
        step_count = 0
        while step_count < steps:
            # Movimiento de la esfera hacia el centro de point_b
            sphere_x += delta_x / steps
            sphere_y += delta_y / steps
            step_count += 1

            # Dibujar la pantalla
            screen.fill(WHITE)

            # Dibujar el árbol (obstáculo)
            screen.blit(tree_image, tree_rect)

            # Dibujar el punto A y el punto B
            pygame.draw.rect(screen, ORANGE, point_a)
            pygame.draw.rect(screen, ORANGE, point_b)

            # Dibujar la esfera
            pygame.draw.circle(screen, BLACK, (int(sphere_x), int(sphere_y)), sphere_radius)

            # Mostrar el cronómetro
            elapsed_time = time.time() - start_time  # Actualizar el tiempo transcurrido
            timer_text = font.render(f'Tiempo transcurrido: {elapsed_time:.2f} s', True, BLACK)
            screen.blit(timer_text, (WIDTH // 2 - timer_text.get_width() // 2, 10))

            # Mostrar el autor
            author_text = font.render('Autor: Carolina Chitiva', True, BLACK)
            screen.blit(author_text, (10, 10))

            pygame.display.flip()
            pygame.time.Clock().tick(60)

        # La esfera ha llegado al centro de point_b, mostramos el mensaje
        game_over = True
        print(f"Objetivo alcanzado en {elapsed_time:.2f} segundos.")
        pygame.time.delay(1000)  # Esperar 1 segundo

    # Dibujar el árbol (obstáculo)
    screen.blit(tree_image, tree_rect)

    # Dibujar el punto A y el punto B
    pygame.draw.rect(screen, ORANGE, point_a)
    pygame.draw.rect(screen, ORANGE, point_b)

    # Dibujar la esfera
    pygame.draw.circle(screen, BLACK, (int(sphere_x), int(sphere_y)), sphere_radius)

    # Mostrar el cronómetro solo si el juego no ha terminado
    if not game_over:
        elapsed_time = time.time() - start_time  # Actualizar el tiempo transcurrido
        timer_text = font.render(f'Tiempo transcurrido: {elapsed_time:.2f} s', True, BLACK)
        screen.blit(timer_text, (WIDTH // 2 - timer_text.get_width() // 2, 10))

    # Mostrar el autor
    author_text = font.render('Autor: Carolina Chitiva', True, BLACK)
    screen.blit(author_text, (10, 10))

    # Si el juego ha terminado, mostrar el mensaje y el botón
    if game_over:
        finish_message = font.render(f'¡Has terminado el recorrido en {elapsed_time:.2f} segundos!', True, BLACK)
        screen.blit(finish_message, (WIDTH // 2 - finish_message.get_width() // 2, HEIGHT // 2))

        # Dibujar el botón de reiniciar
        restart_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 50, 200, 50)
        pygame.draw.rect(screen, GREEN, restart_button)
        restart_text = font.render('Reiniciar', True, WHITE)
        screen.blit(restart_text, (restart_button.centerx - restart_text.get_width() // 2, restart_button.centery - restart_text.get_height() // 2))

    pygame.display.flip()
    pygame.time.Clock().tick(60)

# Salir del juego
pygame.quit()
