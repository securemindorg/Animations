from manim import *

class MyScene(Scene):
    def construct(self):
        # Add a background effect (gradient rectangle)
        background = Rectangle(
            width=config.frame_width,  # Use MANIM's config.frame_width
            height=config.frame_height,  # Use MANIM's config.frame_height
            fill_color=BLUE_C,
            fill_opacity=0.1,
        ).set_z_index(-1)  # Ensure it is behind all elements

        self.add(background)  # Add background to the scener

        matrix_elements = [
            [Text(str(num)) for num in row]
            for row in [
                [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0],
                [10, 11, 12, 13, 14, 9, 15, 5, 16, 0, 0, 0],
                [10, 17, 18, 19, 20, 21, 22, 23, 9, 8, 24, 25]
            ]
        ]

        m3 = MobjectMatrix(matrix_elements)
        m3.scale(0.5)
        self.play(FadeIn(m3), shift=DOWN)
        self.wait(5)

