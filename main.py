from manim import *
from manim_slides import Slide

# Escala a fonte para resolver um bug interno do Manim com Fontes customizadas
def escalaFonte(texto):
    out = Text(texto, font_size=72)
    out.scale(1/3)

    return out

# Toma conte de organizar os cargos
def blocoCargo(cargo,nome):
    cargoText=escalaFonte(cargo)
    cargoText.font_size=26

    nomes = nome.split("\n")
    nome_objs = []

    dist = cargoText    # Distancia

    # Isso aqui é uma gambiarra para poder centralizar nomes separados por "\n" para casos de um cargo com vários nomes
    for linha in nomes:                                  # Separou anteriormente cada nome
        nomeText = escalaFonte(linha) 
        nomeText.font_size = 16
        
        # Centraliza horizontalmente
        nomeText.move_to([cargoText.get_x(), dist.get_bottom()[1] - 0.3, 0])

        nome_objs.append(nomeText)  # Coloca no vetor
        dist = nomeText # Atualiza distancia de referencia para esse novo nome já ajeitado

    return Group(cargoText, *nome_objs)


class main(Scene):
    def construct(self):
        # ------------------------- CONFIGURAÇÕES? -------------------------
        self.camera.background_color="#1E1E1E"
        Text.set_default(font = "Manrope")

        # ------------------------- OBJETOS ---------------------------
        # O que quer que estivesse aqui antes
        exemplo=Text("Exemplo")

        # A logo
        logo = ImageMobject("/home/autumn/Downloads/icon_c.png").scale(0.2)
        logoOrigin=logo.copy().move_to(UP*8).rotate(PI)
        # O cursor
        cursor=ImageMobject("/home/autumn/Downloads/cursor.png").move_to(DOWN*6+LEFT*2).scale(0.05)
        
        # Os nomes e cargos em si
        titulo=escalaFonte("Creditos")
        titulo.color="#AA77C7"
        titulo.font_size=30

        blocos=[ 
                 blocoCargo("Diretor","Alguém Ai"),
                 blocoCargo("Tutor","Fulano de tal"),
                 blocoCargo("Redator","Fulaninho"),
                 blocoCargo("Manimators","Aquele cara \nAquele outro cara lá")
                ]
        
        creditos=Group(titulo)
        dist=titulo
        for bloco in blocos:
            bloco.move_to(dist.get_bottom() + DOWN)
            creditos.add(bloco)
            dist=bloco
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
            
        

        



