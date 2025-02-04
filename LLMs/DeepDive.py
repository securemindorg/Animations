from manim import *
import numpy as np

##############################
# Scene 1: Introduction
##############################
class Intro(Scene):
    def construct(self):
        title = Text("Inside a Large Language Model", font_size=48)
        subtitle = Text("From Tokenization to Text Generation", font_size=36)
        title.to_edge(UP)
        subtitle.next_to(title, DOWN)
        self.play(Write(title))
        self.wait(1)
        self.play(Write(subtitle))
        self.wait(2)
        self.play(FadeOut(VGroup(title, subtitle)))


##############################
# Scene 2: Tokenization Visualization
##############################
class TokenizationScene(Scene):
    def construct(self):
        # Display the input text.
        input_text = Text("Hello, how are you?", font_size=42)
        input_text.to_edge(UP)
        self.play(Write(input_text))
        self.wait(1)

        # Convert the input into tokens.
        token_list = ["Hello", ",", "how", "are", "you", "?"]
        tokens = VGroup(*[Text(token, font_size=36) for token in token_list])
        tokens.arrange(RIGHT, buff=0.5).next_to(input_text, DOWN, buff=1)

        # Animate the transformation from sentence to tokens.
        self.play(ReplacementTransform(input_text.copy(), tokens))
        self.wait(2)

        # Optionally, draw a box around each token.
        for token in tokens:
            rect = SurroundingRectangle(token, color=YELLOW)
            self.play(Create(rect), run_time=0.3)
            self.wait(0.2)
        self.wait(2)
        self.play(FadeOut(Group(tokens, *self.mobjects)))


##############################
# Scene 3: Embedding (Encoding) Stage
##############################
class EmbeddingScene(Scene):
    def construct(self):
        # List of tokens and create token mobjects.
        token_list = ["Hello", ",", "how", "are", "you", "?"]
        tokens = VGroup(*[Text(token, font_size=36) for token in token_list])
        tokens.arrange(RIGHT, buff=0.5)
        # Position tokens near the upper left of the screen.
        tokens.to_edge(LEFT, buff=1).shift(UP * 1.5)
        self.play(Write(tokens))
        self.wait(1)

        # Create embedding circles corresponding to each token.
        embeddings = VGroup(*[Circle(radius=0.5, color=BLUE) for _ in token_list])
        embeddings.arrange(RIGHT, buff=1)
        # Position embeddings near the lower right of the screen.
        embeddings.to_edge(RIGHT, buff=1).shift(DOWN * 1.5)

        # Draw arrows from each token to its corresponding embedding.
        for i, token in enumerate(tokens):
            arrow = Arrow(token.get_right(), embeddings[i].get_left(), buff=0.1, stroke_width=2, color=YELLOW)
            self.play(Create(arrow), run_time=0.5)
        self.wait(1)

        # Label each embedding circle with an "E".
        for emb in embeddings:
            label = Text("E", font_size=24).move_to(emb.get_center())
            self.play(Write(label), run_time=0.3)
        self.wait(2)

        self.play(FadeOut(Group(tokens, embeddings, *self.mobjects)))


##############################
# Scene 4: Multi-Layer Perceptron (MLP) Visualization
##############################
class MLPScene(Scene):
    def construct(self):
        # Input layer: 4 neurons.
        input_neurons = VGroup(*[Dot(color=WHITE) for _ in range(4)])
        input_neurons.arrange(DOWN, buff=0.6).to_edge(LEFT, buff=1)

        # Hidden layer: 3 neurons.
        hidden_neurons = VGroup(*[Dot(color=WHITE) for _ in range(3)])
        hidden_neurons.arrange(DOWN, buff=0.6).shift(RIGHT * 2)

        # Output layer: 1 neuron.
        output_neuron = Dot(color=WHITE)
        output_neuron.next_to(hidden_neurons, RIGHT, buff=1.5)

        # Label layers.
        input_label = Text("Input", font_size=24).next_to(input_neurons, UP)
        hidden_label = Text("Hidden", font_size=24).next_to(hidden_neurons, UP)
        output_label = Text("Output", font_size=24).next_to(output_neuron, UP)

        self.play(Write(input_neurons), Write(hidden_neurons), Write(output_neuron))
        self.play(Write(input_label), Write(hidden_label), Write(output_label))
        self.wait(1)

        # Fully connect input to hidden.
        for inp in input_neurons:
            for hid in hidden_neurons:
                arrow = Arrow(inp.get_right(), hid.get_left(), buff=0.1, stroke_width=2, color=YELLOW)
                self.play(Create(arrow), run_time=0.3)
        self.wait(1)

        # Fully connect hidden to output.
        for hid in hidden_neurons:
            arrow = Arrow(hid.get_right(), output_neuron.get_left(), buff=0.1, stroke_width=2, color=YELLOW)
            self.play(Create(arrow), run_time=0.3)
        self.wait(2)

        self.play(FadeOut(Group(input_neurons, hidden_neurons, output_neuron,
                                  input_label, hidden_label, output_label, *self.mobjects)))


