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

        # ------------------------ ANIMAÇÕES ---------------------
        self.add(creditos.move_to(DOWN*10))
        self.play(creditos.animate.move_to(ORIGIN),run_time=2.5)


        # Aqui tem que acontece o FadeIn() dos QR Codes ao mesmo tempo 
        self.play(creditos.animate.move_to(RIGHT*4), FadeIn(qrCodes.move_to(LEFT*4)), run_time=2)

        



