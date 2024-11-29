transform cameraReset:
    subpixel True
    xoffset 0
    yoffset 0
    xpos 0
    ypos 0
    xzoom 1.0
    zoom 1.0
    blur 0.0
    rotate 0.0
    matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)

transform shakeHead:
    subpixel True
    xpos -50*(not renpy.is_skipping())
    ease2 0.21*(not renpy.is_skipping()) xpos 50
    ease2 0.22*(not renpy.is_skipping()) xpos -50
    ease2 0.22*(not renpy.is_skipping()) xpos 50 
    ease2 0.20*(not renpy.is_skipping()) xpos 0

transform nodHead:
    subpixel True
    ease2 0.21*(not renpy.is_skipping()) ypos -10
    ease2 0.22*(not renpy.is_skipping()) ypos -30
    ease2 0.22*(not renpy.is_skipping()) ypos -10
    ease2 0.22*(not renpy.is_skipping()) ypos -30
    ease2 0.20*(not renpy.is_skipping()) ypos 0

transform continuousShake:
    subpixel True
    blur 8
    matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.15)*HueMatrix(0.0) 
    linear 0.1*(not renpy.is_skipping()) xoffset -2 yoffset 2 
    linear 0.1*(not renpy.is_skipping()) xoffset 3 yoffset -3 
    linear 0.1*(not renpy.is_skipping()) xoffset 2 yoffset -2
    linear 0.1*(not renpy.is_skipping()) xoffset -3 yoffset 3
    linear 0.1*(not renpy.is_skipping()) xoffset 0 yoffset 0
    .1
    repeat

transform shakeOnceDim:
    subpixel True
    blur 8
    matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.15)*HueMatrix(0.0) 
    linear 0.1*(not renpy.is_skipping()) xoffset -2 yoffset 2 
    linear 0.1*(not renpy.is_skipping()) xoffset 3 yoffset -3 
    linear 0.1*(not renpy.is_skipping()) xoffset 2 yoffset -2
    linear 0.1*(not renpy.is_skipping()) xoffset -3 yoffset 3
    linear 0.1*(not renpy.is_skipping()) xoffset 0 yoffset 0

transform shakeOnce:
    subpixel True
    blur 8
    linear 0.1*(not renpy.is_skipping()) xoffset -2 yoffset 2 
    linear 0.1*(not renpy.is_skipping()) xoffset 3 yoffset -3 
    linear 0.1*(not renpy.is_skipping()) xoffset 2 yoffset -2
    linear 0.1*(not renpy.is_skipping()) xoffset -3 yoffset 3
    linear 0.1*(not renpy.is_skipping()) xoffset 0 yoffset 0
    blur 0

transform shakeOnceNoBlur:
    subpixel True
    linear 0.1*(not renpy.is_skipping()) xoffset -2 yoffset 2 
    linear 0.1*(not renpy.is_skipping()) xoffset 3 yoffset -3 
    linear 0.1*(not renpy.is_skipping()) xoffset 2 yoffset -2
    linear 0.1*(not renpy.is_skipping()) xoffset -3 yoffset 3
    linear 0.1*(not renpy.is_skipping()) xoffset 0 yoffset 0

transform headPat:
    subpixel True 
    ypos 0 
    linear 0.20 ypos 15 
    linear 0.19 ypos 0 
    linear 0.19 ypos 10 
    linear 0.17 ypos 0

transform liftUp:
    subpixel True 
    ypos 0 
    power_in2 0.22 ypos -80 
    power_in2 0.13 ypos -70

transform zoomOnDoor:
    subpixel True 
    xpos 0 offset (0.0, 0.0) zoom 1.0 
    ease 0.50 xpos 0 offset (1926.0, 243.0) zoom 1.48

transform tiltHead:
    subpixel True 
    parallel:
        xpos 0 
        easein 0.26 xpos 150 
    parallel:
        rotate 0.0 
        linear 0.26 rotate 2.0 