##############################
# Scene 5: Other Model Components – Positional Encoding & Self-Attention
##############################
class AdvancedComponentsScene(Scene):
    def construct(self):
        # Positional Encoding Visualization.
        pos_title = Text("Positional Encoding", font_size=36).to_edge(UP)
        self.play(Write(pos_title))
        token_list = ["Token1", "Token2", "Token3"]
        tokens = VGroup(*[Text(token, font_size=32) for token in token_list])
        tokens.arrange(RIGHT, buff=1).shift(UP * 0.5)
        self.play(Write(tokens))
        positions = VGroup(*[Text(f"Pos {i+1}", font_size=24) for i in range(len(token_list))])
        positions.arrange(RIGHT, buff=1).next_to(tokens, DOWN, buff=0.3)
        self.play(Write(positions))
        self.wait(2)
        self.play(FadeOut(Group(pos_title, tokens, positions)))

        # Self-Attention Mechanism (simplified).
        attn_title = Text("Self-Attention Mechanism", font_size=36).to_edge(UP)
        self.play(Write(attn_title))
        attn_tokens = VGroup(*[Text(token, font_size=28) for token in ["The", "cat", "sat", "on", "the", "mat"]])
        attn_tokens.arrange(RIGHT, buff=0.5).to_edge(DOWN)
        self.play(Write(attn_tokens))
        self.wait(1)
        # Draw arrows from each token to every other token.
        for i in range(len(attn_tokens)):
            for j in range(len(attn_tokens)):
                if i != j:
                    arrow = Arrow(attn_tokens[i].get_top(), attn_tokens[j].get_top(), buff=0.1, stroke_width=1, color=GREEN)
                    self.play(Create(arrow), run_time=0.2)
        self.wait(2)
        self.play(FadeOut(Group(attn_title, attn_tokens, *self.mobjects)))


##############################
# Scene 6: Querying and Text Generation
##############################
class QueryingScene(Scene):
    def construct(self):
        # Show the user’s query input.
        query_text = Text("User Query: What's the weather like?", font_size=36)
        query_text.to_edge(UP)
        self.play(Write(query_text))
        self.wait(2)

        # Represent the query inside a prompt box.
        prompt_box = RoundedRectangle(width=8, height=2, corner_radius=0.2, fill_color=BLUE, fill_opacity=0.2)
        prompt_box.next_to(query_text, DOWN, buff=0.5)
        prompt_content = Text("What's the weather like?", font_size=32)
        prompt_content.move_to(prompt_box.get_center())
        self.play(Create(prompt_box), Write(prompt_content))
        self.wait(2)

        # Animate text generation by sequentially adding tokens.
        generated_title = Text("Generating Response...", font_size=36).next_to(prompt_box, DOWN, buff=1)
        self.play(Write(generated_title))
        self.wait(1)

        generated_tokens = ["It's", "sunny", "and", "warm", "today", "."]
        generated_text = VGroup()
        for i, token in enumerate(generated_tokens):
            new_token = Text(token, font_size=36)
            new_token.next_to(prompt_box, DOWN, buff=2).shift(RIGHT * (i * 1.5))
            generated_text.add(new_token)
            self.play(Write(new_token), run_time=0.5)
            self.wait(0.3)
        self.wait(2)
        self.play(FadeOut(Group(query_text, prompt_box, prompt_content, generated_title, generated_text)))


