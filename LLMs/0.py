from manim import *
import networkx as nx
import numpy as np

class TitleScene(Scene):
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
        title = Text("Large Language Models", color=WHITE, font='Comic Sans MS').scale(1).set_stroke(BLACK, width=1).move_to(UP * 1)
        underline = Line(LEFT, RIGHT, color=WHITE).scale(4).next_to(title, DOWN)
        #self.play(Write(title))
        #self.wait(1)
        #signature = Text('Joshua S. White, PhD').scale(.5).to_corner(DR)
        #self.play(Create(underline)) #, FadeIn(signature))

        # Create a graph with multiple nodes
        G = nx.Graph()
        G.add_edges_from([(0, 1), (1, 2), (1, 6), (0, 7), (7, 8), (4, 5), (5, 0), (0, 2), (3, 5)])

        # Get positions using spring layout
        positions = nx.spring_layout(G)

        # Convert positions to the format MANIM understands
        manim_positions = {node: np.array([x, y, 0]) for node, (x, y) in positions.items()}

        # Define labels for nodes (optional)
        labels = {i: str(i) for i in G.nodes}

        # Create a Graph in MANIM
        graph = Graph(
            list(G.nodes),
            list(G.edges),
            layout=manim_positions,
            #labels=labels,
            vertex_config={"radius": 0.10, "color": WHITE},
            edge_config={"stroke_width": 2, "color": GREY},
        )

        # Position the graph in the bottom-left corner
        graph.move_to(UP * -1)

        # Add the graph to the scene
        self.play(Create(graph))

        # Animate slight movement of the nodes
        for _ in range(5):  # Repeat a few times for dynamic effect
            new_positions = {
                node: graph.vertices[node].get_center() + np.random.uniform(-0.05, 0.05, size=3)
                for node in manim_positions
            }
            self.play(
                graph.animate.change_layout(new_positions, layout_scale=1),
                run_time=0.5,  # Slower animation for smoother transitions
                rate_func=smooth  # Use a smooth rate function
            )

        # Transform the graph into the name "Joshua S. White"
        name_text = Text("Joshua S. White, PhD", color=WHITE, font='Comic Sans MS').scale(.5).to_corner(DR)

        self.play(Write(title))
        self.wait(1)
        self.play(Create(underline))
        self.wait(1)
        self.play(Transform(underline, name_text))

        # Hold the graph in its final state
        self.wait(4)

        #self.play(FadeOut(title), FadeOut(underline), FadeOut(signature), FadeOut(graph))

        # Fade the entire scene to black
        fade_to_black = Rectangle(
            width=config.frame_width,
            height=config.frame_height,
            fill_color=BLACK,
            fill_opacity=1,
        ).set_z_index(1)  # Ensure it covers everything

        self.play(FadeIn(fade_to_black, run_time=3))
