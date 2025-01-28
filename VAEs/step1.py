from manim import *
import networkx as nx
import numpy as np

class TokenizationVisualization(Scene):
    def construct(self):
        # Add a background effect (gradient rectangle)
        background = Rectangle(
            width=config.frame_width,  # Use MANIM's config.frame_width
            height=config.frame_height,  # Use MANIM's config.frame_height
            fill_color=BLUE_C,
            fill_opacity=0.1,
        ).set_z_index(-1)  # Ensure it is behind all elements

        self.add(background)  # Add background to the scene

        # Step 1: Display the input sentences on the left
        sentences = [
            "Utica University offers courses in Machine Learning and AI",
            "I just attended an amazing AI workshop in California!",
            "I love to read about technologies such as AI and Green Tech",
        ]
        sentences_text = Text("Input Sentences:", font_size=28).to_edge(UP)
        self.play(Write(sentences_text))
        self.wait(1)

        # Display each sentence aligned to the left
        sentence_group = VGroup(*[Text(f"{i+1}. {sentence}", font_size=24).scale(0.7) for i, sentence in enumerate(sentences)])
        sentence_group.arrange(DOWN, aligned_edge=LEFT).to_edge(LEFT, buff=1)
        self.play(FadeIn(sentence_group, shift=DOWN))
        self.wait(2)

        # Fade out the initial sentences before starting tokenization
        self.play(FadeOut(sentences_text), FadeOut(sentence_group))
        self.wait(1)

        # Step 2: Tokenization process
        tokenizer_text = Text("Step 1: Tokenization", font_size=28).to_edge(UP)
        self.play(Write(tokenizer_text))
        self.wait(1)

        # Word-to-token mapping
        word_mapping = {
            "Utica": 1, "University": 2, "offers": 3, "courses": 4, "in": 5,
            "Machine": 6, "Learning": 7, "and": 8, "AI": 9, "I": 10,
            "just": 11, "attended": 12, "an": 13, "amazing": 14, "workshop": 15,
            "California": 16, "love": 17, "to": 18, "read": 19, "about": 20,
            "technologies": 21, "such": 22, "as": 23, "Green": 24, "Tech": 25,
        }

        # Animate tokenization for each sentence
        all_tokens = []  # To store all token sequences for the matrix
        for i, sentence in enumerate(sentences):
            words = sentence.split()
            word_objects = VGroup(*[Text(word, font_size=20) for word in words])
            word_objects.arrange(RIGHT, buff=0.5).to_edge(LEFT, buff=1).shift(UP * (1 - i * 1))  # Adjust vertical position

            # Underline each word
            underlines = VGroup(*[Underline(word) for word in word_objects])
            self.play(FadeIn(word_objects))
            self.play(Create(underlines))
            self.wait(2)

            # Assign tokens beneath each word
            tokens = VGroup(*[Text(str(word_mapping[word.strip(",.!?")]), font_size=18) for word in words])
            for token, word in zip(tokens, word_objects):
                token.next_to(word, DOWN)
            self.play(FadeIn(tokens))
            self.wait(2)

            # Collect token sequence for the matrix
            token_sequence = [word_mapping[word.strip(",.!?")] for word in words]
            all_tokens.append(token_sequence)

            # Fade out the words and underlines, leaving only the tokens
            #self.play(FadeOut(word_objects), FadeOut(underlines))
            self.wait(2)

        # Clear the tokenization heading
        #self.play(FadeOut(tokenizer_text))
        self.wait(5)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Add a background effect (gradient rectangle)
        background = Rectangle(
            width=config.frame_width,  # Use MANIM's config.frame_width
            height=config.frame_height,  # Use MANIM's config.frame_height
            fill_color=BLUE_C,
            fill_opacity=0.1,
        ).set_z_index(-1)  # Ensure it is behind all elements
        self.add(background)  # Add background to the scene

        matrix_elements = [
            [Text(str(num)) for num in row]
            for row in [
                [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0],
                [10, 11, 12, 13, 14, 9, 15, 5, 16, 0, 0, 0],
                [10, 17, 18, 19, 20, 21, 22, 23, 9, 8, 24, 25]
            ]
        ]

        m3 = MobjectMatrix(matrix_elements)
        m3.scale(0.5)
        matrix_text = Text("We now will add padding and construct our matrix", font_size=28).to_edge(UP)

        self.play(Write(matrix_text))
        self.wait(1)
        self.play(FadeIn(m3), shift=DOWN)
        self.wait(10)
