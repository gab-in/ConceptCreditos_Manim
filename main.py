from manim import *
from manim_slides import Slide

def blocoCargo(cargo,nome):
    cargoText=Text(cargo,font_size=20)
    nomeText=Text(nome,font_size=10)
    nomeText.next_to(cargoText,DOWN)

    return Group(cargoText,nomeText)

class main(Scene):
    def construct(self):
        # ------------------------- CONFIGURAÇÕES? -------------------------
        self.camera.background_color="#1E1E1E"

        # ------------------------- OBJETOS ---------------------------
        # Os nomes e cargos em si
        titulo=Tex("Creditos")

        blocos=[ 
                 blocoCargo("Diretor","Alguém Ai"),
                 blocoCargo("Tutor","Fulano de tal"),
                 blocoCargo("Redator","Fulaninho"),
                 blocoCargo("Manimators","Aquele cara \n\nAquele outro cara lá")
                ]
        
        creditos=Group(titulo)
        dist=titulo
        for bloco in blocos:
            bloco.move_to(dist.get_bottom() + DOWN)
            creditos.add(bloco)
            dist=bloco

        # ------------------------ ANIMAÇÕES ---------------------
        # Nomes e Cargos
        self.play(AnimationGroup(FadeIn(creditos.move_to(ORIGIN))))
            
        

        



