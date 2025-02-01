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
        title.to_edge(UP, buff=0.3)  # Reduced top buffer
        self.play(Write(title))

        # Scale factor for entire diagram
        SCALE_FACTOR = 0.6  # Adjust this value to make everything smaller/larger

        # Create input and output text boxes
        input_text = Text("Input", font_size=24)
        output_text = Text("Output", font_size=24)

        # Create main components
        def create_layer_block(text, color=BLUE):
            rect = Rectangle(height=0.8, width=2, color=color)
            rect.set_fill(color, opacity=0.2)
            label = Text(text, font_size=20)
            label.move_to(rect)
            return VGroup(rect, label)

        # Create encoder stack
        encoder_stack = VGroup()
        for i in range(3):
            # Multi-head attention
            mha = create_layer_block("Multi-Head\nAttention", BLUE)
            # Add & Norm
            add_norm1 = create_layer_block("Add & Norm", GREEN)
            # Feed Forward
            ff = create_layer_block("Feed\nForward", BLUE)
            # Add & Norm
            add_norm2 = create_layer_block("Add & Norm", GREEN)

            # Arrange layer components
            layer = VGroup(mha, add_norm1, ff, add_norm2)
            layer.arrange(DOWN, buff=0.2)  # Reduced buffer between components
            encoder_stack.add(layer)

        encoder_stack.arrange(RIGHT, buff=0.8)  # Reduced buffer between layers
        encoder_stack.scale(SCALE_FACTOR)
        encoder_stack.shift(LEFT * 3)  # Removed DOWN shift

        # Create decoder stack
        decoder_stack = VGroup()
        for i in range(3):
            # Masked Multi-head attention
            masked_mha = create_layer_block("Masked\nMulti-Head\nAttention", RED)
            # Add & Norm
            add_norm1 = create_layer_block("Add & Norm", GREEN)
            # Multi-head attention
            mha = create_layer_block("Multi-Head\nAttention", BLUE)
            # Add & Norm
            add_norm2 = create_layer_block("Add & Norm", GREEN)
            # Feed Forward
            ff = create_layer_block("Feed\nForward", BLUE)
            # Add & Norm
            add_norm3 = create_layer_block("Add & Norm", GREEN)

            # Arrange layer components
            layer = VGroup(masked_mha, add_norm1, mha, add_norm2, ff, add_norm3)
            layer.arrange(DOWN, buff=0.2)  # Reduced buffer
            decoder_stack.add(layer)

        decoder_stack.arrange(RIGHT, buff=0.8)  # Reduced buffer
        decoder_stack.scale(SCALE_FACTOR)
        decoder_stack.shift(RIGHT * 3)  # Removed DOWN shift

        # Position entire diagram lower on screen
        diagram_group = VGroup(encoder_stack, decoder_stack)
        diagram_group.shift(DOWN * 0.5)  # Adjust this value as needed

        # Create embedding layers
        input_embedding = create_layer_block("Input\nEmbedding", YELLOW)
        input_embedding.scale(SCALE_FACTOR)
        input_embedding.next_to(encoder_stack, UP, buff=0.3)

        output_embedding = create_layer_block("Output\nEmbedding", YELLOW)
        output_embedding.scale(SCALE_FACTOR)
        output_embedding.next_to(decoder_stack, UP, buff=0.3)

        # Create positional encoding layers
        pos_encoding1 = create_layer_block("Positional\nEncoding", ORANGE)
        pos_encoding1.scale(SCALE_FACTOR)
        pos_encoding1.next_to(input_embedding, UP, buff=0.3)

        pos_encoding2 = create_layer_block("Positional\nEncoding", ORANGE)
        pos_encoding2.scale(SCALE_FACTOR)
        pos_encoding2.next_to(output_embedding, UP, buff=0.3)

        # Scale and position input/output text
        input_text.scale(SCALE_FACTOR)
        output_text.scale(SCALE_FACTOR)
        input_text.next_to(pos_encoding1, UP, buff=0.3)
        output_text.next_to(pos_encoding2, UP, buff=0.3)

        # Create connections
        def create_arrow(start, end):
            return Arrow(start.get_bottom(), end.get_top(), buff=0.1)

        # Add arrows
        arrows = VGroup()
        # Input to positional encoding
        arrows.add(create_arrow(input_text, pos_encoding1))
        # Positional encoding to embedding
        arrows.add(create_arrow(pos_encoding1, input_embedding))
        # Embedding to encoder
        arrows.add(create_arrow(input_embedding, encoder_stack[0]))

        # Output to positional encoding
        arrows.add(create_arrow(output_text, pos_encoding2))
        # Positional encoding to embedding
        arrows.add(create_arrow(pos_encoding2, output_embedding))
        # Embedding to decoder
        arrows.add(create_arrow(output_embedding, decoder_stack[0]))

        # Cross attention arrows
        cross_attention = Arrow(
            encoder_stack.get_right(),
            decoder_stack.get_left(),
            color=YELLOW,
            buff=0.1
        )

        # Animation sequence
        self.play(
            Create(input_text),
            Create(output_text)
        )

        # Create embeddings and positional encodings
        self.play(
            Create(pos_encoding1),
            Create(pos_encoding2),
            Create(input_embedding),
            Create(output_embedding)
        )

        # Create encoder and decoder stacks
        self.play(Create(encoder_stack))
        self.play(Create(decoder_stack))

        # Add arrows
        self.play(Create(arrows))
        self.play(Create(cross_attention))

        # Add labels with proper scaling
        encoder_label = Text("Encoder", font_size=24, color=BLUE)
        encoder_label.scale(SCALE_FACTOR)
        encoder_label.next_to(encoder_stack, UP, buff=0.1)

        decoder_label = Text("Decoder", font_size=24, color=RED)
        decoder_label.scale(SCALE_FACTOR)
        decoder_label.next_to(decoder_stack, UP, buff=0.1)

        self.play(
            Write(encoder_label),
            Write(decoder_label)
        )

        # Final pause
        self.wait(2)

# To render:
# manim -pqh transformer_architecture.py TransformerArchitecture
