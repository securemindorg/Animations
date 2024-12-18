from manim import *
import networkx as nx
import numpy as np

class CollatzTree(Scene):
    def construct(self):
        # Title
        title = Text("Collatz Conjecture Tree").scale(1.2)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

        # Generate the Collatz Tree
        def generate_collatz_tree(n):
            graph = nx.DiGraph()
            for i in range(1, n + 1):
                current = i
                while current != 1:
                    if current % 2 == 0:
                        next_node = current // 2
                    else:
                        next_node = (current - 1) // 3
                        if (next_node * 3 + 1) != current:  # Ensure valid reverse step
                            break
                    graph.add_edge(next_node, current)
                    current = next_node
            return graph

        # Create the tree for numbers up to 100
        max_number = 100
        collatz_graph = generate_collatz_tree(max_number)

        # Use graphviz_layout for hierarchical positioning
        try:
            pos = nx.nx_agraph.graphviz_layout(collatz_graph, prog="dot")
        except ImportError:
            raise ImportError("Graphviz is required for this layout. Install it with `pip install pygraphviz`.")

        # Map positions to Manim coordinates
        manim_pos = {str(node): np.array([x / 100, y / 100, 0]) for node, (x, y) in pos.items()}

        # Create the graph in Manim
        vertices = [str(node) for node in collatz_graph.nodes()]
        edges = [(str(a), str(b)) for a, b in collatz_graph.edges()]
        graph = Graph(
            vertices,
            edges,
            layout=manim_pos,
            layout_scale=1,
            labels=False,
            vertex_config={"radius": 0.05, "fill_color": GREEN},
            edge_config={"stroke_color": YELLOW, "stroke_width": 1},
        )

        # Animate the graph
        self.play(Create(graph), run_time=5)
        self.wait(2)

        # Conclusion
        conclusion = Text("""
The Collatz Conjecture Tree shows how all numbers
eventually converge to 1 under the conjecture's rules.
""", font_size=28).to_edge(DOWN)
        self.play(Write(conclusion), run_time=5)
        self.wait(4)
