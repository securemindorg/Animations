from manim import *

class TransformerArchitecture(Scene):
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
        title = Text("Transformer Architecture", font_size=30)
        title.to_edge(UP)
        self.play(Write(title))

        # Create basic transformer block structure
        def create_block(label, color=BLUE):
            block = Rectangle(height=0.8, width=2, color=color)  # Reduced height
            text = Text(label, font_size=20).move_to(block.get_center())
            return VGroup(block, text)

        # Start higher on the screen
        input_text = Text("Input Text", font_size=20)
        input_text.next_to(title, DOWN, buff=1)  # Reduced buffer

        # Reduced vertical spacing between components
        embedding = create_block("Embedding", YELLOW)
        embedding.next_to(input_text, DOWN, buff=0.5)  # Reduced buffer

        # Create multiple attention heads with reduced size
        attention_heads = VGroup()
        for i in range(3):
            head = create_block(f"Attention\nHead {i+1}", BLUE)
            attention_heads.add(head)
        attention_heads.arrange(RIGHT, buff=0.3)  # Reduced buffer
        attention_heads.next_to(embedding, DOWN, buff=0.5)  # Reduced buffer

        # Feed Forward and Layer Norm
        feed_forward = create_block("Feed Forward", GREEN)
        feed_forward.next_to(attention_heads, DOWN, buff=0.5)  # Reduced buffer

        layer_norm = create_block("Layer Norm", RED)
        layer_norm.next_to(feed_forward, DOWN, buff=0.25)  # Reduced buffer

        # Output
        output = Text("Output", font_size=20)
        output.next_to(layer_norm, DOWN, buff=0.25)  # Reduced buffer

        # Create a container for the entire diagram
        diagram = VGroup(
            input_text, embedding, attention_heads,
            feed_forward, layer_norm, output
        )

        # Center the entire diagram vertically
        diagram.move_to(ORIGIN)

        # Arrows connecting components
        arrows = VGroup()
        arrows.add(Arrow(input_text.get_bottom(), embedding.get_top()))
        arrows.add(Arrow(embedding.get_bottom(), attention_heads.get_top()))
        arrows.add(Arrow(attention_heads.get_bottom(), feed_forward.get_top()))
        arrows.add(Arrow(feed_forward.get_bottom(), layer_norm.get_top()))
        arrows.add(Arrow(layer_norm.get_bottom(), output.get_top()))

        # Animation sequence
        self.play(Write(input_text))
        self.wait(1)

        # Embed animation
        self.play(
            Create(embedding),
            Create(arrows[0])
        )
        self.wait(1)

        # Attention mechanism animation
        self.play(
            Create(attention_heads),
            Create(arrows[1])
        )

        # Animated highlight for attention process
        attention_highlight = Rectangle(
            height=attention_heads.height + 0.4,
            width=attention_heads.width + 0.4,
            color=YELLOW
        ).move_to(attention_heads)
        self.play(Create(attention_highlight))
        self.play(FadeOut(attention_highlight))
        self.wait(1)

        # Feed forward and normalization
        self.play(
            Create(feed_forward),
            Create(arrows[2])
        )
        self.play(
            Create(layer_norm),
            Create(arrows[3])
        )
        self.wait(1)

        # Output animation
        self.play(
            Write(output),
            Create(arrows[4])
        )
        self.wait(2)

        # Optional: Add a pulsing effect to show data flow
        self.play(
            *[
                Succession(
                    arrow.animate.set_color(YELLOW),
                    arrow.animate.set_color(WHITE)
                )
                for arrow in arrows
            ],
            run_time=2
        )
        self.wait(2)


class AttentionMechanism(Scene):
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
        title = Text("Self-Attention Mechanism", font_size=40)
        title.to_edge(UP)
        self.play(Write(title))

        # Create token representations
        def create_token(text, position):
            token = Rectangle(height=0.5, width=1)
            label = Text(text, font_size=30).move_to(token.get_center())
            token_group = VGroup(token, label)
            token_group.move_to(position)
            return token_group

        # Create input tokens
        tokens = VGroup()
        input_text = ["The", "cat", "sat"]
        for i, word in enumerate(input_text):
            token = create_token(word, [i*2 - 2, 2, 0])
            tokens.add(token)

        # Create attention weights
        weights = VGroup()
        for i in range(len(input_text)):
            for j in range(len(input_text)):
                weight = Line(
                    tokens[i].get_bottom(),
                    tokens[j].get_top(),
                    stroke_opacity=0.5
                )
                weights.add(weight)

        # Animation
        self.play(Create(tokens))
        self.wait(4)

        # Animate attention weights
        self.play(Create(weights))

        # Highlight attention pattern
        for i in range(len(input_text)):
            highlight = VGroup()
            for j in range(len(input_text)):
                weight = weights[i*len(input_text) + j].copy()
                weight.set_color(YELLOW)
                highlight.add(weight)
            self.play(
                Create(highlight),
                run_time=4
            )
            self.play(
                FadeOut(highlight),
                run_time=4
            )

        self.wait(4)

        # Fade out everything for transition
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

class PositionalEncoding(Scene):
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
        title = Text("Positional Encoding", font_size=40)
        title.to_edge(UP)
        self.play(Write(title))

        # Create a sine wave visualization
        axes = Axes(
            x_range=[0, 10],
            y_range=[-1, 1],
            axis_config={"color": BLUE},
        )

        # Different frequency sine waves
        sin_graph1 = axes.plot(lambda x: np.sin(x), color=BLUE)
        sin_graph2 = axes.plot(lambda x: np.sin(2*x), color=RED)
        sin_graph3 = axes.plot(lambda x: np.sin(4*x), color=GREEN)

        # Labels
        labels = VGroup(
            Text("Position", font_size=20).next_to(axes.x_axis, DOWN),
            Text("Value", font_size=20).next_to(axes.y_axis, LEFT)
        )

        # Animation
        self.play(Create(axes), Write(labels))
        self.wait(4)
        self.play(Create(sin_graph1))
        self.wait(4)
        self.play(Create(sin_graph2))
        self.wait(4)
        self.play(Create(sin_graph3))
        self.wait(2)

        # Final pause
        self.wait(2)

        # Fade out everything for transition
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

# To render:
# manim -pqh transformer_architecture.py TransformerArchitecture
# manim -pqh transformer_architecture.py AttentionMechanism
# manim -pqh transformer_architecture.py PositionalEncoding
