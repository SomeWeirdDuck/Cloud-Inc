init 1:
    $ flag_windows = False
    $ flag_linux = False

#BG

    image test = "images/bg/windows.jpg"
    image clouds = "images/bg/clouds2.jpg"
    image clouds2 = "images/bg/clouds.jpg"
    image hata = "images/bg/kvartira.jpg"
    image street = "images/bg/ylica.png"
    image black_screen = "images/bg/black.jpg"
    image Cloud_Building = "images/bg/office_building.jpg"
    image office = "images/bg/office.jpg"
    image bus = "images/bg/bus.jpg"
    image elevator = "images/bg/elevator.png"
    image d_273 = "images/bg/doors_273.jpg"
    image d_274 = "images/bg/doors_274.jpg"
    image d_500 = "images/bg/doors_500.jpg"
    image kab_day = "images/bg/cabinet_day.png"
    image kab_evening = "images/bg/cabinet_evening.png"
    image kab_lamp = "images/bg/cabinet_lamp.png"
    image kab_night = "images/bg/cabinet_night.png"

#CG
    
    image dead = "images/cg/cabinet_evening_dead.png"

#Logo

    image limon_logo = "images/bg/Limon_Production_Promo.png"
    image gus_logo = "images/bg/Gus_Entertainment_Promo.png"

#Sprites

    image kid1_crying = "images/sprites/kid1_crying.png"
    image hosy = "images/sprites/waifu.png"

#Characters
    python:
        import os
        if renpy.windows:
            flag_windows = True
            my_user = os.environ.get( "USERNAME" ) + "Ъ"
        elif renpy.linux:
            flag_linux = True
            import pwd
            my_user = pwd.getpwuid(os.getuid()).pw_name + "Ъ"
    define me = Character(my_user, color="#0000ab")
    define mom = Character("МацЪ", color="#00ff00")
    define kid1 = Character("илил ишшишлиш", color="#7f7f00", font="fonts/BirchCtt.ttf")
    define n = Character(None, kind=nvl)
    define op = Character("ОператорЪ", color="#a1e6f1")
    define rab = Character("РаботникЪ", color="#ba0000")
    define ht = Character("ХосиЪ", color="#da67a3")

#Music

    $ knock = "audio/fx/knock.mp3"
    $ nyaa = "audio/fx/nyaa.mp3"
    $ unravel = "audio/fx/unravel.mp3"
    $ m_nya = "audio/fx/man_nya.mp3"
    $ negr = "audio/fx/sad_negro.mp3"


#Some python
