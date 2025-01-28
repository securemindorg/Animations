from manim import *

class OutroScene(Scene):
    def construct(self):
        # Add a background effect (gradient rectangle)
        background = Rectangle(
            width=config.frame_width,  # Use MANIM's config.frame_width
            height=config.frame_height,  # Use MANIM's config.frame_height
            fill_color=BLUE_C,
            fill_opacity=0.1,
        ).set_z_index(-1)  # Ensure it is behind all elements
        self.add(background)  # Add background to the scene

        # Create thank you message
        thank_you = Text("Thank You for Watching!", color=WHITE).scale(1.2)
        thank_you.to_edge(UP, buff=1.5)

        # Create social media links/handles
        social_text = VGroup(
            Text("Follow for more AI & ML content", color=WHITE).scale(0.7),
        ).arrange(DOWN, buff=0.4)
        social_text.next_to(thank_you, DOWN, buff=0.8)

        # Create subscribe animation
        subscribe_box = RoundedRectangle(
            height=0.8,
            width=3,
            corner_radius=0.2,
            color=RED,
            fill_opacity=0.3
        )
        subscribe_text = Text("Subscribe", color=WHITE).scale(0.6)
        subscribe_group = VGroup(subscribe_box, subscribe_text)
        subscribe_group.to_edge(DOWN, buff=1)

        # Animate elements
        self.play(Write(thank_you))
        self.wait(0.5)

        # Animate social media links one by one
        for text in social_text:
            self.play(Write(text))
            self.wait(0.3)

        # Animate subscribe button with pulse effect
        self.play(Create(subscribe_box), Write(subscribe_text))
        self.play(
            subscribe_box.animate.scale(1.1),
            subscribe_text.animate.scale(1.1),
            rate_func=there_and_back,
            run_time=1
        )

        self.wait(2)

        # Optional: Add a fade out effect
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=1
        )
