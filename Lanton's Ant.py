import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class LangtonsAnt:
    def __init__(self,
                 board_size=(100, 100),
                 ant_position=(50, 50),
                 ant_direction="up",
                 move_rules="rl",
                 initial_state="white",
                 iterations=1000,
                 show_animation=True,
                 show_grid=False,
                 show_info=True,
                 show_initial_ant=True):

        self.board_size = board_size
        self.ant_position = list(ant_position)
        self.ant_direction = ant_direction
        self.move_rules = move_rules
        self.iterations = iterations
        self.show_animation = show_animation
        self.show_grid = show_grid
        self.show_info = show_info
        self.show_initial_ant = show_initial_ant

        if initial_state == "white":
            self.board = np.zeros(board_size)
        elif initial_state == "black":
            self.board = np.ones(board_size)
        elif initial_state == "checkerboard":
            self.board = np.indices(board_size).sum(axis=0) % 2
        else:
            raise ValueError(f"Invalid initial state: {initial_state}")

        self.directions = {
            "up": (-1, 0),
            "right": (0, 1),
            "down": (1, 0),
            "left": (0, -1)
        }

    def move(self):
        row, col = self.directions[self.ant_direction]
        self.ant_position[0] += row
        self.ant_position[1] += col
        self.ant_position = [self.ant_position[0] % self.board_size[0], self.ant_position[1] % self.board_size[1]]

    def turn(self, direction):
        if direction == "l":
            if self.ant_direction == "up":
                self.ant_direction = "left"
            elif self.ant_direction == "right":
                self.ant_direction = "up"
            elif self.ant_direction == "down":
                self.ant_direction = "right"
            else:
                self.ant_direction = "down"
        else:
            if self.ant_direction == "up":
                self.ant_direction = "right"
            elif self.ant_direction == "right":
                self.ant_direction = "down"
            elif self.ant_direction == "down":
                self.ant_direction = "left"
            else:
                self.ant_direction = "up"

    def step(self):
        current_color = self.board[self.ant_position[0], self.ant_position[1]]
        if current_color == 0:
            self.turn(self.move_rules[0])
        else:
            self.turn(self.move_rules[1])
        self.board[self.ant_position[0], self.ant_position[1]] = 1 - current_color
        self.move()

    def run(self, output_file="langtons_ant.gif"):
        if self.show_animation:
            fig, ax = plt.subplots()
            plt.axis("off")
            ims = []

            for _ in range(self.iterations):
                im = ax.imshow(self.board, cmap="gray_r", animated=True)
                ims.append([im])
                self.step()

            ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True, repeat_delay=1000)

            ani.save(output_file, writer="imagemagick", fps=15)
            plt.show()

        else:
            initial_board = self.board.copy()
            initial_ant_position = self.ant_position.copy()
            initial_ant_direction = self.ant_direction

            for _ in range(self.iterations):
                self.step()
            plt.figure(figsize=(10, 10))

            direction_marker = {'up': '^', 'right': '>', 'down': 'v', 'left': '<'}

            if self.show_info:
                title = f"Langton's Ant\nBoard size: {self.board_size}\nSteps: {self.iterations}\nInitial direction: {initial_ant_direction}\nMove rules: {self.move_rules}"
                plt.title(title, fontsize=10, pad=15)
            plt.imshow(self.board, cmap="gray_r")

            if self.show_initial_ant:
                plt.scatter(initial_ant_position[0], initial_ant_position[1], s=100,
                            marker=direction_marker[initial_ant_direction], color='red')

            if self.show_grid:
                plt.grid(True, which='both', color='black', linewidth=1)
                plt.xticks(np.arange(-0.5, self.board_size[1], 1), [])
                plt.yticks(np.arange(-0.5, self.board_size[0], 1), [])
            else:
                plt.grid(False)
            plt.show()


if __name__ == "__main__":
    board_size = (100, 100)
    ant_position = (50, 50)
    ant_direction = "up"
    move_rules = "rl"
    initial_state = "white"
    interations = 11000
    show_animation = False
    show_grid = False
    show_info = True
    show_initial_ant = True
    output_file = "langtons_ant.gif"

    ant_simulator = LangtonsAnt(board_size=board_size, ant_position=ant_position, ant_direction=ant_direction, move_rules=move_rules, initial_state=initial_state, iterations=interations, show_animation=show_animation, show_grid=show_grid, show_info=show_info, show_initial_ant=show_initial_ant)
    ant_simulator.run(output_file=output_file)
