from manim import *
from manim_slides import Slide

def escalaFonte(texto):
    out = Text(texto, font_size=72)
    out.scale(1/3)

    return out

def blocoCargo(cargo,nome):
    cargoText=escalaFonte(cargo)
    cargoText.font_size=20

    nomeText=escalaFonte(nome)
    nomeText.font_size=10
    nomeText.next_to(cargoText,DOWN)

    return Group(cargoText,nomeText)

def blocoQrCode(preview,qrCode):
    qrCode.scale(0.2)

    previewQrCode=escalaFonte(preview)
    previewQrCode.color="#AA77C7"
    previewQrCode.font_size=20
    previewQrCode.next_to(qrCode,UP)

    return Group(qrCode,previewQrCode)

class main(Scene):
    def construct(self):
        # ------------------------- CONFIGURAÇÕES? -------------------------
        self.camera.background_color="#1E1E1E"
        Text.set_default(font = "Manrope")

        # ------------------------- OBJETOS ---------------------------
        # Os nomes e cargos em si
        titulo=escalaFonte("Creditos")
        titulo.color="#AA77C7"

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
            
        # Os QrCodes para acesso às outras plataformas
        blocos=[
            blocoQrCode("Youtube", ImageMobject("/home/autumn/Imagens/Never1.png")),
            blocoQrCode("Moodle", ImageMobject("/home/autumn/Imagens/Never1.png")),
            #blocoQrCode("Discord", ImageMobject("/home/autumn/Imagens/Never1.png"))
        ]

        qrCodes=Group()
        dist=blocos[0]
        for bloco in blocos:
            bloco.move_to(dist.get_bottom()+DOWN*1.5)
            qrCodes.add(bloco)
            dist=bloco

        # MObjetos animados como menu ps2
        triangle = Triangle(color="#e07a5f", fill_opacity=1).move_to(LEFT*2 + DOWN*2)
        circle = Circle(color="#87c2a5", fill_opacity=1).move_to(RIGHT*2 + UP*2)
        square = Square(color="#525893", fill_opacity=1).move_to(LEFT*3 + DOWN*3) #LEFT*6+DOWN*2
        #.scale(0.4)

        # Aqui as rotas que o MObjects vão tomar
        rota1= Circle(radius=1.5)
        rota2 = rota1.copy().rotate(2*PI/3)
        rota3= rota1.copy().rotate(4*PI/3)

        # ------------------------ ANIMAÇÕES ---------------------
        # Nomes e Cargos
        self.add(creditos.move_to(DOWN*10))
        self.play(creditos.animate.move_to(ORIGIN),run_time=2.5)

        # Aqui tem que acontece o FadeIn() dos QR Codes ao mesmo tempo que os nomes e cargos vão para a direita
        self.play(creditos.animate.move_to(RIGHT*4), FadeIn(qrCodes.move_to(LEFT*4)), run_time=2)

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

            
        

        