class AdvancedComponentsScene(Scene):
    def construct(self):
        # --- Part 1: Positional Encoding Visualization ---
        pos_title = Text("Positional Encoding", font_size=36).to_edge(UP)
        self.play(Write(pos_title))
        token_list = ["Token1", "Token2", "Token3"]
        tokens = VGroup(*[Text(token, font_size=32) for token in token_list])
        tokens.arrange(RIGHT, buff=1.2).shift(UP * 0.5)
        self.play(Write(tokens))
        positions = VGroup(*[Text(f"Pos {i+1}", font_size=24) for i in range(len(token_list))])
        positions.arrange(RIGHT, buff=1.2).next_to(tokens, DOWN, buff=0.5)
        self.play(Write(positions))
        self.wait(2)
        self.play(FadeOut(Group(pos_title, tokens, positions)))

        # --- Part 2: Self-Attention Mechanism Visualization ---
        attn_title = Text("Self-Attention Mechanism", font_size=36).to_edge(UP)
        self.play(Write(attn_title))
        attn_tokens = VGroup(*[Text(token, font_size=28) for token in ["The", "cat", "sat", "on", "the", "mat"]])
        attn_tokens.arrange(RIGHT, buff=1.5).to_edge(buff=1)
        self.play(Write(attn_tokens))
        self.wait(1)

        # Draw arrows from each token to every other token.
        arrows = []
        for i, token_i in enumerate(attn_tokens):
            for j, token_j in enumerate(attn_tokens):
                if i != j:
                    # Offset the starting and ending points upward slightly
                    start_point = token_i.get_top() + UP * 0.2
                    end_point = token_j.get_top() + UP * 0.2
                    # Use a positive arc if token_j is to the right of token_i,
                    # and a negative arc if it is to the left.
                    arc = 0.3 if j > i else -0.3
                    arrow = Arrow(
                        start_point,
                        end_point,
                        buff=0.1,
                        stroke_width=1,
                        color=GREEN,
                        path_arc=arc
                    )
                    arrows.append(arrow)
        arrows_group = VGroup(*arrows)
        self.play(Create(arrows_group), run_time=2)
        self.wait(2)
        self.play(FadeOut(Group(attn_title, attn_tokens, arrows_group)))

