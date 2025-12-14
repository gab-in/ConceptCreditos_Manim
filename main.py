from manim import *
from manim_slides import Slide
config.background_color="#1E1E1E"
Text.set_default(font = "Manrope")

class Creditos(Scene):
    def construct(self):

        # ------------------------- OBJETOS ---------------------------
        # O que quer que estivesse aqui antes
        exemplo=Text("Exemplo")

        # O triangulo da vinheta 
        triangle1 = Triangle(color="#0F0F0F",stroke_width=8).move_to(UP*6)
        triangle2 = Triangle(color="#0F0F0F", fill_opacity=1).move_to(DOWN*2.5)
        
        # Os nomes e cargos em si
        titulo=Text("Créditos", font_size=80)
        titulo.color="#AA77C7"
 
        diretor = VGroup(Text("Diretor", font_size=60), Text("Alguém Ai", font_size=50)).arrange(DOWN, buff=0.3)
        tutor = VGroup(Text("Tutor", font_size=60), Text("Fulano de tal", font_size=50)).arrange(DOWN, buff=0.3)
        redator = VGroup(Text("Redator", font_size=60),Text("Fulaninho", font_size=50)).arrange(DOWN, buff=0.3)
        manimator = VGroup(Text("Manimators", font_size=60),Text("Aquele cara", font_size=50), Text("Aquele outro cara lá", font_size=40)).arrange(DOWN, buff=0.3)
        
        creditos = VGroup(titulo, diretor, tutor, redator, manimator).arrange(DOWN, buff=1).scale(0.5)

        # ------------------------ ANIMAÇÕES ---------------------
        self.add(exemplo)
        always_rotate(triangle1, rate=PI)
        self.play(triangle1.animate.shift(DOWN*8))
        self.play(Transform(triangle1,triangle2))
        self.remove(triangle1)
        self.play(
            ScaleInPlace(triangle2, 30)
        )
        
        # Nomes e Cargos
        self.play(FadeIn(creditos))
        self.wait()
            
        

        

