from manim import *
from manim_slides import Slide

class main(Scene):
    def construct(self):
        # ------------------------- CONFIGURAÇÕES? -------------------------
        self.camera.background_color="#1E1E1E"
        
        # ------------------------- OBJETOS ---------------------------
        # MObjetos animados como menu ps2
        triangle = Triangle(color="#e07a5f", fill_opacity=1).move_to(LEFT*6 + DOWN*2)
        circle = Circle(color="#87c2a5", fill_opacity=1).move_to(RIGHT*6 + UP*2)
        square = Square(color="#525893", fill_opacity=1).move_to(LEFT*6 + UP*2) #LEFT*6+DOWN*2
        #.scale(0.4)

        # Aqui as rotas que o MObjects vão tomar
        rota1= Circle(radius=1.5)
        rota2 = rota1.copy().rotate(2*PI/3)
        rota3= rota1.copy().rotate(4*PI/3)

        # ------------------------ ANIMAÇÕES ---------------------
        #  FadeIn() dos MObjects 
        self.play(AnimationGroup(
            FadeIn(triangle.scale(0.4)),
            triangle.animate.move_to(rota1.point_from_proportion(0)),
            run_time=1,
            rate_func=linear
        ))
        
        # Rotaciona o Triangulo e da FadeIn() no círculo
        self.play(AnimationGroup(
            MoveAlongPath(triangle, rota1), 
            FadeIn(circle.scale(0.4)),
            circle.animate.move_to(rota1.point_from_proportion(1/3)),
            run_time=2,
            rate_func=linear
        ))

        # Rotaciona Triangulo e Circulo e da FadeIn() no quadrado
        self.play(AnimationGroup(
            MoveAlongPath(triangle,rota1),
            MoveAlongPath(circle,rota2),
            FadeIn(square.scale(0.4)),
            square.animate.move_to(rota1.point_from_proportion(2/3)),
            run_time=2,
            rate_func=linear
        ))

        # Rotaciona Triangulo, Circulo e Quadrado
        for i in range(3):
            self.play(AnimationGroup(
                MoveAlongPath(triangle,rota1),
                MoveAlongPath(circle,rota2),
                MoveAlongPath(square,rota3),
                run_time=2,
                rate_func=linear
            ))

        



