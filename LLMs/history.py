from manim import *

class TransformerPaper(Scene):
    def construct(self):

        # Add a background effect (gradient rectangle)
        background = Rectangle(
            width=config.frame_width,  # Use MANIM's config.frame_width
            height=config.frame_height,  # Use MANIM's config.frame_height
            fill_color=BLUE_C,
            fill_opacity=0.1,
        ).set_z_index(-1)  # Ensure it is behind all elements

        self.add(background)  # Add background to the scene

        # Title with reduced padding
        title = Text("Attention is All You Need", font_size=40)
        subtitle = Text("The Paper That Changed NLP: arXiv:1706.03762", font_size=30, color=BLUE)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.2)
        title_group.to_edge(UP, buff=0.4)

        # Load the paper image
        paper_image = ImageMobject("20250131_213047.png")
        # Scale the image to appropriate size
        paper_image.height = 3.5

        # Position paper to top-left
        paper_image.to_corner(LEFT + UP, buff=1)
        paper_image.shift(DOWN * 1.5)

        # Authors column
        authors_title = Text("Authors:", font_size=20, color=YELLOW)
        authors = VGroup(
            Text("• Ashish Vaswani", font_size=16),
            Text("• Noam Shazeer", font_size=16),
            Text("• Niki Parmar", font_size=16),
            Text("• Jakob Uszkoreit", font_size=16),
            Text("• Llion Jones", font_size=16),
            Text("• Aidan N. Gomez", font_size=16),
            Text("• Łukasz Kaiser", font_size=16),
            Text("• Illia Polosukhin", font_size=16)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)

        authors_column = VGroup(authors_title, authors).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        authors_column.next_to(paper_image, RIGHT, buff=1)
        authors_column.align_to(paper_image, UP)

        # Facts and Impact sections
        facts_title = Text("Key Facts:", font_size=20, color=YELLOW)
        facts = VGroup(
            Text("• Published: June 2017", font_size=16),
            Text("• Institution: Google Brain & Research", font_size=16),
            Text("• Citations: 100,000+", font_size=16),
            Text("• Published on arXiv", font_size=16)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)

        facts_group = VGroup(facts_title, facts).arrange(DOWN, aligned_edge=LEFT, buff=0.2)

        impact_title = Text("Impact:", font_size=20, color=YELLOW)
        impact = VGroup(
            Text("• Foundation for BERT, GPT, T5", font_size=16),
            Text("• Revolutionary self-attention", font_size=16),
            Text("• Eliminated RNNs/CNNs", font_size=16),
            Text("• State-of-the-art in NLP", font_size=16),
            Text("• Inspired Vision Transformers", font_size=16)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)

        impact_group = VGroup(impact_title, impact).arrange(DOWN, aligned_edge=LEFT, buff=0.2)

        # Position the right column
        right_column = VGroup(facts_group, impact_group).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        right_column.next_to(authors_column, RIGHT, buff=1)
        right_column.align_to(authors_column, UP)

        # Animation sequence
        self.play(Write(title_group))

        self.wait(2)

        self.play(FadeIn(paper_image))

        self.wait(4)

        # Animate and highlight authors section
        self.play(Write(authors_title))
        for author in authors:
            self.play(Write(author), run_time=0.5)
        highlight_authors = SurroundingRectangle(authors_column, color=YELLOW, buff=0.1)
        self.play(Create(highlight_authors))
        self.play(FadeOut(highlight_authors))

        self.wait(4)

        # Animate and highlight facts section
        self.play(Write(facts_title))
        for fact in facts:
            self.play(Write(fact), run_time=0.5)
        highlight_facts = SurroundingRectangle(facts_group, color=YELLOW, buff=0.1)
        self.play(Create(highlight_facts))
        self.play(FadeOut(highlight_facts))

        self.wait(4)

        # Animate and highlight impact section
        self.play(Write(impact_title))
        for impact_point in impact:
            self.play(Write(impact_point), run_time=0.5)
        highlight_impact = SurroundingRectangle(impact_group, color=YELLOW, buff=0.1)
        self.play(Create(highlight_impact))
        self.play(FadeOut(highlight_impact))

        self.wait(40)
