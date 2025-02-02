from manim import *
import numpy as np

class BiasAmplification(Scene):
    def construct(self):
        # Add a background effect (gradient rectangle)
        background = Rectangle(
            width=config.frame_width,  # Use MANIM's config.frame_width
            height=config.frame_height,  # Use MANIM's config.frame_height
            fill_color=BLUE_C,
            fill_opacity=0.1,
        ).set_z_index(-1)  # Ensure it is behind all elements
        self.add(background)  # Add background to the scene

        # Title - moved higher
        title = Text("Bias Amplification", font_size=30)
        subtitle = Text("The Snowball Effect", font_size=20, color=BLUE)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.3)
        title_group.to_edge(UP, buff=0.4)  # Increased top buffer

        # Initial bias visualization - adjusted position
        initial_circle = Circle(radius=0.3, color=RED_A)
        initial_circle.set_fill(RED_A, opacity=0.5)
        initial_label = Text("Initial Bias", font_size=20)
        initial_label.next_to(initial_circle, DOWN)
        initial_group = VGroup(initial_circle, initial_label)
        initial_group.shift(LEFT * 6 + UP * 1.5)  # Moved further left and up

        # Feedback loop - adjusted size and position
        feedback_radius = 1.5  # Reduced radius
        center_point = ORIGIN + LEFT + UP * 0.5  # Moved up and adjusted right position
        arrows = VGroup()
        labels = VGroup()

        for i in range(4):
            angle = i * PI/2
            next_angle = (i + 1) * PI/2
            start = center_point + feedback_radius * np.array([np.cos(angle), np.sin(angle), 0])
            end = center_point + feedback_radius * np.array([np.cos(next_angle), np.sin(next_angle), 0])
            arrow = Arrow(start, end, color=YELLOW)
            arrows.add(arrow)

        # Adjusted feedback loop labels
        feedback_labels = [
            "Biased\nPredictions",
            "Reinforced\nDecisions",
            "Skewed\nData",
            "Stronger\nBias"
        ]

        for i, label_text in enumerate(feedback_labels):
            angle = i * PI/2
            pos = center_point + (feedback_radius + 0.7) * np.array([np.cos(angle + PI/4), np.sin(angle + PI/4), 0])
            label = Text(label_text, font_size=16)  # Reduced font size
            label.move_to(pos)
            labels.add(label)

        # Snowball effect - adjusted positions
        snowballs = VGroup()
        snowball_labels = VGroup()
        sizes = [0.3, 0.5, 0.7, 0.9]  # Slightly reduced sizes
        positions = [LEFT * 6, LEFT * 3, RIGHT * 0, RIGHT * 3]  # Adjusted spacing
        opacities = [0.3, 0.5, 0.7, 0.9]

        for i, (size, pos, opacity) in enumerate(zip(sizes, positions, opacities)):
            ball = Circle(radius=size, color=RED)
            ball.set_fill(RED, opacity=opacity)
            ball.move_to(pos + DOWN * 2.5)  # Moved lower
            label = Text(f"Stage {i+1}", font_size=16)
            label.next_to(ball, DOWN, buff=0.2)  # Reduced buffer
            snowballs.add(ball)
            snowball_labels.add(label)

        # Explanation text - adjusted position
        explanation = VGroup(
            Text("As the model learns:", font_size=24, color=YELLOW),
            Text("• Small biases grow larger", font_size=20),
            Text("• Feedback loops reinforce bias", font_size=20),
            Text("• Effects cascade through system", font_size=20)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        explanation.to_edge(RIGHT, buff=0.5)
        explanation.shift(UP * 2)  # Moved up to avoid overlap with snowballs

        # Animation sequence remains the same
        self.play(Write(title_group))
        self.wait(0.5)

        self.play(
            Create(initial_circle),
            Write(initial_label)
        )
        self.wait(0.5)

        for arrow, label in zip(arrows, labels):
            self.play(
                GrowArrow(arrow),
                Write(label),
                run_time=0.75
            )
        self.wait(1)

        for i in range(len(snowballs)):
            if i == 0:
                self.play(
                    Transform(initial_circle.copy(), snowballs[i]),
                    Write(snowball_labels[i])
                )
            else:
                self.play(
                    Transform(snowballs[i-1].copy(), snowballs[i]),
                    Write(snowball_labels[i])
                )
            self.wait(0.3)

        self.play(Write(explanation))
        self.wait(2)

        highlight_group = VGroup(snowballs, arrows)
        self.play(
            highlight_group.animate.set_color(YELLOW),
            rate_func=there_and_back,
            run_time=2
        )
        self.wait(1)

        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )
