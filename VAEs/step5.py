from manim import *

class LatentSpaceScaling(Scene):
    def construct(self):
        # Add a background effect (gradient rectangle)
        background = Rectangle(
            width=config.frame_width,  # Use MANIM's config.frame_width
            height=config.frame_height,  # Use MANIM's config.frame_height
            fill_color=BLUE_C,
            fill_opacity=0.1,
        ).set_z_index(-1)  # Ensure it is behind all elements
        self.add(background)  # Add background to the scene

        sentences_text = Text("Latent Space Scaling Vs. Data Growth", font_size=28).to_edge(UP)
        self.play(Write(sentences_text))
        self.wait(1)

        # Create initial axes for data vs. space comparison
        axes = Axes(
            x_range=[0, 10, 2],
            y_range=[0, 10, 2],
            axis_config={"color": WHITE},
            x_length=5,  # Reduced from 6
            y_length=5   # Reduced from 6
        ).scale(0.7)    # Reduced scale from 0.8

        # Add labels
        x_label = Text("Amount of Input Data", color=WHITE).scale(0.4)
        y_label = Text("Space Required", color=WHITE).scale(0.4)
        x_label.next_to(axes, DOWN)
        y_label.next_to(axes, LEFT).rotate(90 * DEGREES)

        # Position the graph more to the right
        graph_group = VGroup(axes, x_label, y_label)
        graph_group.shift(RIGHT * 3)  # Moved further right

        self.play(Create(graph_group))
        self.wait(4)

        # Create lines showing different scaling
        linear_line = axes.plot(lambda x: x, color=RED)
        latent_line = axes.plot(lambda x: np.log(x + 1) * 2, color=GREEN)

        # Add labels for lines
        linear_label = Text("Raw Data Storage", color=RED).scale(0.3)
        latent_label = Text("Latent Space", color=GREEN).scale(0.3)

        linear_label.next_to(linear_line, RIGHT)
        latent_label.next_to(latent_line, RIGHT)

        # Animate the lines appearing
        self.play(
            Create(linear_line),
            Write(linear_label)
        )
        self.wait(5)
        self.play(
            Create(latent_line),
            Write(latent_label)
        )
        self.wait(5)

        # Create visualization of data points being added
        data_container = Rectangle(height=4, width=2, color=WHITE)
        data_container.to_edge(LEFT).shift(RIGHT)  # Shifted slightly right
        data_label = Text("Input Data", color=WHITE).scale(0.5)
        data_label.next_to(data_container, UP)

        self.play(
            Create(data_container),
            Write(data_label)
        )

        # Animate adding data points and showing compression
        for i in range(5):
            new_point = Dot(color=YELLOW)
            new_point.move_to(data_container.get_center() + UP * (1-i*0.5))

            latent_circle = Circle(radius=0.3, color=BLUE_E, fill_opacity=0.2)
            latent_circle.next_to(data_container, RIGHT, buff=2)

            arrow = Arrow(new_point.get_center(), latent_circle.get_center(), color=WHITE)

            self.play(
                Create(new_point),
                Create(arrow),
                Create(latent_circle)
            )

            if i == 0:
                explain_text = Text(
                    "New data points are efficiently encoded in existing latent space.\nThe latent space grows logarithmically while maintaing information",
                    color=WHITE
                ).scale(0.4)
                explain_text.to_edge(DOWN).shift(UP * 0.4)  # Moved up slightly
                self.play(Write(explain_text))



        self.wait(10)
