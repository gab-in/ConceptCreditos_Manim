from manim import *
from manim_slides import Slide
config.background_color="#1E1E1E"
Text.set_default(font = "Manrope")

class main(Scene):
    def construct(self):
        # ------------------------- OBJETOS ---------------------------
        # O que quer que estivesse aqui antes
        exemplo=Text("Exemplo")

        # A logo
        logo = ImageMobject("/home/autumn/Downloads/icon_c.png").scale(0.2)
        logoOrigin=logo.copy().move_to(UP*8).rotate(PI)
        # O cursor
        cursor=ImageMobject("/home/autumn/Downloads/cursor.png").move_to(DOWN*6+LEFT*2).scale(0.05)
        
        # Os nomes e cargos em si
        titulo=Text("Créditos", font_size=80)
        titulo.color="#AA77C7"
 
        diretor = VGroup(Text("Diretor", font_size=60), Text("Alguém Ai", font_size=50)).arrange(DOWN, buff=0.3)
        tutor = VGroup(Text("Tutor", font_size=60), Text("Fulano de tal", font_size=50)).arrange(DOWN, buff=0.3)
        redator = VGroup(Text("Redator", font_size=60),Text("Fulaninho", font_size=50)).arrange(DOWN, buff=0.3)
        manimator = VGroup(Text("Manimators", font_size=60),Text("Aquele cara", font_size=50), Text("Aquele outro cara lá", font_size=40)).arrange(DOWN, buff=0.3)
        
        creditos = VGroup(titulo, diretor, tutor, redator, manimator).arrange(DOWN, buff=1).scale(0.5)
        # ------------------------ ANIMAÇÕES ---------------------
        # O que quer que tivesse aqui antes
        self.add(exemplo)

        # Abandonei o giro; o manim limita as ações nesse sentido, não dá para usar as constantes Rotate() e move_to() simultaneamente
        # e os métodos que eu encontrei de fazer girar tornam o tempo da animação instável. Sempre cai fora do tempo que eu queria
        self.play(
            logoOrigin.animate.become(logo),
            run_time=2
        )

        # Cursor aparece e se move
        self.play(cursor.animate.move_to(ORIGIN+RIGHT*0.2+DOWN*0.2))
        self.play(cursor.animate.scale(0.8),run_time=0.1,rate_func=linear)  # Clica
        self.play(cursor.animate.scale(1.2),run_time=0.1,rate_func=linear)  #
        
        # Vinheta Puxada
        self.play(
            GrowFromCenter(Rectangle(color="#0A0A0A",fill_opacity=1,width=20, height=10),run_time=0.5)
        )
        
        # Nomes e Cargos
        self.play(AnimationGroup(FadeIn(creditos.move_to(ORIGIN))))
            
        

        



