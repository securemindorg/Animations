from manim import *

class SolutionsAndMitigation(Scene):
    def create_solution_box(self, title, details, icon, color):
        box = VGroup()

        # Create icon
        if icon == "data":
            icon_mob = VGroup(
                Rectangle(height=0.3, width=0.4, color=color),
                Rectangle(height=0.3, width=0.4, color=color).next_to(ORIGIN, RIGHT, buff=0.1),
                Rectangle(height=0.3, width=0.4, color=color).next_to(ORIGIN, DOWN, buff=0.1)
            )
        elif icon == "check":
            icon_mob = VGroup(
                Line(ORIGIN, RIGHT * 0.3 + UP * 0.3, color=color),
                Line(RIGHT * 0.3 + UP * 0.3, RIGHT * 0.6 + DOWN * 0.3, color=color)
            )
        elif icon == "cycle":
            icon_mob = VGroup(
                Arc(radius=0.3, angle=TAU * 0.8, color=color),
                Arrow(
                    start=RIGHT * 0.3,
                    end=RIGHT * 0.5,
                    color=color
                ).scale(0.3)
            )
        elif icon == "people":
            icon_mob = VGroup(
                Circle(radius=0.15, color=color),
                Circle(radius=0.15, color=color).shift(RIGHT * 0.4),
                Circle(radius=0.15, color=color).shift(LEFT * 0.4)
            )
        else:  # eye for oversight
            icon_mob = VGroup(
                Circle(radius=0.2, color=color),
                Circle(radius=0.1, color=color).move_to(ORIGIN)
            )

        title_text = Text(title, font_size=24, color=color)
        detail_text = Text(details, font_size=18, color=WHITE)

        box.add(icon_mob, title_text, detail_text)
        box.arrange(DOWN, buff=0.2, aligned_edge=LEFT)
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
        title = Text("Solutions & Mitigation Strategies", font_size=30)
        subtitle = Text("Building Fairer AI Systems", font_size=20, color=BLUE)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.3)
        title_group.to_edge(UP, buff=0.5)

        # Create solution boxes
        balanced_data = self.create_solution_box(
            "Balanced Training Data",
            "• Diverse and representative datasets\n• Equal representation across groups\n• Regular data quality checks",
            "data",
            BLUE
        )

        feature_selection = self.create_solution_box(
            "Careful Feature Selection",
            "• Remove sensitive attributes\n• Test for proxy variables\n• Validate feature importance",
            "check",
            GREEN
        )

        bias_audits = self.create_solution_box(
            "Regular Bias Audits",
            "• Automated testing pipelines\n• Performance across groups\n• Continuous monitoring",
            "cycle",
            YELLOW
        )

        human_oversight = self.create_solution_box(
            "Human Oversight",
            "• Expert review of decisions\n• Appeal mechanisms\n• Transparency in process",
            "eye",
            RED
        )

        diverse_teams = self.create_solution_box(
            "Diverse Development Teams",
            "• Multiple perspectives\n• Inclusive design process\n• Cross-cultural insights",
            "people",
            PURPLE
        )

        # Arrange solutions vertically with proper spacing
        solutions = VGroup(balanced_data, feature_selection, bias_audits, human_oversight, diverse_teams)
        solutions.arrange_in_grid(rows=3, cols=2, buff=0.5).scale(0.8)
        solutions.next_to(title_group, DOWN, buff=0.5)

        # Create connecting framework
        framework = VGroup()
        for i in range(len(solutions)):
            for j in range(i + 1, len(solutions)):
                line = DashedLine(
                    solutions[i].get_center(),
                    solutions[j].get_center(),
                    color=GRAY,
                    dash_length=0.1
                )
                framework.add(line)

        # Animation sequence
        self.play(Write(title_group))
        self.wait(0.5)

        # Animate each solution box with highlight
        highlights = VGroup()
        for solution in solutions:
            self.play(
                FadeIn(solution, shift=UP * 0.5),
                run_time=0.8
            )

            highlight = SurroundingRectangle(solution, buff=0.1, color=solution[1].get_color())
            highlights.add(highlight)
            self.play(Create(highlight))
            self.wait(0.3)

        # Add connecting framework
        self.play(Create(framework), run_time=1.5)

        # Add final message
        final_message = Text(
            "Implementing these solutions requires ongoing commitment",
            font_size=20,
            color=YELLOW
        ).next_to(solutions, DOWN, buff=0.5)

        self.play(Write(final_message))
        self.wait(0.5)

        # Pulse animation for emphasis
        self.play(
            *[
                solution.animate.scale(1.05)
                for solution in solutions
            ],
            rate_func=there_and_back,
            run_time=1
        )
        self.wait(1)

        # Fade out
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

# To render:
# manim -pqh solutions_and_mitigation.py SolutionsAndMitigation
