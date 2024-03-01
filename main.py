from manim import *

#python -m manim -p -ql main.py Commutativity

class Commutativity(Scene):
    def construct(self):

        #Writes title and subtitle
        title = Text("Addition is commutative").scale(0.75).to_edge(UP)
        subtitle = Text("A1").scale(0.75).next_to(title, DOWN)

        self.play(Write(title))
        self.play(Write(subtitle))

        #Left hand side of equation and equals are defined
        part1 = Text("x + y", font_size = 48)
        equals = Text("=", font_size = 48).next_to(part1, RIGHT)
        part1_duplicate = part1.copy().next_to(part1, LEFT) #Used to transform into part2

        #Right hand side of the equation
        part2 = Text("y + x", font_size = 48).next_to(equals, RIGHT)

        #Equation is grouped and moved to origin
        equation = VGroup(part1, equals, part2)
        equation.move_to(ORIGIN)

        #Equation is written
        self.play(Write(part1), Write(equals))

        #Animation handled here
        self.play(Transform(part1_duplicate, part2))

        self.wait(2)

        new_title = Text("...as is multiplication").scale(0.75).to_edge(UP)
        self.play(Transform(title, new_title))

        new_subtitle = Text("A2").scale(0.75).next_to(title, DOWN)
        self.play(Transform(subtitle, new_subtitle))

        new_lhs = MathTex("x", "\\times", "y", font_size = 48).scale(1.2).next_to(equals, LEFT)
        new_rhs = MathTex("y", "\\times", "x", font_size = 48).scale(1.2).next_to(equals, RIGHT)
        new_equation = VGroup(new_lhs, equals, new_rhs)
        new_equation.move_to(ORIGIN)

        self.play(Transform(part1, new_lhs))
        self.play(Transform(part1_duplicate, new_rhs))

        self.wait(2)


#python -m manim -p -ql main.py Associativity

class Associativity(Scene):
    def construct(self):

        #Writes title and subtitle
        title = Text("Addition is associative").scale(0.75).to_edge(UP)
        subtitle = Text("A3").scale(0.75).next_to(title, DOWN)

        self.play(Write(title))
        self.play(Write(subtitle))

        # Define the parts of the equation
        equals = Text(" = ")
        lhs = Text("x + y + z", font_size=48).next_to(equals, LEFT)
        rhs = Text("x + y + z", font_size=48).next_to(equals, RIGHT)
        
        #Left hand side parentheses
        lhs_paren = Text("(", font_size=48).next_to(lhs[0], LEFT, buff=0)
        lhs_paren_close = Text(")", font_size=48).next_to(lhs[2], RIGHT, buff=0)

        # Define the initial and final positions of the parentheses
        paren_left_initial = Text("(", font_size=48).next_to(rhs[0], LEFT, buff=0)
        paren_right_initial = Text(")", font_size=48).next_to(rhs[2], RIGHT, buff=0)
        
        paren_left_final = Text("(", font_size=48).next_to(rhs[2], LEFT, buff=0)
        paren_right_final = Text(")", font_size=48).next_to(rhs[-1], RIGHT, buff=0)

        lhs_paren.align_to(lhs, DOWN)
        lhs_paren_close.align_to(lhs, DOWN)
        paren_left_initial.align_to(lhs, DOWN)
        paren_right_initial.align_to(lhs, DOWN)
        paren_left_final.align_to(lhs, DOWN)
        paren_right_final.align_to(lhs, DOWN)
        
        # Group the initial equation and parentheses
        initial_group = VGroup(lhs, lhs_paren, lhs_paren_close, equals, rhs, paren_left_initial, paren_right_initial)

        # Display the initial equation with parentheses around x + y
        self.play(Write(initial_group))
        self.wait(1)
        
        # Transform the initial parentheses to their new positions around y + z
        self.play(
            ReplacementTransform(paren_left_initial, paren_left_final),
            ReplacementTransform(paren_right_initial, paren_right_final),
        )

        self.wait(2)
        
        new_title = Text("...as is multiplication").scale(0.75).to_edge(UP)
        self.play(Transform(title, new_title))

        new_subtitle = Text("A4").scale(0.75).next_to(title, DOWN)
        self.play(Transform(subtitle, new_subtitle))

        new_lhs = MathTex("x", "\\times", "y" , "\\times", "z", font_size = 48).scale(1.2).next_to(equals, LEFT)
        new_rhs = MathTex("x", "\\times", "y", "\\times", "z", font_size = 48).scale(1.2).next_to(equals, RIGHT)
        new_equation = VGroup(new_lhs, equals, new_rhs)
        new_equation.move_to(ORIGIN)

        self.play(Transform(lhs, new_lhs))
        self.play(Transform(rhs, new_rhs))

        self.wait(2)


