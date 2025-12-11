from manim import *
from manim_slides import Slide

def blocoCargo(cargo,nome):
    cargoText=Text(cargo,font_size=20)
    nomeText=Text(nome,font_size=10)
    nomeText.next_to(cargoText,DOWN)

    return Group(cargoText,nomeText)

def blocoQrCode(preview,qrCode):
    qrCode.scale(0.2)
    previewQrCode=Text(preview,font_size=20)
    previewQrCode.next_to(qrCode,UP)

    return Group(qrCode,previewQrCode)

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
            
        # Os QrCodes para acesso às outras plataformas
        blocos=[
            blocoQrCode("Youtube", ImageMobject("/home/autumn/Imagens/Never1.png")),
            blocoQrCode("Moodle", ImageMobject("/home/autumn/Imagens/Never1.png")),
            blocoQrCode("Discord", ImageMobject("/home/autumn/Imagens/Never1.png"))
        ]

        qrCodes=Group()
        dist=blocos[0]
        for bloco in blocos:
            bloco.move_to(dist.get_bottom()+DOWN*1.5)
            qrCodes.add(bloco)
            dist=bloco

        # Finalmente, as figuras geométricas da logo do Manim
        triangle = Triangle(color="#e07a5f", fill_opacity=1).move_to(LEFT*6+DOWN*2)
        circle1 = Circle(color="#87c2a5", fill_opacity=1).move_to(LEFT*6+UP*3)
        circle2 = Circle(color="#c7a444", fill_opacity=1).move_to(RIGHT*6+DOWN*3)
        square = Square(color="#525893", fill_opacity=1).move_to(RIGHT*6+UP*2)
        grupoFlutuanteDireito=VGroup(triangle,circle1)
        grupoFlutuanteEsquerdo=VGroup(circle2,square)
        #.scale(0.8)

        # ------------------------ ANIMAÇÕES ---------------------
        # Nomes e Cargos
        self.add(creditos.move_to(DOWN*10))
        self.play(creditos.animate.move_to(ORIGIN),run_time=2.5)

        # Aqui tem que acontece o FadeIn() dos QR Codes ao mesmo tempo que os nomes e cargos vão para a direita
        self.play(creditos.animate.move_to(RIGHT*2.5), FadeIn(qrCodes.move_to(LEFT*2.5)), run_time=2)

        # Aqui as figuras geométricas do Manim vão aparecer
        self.play(Create(grupoFlutuanteDireito.scale(0.8)),Create(grupoFlutuanteEsquerdo.scale(0.8)),run_time=2)

        movimentos = [
                        (UP*0.5, DOWN*0.5),
                        (DOWN*0.5, UP*0.5),
                        (DOWN*0.5, UP*0.5),
                        (UP*0.5, DOWN*0.5),
                        ]
        for i in range(2):  # repete o ciclo
            for mov_dir, mov_esq in movimentos:
                self.play(
                    AnimationGroup(
                        grupoFlutuanteDireito.animate.shift(mov_dir),
                        grupoFlutuanteEsquerdo.animate.shift(mov_esq),
                        run_time=3
                    )
                )

            
        

        



