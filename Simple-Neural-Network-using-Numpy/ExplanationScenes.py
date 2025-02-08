from manim import *
import numpy as np

# Helper functions for activation
def relu(x):
    return np.maximum(0, x)

def softmax(x):
    # stable softmax
    z = x - np.max(x)
    exp_z = np.exp(z)
    return exp_z / np.sum(exp_z)

def draw_circle_with_text(text_str, radius=0.3, fill_color=GRAY, fill_opacity=0.6):
    circle = Circle(radius=radius, color=WHITE, stroke_width=2,
                    fill_color=fill_color, fill_opacity=fill_opacity)
    text = Text(text_str, font_size=24)
    group = VGroup(circle, text)
    text.move_to(circle.get_center())
    return group

###############################################################################
# Revised Scene 1: Forward Propagation - With Adjusted Arrows to Prevent Overlap
###############################################################################

class ForwardPropagationScene(Scene):
    def construct(self):
        # Create Input node with label
        input_label = Text("Input", font_size=28)
        input_node = draw_circle_with_text("x")
        input_group = VGroup(input_node, input_label).arrange(DOWN, buff=0.2)
        input_group.to_edge(LEFT, buff=1)

        # Create hidden layer (for simplicity, a column of 4 nodes)
        hidden_nodes = VGroup(*[draw_circle_with_text(f"h{i+1}") for i in range(4)])
        hidden_nodes.arrange(DOWN, buff=1)
        hidden_nodes.to_edge(RIGHT, buff=4)

        # Create output node
        output_node = draw_circle_with_text("o")
        output_node.to_edge(RIGHT, buff=1)

        # Animate creation of elements
        self.play(FadeIn(input_group), FadeIn(hidden_nodes), FadeIn(output_node))
        self.wait(1)

        # Draw connections from input to hidden nodes.
        # Slightly nudge arrow endpoints upward/downward to avoid overlapping the node texts.
        arrows_input_to_hidden = VGroup()
        for node in hidden_nodes:
            # Starting point is from the right edge of input shifted slightly upward.
            start = input_node.get_right() + 0.15 * UP
            # End point is node's left edge, nudged downward.
            end = node.get_left() + 0.15 * DOWN
            arrow = Arrow(start, end, buff=0.1, color=YELLOW, stroke_width=2)
            arrows_input_to_hidden.add(arrow)
        self.play(LaggedStart(*[Create(arrow) for arrow in arrows_input_to_hidden], lag_ratio=0.3))

        # Draw connections from hidden nodes to the output node with similar offsets.
        arrows_hidden_to_output = VGroup()
        for node in hidden_nodes:
            start = node.get_right() + 0.15 * UP
            end = output_node.get_left() + 0.15 * DOWN
            arrow = Arrow(start, end, buff=0.1, color=YELLOW, stroke_width=2)
            arrows_hidden_to_output.add(arrow)
        self.play(LaggedStart(*[Create(arrow) for arrow in arrows_hidden_to_output], lag_ratio=0.2))
        self.wait(1)

        # Animate a pulse representing the forward pass.
        pulse = Dot(point=input_node.get_center(), color=YELLOW)
        self.play(FadeIn(pulse))

        # Move the pulse to each hidden node (adjusting its position to avoid text)
        for node in hidden_nodes:
            target = node.get_left() + LEFT * 0.5  # shift left from the node's left edge
            self.play(pulse.animate.move_to(target), run_time=0.5)
            # Update hidden node label with a new activation value (using ReLU as an example)
            value = np.round(relu(np.random.randn()), 2)
            new_label = Text(str(value), font_size=20)
            new_label.move_to(node.get_center())
            self.play(Transform(node[1], new_label), run_time=0.3)
            self.wait(0.2)

        # Propagate from the last hidden node to the output.
        target = output_node.get_left() + LEFT * 0.5
        self.play(pulse.animate.move_to(target), run_time=0.7)
        out_val = softmax(np.array([np.random.randn()]))
        out_text = Text(f"{np.round(out_val[0],2)}", font_size=20)
        out_text.move_to(output_node.get_center())
        self.play(Transform(output_node[1], out_text), run_time=0.5)
        self.play(FadeOut(pulse))
        self.wait(2)

###############################################################################
# Revised Scene 2: Backpropagation - With Adjusted Arrow Offsets and Label Placement
###############################################################################

