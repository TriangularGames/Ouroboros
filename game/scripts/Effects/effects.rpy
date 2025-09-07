define dis = {"master": Dissolve(0.5)}
define slowdis = {"master": Dissolve(1.5)}

## Images for Chaos:

define fearGood = "images/fearGoodEnd.webp"
define fearBad = "images/fearbad.webp"
define careGood = "images/caregood.webp"
define careBad = "images/carebad.webp"
define careSpecial = "images/carespecial.webp"
define amnesiaGood = "images/amnesiagood.webp"
define amnesiaBad = "images/amnesiabad.webp"

init:
    $ flash = Fade(0.15,0,.25, color="#800")

transform swipeDown:
    ypos -2000
    ease 0.8*(not renpy.is_skipping()) ypos 0

transform blink:
    "eyehalfopened.webp"
    .2*(not renpy.is_skipping())
    "eyeclosed.webp" 
    .2*(not renpy.is_skipping())
    "eyeopen.webp"
    .3*(not renpy.is_skipping())
    "eyehalfopened.webp"
    .2*(not renpy.is_skipping())
    "eyeclosed.webp"
    .2*(not renpy.is_skipping())
    "eyeopen.webp"
    .3*(not renpy.is_skipping())
    "eyehalfopened.webp"
    .2*(not renpy.is_skipping())
    "eyeclosed.webp"
    .2*(not renpy.is_skipping())
    "eyeopen.webp"
    alpha 0.0

transform closeEyes:
    "eyeopen.webp"
    .2*(not renpy.is_skipping())
    "eyeclosed.webp"
    .2*(not renpy.is_skipping())
    "eyehalfopened.webp"
    .3*(not renpy.is_skipping())
    "eyeopen.webp"
    .2*(not renpy.is_skipping())
    "eyeclosed.webp"
    .2*(not renpy.is_skipping())
    "black.webp"
    alpha 1.0

transform shortBlink:
    "eyeclosed.webp" 
    .2*(not renpy.is_skipping())
    "eyeopen.webp"
    .3*(not renpy.is_skipping())
    "eyehalfopened.webp"
    .2*(not renpy.is_skipping())
    alpha 0.0

## V Cadmus specific effects/animations here! V

transform cadFidget:
    subpixel True
    xalign 0.4 xoffset 0 yoffset 0 zoom 0.45
    ease 0.4*(not renpy.is_skipping()) xoffset -5 yoffset 4
    ease 0.3*(not renpy.is_skipping()) xoffset 0 yoffset 0
    ease 0.4*(not renpy.is_skipping()) xoffset 5 yoffset 4
    ease 0.3*(not renpy.is_skipping()) xoffset 0 yoffset 0
    xalign 0.4 xoffset 0 yoffset 0 zoom 0.45

## FIXME: put chuckles in where he chuckle pls
transform cadChuckle:
    subpixel True
    yzoom 1.0
    ease 0.15*(not renpy.is_skipping()) yzoom 1.01
    ease 0.15*(not renpy.is_skipping()) yzoom 1.0
    ease 0.15*(not renpy.is_skipping()) yzoom 1.01
    ease 0.15*(not renpy.is_skipping()) yzoom 1.0
    ease 0.15*(not renpy.is_skipping()) yzoom 1.01
    ease 0.15*(not renpy.is_skipping()) yzoom 1.0
    xalign 0.4 xoffset 0 yoffset 0 zoom 0.45 yzoom 1.0

transform eyesShakingSit:
    subpixel True
    "images/Cadmus/pupils_snake.webp"
    xalign 0.4 xoffset 0 yoffset -3 zoom 0.45
    xoffset -2.0 yoffset -1.0
    power_in3 0.06*(not renpy.is_skipping()) xoffset 2.0 yoffset 1.0
    power_in3 0.06*(not renpy.is_skipping()) xoffset -2.0 yoffset 2.0
    power_in3 0.06*(not renpy.is_skipping()) xoffset 2.0 yoffset 1.0
    power_in3 0.06*(not renpy.is_skipping()) xoffset -2.0 yoffset -1.0
    power_in3 0.06*(not renpy.is_skipping()) xoffset 2.0 yoffset -2.0
    power_in3 0.06*(not renpy.is_skipping()) xoffset -2.0 yoffset -1.0
    power_in3 0.06*(not renpy.is_skipping()) xoffset 2.0 yoffset 1.0
    power_in3 0.06*(not renpy.is_skipping()) xoffset -2.0 yoffset -1.0
    power_in3 0.06*(not renpy.is_skipping()) xoffset 0.0 yoffset -3.0
    pause 0.01
    repeat

