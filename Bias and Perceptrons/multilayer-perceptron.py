from manim import *

class MultilayerPerceptronBias(Scene):
    def construct(self):
        # Title
        title = Text("Multi-Layer Networks: Bias Multiplication", font_size=40)
        subtitle = Text("How Deep Learning Amplifies Biases", font_size=30, color=BLUE)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.3)
        title_group.to_edge(UP, buff=0.5)

        # Create multi-layer network
        def create_layer(num_nodes, color):
            layer = VGroup(*[Circle(radius=0.2, color=color) for _ in range(num_nodes)])
            layer.arrange(DOWN, buff=0.4)
            return layer

        # Create layers with different sizes
        input_layer = create_layer(4, BLUE)
        hidden_layer1 = create_layer(5, GREEN)
        hidden_layer2 = create_layer(5, GREEN)
        output_layer = create_layer(3, RED)

        # Arrange layers horizontally - Shifted left
        layers = VGroup(input_layer, hidden_layer1, hidden_layer2, output_layer)
        layers.arrange(RIGHT, buff=2)
        layers.scale(0.8).shift(DOWN * 0.5 + LEFT * 3)  # Added LEFT * 3

        # Create connections between layers
        connections = VGroup()
        bias_connections = VGroup()

        def connect_layers(layer1, layer2, highlight_path=False):
            layer_connections = VGroup()
            for node1 in layer1:
                for node2 in layer2:
                    connection = Line(
                        node1.get_right(),
                        node2.get_left(),
                        stroke_opacity=0.3
                    )
                    if highlight_path:
                        connection.set_color(YELLOW)
                        bias_connections.add(connection)
                    else:
                        connection.set_color(GRAY)
                    layer_connections.add(connection)
            return layer_connections

        # Create all connections
        for i in range(len(layers) - 1):
            connections.add(connect_layers(layers[i], layers[i + 1]))

        # Animation sequence
        self.play(Write(title_group))
        self.wait(2)

        # Show network structure
        self.play(Create(layers))
        self.play(Create(connections), run_time=2)
        self.wait(2)

        # Label the layers
        labels = VGroup(
            Text("Input\nLayer", font_size=20).next_to(input_layer, DOWN),
            Text("Hidden\nLayers", font_size=20).next_to(hidden_layer1, DOWN),
            Text("Output", font_size=20).next_to(output_layer, DOWN)
        )
        self.play(Write(labels))

        # Highlight bias path
        bias_path = VGroup()
        for i in range(len(layers) - 1):
            bias_path.add(connect_layers(
                VGroup(layers[i][0]),
                VGroup(layers[i + 1][0]),
                highlight_path=True
            ))

        # Show bias amplification
        self.play(Create(bias_path), run_time=2)
        self.wait(2)

        # Add explanation text - Adjusted position to right side
        explanations = VGroup(
            Text("1. Initial bias in input", font_size=24, color=YELLOW),
            Text("2. Amplified through hidden layers", font_size=24, color=YELLOW),
            Text("3. Compounds in final output", font_size=24, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        explanations.to_edge(RIGHT, buff=0.5)  # Now has space on the right

        for explanation in explanations:
            self.play(Write(explanation), run_time=0.8)
        self.wait(2)


        # Show bias multiplication effect - Adjusted positions
        bias_values = VGroup(
            Text("×1.5", font_size=20, color=YELLOW).next_to(layers[0], UP),
            Text("×2.0", font_size=20, color=YELLOW).next_to(layers[1], UP),
            Text("×2.5", font_size=20, color=YELLOW).next_to(layers[2], UP),
            Text("×7.5", font_size=20, color=RED).next_to(layers[3], UP)
        )

        self.play(Write(bias_values), run_time=2)
        self.wait(2)

        # Add final impact text - Adjusted position
        impact_text = Text(
            "Small initial biases can be\nmultiplied 7.5x or more\nin deep networks",
            font_size=28,
            color=RED
        ).to_edge(RIGHT, buff=0.5).shift(DOWN * 2)  # Positioned to right side and down

        self.play(Write(impact_text))
        self.wait(2)

        # Pulse animation for emphasis
        self.play(
            bias_path.animate.set_color(RED),
            rate_func=there_and_back,
            run_time=1
        )
        self.wait(4)

        # Fade out
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=0.5
        )

# To render:
# manim -pqh multilayer_perceptron_bias.py MultilayerPerceptronBias
