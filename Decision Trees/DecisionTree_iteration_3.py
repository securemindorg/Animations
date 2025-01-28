from manim import *
import numpy as np

class DetailedDecisionTree(Scene):
    def create_table(self, data, headers):
        table = MobjectTable(
            [[Text(str(item), font_size=20) for item in row] for row in data],
            row_labels=[Text(f"{i+1}", font_size=20) for i in range(len(data))],
            col_labels=[Text(str(h), font_size=20) for h in headers],
            include_outer_lines=True
        ).scale(0.5)
        return table

    def create_gini_calculation(self, counts, total, position):
        calc_group = VGroup()
        
        # Show counts
        count_text = Text(f"Counts: {counts}", font_size=25)
        
        # Calculate probabilities
        probs = [count/total for count in counts]
        prob_text = Text(f"Probabilities: [{', '.join([f'{p:.3f}' for p in probs])}]", font_size=25)
        
        # Calculate squared probabilities
        squared_probs = [p*p for p in probs]
        squared_text = Text(f"Squared probs: [{', '.join([f'{p:.3f}' for p in squared_probs])}]", font_size=25)
        
        # Calculate final Gini
        gini = 1 - sum(squared_probs)
        gini_text = Text(f"Gini = 1 - {sum(squared_probs):.3f} = {gini:.3f}", font_size=25)
        
        calc_group.add(count_text, prob_text, squared_text, gini_text)
        calc_group.arrange(DOWN, aligned_edge=LEFT)
        calc_group.move_to(position)
        
        return calc_group, gini

    def construct(self):
        # Title
        title = Text("Decision Tree Learning Process", font_size=40)
        self.play(Write(title), run_time=2)
        self.play(title.animate.scale(0.6).to_edge(UP), run_time=1.5)

        # Create sample dataset
        data = [
            ["30", "50k", "No", "Don't Buy"],
            ["45", "60k", "No", "Buy"],
            ["25", "30k", "Yes", "Don't Buy"],
            ["35", "85k", "No", "Buy"],
            ["28", "40k", "Yes", "Don't Buy"],
            ["32", "70k", "No", "Buy"]
        ]
        headers = ["Age", "Income", "Student", "Decision"]
        
        # Create and show table
        table = self.create_table(data, headers)
        self.play(Create(table), run_time=2)
        
        # Slide table to the right
        self.play(table.animate.scale(0.8).to_edge(RIGHT), run_time=1.5)

        # Initial Gini calculation
        initial_gini_title = Text("Initial Gini Impurity Calculation:", font_size=30).to_edge(LEFT).shift(UP * 2)
        self.play(Write(initial_gini_title), run_time=1.5)
        
        initial_calc_group, initial_gini = self.create_gini_calculation(
            [3, 3],  # Buy, Don't Buy
            6,       # Total samples
            LEFT * 3
        )
        
        # Animate each step of initial Gini calculation
        for i in range(len(initial_calc_group)):
            self.play(Write(initial_calc_group[i]), run_time=1.5)
            self.wait(1)

        self.play(
            initial_calc_group.animate.scale(0.7).to_edge(LEFT).shift(UP),
            run_time=1.5
        )

        # Create root node
        root = VGroup()
        circle = Circle(radius=0.5, color=BLUE)
        text = Text("Age > 30?", font_size=20)
        text.move_to(circle.get_center())
        root.add(circle, text)
        root.move_to(ORIGIN + UP * 2)

        self.play(Create(root), run_time=1.5)

        # Left split Gini calculation
        left_title = Text("Left Split (Age > 30):", font_size=25).next_to(initial_calc_group, DOWN, buff=0.5)
        self.play(Write(left_title), run_time=1.5)
        
        left_calc_group, left_gini = self.create_gini_calculation(
            [2, 1],  # Buy, Don't Buy
            3,       # Total samples
            left_title.get_center() + DOWN
        )
        
        for i in range(len(left_calc_group)):
            self.play(Write(left_calc_group[i]), run_time=1.5)
            self.wait(1)

        # Right split Gini calculation
        right_title = Text("Right Split (Age ≤ 30):", font_size=25).next_to(left_calc_group, DOWN, buff=0.5)
        self.play(Write(right_title), run_time=1.5)
        
        right_calc_group, right_gini = self.create_gini_calculation(
            [1, 2],  # Buy, Don't Buy
            3,       # Total samples
            right_title.get_center() + DOWN
        )
        
        for i in range(len(right_calc_group)):
            self.play(Write(right_calc_group[i]), run_time=1.5)
            self.wait(1)

        # Create child nodes
        left_node = VGroup(
            Circle(radius=0.5, color=GREEN),
            Text("Income > 60k?", font_size=20)
        ).arrange(ORIGIN)
        left_node.move_to(LEFT * 2 + UP * 0.5)

        right_node = VGroup(
            Circle(radius=0.5, color=RED),
            Text("Student?", font_size=20)
        ).arrange(ORIGIN)
        right_node.move_to(RIGHT * 2 + UP * 0.5)

        # Create edges
        edges = VGroup(
            Line(root[0].get_bottom(), left_node[0].get_top()),
            Line(root[0].get_bottom(), right_node[0].get_top())
        )

        self.play(
            Create(edges),
            Create(left_node),
            Create(right_node),
            run_time=2
        )

        # Show model evaluation
        eval_box = VGroup(
            Text("Model Evaluation", font_size=30, color=YELLOW),
            Text("New Sample:", font_size=25),
            Text("Age: 40", font_size=25),
            Text("Income: 75k", font_size=25),
            Text("Student: No", font_size=25)
        ).arrange(DOWN, aligned_edge=LEFT)
        eval_box.to_edge(LEFT).shift(DOWN * 2)

        self.play(Write(eval_box), run_time=2)

        # Highlight decision path
        path = VGroup(
            root[0].copy(),
            edges[0].copy(),
            left_node[0].copy()
        ).set_color(YELLOW)

        self.play(Create(path), run_time=2)

        prediction = Text(
            "Prediction: Buy",
            font_size=30,
            color=GREEN
        ).next_to(eval_box, RIGHT, buff=1)

        self.play(Write(prediction), run_time=1.5)
        self.wait(3)
