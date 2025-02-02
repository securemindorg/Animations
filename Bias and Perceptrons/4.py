from manim import *
import numpy as np

class BiasInAI(Scene):
    def create_dataset_scatter(self, axes, data_points, color):
        return VGroup(*[Dot(axes.c2p(x, y), color=color) for x, y in data_points])

    def construct(self):

        # Add a background effect (gradient rectangle)
        background = Rectangle(
            width=config.frame_width,  # Use MANIM's config.frame_width
            height=config.frame_height,  # Use MANIM's config.frame_height
            fill_color=BLUE_C,
            fill_opacity=0.1,
        ).set_z_index(-1)  # Ensure it is behind all elements
        self.add(background)  # Add background to the scene


        # Part 1: Training Data Bias
        title1 = Text("Where Bias Enters: Training Data", font_size=30)
        subtitle1 = Text("Biased Input → Biased Decisions", font_size=20, color=BLUE)
        title_group1 = VGroup(title1, subtitle1).arrange(DOWN, buff=0.3)
        title_group1.to_edge(UP, buff=0.4)

        # Create coordinate system
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 10, 1],
            axis_config={"include_tip": True},
            x_length=6,
            y_length=6
        )
        axes_labels = VGroup(
            Text("Years of Experience", font_size=18).next_to(axes.x_axis, DOWN),
            Text("Performance Score", font_size=18).next_to(axes.y_axis, RIGHT, buff=-0.5).rotate(90 * DEGREES)
        )
        graph_group = VGroup(axes, axes_labels).shift(LEFT * 3)

        # Create biased dataset (mostly male candidates)
        np.random.seed(42)
        male_data = [(np.random.uniform(4, 9), np.random.uniform(5, 9)) for _ in range(15)]
        female_data = [(np.random.uniform(4, 9), np.random.uniform(5, 9)) for _ in range(5)]

        male_dots = self.create_dataset_scatter(axes, male_data, BLUE)
        female_dots = self.create_dataset_scatter(axes, female_data, PINK)

        legend = VGroup(
            Dot(color=BLUE), Text("Male", font_size=20),
            Dot(color=PINK), Text("Female", font_size=20)
        ).arrange(RIGHT, buff=0.2)
        legend.to_corner(UR, buff=0.5)

        # Animation sequence for Training Data Bias
        self.play(Write(title_group1))
        self.wait(4)


        self.play(
            Create(axes),
            Write(axes_labels)
        )
        self.play(
            Create(legend),
            *[GrowFromCenter(dot) for dot in male_dots],
            *[GrowFromCenter(dot) for dot in female_dots]
        )

        bias_text = Text(
            '"Garbage in, garbage out"\nModel trained on biased data\nwill make biased predictions',
            font_size=24,
            color=YELLOW
        ).shift(RIGHT * 3)
        self.play(Write(bias_text))
        self.wait(4)

        # Transition to Feature Selection Bias
        self.play(
            *[FadeOut(mob) for mob in [bias_text, legend, male_dots, female_dots]]
        )
        self.wait(4)

        # Part 2: Feature Selection Bias
        title2 = Text("Feature Selection Bias", font_size=30)
        subtitle2 = Text("Choosing What to Measure", font_size=20, color=BLUE)
        title_group2 = VGroup(title2, subtitle2).arrange(UP)
        title_group2.to_edge(UP, buff=0.4)

        # Create feature comparison
        feature_box = VGroup(
            Text("Selected Features:", color=GREEN, font_size=24),
            Text("• Years of Experience", font_size=20),
            Text("• University Ranking", font_size=20),
            Text("Ignored Features:", color=RED, font_size=24),
            Text("• Problem Solving", font_size=20),
            Text("• Team Collaboration", font_size=20),
            Text("• Communication Skills", font_size=20)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        feature_box.shift(RIGHT * 3)

        self.play(
            Transform(title_group1, title_group2),
            Write(feature_box)
        )
        self.wait(4)

        # Part 3: Historical Data Reflection
        title3 = Text("Historical Data Reflection", font_size=30)
        subtitle3 = Text("Past Biases Shape Future Decisions", font_size=20, color=BLUE)
        title_group3 = VGroup(title3, subtitle3).arrange(DOWN, buff=0.3)
        title_group3.to_edge(UP, buff=0.4)

        # Create historical trend visualization
        years = [2015, 2016, 2017, 2018, 2019]
        male_ratio = [0.8, 0.75, 0.72, 0.7, 0.68]
        female_ratio = [0.2, 0.25, 0.28, 0.3, 0.32]

        historical_chart = VGroup()
        for i in range(len(years)):
            bar_male = Rectangle(
                height=male_ratio[i] * 3,
                width=0.5,
                color=BLUE,
                fill_opacity=0.7
            )
            bar_female = Rectangle(
                height=female_ratio[i] * 3,
                width=0.5,
                color=PINK,
                fill_opacity=0.7
            )
            bar_female.next_to(bar_male, UP, buff=0)
            year_label = Text(str(years[i]), font_size=16)
            year_label.next_to(bar_male, DOWN)
            group = VGroup(bar_male, bar_female, year_label)
            group.shift(RIGHT * i - RIGHT * 2)
            historical_chart.add(group)

        historical_chart.shift(RIGHT * 3)

        self.play(
            Transform(title_group1, title_group3),
            FadeOut(feature_box),
            Create(historical_chart)
        )
        self.wait(4)

        historical_text = Text(
            "Historical hiring patterns\nbecome encoded in the model",
            font_size=24,
            color=YELLOW
        ).next_to(historical_chart, DOWN, buff=0.5)

        self.play(Write(historical_text))
        self.wait(4)

        # Final fadeout
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

# To render:
# manim -pqh bias_in_ai.py BiasInAI