#############################
class MLPForwardPassScene(Scene):
    def construct(self):
        # --- LAYER SETUP ---
        # Input layer: Create 3 neurons and label them with input values.
        input_labels = ["x₁", "x₂", "x₃"]
        input_neurons = VGroup(*[
            Circle(radius=0.3, color=WHITE) for _ in input_labels
        ])
        for i, neuron in enumerate(input_neurons):
            label = Text(input_labels[i], font_size=24).move_to(neuron.get_center())
            neuron.add(label)
        input_neurons.arrange(DOWN, buff=0.8).to_edge(LEFT, buff=1)
        input_layer_label = Text("Input Layer", font_size=28).next_to(input_neurons, UP)

        # Hidden layer: Create 3 neurons and label them with h (for hidden).
        hidden_neurons = VGroup(*[
            Circle(radius=0.3, color=WHITE) for _ in range(3)
        ])
        for j, neuron in enumerate(hidden_neurons):
            label = Text(f"h{j+1}", font_size=24).move_to(neuron.get_center())
            neuron.add(label)
        hidden_neurons.arrange(DOWN, buff=0.8).move_to(RIGHT * 0.5)
        hidden_layer_label = Text("Hidden Layer", font_size=28).next_to(hidden_neurons, UP)

        # Output layer: Create 1 neuron and label it.
        output_neuron = Circle(radius=0.3, color=WHITE)
        output_neuron.move_to(RIGHT * 3)
        output_label = Text("y", font_size=24).move_to(output_neuron.get_center())
        output_neuron.add(output_label)
        output_layer_label = Text("Output Layer", font_size=28).next_to(output_neuron, UP)

        # --- DRAW THE DIAGRAM ---
        self.play(Write(input_layer_label), Write(hidden_layer_label), Write(output_layer_label))
        self.play(Create(input_neurons), Create(hidden_neurons), Create(output_neuron))
        self.wait(1)

        # Draw arrows connecting input to hidden neurons.
        input_to_hidden_arrows = VGroup()
        for inp in input_neurons:
            for hid in hidden_neurons:
                arrow = Arrow(start=inp.get_right(),
                              end=hid.get_left(),
                              buff=0.1,
                              stroke_width=2,
                              color=YELLOW)
                input_to_hidden_arrows.add(arrow)
        self.play(Create(input_to_hidden_arrows))
        self.wait(1)

        # --- ANIMATE DATA FLOW: Input -> Hidden ---
        # For each input neuron, animate a small red dot traveling to the first hidden neuron.
        for inp in input_neurons:
            dot = Dot(color=RED, radius=0.1)
            dot.move_to(inp.get_center())
            self.play(FadeIn(dot), run_time=0.3)
            # Target: first hidden neuron (for illustration purposes)
            target_hidden = hidden_neurons[0]
            self.play(dot.animate.move_to(target_hidden.get_center()), run_time=0.5)
            self.wait(0.3)
            self.play(FadeOut(dot), run_time=0.2)
        self.wait(1)

        # Draw arrows connecting hidden neurons to the output neuron.
        hidden_to_output_arrows = VGroup()
        for hid in hidden_neurons:
            arrow = Arrow(start=hid.get_right(),
                          end=output_neuron.get_left(),
                          buff=0.1,
                          stroke_width=2,
                          color=YELLOW)
            hidden_to_output_arrows.add(arrow)
        self.play(Create(hidden_to_output_arrows))
        self.wait(1)

        # --- ANIMATE DATA FLOW: Hidden -> Output ---
        # For each hidden neuron, animate a small orange dot traveling to the output neuron.
        for hid in hidden_neurons:
            dot = Dot(color=ORANGE, radius=0.1)
            dot.move_to(hid.get_center())
            self.play(FadeIn(dot), run_time=0.3)
            self.play(dot.animate.move_to(output_neuron.get_center()), run_time=0.5)
            self.wait(0.3)
            self.play(FadeOut(dot), run_time=0.2)
        self.wait(1)

        # --- EXPLANATORY TEXT ---
        explanation = Text(
            "Each layer computes a weighted sum, applies a non-linear activation, and passes the result forward.",
            font_size=24
        )
        explanation.to_edge(DOWN)
        self.play(FadeIn(explanation))
        self.wait(3)

        # Fade everything out.
        self.play(FadeOut(Group(
            input_layer_label, hidden_layer_label, output_layer_label,
            input_neurons, hidden_neurons, output_neuron,
            input_to_hidden_arrows, hidden_to_output_arrows, explanation
        )))


#################################################
# Scene 1: Multi-Head Self-Attention Visualization
#################################################
class MultiHeadAttentionScene(Scene):
    def construct(self):
        # Title
        title = Text("Multi-Head Self-Attention", font_size=36).to_edge(UP)
        self.play(Write(title))

        # Create a row of tokens (inputs).
        tokens = VGroup(*[Text(token, font_size=28) for token in ["The", "quick", "brown", "fox"]])
        tokens.arrange(RIGHT, buff=0.8).to_edge(LEFT, buff=1)
        self.play(Write(tokens))

        # Create multiple attention head boxes.
        num_heads = 3
        head_boxes = VGroup()
        for i in range(num_heads):
            box = RoundedRectangle(corner_radius=0.2, width=2, height=1, color=BLUE)
            label = Text(f"Head {i+1}", font_size=24).move_to(box.get_center())
            head_boxes.add(VGroup(box, label))
        head_boxes.arrange(RIGHT, buff=1).to_edge(RIGHT, buff=1)
        self.play(Create(head_boxes))

        # Animate arrows from each token to each head.
        arrows = VGroup()
        for token in tokens:
            for head in head_boxes:
                arrow = Arrow(start=token.get_right(),
                              end=head.get_left(),
                              buff=0.1,
                              stroke_width=2,
                              color=YELLOW)
                arrows.add(arrow)
        self.play(Create(arrows), run_time=2)

        # Combine outputs from heads.
        combined_box = RoundedRectangle(corner_radius=0.2, width=3, height=1, color=GREEN)
        combined_text = Text("Combined Output", font_size=24).move_to(combined_box.get_center())
        combined_output = VGroup(combined_box, combined_text)
        combined_output.next_to(head_boxes, DOWN, buff=1)
        self.play(Create(combined_output))

        # Animate arrows from each head to the combined output.
        arrows_to_combined = VGroup()
        for head in head_boxes:
            arrow = Arrow(start=head.get_bottom(),
                          end=combined_output.get_top(),
                          buff=0.1,
                          stroke_width=2,
                          color=YELLOW)
            arrows_to_combined.add(arrow)
        self.play(Create(arrows_to_combined), run_time=2)

        self.wait(2)
        self.play(FadeOut(Group(title, tokens, head_boxes, arrows, combined_output, arrows_to_combined)))


