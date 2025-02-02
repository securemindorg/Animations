from manim import *

class Introduction(Scene):
    def construct(self):
        # Add a background effect (gradient rectangle)
        background = Rectangle(
            width=config.frame_width,  # Use MANIM's config.frame_width
            height=config.frame_height,  # Use MANIM's config.frame_height
            fill_color=BLUE_C,
            fill_opacity=0.1,
        ).set_z_index(-1)  # Ensure it is behind all elements
        self.add(background)  # Add background to the scene


        # Opening hook
        hook_text = Text(
            "Ever wonder why AI seems to\nmake biased decisions?",
            font_size=30
        )

        # Create simple AI decision visualization
        decision_circle = Circle(radius=1, color=BLUE)
        x_mark = VGroup(
            Line(UP + LEFT, DOWN + RIGHT, color=RED),
            Line(UP + RIGHT, DOWN + LEFT, color=RED)
        ).scale(0.5)
        check_mark = VGroup(
            Line(LEFT, ORIGIN, color=GREEN),
            Line(ORIGIN, UP + RIGHT, color=GREEN)
        ).scale(0.5)

        decisions = VGroup(
            decision_circle.copy().shift(LEFT * 3),
            decision_circle.copy(),
            decision_circle.copy().shift(RIGHT * 3)
        )

        marks = VGroup(
            x_mark.copy().move_to(decisions[0]),
            check_mark.copy().move_to(decisions[1]),
            x_mark.copy().move_to(decisions[2])
        )

        # Answer text
        answer_text = Text(
            "The answer lies in its simplest\nbuilding block - the perceptron.",
            font_size=26,
            color=YELLOW
        )

        # Create simplified perceptron
        perceptron = VGroup()
        input_nodes = VGroup(*[Circle(radius=0.2, color=BLUE) for _ in range(3)])
        input_nodes.arrange(DOWN, buff=0.5)
        output_node = Circle(radius=0.2, color=RED)
        output_node.next_to(input_nodes, RIGHT, buff=2)

        connections = VGroup(*[
            Line(
                node.get_right(),
                output_node.get_left(),
                color=YELLOW
            ) for node in input_nodes
        ])

        perceptron.add(input_nodes, connections, output_node)

        # Topics to be covered
        topics = VGroup(
            Text("• What is a Perceptron?", font_size=16),
            Text("• How Bias Enters the System", font_size=16),
            Text("• Real-World Impact", font_size=16),
            Text("• Solutions & Mitigation", font_size=16)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)

        # Why it matters text
        importance = Text(
            "Understanding this is crucial for\nbuilding fair AI systems",
            font_size=32,
            color=GREEN
        )

        # Animation sequence
        # 1. Show hook
        self.play(Write(hook_text))
        self.wait(0.5)
        self.wait(2)

        # 2. Show AI decisions
        self.play(
            hook_text.animate.scale(0.7).to_edge(UP),
            run_time=1
        )

        self.play(
            *[Create(circle) for circle in decisions],
            run_time=1
        )

        self.play(
            *[Create(mark) for mark in marks],
            run_time=1
        )
        self.wait(2)

        # 3. Show answer
        self.play(
            Write(answer_text.next_to(decisions, DOWN, buff=0.75))
        )
        self.wait(2)

        # 4. Transform to perceptron
        self.play(
            *[FadeOut(mob) for mob in [answer_text, decisions, marks]],
            run_time=1
        )

        perceptron.move_to(ORIGIN)
        self.play(Create(perceptron))

        # Add ripple effect through perceptron
        for connection in connections:
            self.play(
                Flash(
                    connection.get_center(),
                    color=YELLOW,
                    line_length=0.2,
                    flash_radius=0.5
                ),
                run_time=0.3
            )

        # 5. Show topics
        topics.next_to(perceptron, DOWN, buff=0.75)
        for topic in topics:
            self.play(
                Write(topic),
                run_time=0.3
            )

        # 6. Show importance
        importance.next_to(topics, DOWN, buff=0.75)
        self.play(
            Write(importance),
            run_time=1
        )

        # Final emphasis
        final_group = VGroup(perceptron, topics, importance)
        surrounding_rect = SurroundingRectangle(
            final_group,
            buff=0.3,
            color=BLUE
        )



        self.wait(4)

        # Fade out
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=0.5
        )

# To render:
# manim -pqh introduction.py Introduction
