from manim import *

class CollatzConjectureManual(Scene):
    def construct(self):
        # Title
        title = Text("The Collatz Conjecture").scale(1.2)
        underline = Line(LEFT, RIGHT).scale(4).next_to(title, DOWN)
        self.play(Write(title), Create(underline))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(underline))

        # Introduction text
        intro_text = Text("""
The Collatz Conjecture is a mathematical conjecture that applies to positive integers:

1. If the number is even, divide it by 2.
2. If the number is odd, multiply it by 3 and add 1.

Repeat these steps with the new value.

The conjecture states that no matter what positive integer you start with,
you will always eventually reach 1.
""", font_size=28).scale(0.9)
        self.play(Write(intro_text), run_time=10)
        self.wait(4)
        self.play(FadeOut(intro_text))

        # Visual demonstration of rules
        even_rule = Tex(r"If $n$ is even: $n \rightarrow \dfrac{n}{2}$", color=BLUE).shift(UP*1)
        odd_rule = Tex(r"If $n$ is odd: $n \rightarrow 3n + 1$", color=RED).shift(DOWN*1)
        self.play(Write(even_rule))
        self.play(Write(odd_rule))
        self.wait(3)
        self.play(FadeOut(even_rule), FadeOut(odd_rule))

        # Print the rules to the screen
        rule_text_even = Text("n is even, n → n/2", color=BLUE, font_size=22).shift(UP * 0.9 + LEFT * 5.5)
        rule_text_odd = Text("n is odd, n → 3n + 1", color=RED, font_size=22).shift(DOWN * 0.9 + LEFT * 5.5)
        self.play(Write(rule_text_even))
        self.wait(0.25)
        self.play(Write(rule_text_odd))
        self.wait(2)

        # Graph 1: Starting at 4
        graph1_start = UP * 2.5 + RIGHT * 6
        node_4 = Text("4", font_size=36).move_to(graph1_start)
        node_2 = Text("2", font_size=36).next_to(node_4, DOWN, buff=1)
        node_1 = Text("1", font_size=36).next_to(node_2, DOWN, buff=1)

        arrow_4_to_2 = Arrow(node_4.get_bottom(), node_2.get_top(), buff=0.1, color=BLUE)
        arrow_2_to_1 = Arrow(node_2.get_bottom(), node_1.get_top(), buff=0.1, color=BLUE)

        self.play(Write(node_4))
        self.wait(0.5)
        self.play(Create(arrow_4_to_2), Write(node_2))
        self.wait(0.5)
        self.play(Create(arrow_2_to_1), Write(node_1))
        self.wait(1)

        # Graph 2: Starting at 10
        graph2_start = UP * 2.5 + RIGHT * 3
        node_10 = Text("10", font_size=36).move_to(graph2_start)
        node_5 = Text("5", font_size=36).next_to(node_10, DOWN, buff=1)
        node_16 = Text("16", font_size=36).next_to(node_5, DOWN, buff=1)
        node_8 = Text("8", font_size=36).next_to(node_16, DOWN, buff=1)

        arrow_10_to_5 = Arrow(node_10.get_bottom(), node_5.get_top(), buff=0.1, color=BLUE)
        arrow_5_to_16 = Arrow(node_5.get_bottom(), node_16.get_top(), buff=0.1, color=RED)
        arrow_16_to_8 = Arrow(node_16.get_bottom(), node_8.get_top(), buff=0.1, color=BLUE)
        arrow_8_to_4 = Arrow(node_8.get_top(), node_4.get_bottom(), buff=0.1, color=BLUE)

        self.play(Write(node_10))
        self.wait(0.5)
        self.play(Create(arrow_10_to_5), Write(node_5))
        self.wait(0.5)
        self.play(Create(arrow_5_to_16), Write(node_16))
        self.wait(0.5)
        self.play(Create(arrow_16_to_8), Write(node_8))
        self.wait(0.5)
        self.play(Create(arrow_8_to_4))
        self.wait(1)

        # Graph 3: Starting at 7
        graph3_start = UP * 2.5 + LEFT * 3
        node_7 = Text("7", font_size=36).move_to(graph3_start)
        node_22 = Text("22", font_size=36).next_to(node_7, DOWN, buff=1)
        node_11 = Text("11", font_size=36).next_to(node_22, DOWN, buff=1)
        node_34 = Text("34", font_size=36).next_to(node_11, DOWN, buff=1)
        node_17 = Text("17", font_size=36).next_to(node_34, DOWN, buff=1)

        # Graph 4: Starting at 7
        graph4_start = UP * 2.5 + LEFT * 0
        node_52 = Text("52", font_size=36).move_to(graph4_start)
        node_26 = Text("26", font_size=36).next_to(node_52, DOWN, buff=1)
        node_13 = Text("13", font_size=36).next_to(node_26, DOWN, buff=1)
        node_40 = Text("40", font_size=36).next_to(node_13, DOWN, buff=1)
        node_20 = Text("20", font_size=36).next_to(node_40, DOWN, buff=1)

        arrow_7_to_22 = Arrow(node_7.get_bottom(), node_22.get_top(), buff=0.1, color=RED)
        arrow_22_to_11 = Arrow(node_22.get_bottom(), node_11.get_top(), buff=0.1, color=BLUE)
        arrow_11_to_34 = Arrow(node_11.get_bottom(), node_34.get_top(), buff=0.1, color=RED)
        arrow_34_to_17 = Arrow(node_34.get_bottom(), node_17.get_top(), buff=0.1, color=BLUE)

        arrow_17_to_52 = Arrow(node_17.get_top(), node_52.get_bottom(), buff=0.1, color=BLUE)

        arrow_52_to_26 = Arrow(node_52.get_bottom(), node_26.get_top(), buff=0.1, color=BLUE)
        arrow_26_to_13 = Arrow(node_26.get_bottom(), node_13.get_top(), buff=0.1, color=BLUE)
        arrow_13_to_40 = Arrow(node_13.get_bottom(), node_40.get_top(), buff=0.1, color=RED)
        arrow_40_to_20 = Arrow(node_40.get_bottom(), node_20.get_top(), buff=0.1, color=BLUE)

        arrow_20_to_10 = Arrow(node_20.get_top(), node_10.get_bottom(), buff=0.1, color=BLUE)


        self.play(Write(node_7))
        self.wait(0.5)
        self.play(Create(arrow_7_to_22), Write(node_22))
        self.wait(0.5)
        self.play(Create(arrow_22_to_11), Write(node_11))
        self.wait(0.5)
        self.play(Create(arrow_11_to_34), Write(node_34))
        self.wait(0.5)
        self.play(Create(arrow_34_to_17), Write(node_17))
        self.wait(0.5)
        self.play(Create(arrow_17_to_52), Write(node_52))
        self.wait(0.5)
        self.play(Create(arrow_52_to_26), Write(node_26))
        self.wait(0.5)
        self.play(Create(arrow_26_to_13), Write(node_13))
        self.wait(0.5)
        self.play(Create(arrow_13_to_40), Write(node_40))
        self.wait(0.5)
        self.play(Create(arrow_40_to_20), Write(node_20))
        self.wait(0.5)
        self.play(Create(arrow_20_to_10))
        self.wait(1)

        # this should allow the camera to zoom out a bit to make space for the conclusion... maybe
        # this does work but I'm not going to use it because it makes it hard to red
        #self.play(
        #    *[obj.animate.scale(0.65).shift(UP * 1) for obj in self.mobjects],
        #    run_time=2
        #)


        # clear the screen before proceeding to the next step
        #self.play(FadeOut(rule_text_even), FadeOut(rule_text_odd))
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )

        # Conclusion
        conclusion = Text("""
No matter which positive integer we start with,
the sequence eventually reaches 1.

The Collatz Conjecture remains unproven,
but holds true for all numbers tested so far.
""", font_size=24) #.to_edge(DOWN)
        self.play(Write(conclusion), run_time=8)
        self.wait(4)
