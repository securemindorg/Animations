from manim import *
import random  # used to randomize colors for demonstration, if desired

class TitleScene(Scene):
    def construct(self):
        # Title and subtitle introducing the GAN overview
        title = Text("Generative Adversarial Network (GAN)", font_size=48)
        subtitle = Text("Understanding the Adversarial Process", font_size=24)
        subtitle.next_to(title, DOWN)

        self.play(Write(title))
        self.play(Write(subtitle))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(subtitle))

class ArchitectureScene(Scene):
    def construct(self):
        # Create the Generator box with a label
        generator_box = RoundedRectangle(corner_radius=0.5, width=3, height=2, color=BLUE)
        generator_label = Text("Generator", font_size=24, color=BLUE)
        generator_group = VGroup(generator_box, generator_label).arrange(DOWN)
        generator_group.to_edge(LEFT, buff=1)

        # Create the Discriminator box with a label
        discriminator_box = RoundedRectangle(corner_radius=0.5, width=3, height=2, color=RED)
        discriminator_label = Text("Discriminator", font_size=24, color=RED)
        discriminator_group = VGroup(discriminator_box, discriminator_label).arrange(DOWN)
        discriminator_group.to_edge(RIGHT, buff=1)

        # Represent input noise coming into the Generator
        noise_text = Text("Noise", font_size=24)
        noise_text.next_to(generator_group, UP)
        arrow_noise = Arrow(start=noise_text.get_bottom(), end=generator_box.get_top(), buff=0.1)

        # Represent output from Generator that goes to the Discriminator as Fake Data
        fake_data_text = Text("Fake Data", font_size=24)
        fake_data_text.next_to(discriminator_group, UP)
        arrow_fake = Arrow(start=generator_box.get_right(), end=discriminator_box.get_left(), buff=0.1)

        # Represent the Real Data feeding into the Discriminator from below
        real_data_text = Text("Real Data", font_size=24)
        real_data_text.next_to(discriminator_group, DOWN)
        arrow_real = Arrow(start=discriminator_box.get_bottom(), end=real_data_text.get_top(), buff=0.1)

        # Animate all elements into the scene
        self.play(Write(noise_text))
        self.play(Create(arrow_noise))
        self.play(Create(generator_group))
        self.wait(1)
        self.play(Create(arrow_fake))
        self.play(Create(discriminator_group))
        self.wait(1)
        self.play(Write(real_data_text))
        self.play(Create(arrow_real))
        self.wait(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects])

class MathScene(Scene):
    def construct(self):
        # Display the core GAN objective function using LaTeX
        equation = MathTex(
            r"\min_G \max_D V(D,G) ="
            r"\mathbb{E}_{x\sim p_{data}(x)}[\log D(x)] + "
            r"\mathbb{E}_{z\sim p_z(z)}[\log(1 - D(G(z)))]",
            font_size=36
        )
        self.play(Write(equation))
        self.wait(3)

        # Optionally, add emphasis for the two parts: discriminator (red) and generator (blue)
        disc_text = Text("Discriminator Reward", font_size=24, color=RED)
        gen_text = Text("Generator Reward", font_size=24, color=BLUE)

        disc_text.next_to(equation, DOWN, buff=0.5).shift(LEFT*2)
        gen_text.next_to(equation, DOWN, buff=0.5).shift(RIGHT*2)

        self.play(Write(disc_text), Write(gen_text))
        self.wait(2)
        self.play(FadeOut(equation), FadeOut(disc_text), FadeOut(gen_text))

class TrainingProcessScene(Scene):
    def construct(self):
        # Step-by-step explanation of the GAN training process
        steps = [
            "1. Sample real data from the data distribution",
            "2. Sample noise and generate fake data",
            "3. Discriminator distinguishes Real vs. Fake",
            "4. Backpropagate errors to update both networks",
        ]
        step_texts = VGroup(*[Text(step, font_size=28) for step in steps]).arrange(DOWN, buff=0.5)
        self.play(Write(step_texts))
        self.wait(3)
        self.play(FadeOut(step_texts))

class ExampleCaseScene(Scene):
    def construct(self):
        # Example showcasing the generation process (e.g., handwritten digits)
        title = Text("Example: Generating Handwritten Digits", font_size=32)
        self.play(Write(title))
        self.wait(1)

        # Demonstrate the transformation from noise to a generated digit
        noise = Text("Noise", font_size=28, color=GRAY)
        digit = Text("Generated Digit", font_size=28, color=GREEN)

        noise.to_edge(LEFT, buff=1)
        digit.to_edge(RIGHT, buff=1)

        arrow = Arrow(start=noise.get_right(), end=digit.get_left(), buff=0.2)

        self.play(FadeIn(noise))
        self.play(FadeIn(digit))
        self.play(Create(arrow))
        self.wait(2)

        # To further illustrate the evolution, you could animate a transition:
        fake_digit = Circle(radius=0.75, color=GREEN).set_fill(GREEN, opacity=0.7)
        fake_digit.move_to(digit.get_center())
        self.play(Transform(digit, fake_digit))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(noise), FadeOut(digit), FadeOut(arrow))
