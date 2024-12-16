from manim import *

class DetailedDecisionTree(Scene):
    def create_table(self, data, headers):
        # Create table with proper Text mobjects
        table = MobjectTable(
            [[Text(str(item), font_size=20) for item in row] for row in data],
            row_labels=[Text(f"{i+1}", font_size=20) for i in range(len(data))],
            col_labels=[Text(str(h), font_size=20) for h in headers],
            include_outer_lines=True
        ).scale(0.5)
        return table

    def construct(self):
        # Title
        title = Text("Decision Tree Learning Process", font_size=40)
        self.play(Write(title))
        self.play(title.animate.scale(0.6).to_edge(UP))

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
        self.play(Create(table))
        self.wait()

        # Create tree nodes using VGroup
        def create_node(text, color, position):
            node = VGroup()
            circle = Circle(radius=0.5, color=color)
            text_obj = Text(text, font_size=20)
            text_obj.move_to(circle.get_center())
            node.add(circle, text_obj)
            node.move_to(position)
            return node

        # Root node
        root = create_node("Age > 30?", BLUE, UP * 2)
        
        # Child nodes
        left_node = create_node("Income > 60k?", GREEN, UP * 0.5 + LEFT * 2)
        right_node = create_node("Student?", RED, UP * 0.5 + RIGHT * 2)

        # Create edges
        edges = VGroup(
            Line(root[0].get_bottom(), left_node[0].get_top()),
            Line(root[0].get_bottom(), right_node[0].get_top())
        )

        # Gini calculations
        gini_calc = VGroup(
            Text("Initial Gini = 0.5", font_size=25),
            Text("Left Split Gini = 0.444", font_size=25),
            Text("Right Split Gini = 0.444", font_size=25)
        ).arrange(DOWN).next_to(table, DOWN)

        # Animation sequence
        self.play(Write(gini_calc))
        self.wait()
        
        self.play(
            FadeOut(table),
            FadeOut(gini_calc)
        )

        # Build tree
        self.play(Create(root))
        self.play(
            Create(edges),
            Create(left_node),
            Create(right_node)
        )

        # Model evaluation
        new_sample = VGroup(
            Text("New Sample:", font_size=25),
            Text("Age: 40", font_size=25),
            Text("Income: 75k", font_size=25),
            Text("Student: No", font_size=25)
        ).arrange(DOWN, aligned_edge=LEFT).to_edge(LEFT)

        self.play(Write(new_sample))

        # Decision path
        path = VGroup(
            root[0].copy(),
            edges[0].copy(),
            left_node[0].copy()
        ).set_color(YELLOW)

        self.play(Create(path))

        prediction = Text(
            "Prediction: Buy",
            font_size=30,
            color=GREEN
        ).next_to(new_sample, RIGHT, buff=1)

        self.play(Write(prediction))
        self.wait(2)
