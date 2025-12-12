from manim import *
from manim_slides import Slide

def escalaFonte(texto):
    # Escala o código para resolver um bug interno do Manim com Fontes customizadas
    out = Text(texto, font_size=72)
    out.scale(1/3)

    return out

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

        # ------------------------- OBJETOS ---------------------------
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
        # Nomes e Cargos
        self.add(creditos.move_to(DOWN*10))
        self.play(creditos.animate.move_to(ORIGIN),run_time=2.5)
            
        

        