#python -m manim -p -ql main.py Distribution

class Distribution(Scene):
    def construct(self):
        
        #Writes title and subtitle
        title = Text("Multiplication distributes through addition").scale(0.75).to_edge(UP)
        subtitle = Text("A5").scale(0.75).next_to(title, DOWN)

        self.play(Write(title))
        self.play(Write(subtitle))


        # Define the symbols
        x = MathTex("x", font_size = 48).scale(1.2)
        times = MathTex("\\times", font_size = 48).scale(1.2)
        left_parenthesis = MathTex("(", font_size = 48).scale(1.2)
        y = MathTex("y", font_size = 48).scale(1.2)
        plus = MathTex("+", font_size = 48).scale(1.2)
        z = MathTex("z", font_size = 48).scale(1.2)
        right_parenthesis = MathTex(")", font_size = 48).scale(1.2)
        equals = MathTex("=", font_size = 48).scale(1.2)

        # Group the symbols
        expression = VGroup(x, times, left_parenthesis, y, plus, z, right_parenthesis, equals)

        # Arrange the symbols
        expression.arrange(RIGHT)

        # Display the initial expression
        self.play(Write(expression))

        # Create copies of x for distribution
        x_copy_to_y = x.copy()
        x_copy_to_z = x.copy()

        # Move x to multiply y and z respectively
        self.play(
            x_copy_to_y.animate.move_to(y.get_center() + LEFT * 0.5),
            x_copy_to_z.animate.move_to(z.get_center() + LEFT * 0.5),
        )



        # Display the distributed expression
        distributed_expression = VGroup(x_copy_to_y, y, plus, x_copy_to_z, z).arrange(RIGHT, buff = 0.2)
        self.play(Transform(expression, distributed_expression))

        # Finish the scene
        self.wait(2)

#python -m manim -p -ql main.py MaxValues
        