#################################################
# Scene 2: Softmax and Token Sampling Visualization
#################################################
class SoftmaxTokenSamplingScene(Scene):
    def construct(self):
        # Title
        title = Text("Softmax and Token Sampling", font_size=36).to_edge(UP)
        self.play(Write(title))

        # Define tokens and example logits.
        token_names = ["Token A", "Token B", "Token C", "Token D", "Token E"]
        logits = [3.0, 1.0, 2.5, 0.5, 1.5]

        # Create token labels at the bottom.
        token_texts = VGroup(*[Text(token, font_size=24) for token in token_names])
        token_texts.arrange(RIGHT, buff=0.8).to_edge(DOWN)
        self.play(Write(token_texts))

        # Create bars representing the logits.
        bars = VGroup()
        for logit in logits:
            # Scale logit values to a bar height (0.5 factor).
            bar = Rectangle(width=0.6, height=logit * 0.5, fill_color=BLUE, fill_opacity=0.6, color=BLUE)
            bars.add(bar)
        bars.arrange(RIGHT, buff=0.8).next_to(token_texts, UP, buff=0.5)
        self.play(Create(bars))

        # Label the logits.
        logits_label = Text("Logits", font_size=24).next_to(bars, UP)
        self.play(Write(logits_label))
        self.wait(1)

        # Animate the softmax transformation.
        softmax_label = Text("Softmax → Probabilities", font_size=24).next_to(logits_label, UP, buff=0.5)
        self.play(Write(softmax_label))

        # Compute the softmax values.
        logits_np = np.array(logits)
        exps = np.exp(logits_np)
        softmax = exps / np.sum(exps)

        # Create new bars for the probability distribution (scaled for visibility).
        prob_bars = VGroup()
        for prob in softmax:
            bar = Rectangle(width=0.6, height=prob * 4, fill_color=ORANGE, fill_opacity=0.6, color=ORANGE)
            prob_bars.add(bar)
        prob_bars.arrange(RIGHT, buff=0.8).next_to(token_texts, UP, buff=0.5)
        self.play(ReplacementTransform(bars, prob_bars), run_time=2)
        self.wait(1)

        # Highlight the token with the highest probability.
        max_index = int(np.argmax(softmax))
        highlight_box = SurroundingRectangle(token_texts[max_index], color=GREEN, buff=0.1)
        self.play(Create(highlight_box))

        sample_text = Text(f"Sampled: {token_names[max_index]}", font_size=24).next_to(highlight_box, UP)
        self.play(Write(sample_text))
        self.wait(2)

        self.play(FadeOut(Group(title, token_texts, prob_bars, logits_label, softmax_label, highlight_box, sample_text)))


