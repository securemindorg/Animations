from manim import *

class RealWorldImplications(Scene):
    def create_case_study(self, title, details, color):
        box = VGroup()
        title_text = Text(title, font_size=24, color=color)
        detail_text = Text(details, font_size=18, color=WHITE)
        box.add(title_text, detail_text)
        box.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        return box

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
        title = Text("Real-World Implications of AI Bias", font_size=40)
        subtitle = Text("Impact on Critical Decisions", font_size=30, color=BLUE)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.3)
        title_group.to_edge(UP, buff=0.5)

        # Create case studies
        hiring = self.create_case_study(
            "Hiring Algorithms",
            "Historical hiring patterns lead to\ngender and racial discrimination",
            YELLOW
        )

        loan = self.create_case_study(
            "Loan Approval Systems",
            "Credit algorithms show bias against\nminority communities",
            GREEN
        )

        facial = self.create_case_study(
            "Facial Recognition",
            "Lower accuracy for minorities\nand women [[1]]",
            RED
        )

        healthcare = self.create_case_study(
            "Healthcare Decisions",
            "CAD systems show reduced accuracy\nfor black patients [[4]]",
            BLUE
        )

        # Arrange case studies in a grid
        cases = VGroup(hiring, loan, facial, healthcare).arrange_in_grid(
            rows=2,
            cols=2,
            buff=0.75
        ).scale(0.9)
        cases.next_to(title_group, DOWN, buff=0.75)

        # Create highlighting rectangles
        highlights = VGroup(*[
            SurroundingRectangle(case, buff=0.2, color=case[0].get_color())
            for case in [hiring, loan, facial, healthcare]
        ])

        # Animation sequence
        self.play(Write(title_group))
        self.wait(0.5)

        # Animate each case study with its highlight
        for case, highlight in zip([hiring, loan, facial, healthcare], highlights):
            self.play(
                FadeIn(case, shift=UP * 0.5),
                run_time=0.8
            )
            self.play(
                Create(highlight),
                run_time=0.5
            )
            self.wait(0.5)

        # Add impact text
        impact_text = Text(
            "These biases affect millions of lives daily",
            font_size=24,
            color=YELLOW
        ).next_to(cases, DOWN, buff=0.5)

        self.play(Write(impact_text))
        self.wait(0.5)

        # Create connection lines between cases
        connections = VGroup()
        for i in range(len(highlights)):
            for j in range(i + 1, len(highlights)):
                line = DashedLine(
                    highlights[i].get_center(),
                    highlights[j].get_center(),
                    color=GRAY,
                    dash_length=0.1
                )
                connections.add(line)

        self.play(
            Create(connections),
            run_time=1.5
        )

        # Pulse animation for emphasis
        self.play(
            *[
                highlight.animate.scale(1.1).set_opacity(0.5)
                for highlight in highlights
            ],
            rate_func=there_and_back,
            run_time=1
        )

        # Final warning text
        warning_text = Text(
            "AI systems must be carefully monitored\nand regularly audited for bias",
            font_size=24,
            color=RED
        ).next_to(impact_text, DOWN, buff=0.5)

        self.play(
            Write(warning_text),
            run_time=1
        )
        self.wait(2)

        # Fade out
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

# To render:
# manim -pqh real_world_implications.py RealWorldImplications
