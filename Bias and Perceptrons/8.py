from manim import *

class Conclusion(Scene):
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
        title = Text("Understanding AI Bias", font_size=30)
        subtitle = Text("From Root Causes to Responsible Development", font_size=20, color=BLUE)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.3)
        title_group.to_edge(UP, buff=0.5)

        # Create simplified perceptron for recap
        perceptron = VGroup()

        # Input nodes
        input_nodes = VGroup(*[Circle(radius=0.2, color=BLUE) for _ in range(3)])
        input_nodes.arrange(DOWN, buff=0.5)

        # Output node
        output_node = Circle(radius=0.2, color=RED)
        output_node.next_to(input_nodes, RIGHT, buff=2)

        # Connections with varying thickness to show bias
        connections = VGroup()
        for i, node in enumerate(input_nodes):
            # Make middle connection thicker to represent bias
            thickness = 3 if i == 1 else 1
            connection = Line(
                node.get_right(),
                output_node.get_left(),
                color=YELLOW,
                stroke_width=thickness
            )
            connections.add(connection)

        perceptron.add(input_nodes, output_node, connections)
        perceptron.scale(0.8).next_to(title_group, DOWN, buff=0.75)

        # Key points
        points = VGroup(
            Text("1. Small biases get amplified", font_size=20),
            Text("2. Systematic problems require systematic solutions", font_size=20),
            Text("3. Responsible AI development is crucial", font_size=20)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        points.next_to(perceptron, DOWN, buff=0.2)

        # Final call to action
        call_to_action = Text(
            "Understanding the root cause\nhelps us build better, fairer AI",
            font_size=32,
            color=YELLOW
        ).next_to(points, DOWN, buff=0.75)

        # Animation sequence
        self.play(Write(title_group))
        self.wait(2)

        # Animate perceptron
        self.play(
            Create(input_nodes),
            Create(output_node)
        )
        self.wait(2)

        # Animate connections with ripple effect
        for connection in connections:
            self.play(
                Create(connection),
                run_time=0.5
            )
            # Add ripple effect along connection
            ripple = connection.copy().set_color(WHITE)
            self.play(
                ripple.animate.set_stroke(width=5),
                rate_func=there_and_back,
                run_time=0.3
            )

        # Highlight bias amplification
        self.play(
            connections[1].animate.set_stroke(width=6, color=RED),
            rate_func=there_and_back,
            run_time=1
        )

        self.wait(2)

        # Animate key points with emphasis
        for point in points:
            self.play(
                Write(point),
                run_time=0.5
            )
            self.play(
                point.animate.scale(1.1).set_color(BLUE),
                rate_func=there_and_back,
                run_time=0.3
            )

        self.wait(2)

        # Animate call to action with dramatic effect
        self.play(
            Write(call_to_action),
            run_time=1
        )

        self.wait(2)

        # Final emphasis animation
        self.play(
            call_to_action.animate.scale(1.1),
            rate_func=there_and_back,
            run_time=1
        )

        self.wait(2)

        # Create highlighting box around the whole scene
        final_highlight = SurroundingRectangle(
            VGroup(perceptron, points, call_to_action),
            buff=0.3,
            color=BLUE
        )

        self.play(
            Create(final_highlight),
            run_time=0.5
        )

        self.wait(2)

        # Pulse animation for emphasis
        self.play(
            final_highlight.animate.scale(1.1).set_color(YELLOW),
            rate_func=there_and_back,
            run_time=1
        )
        self.wait(2)

        # Optional: Add a fade-out transition
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=0.5
        )

# To render:
# manim -pqh conclusion.py Conclusion
