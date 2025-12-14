from manim import *
from manim_slides import Slide
config.background_color="#1E1E1E"
Text.set_default(font = "Manrope")

class main(Scene):
    def construct(self):
        # ------------------------- OBJETOS ---------------------------
        # O que quer que estivesse aqui antes
        exemplo=Text("Exemplo")

        # Caractere {
        charEsquerda=Text("{", font_size=72, stroke_width=10).move_to(LEFT*8)
        charEsquerda.color="#AA77C7"
        # Caractere }
        charDireita=Text("}", font_size=72, stroke_width=10).move_to(RIGHT*8)
        charDireita.color="#AA77C7"
        
        # Os nomes e cargos em si
        titulo=Text("Créditos", font_size=80)
        titulo.color="#AA77C7"

        diretor = VGroup(Text("Diretor", font_size=60), Text("Alguém Ai", font_size=50)).arrange(DOWN, buff=0.3)
        tutor = VGroup(Text("Tutor", font_size=60), Text("Fulano de tal", font_size=50)).arrange(DOWN, buff=0.3)
        redator = VGroup(Text("Redator", font_size=60),Text("Fulaninho", font_size=50)).arrange(DOWN, buff=0.3)
        manimator = VGroup(Text("Manimators", font_size=60),Text("Aquele cara", font_size=50), Text("Aquele outro cara lá", font_size=40)).arrange(DOWN, buff=0.3)
        
        creditos = VGroup(titulo, diretor, tutor, redator, manimator).arrange(DOWN, buff=1).scale(0.5)
        # ------------------------ ANIMAÇÕES ---------------------
        # O que quer que existia antes
        self.add(exemplo)

        # Ei! Puxa a vinheta!
        self.play(
            AnimationGroup(
                charEsquerda.animate.move_to(LEFT),
                charDireita.animate.move_to(RIGHT)
            ))
        
        self.play(
            AnimationGroup(
                charEsquerda.animate.shift(LEFT*1.5),
                charDireita.animate.shift(RIGHT*1.5),
                run_time=0.8,
                rate_func=linear
            )
        )
        
        self.play(GrowFromCenter(Rectangle(color="#0F0F0F", fill_opacity=1, width=20, height=10)),run_time=0.5,rate_func=linear)
        
        # Nomes e Cargos
        self.play(AnimationGroup(FadeIn(creditos.move_to(ORIGIN))))
            
        

        



