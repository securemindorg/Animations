from manim import *
import numpy as np

class PerceptronLearning(Scene):
    def construct(self):
                # Add a background effect (gradient rectangle)
        background = Rectangle(
            width=config.frame_width,  # Use MANIM's config.frame_width
            height=config.frame_height,  # Use MANIM's config.frame_height
            fill_color=BLUE_C,
            fill_opacity=0.1,
        ).set_z_index(-1)  # Ensure it is behind all elements
        self.add(background)  # Add background to the scene

        # Title
        title = Text("How Perceptrons Learn", font_size=40)
        subtitle = Text("Training on Job Application Data", font_size=30, color=BLUE)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.3)
        title_group.to_edge(UP, buff=0.5)

        # Create coordinate system for data visualization
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 10, 1],
            axis_config={"include_tip": True},
            x_length=6,
            y_length=6
        )
        axes_labels = VGroup(
            Text("Years of Experience", font_size=18).next_to(axes.x_axis, DOWN),
            Text("Interview Score", font_size=18).next_to(axes.y_axis, RIGHT, buff=-0.5).rotate(90 * DEGREES)
        )
        graph_group = VGroup(axes, axes_labels).shift(LEFT * 3)

        # Create sample data points
        np.random.seed(42)
        accepted_coords = [(np.random.uniform(5, 9), np.random.uniform(6, 9)) for _ in range(8)]
        rejected_coords = [(np.random.uniform(1, 4), np.random.uniform(1, 5)) for _ in range(8)]

        # Create dots for accepted and rejected applications
        accepted_dots = VGroup(*[
            Dot(axes.c2p(x, y), color=GREEN) for x, y in accepted_coords
        ])
        rejected_dots = VGroup(*[
            Dot(axes.c2p(x, y), color=RED) for x, y in rejected_coords
        ])

        # Create legend
        legend = VGroup(
            Dot(color=GREEN), Text("Accepted", font_size=20, color=GREEN),
            Dot(color=RED), Text("Rejected", font_size=20, color=RED)
        ).arrange(RIGHT, buff=0.2)
        legend.to_corner(UR, buff=0.5)

        # Decision boundary line (initial)
        def get_line_points(m, b):
            x1, x2 = 0, 10
            y1, y2 = m * x1 + b, m * x2 + b
            return axes.c2p(x1, y1), axes.c2p(x2, y2)

        initial_line = Line(
            *get_line_points(0.5, 2),
            color=YELLOW,
            stroke_width=2
        )

        # Right side panel for weights
        weight_panel = VGroup(
            Text("Weights:", font_size=16),
            MathTex("w_1 = 0.5", color=YELLOW),
            MathTex("w_2 = 0.3", color=YELLOW),
            MathTex("b = 2.0", color=GREEN)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        weight_panel.shift(RIGHT * 3)

        # Animation sequence
        self.play(Write(title_group))
        self.wait(2)
        self.play(FadeOut(title_group))

        # Show coordinate system
        self.play(
            Create(axes),
            Write(axes_labels)
        )
        self.wait(0.5)

        # Show legend and initial data points
        self.play(
            Create(legend),
            *[GrowFromCenter(dot) for dot in accepted_dots],
            *[GrowFromCenter(dot) for dot in rejected_dots]
        )
        self.wait(1)

        # Show initial decision boundary
        self.play(
            Create(initial_line),
            Write(weight_panel)
        )
        self.wait(1)

        # Learning animation
        for _ in range(3):
            # Adjust weights (animate line movement)
            new_line = Line(
                *get_line_points(np.random.uniform(0.7, 1.2), np.random.uniform(3, 4)),
                color=YELLOW,
                stroke_width=2
            )

            # Update weight display
            new_weights = VGroup(
                Text("Weights:", font_size=24),
                MathTex(f"w_1 = {np.random.uniform(0.7, 1.2):.1f}", color=YELLOW),
                MathTex(f"w_2 = {np.random.uniform(0.5, 0.8):.1f}", color=YELLOW),
                MathTex(f"b = {np.random.uniform(3, 4):.1f}", color=GREEN)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
            new_weights.shift(RIGHT * 3)

            self.play(
                Transform(initial_line, new_line),
                Transform(weight_panel, new_weights),
                run_time=1.5
            )
            self.wait(0.5)

        # Add explanation text
        explanation = VGroup(
            Text("As the perceptron learns:", font_size=20, color=BLUE),
            Text("• Adjusts weights based on errors", font_size=18),
            Text("• Updates decision boundary", font_size=18),
            Text("• Minimizes misclassifications", font_size=18)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        explanation.next_to(weight_panel, DOWN, buff=0.2)

        self.play(Write(explanation))
        self.wait(2)

        # Final highlight of correct classifications
        final_highlight = VGroup()
        for dot in accepted_dots:
            if dot.get_center()[1] > initial_line.get_end()[1]:
                final_highlight.add(dot.copy().set_color(YELLOW))
        for dot in rejected_dots:
            if dot.get_center()[1] < initial_line.get_end()[1]:
                final_highlight.add(dot.copy().set_color(YELLOW))

        self.play(
            FadeIn(final_highlight),
            rate_func=there_and_back,
            run_time=2
        )
        self.wait(1)

# To render:
# manim -pqh perceptron_learning.py PerceptronLearning
