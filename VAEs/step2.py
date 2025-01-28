from manim import *

class AutoencoderVisualization(Scene):
    def construct(self):
        # Add a background effect (gradient rectangle)
        background = Rectangle(
            width=config.frame_width,  # Use MANIM's config.frame_width
            height=config.frame_height,  # Use MANIM's config.frame_height
            fill_color=BLUE_C,
            fill_opacity=0.1,
        ).set_z_index(-1)  # Ensure it is behind all elements

        self.add(background)  # Add background to the scene

        sentences_text = Text("Text Audoencoder Architecture", font_size=28).to_edge(UP)
        self.play(Write(sentences_text))
        self.wait(1)

        # Create input layer representation
        input_box = Rectangle(height=4, width=1.8, color=WHITE)
        input_label = Text("Input Layer\n(padded text)", color=WHITE).scale(0.4)
        input_group = VGroup(input_box, input_label)
        input_group.shift(LEFT * 5)

        # Create embedding layer
        embed_box = Rectangle(height=3.5, width=1.8, color=YELLOW)
        embed_label = Text("Embedding\n(64 dims)", color=WHITE).scale(0.4)
        embed_group = VGroup(embed_box, embed_label)
        embed_group.shift(LEFT * 2.5)

        # Create LSTM encoder
        lstm_enc_box = Rectangle(height=2, width=1.5, color=BLUE)
        lstm_enc_label = Text("LSTM\n(32 units)", color=WHITE).scale(0.4)
        lstm_enc_group = VGroup(lstm_enc_box, lstm_enc_label)

        # Create latent space representation
        latent_box = Rectangle(height=1, width=1, color=GREEN)
        latent_label = Text("Latent\nSpace", color=WHITE).scale(0.4)
        latent_group = VGroup(latent_box, latent_label)
        latent_group.shift(RIGHT * 2.5)

        # Create decoder components
        decoder_box = Rectangle(height=2, width=1.5, color=RED)
        decoder_label = Text("Decoder\nLSTM", color=WHITE).scale(0.4)
        decoder_group = VGroup(decoder_box, decoder_label)
        decoder_group.shift(RIGHT * 5)

        # Draw arrows connecting components
        arrows = VGroup(
            Arrow(input_group.get_right(), embed_group.get_left(), color=WHITE),
            Arrow(embed_group.get_right(), lstm_enc_group.get_left(), color=WHITE),
            Arrow(lstm_enc_group.get_right(), latent_group.get_left(), color=WHITE),
            Arrow(latent_group.get_right(), decoder_group.get_left(), color=WHITE)
        )

        # Animate the components
        self.play(Create(input_group))
        self.wait(3)
        self.play(Create(arrows[0]))
        self.play(Create(embed_group))
        self.wait(3)
        self.play(Create(arrows[1]))
        self.play(Create(lstm_enc_group))
        self.wait(3)
        self.play(Create(arrows[2]))
        self.play(Create(latent_group))
        self.wait(3)
        self.play(Create(arrows[3]))
        self.play(Create(decoder_group))

        # Add explanation text at the bottom
        explanation = Text(
            "Text → Embeddings → LSTM Encoder → Latent Space → LSTM Decoder",
            color=WHITE
        ).scale(0.4)
        explanation.to_edge(DOWN)
        self.play(Write(explanation))

        self.wait(10)