#################################################
# Scene 3: Transformer Block Components
#################################################
# Custom DashedArrow class: creates a dashed line with an arrow tip.
class DashedArrow(VGroup):
    def __init__(self, start, end, color=RED, dash_length=0.2, **kwargs):
        super().__init__(**kwargs)
        # Create a dashed line from start to end.
        dashed_line = DashedLine(start, end, dash_length=dash_length, color=color)
        # Create an arrow tip.
        arrow_tip = Triangle(fill_color=color, fill_opacity=1, stroke_color=color)
        arrow_tip.scale(0.2)
        # Compute the angle for the arrow tip from start to end.
        angle = Line(start, end).get_angle()
        arrow_tip.rotate(angle)
        # Position the arrow tip at the end point.
        arrow_tip.move_to(end)
        self.add(dashed_line, arrow_tip)

#####################################
# Scene 3: Transformer Block Components
#####################################
class TransformerComponentsScene(Scene):
    def construct(self):
        # Title
        title = Text("Transformer Block Components", font_size=36).to_edge(UP)
        self.play(Write(title))

        # Draw the Input module.
        input_box = RoundedRectangle(corner_radius=0.2, width=3, height=1, color=WHITE)
        input_text = Text("Input", font_size=24).move_to(input_box.get_center())
        input_module = VGroup(input_box, input_text)
        input_module.to_edge(LEFT, buff=1)
        self.play(Create(input_module))

        # Draw the Self-Attention module.
        attn_box = RoundedRectangle(corner_radius=0.2, width=3, height=1, color=BLUE)
        attn_text = Text("Self-Attention", font_size=24).move_to(attn_box.get_center())
        attn_module = VGroup(attn_box, attn_text)
        attn_module.next_to(input_module, RIGHT, buff=1.5)
        self.play(Create(attn_module))

        # Draw the Feed-Forward module.
        ff_box = RoundedRectangle(corner_radius=0.2, width=3, height=1, color=BLUE)
        ff_text = Text("Feed-Forward", font_size=24).move_to(ff_box.get_center())
        ff_module = VGroup(ff_box, ff_text)
        ff_module.next_to(attn_module, RIGHT, buff=1.5)
        self.play(Create(ff_module))

        # Draw the Output module.
        output_box = RoundedRectangle(corner_radius=0.2, width=3, height=1, color=GREEN)
        output_text = Text("Output", font_size=24).move_to(output_box.get_center())
        output_module = VGroup(output_box, output_text)
        output_module.next_to(ff_module, RIGHT, buff=1.5)
        self.play(Create(output_module))

        # Draw arrows for the main forward pass.
        arrow1 = Arrow(start=input_module.get_right(), end=attn_module.get_left(), buff=0.1, color=YELLOW)
        arrow2 = Arrow(start=attn_module.get_right(), end=ff_module.get_left(), buff=0.1, color=YELLOW)
        arrow3 = Arrow(start=ff_module.get_right(), end=output_module.get_left(), buff=0.1, color=YELLOW)
        self.play(Create(arrow1), Create(arrow2), Create(arrow3))

        # Draw a residual (skip) connection using our custom DashedArrow.
        res_arrow = DashedArrow(start=input_module.get_right(), end=ff_module.get_right(), color=RED, dash_length=0.15)
        self.play(Create(res_arrow))

        # Annotate the application of layer normalization.
        ln_text = Text("Layer Norm", font_size=20, color=PURPLE).next_to(ff_module, DOWN, buff=0.3)
        self.play(Write(ln_text))
        self.wait(2)

        # Fade everything out.
        self.play(FadeOut(Group(title, input_module, attn_module, ff_module,
                                  output_module, arrow1, arrow2, arrow3, res_arrow, ln_text)))

