from manim import *
import numpy as np

class GANEdgeDetection(Scene):
    def construct(self):
        # Title
        title = Text("GAN with Edge Detection", font_size=40)
        subtitle = Text("Using 3x3 Sobel Filters", font_size=30)
        title_group = VGroup(title, subtitle).arrange(DOWN)
        
        self.play(Write(title_group))
        self.play(title_group.animate.scale(0.6).to_edge(UP))
        
        # Create 3x3 Sobel filters
        sobel_x = np.array([[-1, 0, 1],
                           [-2, 0, 2],
                           [-1, 0, 1]])
        
        sobel_y = np.array([[-1, -2, -1],
                           [0, 0, 0],
                           [1, 2, 1]])

        def create_filter_visual(filter_array, title_text):
            filter_group = VGroup()
            title = Text(title_text, font_size=25)
            grid = VGroup()
            
            for i in range(3):
                for j in range(3):
                    cell = Square(side_length=0.5)
                    value = Text(str(filter_array[i][j]), font_size=20)
                    value.move_to(cell.get_center())
                    cell_group = VGroup(cell, value)
                    cell_group.shift(RIGHT * j * 0.5 + DOWN * i * 0.5)
                    grid.add(cell_group)
            
            filter_group.add(title, grid)
            filter_group.arrange(DOWN)
            return filter_group

        # Create and show Sobel filters
        sobel_x_visual = create_filter_visual(sobel_x, "Sobel X Filter")
        sobel_y_visual = create_filter_visual(sobel_y, "Sobel Y Filter")
        filters = VGroup(sobel_x_visual, sobel_y_visual).arrange(RIGHT, buff=1)
        filters.shift(UP * 2)
        
        self.play(Create(filters))
        self.wait()

        # Create GAN Architecture
        def create_network_block(width, height, label):
            block = VGroup()
            rect = Rectangle(width=width, height=height)
            text = Text(label, font_size=20)
            text.next_to(rect, DOWN)
            block.add(rect, text)
            return block

        # Generator
        generator = create_network_block(2, 3, "Generator")
        generator.shift(LEFT * 4)

        # Discriminator
        discriminator = create_network_block(2, 3, "Discriminator")
        discriminator.shift(RIGHT * 4)

        # Show GAN components
        self.play(
            Create(generator),
            Create(discriminator)
        )

        # Add arrows for data flow
        arrows = VGroup(
            Arrow(generator.get_right(), discriminator.get_left(), buff=0.5),
            Arrow(UP * 1.5 + RIGHT * 2, discriminator.get_left(), buff=0.5)
        )
        
        arrow_labels = VGroup(
            Text("Generated Edges", font_size=20).next_to(arrows[0], UP),
            Text("Real Edges", font_size=20).next_to(arrows[1], UP)
        )

        self.play(
            Create(arrows),
            Write(arrow_labels)
        )

        # Show edge detection process
        sample_image = Rectangle(width=2, height=2, color=WHITE)
        sample_image.shift(LEFT * 4 + DOWN * 2)
        image_label = Text("Input Image", font_size=20).next_to(sample_image, DOWN)

        edge_image = Rectangle(width=2, height=2, color=BLUE)
        edge_image.shift(RIGHT * 4 + DOWN * 2)
        edge_label = Text("Edge Map", font_size=20).next_to(edge_image, DOWN)

        self.play(
            Create(sample_image),
            Write(image_label),
            Create(edge_image),
            Write(edge_label)
        )

        # Show convolution animation
        kernel = Square(side_length=0.5, color=YELLOW)
        kernel.move_to(sample_image.get_left() + UP * 0.75)
        
        def create_convolution_path():
            path = VMobject()
            start = kernel.get_center()
            path.set_points_as_corners([
                start,
                start + RIGHT * 1.5,
                start + RIGHT * 1.5 + DOWN * 0.5,
                start + DOWN * 0.5,
                start
            ])
            return path

        conv_path = create_convolution_path()
        self.play(Create(kernel))
        self.play(MoveAlongPath(kernel, conv_path), run_time=3)

        # Show training process
        loss_graph = Axes(
            x_range=[0, 5],
            y_range=[0, 1],
            axis_config={"include_tip": False}
        ).scale(0.5)
        loss_graph.shift(DOWN * 2)
        
        loss_label = Text("Training Loss", font_size=20).next_to(loss_graph, UP)
        
        self.play(
            Create(loss_graph),
            Write(loss_label)
        )

        # Animate loss curve
        loss_curve = ParametricFunction(
            lambda t: loss_graph.c2p(t, np.exp(-t/2)),
            t_range=[0, 5],
            color=RED
        )
        
        self.play(Create(loss_curve), run_time=2)
