from manim import *

class LogisticRegression(Scene):
    def construct(self):
        # Title
        title = Text("Logistic Regression").scale(1.5)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        # Create axes
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-0.1, 1.1, 0.2],
            axis_config={"color": BLUE},
        )
        self.play(Create(axes))

        # Create logistic function
        logistic_curve = axes.plot(lambda x: 1 / (1 + np.exp(-x)), color=YELLOW)
        logistic_label = axes.get_graph_label(logistic_curve, label='\\sigma(x) = \\frac{1}{1 + e^{-x}}')

        # Show the logistic curve
        self.play(Create(logistic_curve), Write(logistic_label))
        self.wait(2)

        # Create a point on the curve
        point = Dot(color=RED).move_to(axes.c2p(0, 0.5))
        self.play(Create(point))
        self.wait(1)

        # Show odds
        odds_text = Text("Odds = p / (1 - p)").to_edge(UP)
        self.play(Write(odds_text))
        self.wait(1)

        # Create odds visualization
        odds_box = Rectangle(width=2, height=1, color=GREEN).move_to(axes.c2p(1, 0.5))
        self.play(Create(odds_box))
        self.wait(1)

        # Show logit transformation
        logit_text = Text("Logit(p) = ln(Odds)").to_edge(DOWN)
        self.play(Write(logit_text))
        self.wait(1)

        # Create logit curve
        logit_curve = axes.plot(lambda x: np.log(np.exp(x) / (1 + np.exp(x))), color=PURPLE)
        logit_label = axes.get_graph_label(logit_curve, label='Logit(p)')

        # Show the logit curve
        self.play(Create(logit_curve), Write(logit_label))
        self.wait(2)

        # End scene
        self.play(FadeOut(odds_text), FadeOut(logit_text), FadeOut(odds_box), FadeOut(point), FadeOut(logistic_curve), FadeOut(logit_curve))
        self.wait(1)

        # Final message
        final_message = Text("Logistic Regression helps us model binary outcomes!").scale(1.2)
        self.play(Write(final_message))
        self.wait(3)
        self.play(FadeOut(final_message))

# To run this script, save it as a .py file and run it using the MANIM command line.

