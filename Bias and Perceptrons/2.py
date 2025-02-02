from manim import *

class Perceptron(Scene):
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
        title = Text("What is a Perceptron?", font_size=40)
        subtitle = Text("The Building Block of Neural Networks", font_size=30, color=BLUE)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.3)
        title_group.to_edge(UP, buff=0.5)

        # Create input nodes
        input_nodes = VGroup(*[Circle(radius=0.3, color=BLUE) for _ in range(3)])
        input_nodes.arrange(DOWN, buff=1)
        input_nodes.shift(LEFT * 4)

        # Label input nodes
        input_labels = VGroup(
            Text("x₁", font_size=24),
            Text("x₂", font_size=24),
            Text("x₃", font_size=24)
        )
        for label, node in zip(input_labels, input_nodes):
            label.next_to(node, LEFT)

        # Create bias node
        bias_node = Circle(radius=0.3, color=GREEN)
        bias_node.next_to(input_nodes, UP, buff=0.5)
        bias_label = Text("bias", font_size=24).next_to(bias_node, LEFT)

        # Create output node
        output_node = Circle(radius=0.3, color=RED)
        output_node.shift(RIGHT * 3)
        output_label = Text("Output", font_size=20).next_to(output_node, DOWN)

        # Create weights (arrows)
        weights = VGroup()
        for input_node in input_nodes:
            arrow = Arrow(
                input_node.get_right(),
                output_node.get_left(),
                buff=0.1,
                color=YELLOW
            )
            weights.add(arrow)

        # Bias weight
        bias_weight = Arrow(
            bias_node.get_right(),
            output_node.get_left(),
            buff=0.1,
            color=GREEN
        )

        # Weight labels
        weight_labels = VGroup(
            Text("w₁", font_size=20, color=YELLOW),
            Text("w₂", font_size=20, color=YELLOW),
            Text("w₃", font_size=20, color=YELLOW),
            Text("b", font_size=20, color=GREEN)
        )

        # Position weight labels
        for i, arrow in enumerate(weights):
            weight_labels[i].next_to(arrow, UP, buff=0.1)
        weight_labels[3].next_to(bias_weight, UP, buff=0.1)

        # Activation function box
        activation_box = Rectangle(height=1.5, width=2, color=WHITE)
        activation_box.next_to(output_node, RIGHT, buff=1)
        activation_label = Text("Activation\nFunction", font_size=20)
        activation_label.move_to(activation_box.get_center())

        # Animation sequence
        self.play(Write(title_group))
        self.wait(2)
        self.play(FadeOut(title_group))

        # Show input nodes and labels
        self.play(
            *[Create(node) for node in input_nodes],
            *[Write(label) for label in input_labels]
        )
        self.wait(0.5)

        # Show bias node
        self.play(
            Create(bias_node),
            Write(bias_label)
        )
        self.wait(0.5)

        # Show output node
        self.play(
            Create(output_node),
            Write(output_label)
        )
        self.wait(0.5)

        # Show weights with sequential highlighting
        for arrow, label in zip(weights, weight_labels[:3]):
            self.play(
                GrowArrow(arrow),
                Write(label),
                run_time=0.5
            )

        # Show bias weight
        self.play(
            GrowArrow(bias_weight),
            Write(weight_labels[3])
        )
        self.wait(0.5)

        # Show activation function
        self.play(
            Create(activation_box),
            Write(activation_label)
        )
        self.wait(0.5)

        # Add explanation text at bottom
        explanation = Text(
            '"Think of it as an AI\'s decision-making muscle"',
            font_size=28,
            color=YELLOW
        ).to_edge(DOWN, buff=0.5)
        self.play(Write(explanation))
        self.wait(2)

        # Highlight the full network flow
        network_highlight = VGroup(
            input_nodes, bias_node, weights,
            bias_weight, output_node, activation_box
        )
        self.play(
            network_highlight.animate.set_color(YELLOW),
            rate_func=there_and_back,
            run_time=2
        )
        self.wait(1)

        # Optional: Add formula
        formula = MathTex(
            "output = f(\\sum_{i=1}^{3} w_i x_i + b)",
            font_size=32
        )
        formula.next_to(explanation, UP, buff=0.5)
        self.play(Write(formula))
        self.wait(2)

# To render:
# manim -pqh perceptron.py Perceptron
