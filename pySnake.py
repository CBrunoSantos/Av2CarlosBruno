import pygame
import random
from functools import reduce

# Definição de cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Configurações do jogo
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 20
FPS = 10
STARTING_TIME = 60  # Tempo inicial em segundos
NUM_OBSTACLES = 30  # Número de obstáculos no mapa

# Direções
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Monad Maybe
class Maybe:
    def __init__(self, value):
        self.value = value

    def bind(self, func):
        if isinstance(self, Nothing):
            return self
        try:
            result = func(self.value)
            return Just(result) if result is not None else Nothing()
        except:
            return Nothing()

    def __str__(self):
        return f'Just({self.value})' if isinstance(self, Just) else 'Nothing'

class Just(Maybe):
    def __init__(self, value):
        super().__init__(value)

class Nothing(Maybe):
    def __init__(self):
        super().__init__(None)

# Estados do jogo
class GameState:
    def __init__(self, snake, food, obstacles, running, start_time):
        self.snake = snake
        self.food = food
        self.obstacles = obstacles
        self.running = running
        self.start_time = start_time

# Função para criar uma nova cobra
def create_snake():
    return {
        'positions': [(WIDTH // 2, HEIGHT // 2)],
        'direction': RIGHT,
        'length': 1,
        'score': 0
    }

# Função para mover a cobra usando uma função lambda de alta ordem
move_snake_lambda = lambda snake: {
    'positions': [(snake['positions'][0][0] + snake['direction'][0] * CELL_SIZE,
                   snake['positions'][0][1] + snake['direction'][1] * CELL_SIZE)] + snake['positions'][:-1],
    'direction': snake['direction'],
    'length': snake['length'],
    'score': snake['score']
}

# Função para mudar a direção da cobra
def change_direction(snake, direction):
    if (direction[0] * -1, direction[1] * -1) != snake['direction']:
        snake['direction'] = direction
    return snake

# Função para fazer a cobra crescer
def grow_snake(snake):
    snake['length'] += 1
    snake['score'] += 1
    snake['positions'].append(snake['positions'][-1])
    return snake

# Função para verificar colisões da cobra usando filter
check_collision = lambda snake, obstacles: reduce(
    lambda acc, pos: acc or pos == snake['positions'][0],
    filter(lambda pos: pos == snake['positions'][0], snake['positions'][1:]),
    (snake['positions'][0][0] < 0 or snake['positions'][0][0] >= WIDTH or
     snake['positions'][0][1] < 0 or snake['positions'][0][1] >= HEIGHT) or
    any(snake['positions'][0] == obstacle for obstacle in obstacles)
)

# Função para criar uma nova comida usando map
generate_food = lambda snake, obstacles: Maybe(next(
    (pos for pos in map(
        lambda _: (random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE,
                   random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE),
        iter(int, 1)
    ) if pos not in snake['positions'] and pos not in obstacles), None
))

# Função para desenhar a tela
def draw_screen(screen, snake, food, obstacles, time_remaining):
    screen.fill(BLACK)
    for pos in snake['positions']:
        pygame.draw.rect(screen, GREEN, (*pos, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, RED, (*food, CELL_SIZE, CELL_SIZE))
    for pos in obstacles:
        pygame.draw.rect(screen, BLUE, (*pos, CELL_SIZE, CELL_SIZE))

    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {snake['score']}", True, WHITE)
    screen.blit(score_text, (10, 10))

    time_text = font.render(f"Time: {time_remaining} s", True, WHITE)
    screen.blit(time_text, (10, 40))

    pygame.display.flip()

# Função para gerar obstáculos aleatórios
def generate_obstacles(snake, num_obstacles):
    positions = set(snake['positions'])
    obstacles = []
    while len(obstacles) < num_obstacles:
        pos = (random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE,
               random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE)
        if pos not in positions:
            obstacles.append(pos)
            positions.add(pos)
    return obstacles

# Função principal do jogo
def run_game():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Game")
    clock = pygame.time.Clock()

    # Tela de menu
    show_menu(screen)

    # Inicialização do jogo
    game_state = initialize_game()

    while game_state.running:
        # Verifica eventos do Pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_state.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    game_state.snake = change_direction(game_state.snake, UP)
                elif event.key == pygame.K_DOWN:
                    game_state.snake = change_direction(game_state.snake, DOWN)
                elif event.key == pygame.K_LEFT:
                    game_state.snake = change_direction(game_state.snake, LEFT)
                elif event.key == pygame.K_RIGHT:
                    game_state.snake = change_direction(game_state.snake, RIGHT)

        # Move a cobra
        game_state.snake = move_snake_lambda(game_state.snake)

        # Verifica colisões
        if check_collision(game_state.snake, game_state.obstacles) or time_remaining(game_state.start_time) <= 0:
            game_state.running = False

        # Verifica se comeu a comida
        if game_state.snake['positions'][0] == game_state.food:
            game_state.snake = grow_snake(game_state.snake)
            game_state.food = generate_food(game_state.snake, game_state.obstacles).value

        # Atualiza a tela
        draw_screen(screen, game_state.snake, game_state.food, game_state.obstacles, time_remaining(game_state.start_time))

        # Controla a taxa de quadros por segundo
        clock.tick(FPS)

    pygame.quit()

# Função para mostrar a tela de menu
def show_menu(screen):
    screen.fill(BLACK)
    font = pygame.font.Font(None, 50)
    title_text = font.render("Snake Game", True, WHITE)
    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 2 - 50))
    pygame.display.flip()
    pygame.time.delay(2000)  # Delay de 2 segundos para mostrar o menu

# Função para inicializar o estado do jogo
def initialize_game():
    snake = create_snake()
    obstacles = generate_obstacles(snake, NUM_OBSTACLES)
    food = generate_food(snake, obstacles).value
    start_time = pygame.time.get_ticks()
    return GameState(snake, food, obstacles, True, start_time)

# Função para calcular o tempo decorrido em segundos
time_remaining = lambda start_time: max(0, STARTING_TIME - ((pygame.time.get_ticks() - start_time) // 1000))

# Executa o jogo
if __name__ == "__main__":
    run_game()
