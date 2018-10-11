from big_ol_pile_of_manim_imports import *


class Shapes(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        line = Line(RIGHT*3, RIGHT*5)
        triangle = Polygon(ORIGIN, UR, DR)

        self.add(line)
        self.play(ShowCreation(circle))
        self.play(FadeOut(circle))
        self.play(GrowFromCenter(square))
        self.play(Transform(square, triangle))


class MoreShapes(Scene):
    def construct(self):
        circle = Circle(color=PURPLE_A)
        square = Square(fill_color=GOLD_B, fill_opacity=1, color=GOLD_A)
        square.move_to(UL)
        circle.surround(square)
        
        pointer = CurvedArrow(RIGHT*2, RIGHT*5, color=MAROON_C)
        
        arrow = Arrow(LEFT, UP)
        arrow.next_to(circle, DL)

        rectangle = Rectangle(width=3, height=2)
        rectangle.next_to(arrow, DL)
        ellipse = Ellipse(width=3, height=1, color=RED)
        ellipse.shift(DR*2)
        ring = Annulus(inner_radius=0.5, outer_radius=1, color=BLUE)
        ring.next_to(ellipse, RIGHT)

        self.add(pointer)
        self.play(FadeIn(square))
        self.play(Rotating(square), FadeIn(circle))
        self.play(GrowArrow(arrow))
        self.play(GrowFromCenter(rectangle), GrowFromCenter(ellipse), GrowFromCenter(ring))


class AddingText(Scene):
    def construct(self):
        first_text = TextMobject("Writing with manim is fun")
        second_line = TextMobject("and easy to do!")
        second_line.next_to(first_text, DOWN)
        third_text = TextMobject("for me and you!")
        third_text.next_to(first_text, DOWN)

        self.add(first_text, second_line)
        self.wait(2)
        self.play(Transform(second_line, third_text))
        self.wait(2)
        second_line.shift(DOWN*3)
        self.play(ApplyMethod(first_text.shift, UP*3))


class AddingMoreText(Scene):
    def construct(self):
        quote = TextMobject("Imagination is more important than knowledge")
        quote.set_color(RED)
        quote.to_edge(UP)
        quote2 = TextMobject("A person who never made a mistake never tried anything new")
        quote2.set_color(YELLOW)
        author = TextMobject("-Albert Einstein")
        author.scale(0.75)
        author.next_to(quote.get_corner(DR), DOWN)

        self.add(quote)
        self.add(author)
        self.wait(2)
        self.play(Transform(quote, quote2), ApplyMethod(author.move_to, quote2.get_corner(DR) + DOWN + LEFT*2))
        self.play(ApplyMethod(author.match_color, quote2))
        self.play(FadeOut(quote), Transform(author, author.copy().scale(1.3)))


class RotateAndHighlight(Scene):
    def construct(self):
        square = Square(side_length=5, fill_color=YELLOW, fill_opacity=1)
        
        label = TextMobject("Text at an angle")
        label.bg = BackgroundRectangle(label, fill_opacity=1)
        label_group = VGroup(label.bg, label)  # Order matters
        label_group.rotate(TAU / 8)
        
        label2 = TextMobject("Boxed text", color=BLACK)
        label2.bg = SurroundingRectangle(label2, color=BLUE, fill_color=RED, fill_opacity=0.5)
        label2_group = VGroup(label2, label2.bg)  # Order matters
        label2_group.next_to(label_group, DOWN)

        label3 = TextMobject("Rainbow")
        label3.scale(2)
        label3.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)
        label3.to_edge(DOWN)

        self.add(square)
        self.play(FadeIn(label_group))
        self.play(FadeIn(label2_group))
        self.play(FadeIn(label3))


class BasicEquations(Scene):
    def construct(self):
        eq1 = TextMobject("$\\vec{X}_0 \\cdot \\vec{Y}_1 = 3$")
        eq1.shift(UP*2)
        eq2 = TexMobject("\\vec{F}_{net} = \\sum_i \\vec{F}_i")
        eq2.shift(DOWN*2)

        self.play(Write(eq1))
        self.play(Write(eq2))


