init 1:


#BG

    image test = "images/bg/windows.jpg"
    image clouds = "images/bg/clouds2.jpg"
    image hata = "images/bg/kvartira.jpg"
    image street = "images/bg/ylica.png"
    image black_screen = "images/bg/black.jpg"
    image Cloud_Building = "images/bg/vorota.jpg"
    image office = "images/bg/office.jpg"

#CG



#Logo

    image limon_logo = "images/bg/Limon_Production_Promo.png"
    image gus_logo = "images/bg/Gus_Entertainment_Promo.png"

#Sprites

    image kid1_crying = "images/sprites/kid1_crying.png"

#Characters
    python:
        import os
        import pwd
        my_user = pwd.getpwuid(os.getuid()).pw_name + "Ъ"
    define me = Character(my_user, color="#0000ab")
    define mom = Character("Мацъ", color="#00ff00")
    define kid1 = Character("илил ишшишлиш", color="#7f7f00", font="fonts/BirchCtt.ttf")
    define n = Character(None, kind=nvl)
    define op = Character("ОператорЪ", color="#a1e6f1")
    define rab = Character("РаботникЪ", color="#ba0000")
    define ht = Character("Хоси", color="#da67a3")

#Music

    $ knock = "audio/fx/knock.mp3"
    $ nyaa = "audio/fx/nyaa.mp3"
    $ unravel = "audio/fx/unravel.mp3"
    $ m_nya = "audio/fx/man_nya.mp3"
    $ negr = "audio/fx/sad_negro.mp3"


#Some python
