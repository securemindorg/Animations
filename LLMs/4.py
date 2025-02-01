from manim import *
import numpy as np

class LearningProgress(Scene):
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
        title = Text("LLM Training Progress", font_size=40)
        subtitle = Text("Learning Curves & Metrics", font_size=30, color=BLUE)
        subtitle.next_to(title, DOWN)
        title_group = VGroup(title, subtitle)
        title_group.to_edge(UP)

        # Create coordinate system
        axes = Axes(
            x_range=[0, 10, 2],
            y_range=[0, 1, 0.2],
            tips=True,
            axis_config={
                "color": BLUE,
                "include_numbers": True,
                "font_size": 24
            },
            x_length=8,
            y_length=5
        )
        # Move axes to center
        axes.move_to(ORIGIN)

        # Labels
        x_label = Text("Training Steps (millions)", font_size=24)
        x_label.next_to(axes.x_axis, DOWN)
        y_label = Text("Performance", font_size=24)
        y_label.rotate(90 * DEGREES)
        y_label.next_to(axes.y_axis, LEFT)

        # Create multiple learning curves
        def training_curve(x):
            return 1 - 0.5 * np.exp(-0.3 * x)

        def validation_curve(x):
            return 0.9 - 0.4 * np.exp(-0.3 * x)

        training_line = axes.plot(training_curve, color=GREEN)
        validation_line = axes.plot(validation_curve, color=RED)

        # Create legend and position it below the graph
        legend = VGroup(
            Dot(color=GREEN), Text("Training", font_size=20),
            Dot(color=RED), Text("Validation", font_size=20)
        ).arrange(RIGHT, buff=0.2)
        legend.next_to(axes, DOWN, buff=1)  # Move legend below axes

        # Create dots for tracking progress
        training_dot = Dot(color=GREEN)
        validation_dot = Dot(color=RED)

        # Create value trackers
        training_value = DecimalNumber(
            0,
            num_decimal_places=3,
            color=GREEN,
            font_size=24
        )
        validation_value = DecimalNumber(
            0,
            num_decimal_places=3,
            color=RED,
            font_size=24
        )

        # Create value tracker group and position it
        tracker_group = VGroup(
            Text("Training: ", font_size=24),
            training_value,
            Text("  Validation: ", font_size=24),
            validation_value
        ).arrange(RIGHT)
        tracker_group.next_to(title_group, DOWN, buff=2)

        # Animation sequence
        self.play(Write(title_group))
        self.play(
            Create(axes),
            Write(x_label),
            Write(y_label)
        )
        self.wait(0.5)

        self.play(FadeOut(title_group))

        self.play(Create(legend))
        self.play(Create(training_line), Create(validation_line))

        self.wait(1)

        # Initialize dots at start of curves
        training_dot.move_to(axes.c2p(0, training_curve(0)))
        validation_dot.move_to(axes.c2p(0, validation_curve(0)))

        self.play(Create(training_dot), Create(validation_dot))
        self.play(Write(tracker_group))

        # Animate dots along curves
        def update_training_value(m):
            return m.set_value(training_curve(training_dot.get_center()[0]/axes.x_axis.unit_size))

        def update_validation_value(m):
            return m.set_value(validation_curve(validation_dot.get_center()[0]/axes.x_axis.unit_size))

        training_value.add_updater(update_training_value)
        validation_value.add_updater(update_validation_value)

        self.play(
            MoveAlongPath(training_dot, training_line),
            MoveAlongPath(validation_dot, validation_line),
            run_time=5
        )

        # Add milestone markers
        milestones = [
            {"x": 2, "label": "Initial\nConvergence"},
            {"x": 5, "label": "Mid\nTraining"},
            {"x": 8, "label": "Final\nPhase"}
        ]

        for milestone in milestones:
            x = milestone["x"]
            point = axes.c2p(x, training_curve(x))
            marker = Dot(point, color=YELLOW)
            label = Text(milestone["label"], font_size=16)
            label.next_to(marker, UP, buff=0.2)
            self.play(
                Create(marker),
                Write(label)
            )

        self.wait(2)
