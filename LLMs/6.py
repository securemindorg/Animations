from manim import *

class ClosingScene(Scene):
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
        title = Text("Thank You for Learning About LLMs!", font_size=40)
        subtitle = Text("Key Takeaways", font_size=30, color=BLUE)

        title_group = VGroup(title, subtitle)
        title_group.arrange(DOWN)
        title_group.to_edge(UP)

        # Create key takeaways
        takeaways = [
            "Understanding LLM Architecture",
            "Training Process & Data",
            "Real-world Applications",
            "Future Possibilities"
        ]

        # Create checkmarks and takeaway texts
        takeaway_groups = VGroup()
        for i, point in enumerate(takeaways):
            # Create checkmark
            checkmark = Text("✓", font_size=30, color=GREEN)
            # Create text
            text = Text(point, font_size=24)
            # Group them
            group = VGroup(checkmark, text)
            group.arrange(RIGHT, buff=0.5)
            takeaway_groups.add(group)

        # Arrange takeaways vertically
        takeaway_groups.arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        takeaway_groups.next_to(title_group, DOWN, buff=1)


        # Animation sequence
        self.play(Write(title_group))
        self.wait(2)

        # Animate takeaways appearing with checkmarks
        for group in takeaway_groups:
            self.play(
                Write(group[0]),  # Checkmark
                Write(group[1]),  # Text
                run_time=0.5
            )

        self.wait(5)

        # Create and animate final call to action
        cta = Text("Subscribe and Checkout Data Science @ Utica University!", font_size=28, color=YELLOW)
        cta.next_to(takeaway_groups, DOWN, buff=1)

        # Add pulsing animation to CTA
        self.play(Write(cta))
        self.play(
            cta.animate.scale(1.1),
            rate_func=there_and_back,
            run_time=1
        )


        # Final flourish - create particles emanating from title
        particles = VGroup(*[
            Dot(radius=0.05, color=BLUE)
            for _ in range(20)
        ])

        for dot in particles:
            dot.move_to(title.get_center())
            dot.shift(np.random.random(3) * 0.1)

        def particle_animation(mob):
            mob.shift(
                np.random.random(3) * 2 - 1
            )
            mob.scale(0.9)

        # Animate particles
        self.play(
            *[
                UpdateFromFunc(dot, particle_animation)
                for dot in particles
            ],
            run_time=5
        )

        # Final pause
        self.wait(2)

        # Fade everything out
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=2
        )

# To render:
# manim -pqh closing_scene.py ClosingScene