from manim import *
import numpy as np

def relu(x):
    return np.maximum(0, x)

def softmax(x):
    z = x - np.max(x)
    exp_z = np.exp(z)
    return exp_z / np.sum(exp_z)

def draw_circle_with_text(text_str, radius=0.3, fill_color=GRAY, fill_opacity=0.6):
    circle = Circle(radius=radius, color=WHITE, stroke_width=2,
                    fill_color=fill_color, fill_opacity=fill_opacity)
    text = Text(text_str, font_size=24)
    group = VGroup(circle, text)
    text.move_to(circle.get_center())
    return group

class BackPropagationScene(Scene):
    def construct(self):
        # Title for the scene.
        title = Text("Backpropagation", font_size=40, color=ORANGE)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Build the same network structure.
        input_node = draw_circle_with_text("x")
        input_node.to_edge(LEFT, buff=1)

        # Create a hidden layer (4 nodes) and position them.
        hidden_nodes = VGroup(*[draw_circle_with_text(f"h{i+1}") for i in range(4)])
        hidden_nodes.arrange(DOWN, buff=1)
        hidden_nodes.to_edge(RIGHT, buff=4)

        output_node = draw_circle_with_text("o")
        output_node.to_edge(RIGHT, buff=1)

        # Create faint forward arrows (gray) to indicate the original signal flow.
        forward_arrows = VGroup()
        for node in hidden_nodes:
            start = input_node.get_right() + 0.15 * UP
            end = node.get_left() + 0.15 * DOWN
            arrow = Arrow(start, end, buff=0.1, color=GRAY, stroke_width=1)
            forward_arrows.add(arrow)
        for node in hidden_nodes:
            start = node.get_right() + 0.15 * UP
            end = output_node.get_left() + 0.15 * DOWN
            arrow = Arrow(start, end, buff=0.1, color=GRAY, stroke_width=1)
            forward_arrows.add(arrow)

        self.play(
            FadeIn(input_node),
            FadeIn(hidden_nodes),
            FadeIn(output_node),
            FadeIn(forward_arrows)
        )
        self.wait(1)

        # Display the error message at the output.
        error_text = Text("Error = (prediction - target)", font_size=15, color=RED)
        error_text.next_to(output_node, DOWN, buff=0.3)
        self.play(Write(error_text))
        self.wait(1)

        # Animate backpropagation arrow from the output back to one hidden node.
        # We choose hidden_nodes[2] as an example.
        bp_arrow1 = Arrow(
            output_node.get_left() + 0.2 * DOWN,
            hidden_nodes[2].get_right() + 0.2 * UP,
            buff=0.1, color=ORANGE, stroke_width=2
        )
        self.play(Create(bp_arrow1))
        # Compute midpoint of the arrow and apply a vertical offset so the label is centered.
        label_pos = bp_arrow1.get_center() + UP * 0.3
        dL_do = Text("dL/do", font_size=20, color=ORANGE)
        dL_do.move_to(label_pos)
        self.play(Write(dL_do))
        self.wait(1)

        # Now animate arrows from each hidden node to the input.
        for node in hidden_nodes:
            bp_arrow2 = Arrow(
                node.get_left() + LEFT * 0.2,
                input_node.get_right() + RIGHT * 0.2,
                buff=0.1, color=ORANGE, stroke_width=2
            )
            self.play(Create(bp_arrow2))
            label2_pos = bp_arrow2.get_center() + UP * 0.3
            dL_dh = Text("dL/dh", font_size=20, color=ORANGE)
            dL_dh.move_to(label2_pos)
            self.play(Write(dL_dh), run_time=0.5)
        self.wait(1)

        # Show a summary of the chain rule on screen.
        chain_rule = Text("Chain Rule: dL/dh = dL/do * do/dh", font_size=24, color=ORANGE)
        chain_rule.to_edge(DOWN)
        self.play(Write(chain_rule))
        self.wait(3)

##########################################################################################################

# Some helper functions shared by the scenes

def relu(x):
    return np.maximum(0, x)

def softmax(x):
    # a stable softmax
    z = x - np.max(x)
    exp_z = np.exp(z)
    return exp_z / np.sum(exp_z)

