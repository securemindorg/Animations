from manim import *

class LLMApplications(Scene):
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
        title = Text("LLM Applications & Future", font_size=30)
        subtitle = Text("Real-world Use Cases", font_size=20, color=BLUE)
        subtitle.next_to(title, DOWN)
        title_group = VGroup(title, subtitle)
        title_group.to_edge(UP)

        self.play(Write(title_group))

        # Create application bubbles
        def create_bubble(text, color=BLUE):
            bubble = Circle(radius=1, color=color)
            bubble.set_fill(color, opacity=0.2)
            text_obj = Text(text, font_size=15)
            text_obj.move_to(bubble.get_center())
            return VGroup(bubble, text_obj)

        # Create application examples
        applications = [
            ("Text\nGeneration", BLUE),
            ("Code\nCompletion", GREEN),
            ("Translation", RED),
            ("Analysis", YELLOW),
            ("Chat", PURPLE),
            ("Research", ORANGE)
        ]

        bubbles = VGroup()
        for i, (text, color) in enumerate(applications):
            bubble = create_bubble(text, color)
            angle = i * (2 * PI / len(applications))
            radius = 1.5
            x = radius * np.cos(angle)
            y = radius * np.sin(angle)
            bubble.move_to([x, y, 0])
            bubbles.add(bubble)

        # Center the bubbles
        bubbles.move_to(ORIGIN)

        # Animate bubbles appearing
        for bubble in bubbles:
            self.play(
                Create(bubble[0]),
                Write(bubble[1]),
                run_time=0.5
            )

        self.wait(1)

        # Create connecting lines
        lines = VGroup()
        for i in range(len(bubbles)):
            for j in range(i + 1, len(bubbles)):
                line = DashedLine(
                    bubbles[i].get_center(),
                    bubbles[j].get_center(),
                    dash_length=0.1,
                    color=GRAY
                )
                lines.add(line)

        self.play(Create(lines), run_time=2)

        # Add future implications
        implications = VGroup()
        future_points = [
            "Enhanced Capabilities",
            "Ethical Considerations",
            "Industry Impact",
            "Human Collaboration"
        ]

        for i, point in enumerate(future_points):
            text = Text(point, font_size=24)
            text.to_edge(RIGHT, buff=1)
            text.shift(UP * (1.5 - i))
            implications.add(text)

        # Create arrow pointing to future implications
        arrow = Arrow(
            bubbles.get_right(),
            implications.get_left(),
            color=YELLOW
        )

        # Animate future implications
        self.play(Create(arrow))
        for implication in implications:
            self.play(Write(implication))

        # Add pulsing effect to bubbles
        self.play(
            *[
                bubble[0].animate.scale(1.1)
                for bubble in bubbles
            ],
            run_time=1
        )
        self.play(
            *[
                bubble[0].animate.scale(1/1.1)
                for bubble in bubbles
            ],
            run_time=1
        )

        # Final pause
        self.wait(2)

# To render:
# manim -pqh llm_applications.py LLMApplications
