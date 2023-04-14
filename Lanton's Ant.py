import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class LangtonsAnt:
    def __init__(self, board_size=(100, 100), ant_position=(50, 50), ant_direction="up", move_rules="rl", initial_state="white", iterations=1000, show_animation=True):
        self.board_size = board_size
        self.ant_position = list(ant_position)
        self.ant_direction = ant_direction
        self.move_rules = move_rules
        self.iterations = iterations
        self.show_animation = show_animation

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

    def run(self, output_file="langtons_ant.gif", show_grid=False):
        if self.show_animation:
            fig, ax = plt.subplots()
            plt.axis("off")
            ims = []

            for _ in range(self.iterations):
                im = ax.imshow(self.board, cmap="gray", animated=True)
                ims.append([im])
                self.step()

            ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True, repeat_delay=1000)

            ani.save(output_file, writer="imagemagick", fps=15)
            plt.show()

        else:
            for _ in range(self.iterations):
                self.step()
            plt.figure(figsize=(10, 10))
            plt.imshow(self.board, cmap="gray")
            if show_grid:
                plt.grid()
            plt.grid()
            plt.show()


if __name__ == "__main__":
    board_size = (100, 100)
    ant_position = (50, 50)
    ant_direction = "up"
    move_rules = "rl"
    initial_state = "white"
    interations = 12000
    show_animation = False
    show_grid = False
    output_file = "langtons_ant.gif"

    ant_simulator = LangtonsAnt(board_size=board_size, ant_position=ant_position, ant_direction=ant_direction, move_rules=move_rules, initial_state=initial_state, iterations=interations, show_animation=show_animation)
    ant_simulator.run(output_file=output_file, show_grid=show_grid)
