from manim import *

class SentenceEncoding(Scene):
    def construct(self):
        # Step 1: Display the input sentences
        sentences = [
            "Utica University offers courses in Machine Learning and AI",
            "I just attended an amazing AI workshop in California!",
            "I love to read about technologies such as AI and Green Tech",
            "I am the very model of a modern Major-General",
            "I’ve information vegetable, animal, and mineral",
        ]
        sentences_text = Text("Input Sentences:").to_edge(UP)
        self.play(Write(sentences_text))
        self.wait(1)

        # Display each sentence
        sentence_group = VGroup(*[Text(f"{i+1}. {sentence}", font_size=24).scale(0.7) for i, sentence in enumerate(sentences)])
        sentence_group.arrange(DOWN, aligned_edge=LEFT).next_to(sentences_text, DOWN, buff=0.5)
        self.play(FadeIn(sentence_group, shift=DOWN))
        self.wait(2)

        # Step 2: Tokenization process
        tokenizer_text = Text("Step 1: Tokenization").to_edge(UP)
        self.play(Transform(sentences_text, tokenizer_text))
        self.wait(1)

        # Show word-to-index mapping
        word_mapping = {
            "Utica": 1, "University": 2, "offers": 3, "courses": 4, "in": 5,
            "Machine": 6, "Learning": 7, "and": 8, "AI": 9, "I": 10,
            "just": 11, "attended": 12, "an": 13, "amazing": 14, "workshop": 15,
            "California": 16, "love": 17, "to": 18, "read": 19, "about": 20,
            "technologies": 21, "such": 22, "as": 23, "Green": 24, "Tech": 25,
        }
        mapping_text = Text("Word-to-Index Mapping:", font_size=28).to_edge(UP)
        mapping_group = VGroup(*[Text(f"{word}: {index}", font_size=24).scale(0.6) for word, index in word_mapping.items()])
        mapping_group.arrange(DOWN, aligned_edge=LEFT).next_to(mapping_text, DOWN, buff=0.5)
        self.play(FadeOut(sentence_group), FadeIn(mapping_text, shift=UP), FadeIn(mapping_group, shift=DOWN))
        self.wait(2)

        # Step 3: Convert sentences to sequences
        sequences_text = Text("Step 2: Convert Sentences to Sequences").to_edge(UP)
        self.play(Transform(mapping_text, sequences_text), FadeOut(mapping_group))
        self.wait(1)

        sequences = [
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [10, 11, 12, 13, 14, 9, 15, 5, 16],
            [10, 17, 18, 19, 20, 21, 22, 23, 9, 8, 24, 25],
            [10, 18, 8, 22, 26, 27, 28, 29],
            [10, 30, 31, 32, 33, 34, 35],
        ]
        # Convert sequences into a VGroup of Text objects
        sequence_group = VGroup(*[Text(f"Sentence {i+1}: {', '.join(map(str, seq))}", font_size=24).scale(0.7) for i, seq in enumerate(sequences)])
        sequence_group.arrange(DOWN, aligned_edge=LEFT).next_to(sequences_text, DOWN, buff=0.5)
        self.play(FadeIn(sequence_group, shift=DOWN))
        self.wait(2)

        # Step 4: Padding the sequences
        padding_text = Text("Step 3: Padding the Sequences").to_edge(UP)
        self.play(Transform(sequences_text, padding_text), FadeOut(sequence_group))
        self.wait(1)

        padded_sequences = [
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0],
            [10, 11, 12, 13, 14, 9, 15, 5, 16, 0, 0, 0],
            [10, 17, 18, 19, 20, 21, 22, 23, 9, 8, 24, 25],
            [10, 18, 8, 22, 26, 27, 28, 29, 0, 0, 0, 0],
            [10, 30, 31, 32, 33, 34, 35, 0, 0, 0, 0, 0],
        ]
        # Convert padded sequences into a VGroup of Text objects
        padded_group = VGroup(*[Text(f"Sentence {i+1}: {', '.join(map(str, seq))}", font_size=24).scale(0.7) for i, seq in enumerate(padded_sequences)])
        padded_group.arrange(DOWN, aligned_edge=LEFT).next_to(padding_text, DOWN, buff=0.5)
        self.play(FadeIn(padded_group, shift=DOWN))
        self.wait(2)

        # Step 5: Final matrix representation
        matrix_text = Text("Final Matrix Representation").to_edge(UP)
        self.play(Transform(padding_text, matrix_text), FadeOut(padded_group))
        self.wait(1)

        # Convert padded_sequences into Text objects for MobjectTable
        table_data = [
            [Text(str(num), font_size=24) for num in row] for row in padded_sequences
        ]
        # Create row and column labels
        row_labels = [Text(f"Sentence {i+1}", font_size=24) for i in range(len(padded_sequences))]
        col_labels = [Text(f"Word {i+1}", font_size=24) for i in range(len(padded_sequences[0]))]

        # Create the final table
        matrix = MobjectTable(
            table_data,
            row_labels=row_labels,
            col_labels=col_labels,
            include_outer_lines=True,
        ).scale(0.5).to_edge(DOWN)

        self.play(Create(matrix))
        self.wait(3)
