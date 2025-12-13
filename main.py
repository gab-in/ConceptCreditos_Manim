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
        Text.set_default(font = "Manrope")

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
            
        

        



