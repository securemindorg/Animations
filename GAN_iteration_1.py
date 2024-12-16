from manim import *

class GANIntroduction(Scene):
    def construct(self):
        # Create title
        title = Text("Generative Adversarial Networks (GANs)", font_size=40)
        self.play(Write(title))
        self.wait()
        self.play(title.animate.scale(0.6).to_edge(UP))

        # Create Generator and Discriminator
        generator = Rectangle(height=2, width=3, color=BLUE)
        generator_text = Text("Generator", font_size=30, color=BLUE)
        generator_text.next_to(generator, UP)
        generator_group = VGroup(generator, generator_text)
        generator_group.shift(LEFT * 3)

        discriminator = Rectangle(height=2, width=3, color=RED)
        discriminator_text = Text("Discriminator", font_size=30, color=RED)
        discriminator_text.next_to(discriminator, UP)
        discriminator_group = VGroup(discriminator, discriminator_text)
        discriminator_group.shift(RIGHT * 3)

        # Create random noise input
        noise = Text("Random Noise", font_size=25)
        noise.next_to(generator, LEFT, buff=1)
        noise_arrow = Arrow(noise.get_right(), generator.get_left(), color=GRAY)

        # Create fake/real data representations
        fake_data = Dot(color=BLUE).move_to(generator.get_right())
        real_data = Dot(color=GREEN).move_to(UP * 1)
        
        # Animation sequence
        self.play(Create(generator_group), Create(discriminator_group))
        self.play(Write(noise), Create(noise_arrow))
        
        # Show data flow
        self.play(Create(fake_data))
        self.play(fake_data.animate.move_to(discriminator.get_left()))
        self.play(Create(real_data))
        self.play(real_data.animate.move_to(discriminator.get_left()))

        # Add explanation
        explanation = Text(
            "GANs learn through adversarial training:\n" +
            "Generator creates fake data\n" +
            "Discriminator tries to detect fakes",
            font_size=25
        ).next_to(title, DOWN, buff=0.5)
        
        self.play(Write(explanation))
        self.wait(2)