class MaxValues(Scene):
    def construct(self):

        #DESCRIPTION OF ORDINARY VS COMPUTER ARITHMETIC LIMITS

        title = Text("Ordinary arithmetic has no maximum value").scale(0.75).to_edge(UP)

        self.play(Write(title))

        # Create a NumberPlane
        plane = NumberPlane(x_range=[-30, 30], y_range=[-30, 30])
        self.add(plane)

        # Animation: Expand the NumberPlane bounds
        self.play(
            plane.animate.scale(.3),
            run_time=1.5,
            rate_func=linear,
        )

        '''
        # Continuously move the plane to simulate an infinite scroll
        self.play(
            plane.animate.shift(UP * 5 + RIGHT * 5),
            run_time=2,
            rate_func=linear,
        )
        '''

        # Fade out to suggest the plane goes on infinitely
        self.play(
            FadeOut(plane, shift=UP),
            run_time=.3
        )

        self.wait(2)

        new_title = Text("But computer arithmetic does").scale(0.75).to_edge(UP)
        self.play(
            Transform(title, new_title)
        )

         # Create a NumberPlane
        plane = NumberPlane(x_range=[-10, 10], y_range=[-10, 10])
        self.add(plane)

        # Animation: Expand the NumberPlane bounds
        self.play(
            plane.animate.scale(.3),
            run_time=1.5,
            rate_func=linear,
        )

        # Create a rectangle to represent the path around the scaled plane
        path = Rectangle(width=20*0.3, height=20*0.3, color=RED).move_to(plane.get_center())

        # Animation: Draw the path
        self.play(Create(path), run_time=1.5)

        self.wait(2)

        self.play(Unwrite(title))

        self.play(
            plane.animate.shift(LEFT * 3),
            path.animate.shift(LEFT * 3),
            run_time=1.5
        )

        a10_f = MathTex(r"\forall x, x \leq \text{max}").to_edge(UP * 1.3 + RIGHT * 3)

        self.play(Write(a10_f), run_time=1.5)

        # First line of the regular text
        question_text_line1 = Text("So what happens if an operation", font_size=24).next_to(a10_f, DOWN, buff=0.5)
        self.play(Write(question_text_line1), run_time=1.5)

        # Second line of the regular text, centered relative to the first line
        question_text_line2 = Text("goes out of bounds?", font_size=24).next_to(question_text_line1, DOWN, aligned_edge=ORIGIN)
        self.play(Write(question_text_line2), run_time=1.5)

        self.wait(1.5)

        self.play(Unwrite(question_text_line2), run_time=1.5)
        self.play(Unwrite(question_text_line1), run_time=1.5)

        # Lines on the x-axis
        line1 = Line(plane.c2p(0, 0), plane.c2p(3, 0), color=YELLOW)
        line2 = Line(plane.c2p(3, 0), plane.c2p(11, 0), color=GREEN)

        # Add the lines to the scene
        self.play(Create(line1), Create(line2), run_time=1.5)
        self.play(FocusOn(plane.c2p(11, 0)))

        approach = Text("Strict Interpretation", font_size = 30)
        approach.move_to(a10_f)

        self.play(Transform(a10_f, approach))

        # Create the MathTex object for the mathematical expression
        math_expression = MathTex(r"\neg (\exists x)(x = \text{max} + 1)").next_to(approach, DOWN)

        # Display the math expression
        self.play(Write(math_expression))

        # Create copies of the lines but with red color to use for transformation
        line1_red = line1.copy().set_color(RED)
        line2_red = line2.copy().set_color(RED)

        # Transform lines to red
        self.play(Transform(line1, line1_red), Transform(line2, line2_red))

        # Then make the red lines disappear
        self.play(FadeOut(line1), FadeOut(line2))

        out_of_bounds_text = Text("If an operation goes out of bounds,", font_size=24).next_to(math_expression, DOWN)
        out_of_bounds_text_2 = Text("it ceases to exist", font_size=24).next_to(out_of_bounds_text, DOWN)

        self.play(Write(out_of_bounds_text))
        self.play(Write(out_of_bounds_text_2))   

        self.wait(2)

        new_approach = Text("Firm Boundary", font_size = 30)
        new_approach.move_to(approach)

        line1 = Line(plane.c2p(0, 0), plane.c2p(3, 0), color=YELLOW)
        line2 = Line(plane.c2p(3, 0), plane.c2p(11, 0), color=GREEN)

        self.play(
            Transform(a10_f, new_approach),
            FadeIn(line1), 
            FadeIn(line2)
            )
        
        new_math_expression = MathTex(r"\text{max} + 1 = \text{max}").next_to(approach, DOWN)

        n_out_of_bounds_text = Text("If an operation goes out of bounds,", font_size=24).next_to(math_expression, DOWN)
        n_out_of_bounds_text_2 = Text("it reverts to the max value.", font_size=24).next_to(out_of_bounds_text, DOWN)

        full_red_line = Line(plane.c2p(0, 0), plane.c2p(10, 0), color=GREEN)

        self.play(
            Transform(math_expression, new_math_expression),
            Transform(out_of_bounds_text, n_out_of_bounds_text),
            Transform(out_of_bounds_text_2, n_out_of_bounds_text_2)
        )

        line1_red = line1.copy().set_color(RED)
        line2_red = line2.copy().set_color(RED)

        self.play(
            Transform(line1, line1_red),
            Transform(line2, line2_red)
        )

        self.play(
            Transform(line2_red, full_red_line),
            FadeOut(line1),
            FadeOut(line2))

        self.play(
            Flash(plane.c2p(10, 0))
        )

        self.wait(2)

        approach3 = Text("Modulo Arithmetic", font_size = 30).move_to(approach)
        new_math_expression = MathTex(r"\text{max} + 1 = 0").next_to(approach, DOWN)
        n_out_of_bounds_text_2 = Text("it is computed modulo the max.", font_size=24).next_to(out_of_bounds_text, DOWN)




        self.play(Transform(a10_f, approach3))
        self.play(
            FadeIn(line1),
            FadeIn(line2),
            FadeOut(full_red_line),
            Transform(math_expression, new_math_expression),
            Transform(out_of_bounds_text_2, n_out_of_bounds_text_2)
        )

        short_green_line = Line(plane.c2p(10, 0), plane.c2p(11, 0), color=YELLOW)

        self.play(

            FadeOut(line2_red),
            FadeOut(line1),
            FadeOut(line2),
            FadeIn(short_green_line)
            
        )

        self.play(
            ApplyMethod(short_green_line.move_to, plane.c2p(0.5, 0))
        )

        self.play(
            Flash(plane.c2p(1, 0))
        )

        self.wait(4)












                