#################################################
# Scene 4: Training Dynamics and Backpropagation
#################################################
class TrainingDynamicsScene(Scene):
    def construct(self):
        # Title
        title = Text("Training Dynamics & Backpropagation", font_size=36).to_edge(UP)
        self.play(Write(title))

        # Create modules representing forward pass: Input → Hidden → Output → Loss.
        input_box = RoundedRectangle(corner_radius=0.2, width=2, height=1, color=WHITE)
        input_text = Text("Input", font_size=24).move_to(input_box.get_center())
        input_module = VGroup(input_box, input_text).to_edge(LEFT, buff=1)

        hidden_box = RoundedRectangle(corner_radius=0.2, width=2, height=1, color=BLUE)
        hidden_text = Text("Hidden", font_size=24).move_to(hidden_box.get_center())
        hidden_module = VGroup(hidden_box, hidden_text).next_to(input_module, RIGHT, buff=1)

        output_box = RoundedRectangle(corner_radius=0.2, width=2, height=1, color=GREEN)
        output_text = Text("Output", font_size=24).move_to(output_box.get_center())
        output_module = VGroup(output_box, output_text).next_to(hidden_module, RIGHT, buff=1)

        loss_text = Text("Loss", font_size=24, color=RED).next_to(output_module, RIGHT, buff=1)
        self.play(Create(input_module), Create(hidden_module), Create(output_module), Write(loss_text))

        # Draw forward arrows.
        fwd_arrow1 = Arrow(input_module.get_right(), hidden_module.get_left(), buff=0.1, color=YELLOW)
        fwd_arrow2 = Arrow(hidden_module.get_right(), output_module.get_left(), buff=0.1, color=YELLOW)
        fwd_arrow3 = Arrow(output_module.get_right(), loss_text.get_left(), buff=0.1, color=YELLOW)
        self.play(Create(fwd_arrow1), Create(fwd_arrow2), Create(fwd_arrow3))
        self.wait(1)

        # Animate gradient arrows (backpropagation).
        grad_arrow1 = Arrow(loss_text.get_left(), output_module.get_right(), buff=0.1, color=PURPLE)
        grad_arrow2 = Arrow(output_module.get_left(), hidden_module.get_right(), buff=0.1, color=PURPLE)
        grad_arrow3 = Arrow(hidden_module.get_left(), input_module.get_right(), buff=0.1, color=PURPLE)
        self.play(Create(grad_arrow1), Create(grad_arrow2), Create(grad_arrow3), run_time=2)

        # Annotate with "Gradient Descent".
        gd_text = Text("Gradient Descent", font_size=24, color=PURPLE).next_to(grad_arrow2, UP)
        self.play(Write(gd_text))
        self.wait(2)

        self.play(FadeOut(Group(title, input_module, hidden_module, output_module, loss_text,
                                  fwd_arrow1, fwd_arrow2, fwd_arrow3,
                                  grad_arrow1, grad_arrow2, grad_arrow3, gd_text)))


#################################################
# Scene 5: Comparative Tokenization Methods
#################################################
class TokenizationComparativeScene(Scene):
    def construct(self):
        # Title and sample text.
        title = Text("Comparative Tokenization Methods", font_size=36).to_edge(UP)
        self.play(Write(title))

        sample_text = Text("unbelievable!", font_size=32).to_edge(UP, buff=1.5)
        self.play(Write(sample_text))

        # Column 1: Word-level tokenization.
        word_tokens = VGroup(*[Text("unbelievable!", font_size=28)])
        word_title = Text("Word-level", font_size=24)
        word_group = VGroup(word_title, word_tokens).arrange(DOWN, buff=0.5)
        word_group.to_edge(LEFT, buff=1)

        # Column 2: Subword-level tokenization.
        subword_tokens = VGroup(
            Text("un", font_size=28),
            Text("believable", font_size=28),
            Text("!", font_size=28)
        )
        subword_title = Text("Subword-level", font_size=24)
        subword_group = VGroup(subword_title, subword_tokens).arrange(DOWN, buff=0.5)
        subword_group.move_to(ORIGIN)

        # Column 3: Character-level tokenization.
        char_tokens = VGroup(*[Text(char, font_size=28) for char in list("unbelievable!")])
        char_title = Text("Character-level", font_size=24)
        char_group = VGroup(char_title, char_tokens).arrange(DOWN, buff=0.5)
        char_group.to_edge(RIGHT, buff=1)

        # Arrange columns horizontally.
        columns = VGroup(word_group, subword_group, char_group)
        columns.arrange(RIGHT, buff=1.5, aligned_edge=UP)
        self.play(Write(word_group), Write(subword_group), Write(char_group))
        self.wait(2)

        self.play(FadeOut(Group(title, sample_text, columns)))
