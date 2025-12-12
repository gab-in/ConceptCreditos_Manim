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
            
        # MObjetos animados como menu ps2
        triangle = Triangle(color="#e07a5f", fill_opacity=1).move_to(RIGHT*6+UP*2)
        circle = Circle(color="#87c2a5", fill_opacity=1).move_to(UP*3)
        square = Square(color="#525893", fill_opacity=1).move_to(DOWN*2) #LEFT*6+DOWN*2
        #.scale(0.4)

        # Aqui as rotas que o MObjects vão tomar
        rota1= Circle(radius=1.5).shift(RIGHT*3)
        rota2 = rota1.copy().rotate(2*PI/3)
        rota3= rota1.copy().rotate(4*PI/3)

        # ------------------------ ANIMAÇÕES ---------------------
        self.add(creditos.move_to(DOWN*10))
        self.play(creditos.animate.move_to(ORIGIN),run_time=2.5)

        # Nome+Cargos vai para a direita e FadeIn() dos MObjects 
        self.play(AnimationGroup(
            creditos.animate.move_to(LEFT*3), 
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

        



