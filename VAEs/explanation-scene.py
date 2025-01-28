from manim import *
import numpy as np

class VAEIntroduction(Scene):
    def construct(self):
        # Add a background effect (gradient rectangle)
        background = Rectangle(
            width=config.frame_width,  # Use MANIM's config.frame_width
            height=config.frame_height,  # Use MANIM's config.frame_height
            fill_color=BLUE_C,
            fill_opacity=0.1,
        ).set_z_index(-1)  # Ensure it is behind all elements
        self.add(background)  # Add background to the scene


        # Show the original paper reference
        # First create an ImageMobject from your saved image
        paper_image = ImageMobject("vae-paper.png").scale(1.5)  # Adjust scale as needed
        paper_image.height = 3  # Match the height we used before


        # Use Group instead of VGroup for mixing ImageMobject with other mobjects
        paper_group = Group(paper_image)
        paper_group.to_edge(LEFT).shift(UP)

        # Add a caption below the paper
        paper_caption = Text(
            "Auto-Encoding Variational Bayes\nKingma & Welling, 2013",
            color=WHITE
        ).scale(0.4)
        paper_caption.next_to(paper_group, DOWN, buff=0.2)

        # Animate them appearing
        self.play(
            FadeIn(paper_image),
            Write(paper_caption)
        )

        self.wait(10)

        # Create VAE architecture visualization
        # Input data
        input_box = Rectangle(height=2, width=1, color=WHITE)
        input_label = Text("Input\nData", color=WHITE).scale(0.3)
        input_group = VGroup(input_box, input_label)
        input_group.next_to(paper_group, RIGHT, buff=1)

        # Encoder
        encoder = Rectangle(height=1.5, width=1, color=BLUE)
        encoder_label = Text("Encoder", color=WHITE).scale(0.3)
        encoder_group = VGroup(encoder, encoder_label)
        encoder_group.next_to(input_group, RIGHT, buff=.75)

        # Latent space
        latent_circle = Circle(radius=0.5, color=YELLOW)
        latent_label = Text("Latent\nSpace", color=WHITE).scale(0.3)
        latent_group = VGroup(latent_circle, latent_label)
        latent_group.next_to(encoder_group, RIGHT, buff=.75)

        # Decoder
        decoder = Rectangle(height=1.5, width=1, color=GREEN)
        decoder_label = Text("Decoder", color=WHITE).scale(0.3)
        decoder_group = VGroup(decoder, decoder_label)
        decoder_group.next_to(latent_group, RIGHT, buff=.75)

        # Output
        output_box = Rectangle(height=2, width=1, color=WHITE)
        output_label = Text("Output\nData", color=WHITE).scale(0.3)
        output_group = VGroup(output_box, output_label)
        output_group.next_to(decoder_group, RIGHT, buff=.75)

        # Arrows
        arrows = VGroup(
            Arrow(input_group.get_right(), encoder_group.get_left(), color=WHITE),
            Arrow(encoder_group.get_right(), latent_group.get_left(), color=WHITE),
            Arrow(latent_group.get_right(), decoder_group.get_left(), color=WHITE),
            Arrow(decoder_group.get_right(), output_group.get_left(), color=WHITE)
        )

        # Animate VAE architecture
        components = [input_group, encoder_group, latent_group,
                     decoder_group, output_group]

        for component in components:
            self.play(Create(component))

        for arrow in arrows:
            self.play(Create(arrow))

        self.wait(2)

        # Add explanation text
        explanation = VGroup(
            Text("VAEs learn to:", color=WHITE).scale(0.5),
            Text("1. Compress data into latent space", color=WHITE).scale(0.4),
            Text("2. Generate new data from latent space", color=WHITE).scale(0.4),
            Text("3. Maintain semantic relationships", color=WHITE).scale(0.4)
        ).arrange(DOWN, aligned_edge=LEFT)
        explanation.to_edge(DOWN, buff=1)

        self.play(Write(explanation))
        self.wait(2)

        # Show latent space properties
        latent_props = VGroup(
            Text("• Continuous", color=YELLOW).scale(0.3),
            Text("• Compressed", color=YELLOW).scale(0.3),
            Text("• Meaningful", color=YELLOW).scale(0.3)
        ).arrange(DOWN, aligned_edge=LEFT)
        latent_props.next_to(latent_group, DOWN, buff=0.5)

        self.play(Write(latent_props))

        self.wait(10)

        # Fade out everything
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=1
        )
