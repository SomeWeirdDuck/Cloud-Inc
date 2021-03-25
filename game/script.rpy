
label start:

    jump prologue

label splashscreen:
    scene black
    with Pause(1)

    scene gus_logo with dissolve
    with Pause(2)

    scene black with dissolve
    with Pause(0.5)

    scene limon_logo with dissolve
    with Pause(2)

    scene black with dissolve
    with Pause(1)

    return
