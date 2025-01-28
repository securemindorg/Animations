from manim import *
import numpy as np

class LatentSpaceVisualization(Scene):
    def construct(self):
        # Add a background effect (gradient rectangle)
        background = Rectangle(
            width=config.frame_width,  # Use MANIM's config.frame_width
            height=config.frame_height,  # Use MANIM's config.frame_height
            fill_color=BLUE_C,
            fill_opacity=0.1,
        ).set_z_index(-1)  # Ensure it is behind all elements

        self.add(background)  # Add background to the scene

        sentences_text = Text("Latent Space Visualization Over Epochs", font_size=28).to_edge(UP)
        self.play(Write(sentences_text))
        self.wait(1)

        # Create axes for scatter plot
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            axis_config={"color": WHITE},
            x_length=6,
            y_length=6
        ).scale(0.8)

        # Add labels
        x_label = Text("Dimension 1", color=WHITE).scale(0.4)
        y_label = Text("Dimension 2", color=WHITE).scale(0.4)
        x_label.next_to(axes, DOWN)
        y_label.next_to(axes, LEFT).rotate(90 * DEGREES)

        # Group axes and labels
        plot_group = VGroup(axes, x_label, y_label)
        plot_group.shift(RIGHT * 2)

        # Create epoch counter
        epoch_counter = Text("Epoch: 0", color=WHITE).scale(0.6)
        epoch_counter.to_edge(LEFT).shift(UP * 2)

        self.play(
            Create(axes),
            Write(x_label),
            Write(y_label),
            Write(epoch_counter)
        )

        # Simulate latent vectors evolving over epochs
        n_points = 25  # Number of text samples
        n_epochs = 20

        # Initial random positions
        positions = np.random.randn(n_points, 2) * 3

        # Create dots for each text sample
        dots = VGroup(*[
            Dot(point=axes.c2p(*pos), color=YELLOW, radius=0.08)
            for pos in positions
        ])

        # Add labels for specific points
        labels = ["Utica", "University"]
        label_dots = dots[:2]
        text_labels = VGroup(*[
            Text(label, color=WHITE).scale(0.3).next_to(dot, UP, buff=0.1)
            for label, dot in zip(labels, label_dots)
        ])

        self.play(Create(dots), Write(text_labels))

        # Animate the evolution of points
        for epoch in range(1, n_epochs + 1):
            # Simulate convergence by moving points closer to clusters
            new_positions = positions * 0.8  # Points gradually move closer to origin
            new_positions += np.random.randn(n_points, 2) * 0.3  # Add some randomness

            new_dots = VGroup(*[
                Dot(point=axes.c2p(*pos), color=YELLOW, radius=0.08)
                for pos in new_positions
            ])

            new_text_labels = VGroup(*[
                Text(label, color=WHITE).scale(0.3).next_to(dot, UP, buff=0.1)
                for label, dot in zip(labels, new_dots[:3])
            ])

            self.play(
                Transform(dots, new_dots),
                Transform(text_labels, new_text_labels),
                Transform(
                    epoch_counter,
                    Text(f"Epoch: {epoch}", color=WHITE).scale(0.6).to_edge(LEFT).shift(UP * 2)
                ),
                run_time=1.5
            )

            positions = new_positions
            self.wait(0.5)

        # Add final explanation
        explanation = Text(
            "Points cluster together as the model learns to encode similar texts nearby in latent space",
            color=WHITE
        ).scale(0.4)
        explanation.to_edge(DOWN)
        self.play(Write(explanation))

        self.wait(10)
