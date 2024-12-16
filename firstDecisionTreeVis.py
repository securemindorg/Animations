from manim import *

class DecisionTreeAnimation(Scene):
    def construct(self):
        # Title
        title = Text("Decision Tree Visualization", font_size=40)
        self.play(Write(title))
        self.play(title.animate.scale(0.6).to_edge(UP))
        
        # Create nodes
        root = Circle(radius=0.5, color=BLUE)
        root_text = Text("Age > 30?", font_size=20).move_to(root)
        root_group = VGroup(root, root_text).shift(UP * 2)

        # Left branch (Yes)
        left_node = Circle(radius=0.5, color=GREEN)
        left_text = Text("Income\n> 50k?", font_size=20).move_to(left_node)
        left_group = VGroup(left_node, left_text).shift(UP * 0.5 + LEFT * 2)

        # Right branch (No)
        right_node = Circle(radius=0.5, color=RED)
        right_text = Text("Student?", font_size=20).move_to(right_node)
        right_group = VGroup(right_node, right_text).shift(UP * 0.5 + RIGHT * 2)

        # Left-left leaf (Yes-Yes)
        left_left = Circle(radius=0.5, color=GREEN_E)
        left_left_text = Text("Buy", font_size=20).move_to(left_left)
        left_left_group = VGroup(left_left, left_left_text).shift(DOWN * 1 + LEFT * 3)

        # Left-right leaf (Yes-No)
        left_right = Circle(radius=0.5, color=RED_E)
        left_right_text = Text("Don't Buy", font_size=20).move_to(left_right)
        left_right_group = VGroup(left_right, left_right_text).shift(DOWN * 1 + LEFT * 1)

        # Right-left leaf (No-Yes)
        right_left = Circle(radius=0.5, color=GREEN_E)
        right_left_text = Text("Don't Buy", font_size=20).move_to(right_left)
        right_left_group = VGroup(right_left, right_left_text).shift(DOWN * 1 + RIGHT * 1)

        # Right-right leaf (No-No)
        right_right = Circle(radius=0.5, color=RED_E)
        right_right_text = Text("Buy", font_size=20).move_to(right_right)
        right_right_group = VGroup(right_right, right_right_text).shift(DOWN * 1 + RIGHT * 3)

        # Create edges
        edges = VGroup(
            Line(root.get_bottom(), left_node.get_top()),
            Line(root.get_bottom(), right_node.get_top()),
            Line(left_node.get_bottom(), left_left.get_top()),
            Line(left_node.get_bottom(), left_right.get_top()),
            Line(right_node.get_bottom(), right_left.get_top()),
            Line(right_node.get_bottom(), right_right.get_top()),
        )

        # Edge labels
        yes_no_labels = VGroup(
            Text("Yes", font_size=16).next_to(edges[0], UP),
            Text("No", font_size=16).next_to(edges[1], UP),
            Text("Yes", font_size=16).next_to(edges[2], LEFT),
            Text("No", font_size=16).next_to(edges[3], RIGHT),
            Text("Yes", font_size=16).next_to(edges[4], LEFT),
            Text("No", font_size=16).next_to(edges[5], RIGHT),
        )

        # Animation sequence
        self.play(Create(root_group))
        self.wait(0.5)
        
        # Create first level splits
        self.play(
            Create(edges[0]),
            Create(edges[1]),
            Write(yes_no_labels[0]),
            Write(yes_no_labels[1])
        )
        self.play(Create(left_group), Create(right_group))
        self.wait(0.5)

        # Create second level splits
        self.play(
            Create(edges[2:]),
            Write(yes_no_labels[2:])
        )
        self.play(
            Create(left_left_group),
            Create(left_right_group),
            Create(right_left_group),
            Create(right_right_group)
        )

        # Add explanation
        explanation = Text(
            "Decision trees split data based on features\n" +
            "to make predictions",
            font_size=25,
            color=YELLOW
        ).next_to(title, DOWN, buff=0.5)
        
        self.play(Write(explanation))
        self.wait(2)

        # Highlight a decision path
        path_highlight = VGroup(
            root_group.copy(),
            edges[0].copy(),
            left_group.copy(),
            edges[2].copy(),
            left_left_group.copy()
        ).set_color(YELLOW)
        
        self.play(Create(path_highlight))
        self.wait(2)