class ColoringEquations(Scene):
    def construct(self):
        line1 = TexMobject("\\text{The vector }", "\\vec{F}_{net}", "\\text{ is the net force on object of mass}")
        line1.set_color_by_tex("force", BLUE)
        line2 = TexMobject("m", "\\text{ and acceleration }", "\\vec{a}")
        line2.set_color_by_tex_to_color_map({
            "m": YELLOW,
            "{a}": RED
        })
        sentence = VGroup(line1, line2)
        sentence.arrange_submobjects(DOWN, buff=MED_LARGE_BUFF)
        self.play(Write(sentence))


class UsingBraces(Scene):
    def construct(self):
        eq1A = TextMobject("4x + 3y")
        eq1B = TextMobject("=")
        eq1C = TextMobject("0")
        eq2A = TextMobject("5x - 2y")
        eq2B = TextMobject("=")
        eq2C = TextMobject("3")
        eq1B.next_to(eq1A, RIGHT)
        eq1C.next_to(eq1B, RIGHT)
        eq2A.shift(DOWN)
        eq2B.shift(DOWN)
        eq2C.shift(DOWN)
        eq2A.align_to(eq1A, LEFT)
        eq2B.align_to(eq1B, LEFT)
        eq2C.align_to(eq1C, LEFT)

        eq_group = VGroup(eq1A, eq2A)
        braces = Brace(eq_group, LEFT)
        eq_text = braces.get_text("A pair of equations")

        self.add(eq1A, eq1B, eq1C)
        self.add(eq2A, eq2B, eq2C)
        self.play(GrowFromCenter(braces), Write(eq_text))


class UsingBracesConcise(Scene):
    def construct(self):
        eq1_text = ["4", "x", "+", "3", "y", "=", "0"]
        eq2_text = ["5", "x", "-", "2", "y", "=", "3"]
        eq1_mob = TexMobject(*eq1_text)
        eq2_mob = TexMobject(*eq2_text)
        eq1_mob.set_color_by_tex_to_color_map({
            "x": RED_B,
            "y": GREEN_C
        })
        eq2_mob.set_color_by_tex_to_color_map({
            "x": RED_B,
            "y": GREEN_C
        })

        for i, item in enumerate(eq2_mob):
            item.align_to(eq1_mob[i], LEFT)

        eq1 = VGroup(*eq1_mob)
        eq2 = VGroup(*eq2_mob)
        eq2.shift(DOWN)
        eq_group = VGroup(eq1, eq2)
        braces = Brace(eq_group, LEFT)
        eq_text = braces.get_text("A pair of equations")

        self.play(Write(eq1), Write(eq2))
        self.play(GrowFromCenter(braces), Write(eq_text))


class PlotFunctions(GraphScene):
    CONFIG = {
        "x_min": -10,
        "x_max": 10,
        "y_min": -1.5,
        "y_max": 1.5,
        "graph_origin": ORIGIN,
        "function_color": RED,
        "axes_color": GREEN,
        "x_labeled_nums": range(-10, 12, 2),
    }

    def construct(self):
        self.setup_axes(animate=True)
        func_graph_cos = self.get_graph(self.func_cos, self.function_color)
        func_graph_sin = self.get_graph(self.func_sin)
        vert_line = self.get_vertical_line_to_graph(TAU, func_graph_cos, color=YELLOW)
        graph_label_cos = self.get_graph_label(func_graph_cos, label="\\cos(x)")
        graph_label_sin = self.get_graph_label(func_graph_sin, label="\\sin(x)", x_val=-10, direction=UP/2)
        two_pi = TexMobject("x = 2 \\pi")
        label_coord = self.input_to_graph_point(TAU, func_graph_cos)
        two_pi.next_to(label_coord, UR)

        self.play(ShowCreation(func_graph_cos), ShowCreation(func_graph_sin))
        self.play(ShowCreation(graph_label_cos), ShowCreation(graph_label_sin), ShowCreation(vert_line), ShowCreation(two_pi))

    def func_cos(self, x):
        return np.cos(x)

    def func_sin(self, x):
        return np.sin(x)