def draw_circle_with_text(text_str, radius=0.3, fill_color=GRAY, fill_opacity=0.6):
    circle = Circle(radius=radius, color=WHITE, stroke_width=2, fill_color=fill_color, fill_opacity=fill_opacity)
    text = Text(text_str, font_size=24)
    group = VGroup(circle, text)
    text.move_to(circle.get_center())
    return group

def draw_weight_line(start_point, end_point, weight, max_weight=1.0):
    # Normalize weight, use green for positive and red for negative
    normalized = np.clip(np.abs(weight)/max_weight, 0, 1)
    color = GREEN if weight >= 0 else RED
    line = Line(start_point, end_point, color=color, stroke_width=4*normalized, stroke_opacity=normalized)
    return line

###############################################################################
# Scene 1: Introduction - Explaining the Anatomy of a Neural Network
###############################################################################

class IntroductionScene(Scene):
    def construct(self):
        title = Text("Understanding Neural Networks", font_size=48)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        # Introduce layers
        layers = VGroup(
            Text("Input Layer", font_size=32),
            Text("Hidden Layer(s)", font_size=32),
            Text("Output Layer", font_size=32)
        ).arrange(DOWN, center=False, aligned_edge=LEFT, buff=0.5)

        layers.to_edge(LEFT)
        self.play(LaggedStart(*[FadeIn(layer, shift=RIGHT) for layer in layers]), run_time=2)

        # Explain connections
        explanation = Text(
            "Information flows forward (Forward Propagation)\n"
            "and errors are passed back (Backpropagation)\n"
            "to update the weights (Gradient Descent)",
            font_size=28,
            t2c={"Forward Propagation": YELLOW, "Backpropagation": ORANGE, "Gradient Descent": BLUE}
        )
        explanation.next_to(layers, RIGHT, buff=1)
        self.play(FadeIn(explanation, shift=UP))
        self.wait(3)


###############################################################################
# Scene 4: Weight Update - Applying gradient descent to adjust weights.
###############################################################################
from manim import *
import numpy as np

