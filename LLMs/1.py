from manim import *

class LLMIntroduction(Scene):
    def construct(self):
         # Add a background effect (gradient rectangle)
        background = Rectangle(
            width=config.frame_width,  # Use MANIM's config.frame_width
            height=config.frame_height,  # Use MANIM's config.frame_height
            fill_color=BLUE_C,
            fill_opacity=0.1,
        ).set_z_index(-1)  # Ensure it is behind all elements

        self.add(background)  # Add background to the scene


        # Title sequence
        title = Text("Understanding Large Language Models", font_size=40)
        subtitle = Text("From Text to Intelligence", font_size=30)
        subtitle.set_color(BLUE)
        subtitle.next_to(title, DOWN)

        # Create the initial question
        question = Text("How can AI understand and generate human-like text?",
                       font_size=35)
        question.set_color(YELLOW)

        # Create example bubbles showing LLM capabilities
        chat_bubble = Circle()
        chat_text = Text("Chat", font_size=20)
        chat_text.move_to(chat_bubble.get_center())
        chat_group = VGroup(chat_bubble, chat_text)

        write_bubble = Circle()
        write_text = Text("Write", font_size=20)
        write_text.move_to(write_bubble.get_center())
        write_group = VGroup(write_bubble, write_text)

        code_bubble = Circle()
        code_text = Text("Code", font_size=20)
        code_text.move_to(code_bubble.get_center())
        code_group = VGroup(code_bubble, code_text)

        # Arrange bubbles in a triangle
        bubbles = VGroup(chat_group, write_group, code_group)
        bubbles.arrange_in_grid(rows=2, cols=2, buff=1)

        # Animation sequence
        self.play(Write(title))
        self.wait(1)
        self.play(FadeIn(subtitle))
        self.wait(1)

        # Move title group up and show question
        title_group = VGroup(title, subtitle)
        self.play(
            title_group.animate.scale(0.7).to_edge(UP),
        )
        self.play(Write(question))
        self.wait(1)

        # Move question up and show capabilities
        self.play(
            question.animate.scale(0.7).next_to(title_group, DOWN),
            run_time=1.5
        )

        # Animate bubbles appearing with a pulsing effect
        for bubble in bubbles:
            self.play(
                Create(bubble[0]),
                Write(bubble[1]),
                bubble.animate.scale(1.2),
                run_time=0.5
            )
            self.play(
                bubble.animate.scale(1/1.2),
                run_time=0.3
            )

        # Final pause
        self.wait(2)

        # Fade out everything for transition
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )


# To render:
# manim -pqh LLMIntroduction.py LLMIntroduction
# manim -pqh LLMIntroduction.py BrainTransition
