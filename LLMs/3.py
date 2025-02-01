from manim import *
import numpy as np

class PreTrainingPhase(Scene):
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
        title = Text("LLM Training Process", font_size=40)
        subtitle = Text("Pre-training Phase", font_size=30, color=BLUE)
        subtitle.next_to(title, DOWN)

        # Create title group
        title_group = VGroup(title, subtitle)
        title_group.to_edge(UP)

        self.play(Write(title_group))
        self.wait(0.5)

        # Move all content down by adjusting the starting position
        content_start_position = DOWN * 1.3  # Adjust this value as needed

        # Create text corpus visualization with adjusted position
        def create_document(position, scale=1):
            doc = VGroup()
            for i in range(4):
                line = Rectangle(height=0.1, width=2*scale)
                line.set_fill(BLUE, opacity=0.3)
                line.set_stroke(width=0)
                doc.add(line)
            doc.arrange(DOWN, buff=0.1)
            doc.move_to(position)
            return doc

        # Create multiple documents with adjusted positioning
        documents = VGroup()
        for i in range(3):
            for j in range(3):
                # Adjust the vertical position by adding content_start_position
                doc = create_document([i*3 - 3, j*2 - 1 + content_start_position[1], 0], scale=0.8)
                documents.add(doc)

        self.play(Create(documents))
        self.wait(0.5)

        # Create model representation with adjusted position
        model = Rectangle(height=3, width=2)
        model.set_fill(BLUE_E, opacity=0.3)
        model.move_to([3, content_start_position[1], 0])  # Adjust position
        model_label = Text("Model", font_size=24).move_to(model)
        model_group = VGroup(model, model_label)

        self.play(Create(model_group))

        # Animate data flow
        for doc in documents:
            copy = doc.copy()
            self.play(
                copy.animate.move_to(model.get_left()),
                run_time=2
            )
            self.play(FadeOut(copy), run_time=0.2)

        self.wait(1)

        # Add explanatory text with adjusted position
        explanation = VGroup(
            Text("Pre-training on massive text corpus", font_size=20, color=BLUE),
            Text("Learning language patterns", font_size=20, color=BLUE)
        ).arrange(DOWN, buff=0.3)
        #explanation.next_to(model_group)

        self.play(Write(explanation))
        self.wait(2)



# To render:
# manim -pqh pretraining_scene.py PreTrainingPhase

class NextWordPrediction(Scene):
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
        title = Text("Next Word Prediction", font_size=35)
        title.to_edge(UP)
        self.play(Write(title))

        # Create input sentence
        input_text = Text("The cat sat on the", font_size=30)
        input_text.move_to(UP)

        # Create prediction box
        pred_box = Rectangle(height=1, width=2)
        pred_box.next_to(input_text, RIGHT)

        # Create prediction probabilities
        predictions = VGroup()
        words = ["mat", "chair", "table", "floor"]
        probs = [0.4, 0.3, 0.2, 0.1]

        for i, (word, prob) in enumerate(zip(words, probs)):
            text = Text(f"{word}: {prob:.1f}", font_size=24)
            text.move_to([0, -i*0.5 - 1, 0])
            predictions.add(text)

        # Animation sequence
        self.play(Write(input_text))
        self.play(Create(pred_box))

        # Animate predictions appearing
        for pred in predictions:
            self.play(Write(pred), run_time=0.5)

        # Highlight highest probability
        highlight = SurroundingRectangle(predictions[0], color=YELLOW)
        self.play(Create(highlight))

        self.wait(1)

class FineTuningPhase(Scene):
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
        title = Text("Fine-tuning Phase", font_size=40)
        title.to_edge(UP)
        self.play(Write(title))

        # Create pre-trained model
        pretrained = Rectangle(height=3, width=2, color=BLUE)
        pretrained.set_fill(BLUE, opacity=0.2)
        pretrained_label = Text("Pre-trained\nModel", font_size=24)
        pretrained_label.move_to(pretrained)
        pretrained_group = VGroup(pretrained, pretrained_label)
        pretrained_group.move_to(LEFT*3)

        # Create fine-tuned model
        finetuned = Rectangle(height=3, width=2, color=GREEN)
        finetuned.set_fill(GREEN, opacity=0.2)
        finetuned_label = Text("Fine-tuned\nModel", font_size=24)
        finetuned_label.move_to(finetuned)
        finetuned_group = VGroup(finetuned, finetuned_label)
        finetuned_group.move_to(RIGHT*3)

        # Create task-specific data
        task_data = VGroup()
        for i in range(3):
            data = Rectangle(height=0.3, width=1.5)
            data.set_fill(YELLOW, opacity=0.3)
            data.move_to([0, i-1, 0])
            task_data.add(data)
        task_label = Text("Task-specific\nData", font_size=24)
        task_label.next_to(task_data, DOWN)
        task_group = VGroup(task_data, task_label)

        # Arrows
        arrow1 = Arrow(pretrained.get_right(), task_data.get_left())
        arrow2 = Arrow(task_data.get_right(), finetuned.get_left())

        # Animation sequence
        self.play(Create(pretrained_group))
        self.play(Create(task_group))
        self.play(Create(arrow1))
        self.play(Create(finetuned_group))
        self.play(Create(arrow2))

        # Show transformation
        self.play(
            pretrained_group.animate.set_color(BLUE_E),
            finetuned_group.animate.set_color(GREEN_E),
            run_time=2
        )

        self.wait(1)

class LearningProgress(Scene):
    def construct(self):

        # Add a background effect (gradient rectangle)
        background = Rectangle(
            width=config.frame_width,  # Use MANIM's config.frame_width
            height=config.frame_height,  # Use MANIM's config.frame_height
            fill_color=BLUE_C,
            fill_opacity=0.1,
        ).set_z_index(-1)  # Ensure it is behind all elements
        self.add(background)  # Add background to the scene

        # Create coordinate system
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 1, 0.2],
            axis_config={"color": BLUE},
            x_length=8,
            y_length=5
        )

        # Labels
        x_label = Text("Training Steps", font_size=24)
        x_label.next_to(axes.x_axis, DOWN)
        y_label = Text("Accuracy", font_size=24)
        y_label.next_to(axes.y_axis, LEFT)

        # Create learning curve
        def learning_curve(x):
            return 1 - 0.5 * np.exp(-0.3 * x)

        curve = axes.plot(learning_curve, color=YELLOW)

        # Animation
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.play(Create(curve))

        # Add moving dot
        dot = Dot(color=RED)
        dot.move_to(axes.c2p(0, learning_curve(0)))

        self.play(
            MoveAlongPath(
                dot, curve,
                run_time=3
            )
        )

        self.wait(1)

# To render:
# manim -pqh training_process.py PreTrainingPhase
# manim -pqh training_process.py NextWordPrediction
# manim -pqh training_process.py FineTuningPhase
# manim -pqh training_process.py LearningProgress