class WeightUpdateScene(Scene):
    def construct(self):
        # Title at the top-center
        title = Text("Gradient Descent Weight Update", font_size=40, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Create a random weight matrix for demonstration
        weight_matrix = np.random.randn(3, 3)
        weight_text = Text(f"w =\n{np.array2string(weight_matrix, precision=2)}", font_size=28)
        weight_box = SurroundingRectangle(weight_text, color=BLUE)
        weight_group = VGroup(weight_text, weight_box)
        # Position the weight group to the left-center so items are spread out
        weight_group.move_to(LEFT * 2)

        # Create a gradient matrix (same shape) and group it
        gradient_matrix = np.random.randn(3, 3) * 0.1
        gradient_text = Text(f"∇w =\n{np.array2string(gradient_matrix, precision=2)}", font_size=28)
        grad_box = SurroundingRectangle(gradient_text, color=YELLOW)
        grad_group = VGroup(gradient_text, grad_box)
        # Position the gradient group to the right of the weight group
        grad_group.next_to(weight_group, RIGHT, buff=1.5)

        # Create learning rate text (positioned just below the weight matrix)
        lr_text = Text("Learning Rate = 0.01", font_size=24, color=GREEN)
        lr_text.next_to(weight_group, DOWN, buff=1)

        # Create the weight update formula text below the learning rate label
        update_eq = Text("w_new = w - (learning_rate * ∇w)", font_size=24, color=BLUE)
        update_eq.next_to(lr_text, DOWN, buff=0.5)

        # Animate the appearance of weight matrix, gradient, learning rate, and update formula.
        self.play(FadeIn(weight_group), FadeIn(grad_group))
        self.play(Write(lr_text), Write(update_eq))
        self.wait(1)

        # Calculate updated weights using gradient descent formula
        new_weight_matrix = weight_matrix - 0.01 * gradient_matrix
        new_weight_text = Text(f"w_new =\n{np.array2string(new_weight_matrix, precision=2)}", font_size=28, color=BLUE)
        new_weight_box = SurroundingRectangle(new_weight_text, color=BLUE)
        new_weight_group = VGroup(new_weight_text, new_weight_box)
        # Position new weight values in the same spot as the original weight matrix.
        new_weight_group.move_to(weight_group.get_center())

        # Animate the transformation of the old weight matrix to the new weight matrix
        self.play(Transform(weight_group, new_weight_group), run_time=1.5)
        self.wait(2)

############################################################################################################
# Scene 0: Opening
############################################################################################################

from manim import *
import networkx as nx
import numpy as np

class TitleScene(Scene):
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
        title = Text("Inside Neural Network Training", color=WHITE, font='Comic Sans MS').scale(1).set_stroke(BLACK, width=1).move_to(UP * 1)
        underline = Line(LEFT, RIGHT, color=WHITE).scale(5).next_to(title, DOWN)
        #self.play(Write(title))
        #self.wait(1)
        #signature = Text('Joshua S. White, PhD').scale(.5).to_corner(DR)
        #self.play(Create(underline)) #, FadeIn(signature))

        # Create a graph with multiple nodes
        G = nx.Graph()
        G.add_edges_from([(0, 1), (1, 2), (1, 6), (0, 7), (7, 8), (4, 5), (5, 0), (0, 2), (3, 5)])

        # Get positions using spring layout
        positions = nx.spring_layout(G)

        # Convert positions to the format MANIM understands
        manim_positions = {node: np.array([x, y, 0]) for node, (x, y) in positions.items()}

        # Define labels for nodes (optional)
        labels = {i: str(i) for i in G.nodes}

        # Create a Graph in MANIM
        graph = Graph(
            list(G.nodes),
            list(G.edges),
            layout=manim_positions,
            #labels=labels,
            vertex_config={"radius": 0.10, "color": WHITE},
            edge_config={"stroke_width": 2, "color": GREY},
        )

        # Position the graph in the bottom-left corner
        graph.move_to(UP * -1)

        # Add the graph to the scene
        self.play(Create(graph))

        # Animate slight movement of the nodes
        for _ in range(5):  # Repeat a few times for dynamic effect
            new_positions = {
                node: graph.vertices[node].get_center() + np.random.uniform(-0.05, 0.05, size=3)
                for node in manim_positions
            }
            self.play(
                graph.animate.change_layout(new_positions, layout_scale=1),
                run_time=0.1,  # Slower animation for smoother transitions
                rate_func=smooth  # Use a smooth rate function
            )

        # Transform the graph into the name "Joshua S. White"
        name_text = Text("Joshua S. White, PhD", color=WHITE, font='Comic Sans MS').scale(.5).to_corner(DR)

        self.play(Write(title))
        self.wait(1)
        self.play(Create(underline))
        self.wait(1)
        self.play(Transform(underline, name_text))

        # Hold the graph in its final state
        self.wait(4)

        #self.play(FadeOut(title), FadeOut(underline), FadeOut(signature), FadeOut(graph))

        # Fade the entire scene to black
        fade_to_black = Rectangle(
            width=config.frame_width,
            height=config.frame_height,
            fill_color=BLACK,
            fill_opacity=1,
        ).set_z_index(1)  # Ensure it covers everything

        self.play(FadeIn(fade_to_black, run_time=3))


###############################################################################
# Closing Scene
###############################################################################

from manim import *

class ClosingScene(Scene):
    def construct(self):
        # Title at the top
        title = Text("Neural Network Training: Final Review", font_size=40, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Create bullet points manually by instantiating individual Text objects
        bullet1 = Text("• Forward Propagation: Data flows from input to output", font_size=28)
        bullet2 = Text("• Backpropagation: Gradients are computed backwards", font_size=28)
        bullet3 = Text("• Weight Updates: Gradient descent refines the model", font_size=28)

        # Group and arrange the bullet points vertically
        bullets = VGroup(bullet1, bullet2, bullet3)
        bullets.arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        bullets.to_edge(LEFT, buff=2.25)
        self.play(FadeIn(bullets, shift=RIGHT))
        self.wait(4)

        # Concluding statement below the bullet points
        conclusion_text = Text("Visualizing neural networks demystifies complex concepts.",
                               font_size=28, color=WHITE)
        conclusion_text.next_to(bullets, DOWN, buff=.5)
        self.play(Write(conclusion_text))
        self.wait(2)

        # Thank you note at the bottom
        thank_you = Text("Thank you for watching!", font_size=36, color=GREEN)
        thank_you.to_edge(DOWN)
        self.play(FadeIn(thank_you, shift=UP))
        self.wait(3)

        # Fade out all elements to conclude the scene
        self.play(FadeOut(VGroup(title, bullets, conclusion_text, thank_you)))
