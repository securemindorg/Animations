from manim import *

class TextGenerationVAE(Scene):
    def construct(self):
        # Add a background effect (gradient rectangle)
        background = Rectangle(
            width=config.frame_width,  # Use MANIM's config.frame_width
            height=config.frame_height,  # Use MANIM's config.frame_height
            fill_color=BLUE_C,
            fill_opacity=0.1,
        ).set_z_index(-1)  # Ensure it is behind all elements

        self.add(background)  # Add background to the scene


        sentences_text = Text("Text Generation Using VAE", font_size=28).to_edge(UP)
        self.play(Write(sentences_text))
        self.wait(1)

        # Create latent space visualization
        latent_space = Circle(radius=2, color=BLUE_E, fill_opacity=0.2)
        latent_label = Text("Latent Space", color=WHITE).scale(0.6)
        latent_label.next_to(latent_space, UP)

        # Create random points in latent space
        points = VGroup(*[
            Dot(
                point=latent_space.point_from_proportion(i/5),
                color=YELLOW,
                radius=0.08
            ) for i in range(5)
        ])

        # Initial setup
        self.play(
            Create(latent_space),
            Write(latent_label),
            Create(points)
        )
        self.wait(10)

        # Step 1: Sample point from latent space
        step1_text = Text("1. Sample point from latent space", color=WHITE).scale(0.5)
        step1_text.to_edge(LEFT).shift(UP * 1)

        selected_point = Dot(point=latent_space.get_center(), color=RED, radius=0.12)
        self.play(
            Write(step1_text),
            Create(selected_point)
        )
        self.wait(10)

        # Step 2: Decode vector
        decoder_box = Rectangle(height=2, width=1.5, color=GREEN)
        decoder_label = Text("Decoder\nNetwork", color=WHITE).scale(0.5)
        decoder_group = VGroup(decoder_box, decoder_label)
        decoder_group.shift(RIGHT * 3)

        arrow = Arrow(selected_point.get_center(), decoder_group.get_left(), color=WHITE)

        step2_text = Text("2. Pass through decoder network", color=WHITE).scale(0.5)
        step2_text.next_to(step1_text, DOWN, aligned_edge=LEFT)

        self.play(
            Create(decoder_group),
            Create(arrow),
            Write(step2_text)
        )
        self.wait(10)

        # Step 3: Generate text
        output_text = Text(
            '"The AI system\nprocessed data..."',
            color=WHITE
        ).scale(0.4)
        output_text.next_to(decoder_group, RIGHT)

        step3_text = Text("3. Generate new text sequence", color=WHITE).scale(0.5)
        step3_text.next_to(step2_text, DOWN, aligned_edge=LEFT)

        output_arrow = Arrow(decoder_group.get_right(), output_text.get_left(), color=WHITE)

        self.play(
            Create(output_arrow),
            Write(output_text),
            Write(step3_text)
        )
        self.wait(10)

        # Show interpolation
        interpolation_title = Text("Interpolation between texts:", color=WHITE).scale(0.5)
        interpolation_title.to_edge(DOWN).shift(UP)

        text1 = Text('"Utica University..."', color=YELLOW).scale(0.3)
        text2 = Text('"Tech conference..."', color=YELLOW).scale(0.3)

        interpolation_group = VGroup(text1, Text("→", color=WHITE).scale(0.4), text2)
        interpolation_group.arrange(RIGHT)
        interpolation_group.next_to(interpolation_title, DOWN)

        self.play(
            Write(interpolation_title),
            Write(interpolation_group)
        )

        # Add moving dot to show interpolation
        moving_dot = Dot(color=RED)
        path = Line(text1.get_top(), text2.get_top(), color=YELLOW)
        self.play(
            MoveAlongPath(moving_dot, path),
            run_time=2
        )

        self.wait(10)