transform eyesShakingLean:
    subpixel True
    "images/Cadmus/pupils_crazy.webp"
    zoom 1.0 yalign 0.2 xoffset -260
    xoffset -255 yoffset -5.0
    power_in3 0.06*(not renpy.is_skipping()) xoffset -270 yoffset 5.0
    power_in3 0.06*(not renpy.is_skipping()) xoffset -255 yoffset -4.0
    power_in3 0.06*(not renpy.is_skipping()) xoffset -270 yoffset 4.0
    power_in3 0.06*(not renpy.is_skipping()) xoffset -255 yoffset -3.0
    power_in3 0.06*(not renpy.is_skipping()) xoffset -270 yoffset 3.0
    power_in3 0.06*(not renpy.is_skipping()) xoffset -255 yoffset -2.0
    power_in3 0.06*(not renpy.is_skipping()) xoffset -270 yoffset 2.0
    power_in3 0.06*(not renpy.is_skipping()) xoffset -255 yoffset -1.0
    power_in3 0.06*(not renpy.is_skipping()) xoffset -260 yoffset 0.0
    pause 0.01
    repeat

# Calling above is as follows:
# show black at eyesShaking[insertkindhere]
# show cadmusblinkingneutral: (for sit) [also do hair]
#     xalign 0.4
#     xoffset 0
#     yoffset -3
#     zoom 0.45
# show cadmusblinkingneutral: (for lean) [also do hair]
#     zoom 1.0
#     yalign 0.2
#     xoffset -260
# show cadmus quiveringEyes

# For cleanup:
# hide black
# hide hair
# hide cadmusblinkingneutral

transform fallOff:
    subpixel True
    xrotate 0.0 
    parallel:
        xpos 0.4 
        linear 0.1*(not renpy.is_skipping()) xpos 0.3 
        linear 0.3*(not renpy.is_skipping()) xpos 0.25 
    parallel:
        ypos 0.2 
        linear 0.1*(not renpy.is_skipping()) ypos 0.42 
        linear 0.3*(not renpy.is_skipping()) ypos 1.07 
    parallel:
        zrotate 0.0 
        linear 0.1*(not renpy.is_skipping()) zrotate -18.0 
        linear 0.3*(not renpy.is_skipping()) zrotate -45.0 
    pos (0.25, 1.07) zrotate -45.0 

transform comeUp:
    subpixel True
    xrotate 0.0 
    parallel:
        xpos 0.25 
        linear 0.1*(not renpy.is_skipping()) xpos 0.3 
        linear 0.3*(not renpy.is_skipping()) xpos 0.4 
    parallel:
        ypos 1.07
        linear 0.1*(not renpy.is_skipping()) ypos 0.42 
        linear 0.3*(not renpy.is_skipping()) ypos 0.2
    parallel:
        zrotate -45.0 
        linear 0.1*(not renpy.is_skipping()) zrotate -18.0 
        linear 0.3*(not renpy.is_skipping()) zrotate 0.0 
    xalign 0.4 xoffset 0 yoffset 0 zoom 0.45

transform cadCreepy:
    subpixel True 
    parallel:
        additive 0.0 
        linear 0.18 additive 0.0 
    parallel:
        xpan -2.0 
        power_in3 0.06*(not renpy.is_skipping()) xpan 2.0 
        power_in3 0.06*(not renpy.is_skipping()) xpan -2.0 
        power_in3 0.06*(not renpy.is_skipping()) xpan 2.0
        power_in3 0.06*(not renpy.is_skipping()) xpan -2.0 
        power_in3 0.06*(not renpy.is_skipping()) xpan 2.0
        power_in3 0.06*(not renpy.is_skipping()) xpan -2.0 
        power_in3 0.06*(not renpy.is_skipping()) xpan 2.0
        power_in3 0.06*(not renpy.is_skipping()) xpan -2.0 
        power_in3 0.06*(not renpy.is_skipping()) xpan 0.0
    parallel:
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
        linear 0.6*(not renpy.is_skipping()) matrixcolor InvertMatrix(0.0)*ContrastMatrix(5.0)*SaturationMatrix(0.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) blend 'multiply'