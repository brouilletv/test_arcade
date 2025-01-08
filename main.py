import arcade

color_list = [[255, 0, 0], [0, 255, 0], [0, 0, 255], [255, 128, 0], [255, 255, 255]]
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400
rayon_cercle = 20


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        # Call the parent class's init function
        super().__init__(width, height, title)
        self.cercle_x = SCREEN_WIDTH / 2
        self.cercle_y = SCREEN_HEIGHT / 2
        self.cercle_change_x = 3
        self.cercle_change_y = 3

    def on_update(self, delta_time: float):
        self.cercle_x += self.cercle_change_x
        self.cercle_y += self.cercle_change_y
        if self.cercle_x < rayon_cercle:
            self.cercle_change_x *= -1
        if self.cercle_x > SCREEN_WIDTH - rayon_cercle:
            self.cercle_change_x *= -1
        if self.cercle_y < rayon_cercle:
            self.cercle_change_y *= -1
        if self.cercle_y > SCREEN_HEIGHT - rayon_cercle:
            self.cercle_change_y *= -1

    def on_draw(self):
        self.clear()

        arcade.draw_circle_filled(self.cercle_x, self.cercle_y, rayon_cercle, (255, 0, 0))


def main():
    MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing Example")

    arcade.run()


main()
