define mus = '???'
define cadmus = Character("[mus]", color = "#cc0000")

# music files
define audio.basement = "audio/basement-ambience.mp3"
define audio.corrupted = "audio/basement-ambience-corrupted.mp3"

define music_vol = 0

## Run counter
default persistent.runNumber = 1

## If you're on a first run or not
default persistent.onReplay = False
default persistent.they = "they"
default persistent.their = "their"
default persistent.them = "them"
default persistent.s = ""
default persistent.es = ""
default persistent.person = "person"

## For what endings you've achieved
default persistent.FearBadEnd = False
default persistent.FearGoodEnd = False
default persistent.CareBadEnd = False
default persistent.CareGoodEnd = False
default persistent.CareSpecialEnd = False
default persistent.AmnesiaBadEnd = False
default persistent.AmnesiaGoodEnd = False
default persistent.ChaosEnding = False
default persistent.lastRoute = ""

## From caring ending
default persistent.code = ""

## if you say you remember him or not
define remember = False

## Vars for Route Determining
define caring = 0
define fearing = 0
define chaos = 0

init python:
    config.layers = ['backdrop', 'background', 'master', 'transient', 'screens', 'overlay']

# To prevent going back, uncomment when building
define config.rollback_enabled = False


# The game starts here.

label start:
    stop music fadeout 1.0
    # main font
    $ config.font_replacement_map[('BOOTERFZ.ttf', False, True)] = ('BOOTERFF.ttf', False, False)

    # dyslexic font
    $ config.font_replacement_map[('OpenDyslexic-Regular.otf', True, False)] = ('OpenDyslexic-Bold.otf', False, False)
    $ config.font_replacement_map[('OpenDyslexic-Regular.otf', False, True)] = ('OpenDyslexic-Italic.otf', False, False)
    $ config.font_replacement_map[('OpenDyslexic-Regular.otf', True, True)] = ('OpenDyslexic-Bold-Italic.otf', False, False)

    #music vol setting
    $ music_vol = _preferences.get_volume("music")

    camera:
        perspective True

    if persistent.onReplay == True:
        $ mus = 'Cadmus'
        $ persistent.they = "he"
        $ persistent.their = "his"
        $ persistent.them = "him"
        $ persistent.s = "s"
        $ persistent.es = "es"
        $ persistent.person = "man"
    
    scene black
    show black onlayer backdrop
    show bg basement:
        xpos -100
        ypos -270
    show vignette zorder 4:
        xpos -100
        ypos -270
    show black zorder 5
    show chair at default

    centered "{cps=10}{sc=1}Your head is pounding.{/sc}"
    centered "{cps=10}{sc=1}That's all you can focus on.{/sc}"
    centered "{cps=10}{sc=1}It's entirely disorienting.{/sc}"

    play music basement channel "music_CH1" fadein 1.0
    play music corrupted channel "music_CH2" volume 0.0

    "The sound of a whirring fan slowly fills your ears- a tapping of a foot- shallow breaths."

    hide black
    
    camera:
        subpixel True
        blur 3
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.15)*HueMatrix(0.0) 

    show cadmus at default
    show blank zorder 5 at blink
    "You slowly open your eyes, struggling to adjust to the dimly lit space you find yourself in."
    "A [persistent.person] seated on a chair just in front of you."
    show cadmus smileteeth with dis

    ## Comments from other routes when on a subsequent run
    if persistent.lastRoute == "FG":
        cadmus "Thought you could escape me, little mouse?"

    elif persistent.lastRoute == "FB":
        cadmus "I do hope you learned your lesson, you're safer with me, darling."

    elif persistent.lastRoute == "CG":
        cadmus "I always knew you loved me, my dear."

    elif persistent.lastRoute == "CB":
        cadmus "You have a clear head now, my love?"

    elif persistent.lastRoute == "CS":
        cadmus "Perhaps we'll be more considerate of each other's feelings now, won't we, darling?"

    elif persistent.lastRoute == "AG":
        cadmus "I do hope you've learned not to listen to your demons."

    elif persistent.lastRoute == "AB":
        cadmus "It seems my plan failed, we are both still here."

    else:
        ## This happens on first run
        cadmus "What a blessing, you're finally awake, beautiful."

    if persistent.runNumber > 1:
        menu:
            "What?":
                show cadmus smirking with dis
                cadmus "What?"
                "He chuckles, clearly amused by your question."
                cadmus "Did I say something strange?"
                cadmus "Let's not dwell on it."

            "You know?":
                show cadmus frowning with dis
                "He doesn't seem in a rush to comment."

    show cadmus normalSmile with dis
    "Your eyes strain to settle on [persistent.their] features, the hanging bulb behind [persistent.them] doing a dreadful job at letting you see."
    "Sharp jaw, ragged dark locks, features almost sunken."
    
    if persistent.onReplay:
        "You honestly wish he was a ghost."
    else:
        "If you didn't know any better, you'd think they're a ghost."

    menu:
        "Who are you?":
            show cadmus confused with dis
            cadmus "My my...how dreadful."
            show cadmus at lean
            camera:
                subpixel True
                blur 2
            "The chair creaks as [persistent.they] lean[persistent.s] forward."
            cadmus "You've forgotten? My poor baby..."
            show cadmus at sit
            $ caring += 1

        "Where am I?":
            show cadmus questioning with dis
            cadmus "You can't tell?"
            show cadmus at cadFidget
            "The chair creaks as [persistent.they] adjust[persistent.s] [persistent.their] legs."
            show cadmus disappointed with dis
            cadmus "My poor, poor baby..."
            $ fearing += 1

        "{glitch=15.5}Again?{/glitch}" if (persistent.onReplay and persistent.runNumber >= 3):
            show cadmus smileopenNU with dis
            "He just laughs."
            $ chaos += 1
    
    show cadmus normalSmile with dis
    camera:
        subpixel True
        blur 0.0
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
    
    "The [persistent.person] finally comes into focus, the pounding in your head subsiding for the moment."
    show cadmus smirking with dis
    
    if persistent.onReplay:
        "His green eyes watch you closely, the smirk on his face devilish- knowing."
    else:
        "Their green eyes feel like they're piercing your soul, the smirk on their face devilish- menacing."
    cadmus "Well, we have all the time in the world, I'll make sure you remember me."
    show cadmus normalSmile armsR with dis
    "[persistent.their!c] hand comes towards your face."

    if persistent.onReplay:
        menu:
            "You try to pull away again.":
                camera at shakeOnceNoBlur
                play sound moveInRope
                "Unfortunately for you, you are still tied to the chair you're seated in."
                camera at cameraReset
        
            "You don't move.":
                "You know it's no use, glaring at him."
    else:
        camera at shakeOnceNoBlur
        play sound moveInRope
        "You try to pull away from the stranger's gesture, but you realize you are tied to the chair you're seated in."
        camera at cameraReset


    show cadmus smileopenNU at lean
    "[persistent.they!c] laugh[persistent.s] as [persistent.they] caress[persistent.es] your cheek."

    cadmus "My, you are as feisty as the day we met."
    "[persistent.their!c] laughter continues as [persistent.they] stroke[persistent.s] your cheek with [persistent.their] thumb."
    show cadmus normalSmile with dis
    cadmus "You don't remember your dear, beloved boyfriend? It's Cadmus...surely you wouldn't forget my {i}dashing{/i} face, right?"
    $ mus = 'Cadmus'

    menu:
        "I don't remember you.":
            show cadmus disappointed with dis
            if persistent.lastRoute == "FG":
                cadmus "You ran away and forgot me?"
                cadmus "I'm {i}heartbroken{/i}."

            elif persistent.lastRoute == "FB":
                cadmus "You'll remember, but even if you don't I'll protect you, little mouse."

            elif persistent.lastRoute == "CG":
                cadmus "A heart never forgets, I {i}know{/i} you remember."

            elif persistent.lastRoute == "CB":
                cadmus "I find that {i}hard{/i} to believe."

            elif persistent.lastRoute == "CS":
                cadmus "You deny me, and now you forget me? Oh the {i}humanity{/i}!"

            elif persistent.lastRoute == "AG":
                cadmus "After the suffering I went through? You injure me a second time, love."

            elif persistent.lastRoute == "AB":
                cadmus "It's probably for the best, I'll succeed this time."

            else:
                ## This happens on first run
                cadmus "...what a shame."
                "Despite the fact you think he said it somberly, his eyes don't seem sad at all."
            
            show cadmus armsD -hand zorder 0 at sit
            $ fearing += 1

        "I remember you, you lie.":
            show cadmus smileopenNU with dis
            if persistent.lastRoute == "FG":
                cadmus "You didn't forget me after abandoning me?"

            elif persistent.lastRoute == "FB":
                cadmus "Oh joy, you do, little mouse? Even after what I did?"

            elif persistent.lastRoute == "CG":
                cadmus "You remember me?"

            elif persistent.lastRoute == "CB":
                cadmus "And that's all you remember?"

            elif persistent.lastRoute == "CS":
                cadmus "And you don't remember denying me?"

            elif persistent.lastRoute == "AG":
                cadmus "My suffering was worth it then?"

            elif persistent.lastRoute == "AB":
                cadmus "Certainly you'll let me succeed this time, right?"

            else:
                ## This happens on first run
                cadmus "You do?"

            $ _history = False
            show cadmus creepy at cadCreepy
            cadmus "{font=HelpMe.ttf}{cps=20}{size=40}P E R F E C T.{/size}{/cps}{/font}{nw}"
            show cadmus removeExtras removeBlood:
                xpan 0
                additive 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) blend 'normal'
            $ _history = True

            show cadmus normalSmile
            cadmus "Perfect."
            show cadmus resetArms smileopenNU with dis
            "His hand falls back to his thigh."
            show cadmus at sit
            cadmus "I would hope you wouldn't forget your lover's touch."
            $ remember = True
            $ caring += 1

        "{glitch=15.5}I remember you.{/glitch}" if (persistent.onReplay and persistent.runNumber >= 3):
            play music basement channel "music_CH1" volume 0.0
            play music corrupted channel "music_CH2" volume music_vol

            $ _history = False
            show cadmus questioning with dis
            cadmus "{cps=10}{sc=1.5}Hm. Do you now?{/sc}"
            show cadmus shadowTD with dis
            "{cps=10}{sc=3}His nails dig into your cheek, as he leans closer.{/sc}"
            show cadmus eyeBS smileopenNU with dis
            cadmus "{cps=20}Isn't th{font=HelpMe.ttf}{size=50}at JUST    {/size}{/font}{nw}"
            $ _history = True

            play music basement channel "music_CH1" volume music_vol
            play music corrupted channel "music_CH2" volume 0.0

            show cadmus -eyeBS -shadowTD -hand armsD smirkingSoft at default
            cadmus "I'm so glad, love!"
            show cadmus eyebrowsTD with dis
            "He tucks your hair behind your ear, eyes staring daggers into you."
            show cadmus smileopenNU with dis
            cadmus "I'd be broken up if you {i}ever{/i} forgot me."
            $ chaos += 1

    show cadmus regularE with dis
    "He watches you calmly, pulling something from his pocket- the glint catching your eye."

    show cadmus playfulK with dis
    play sound pullOutKnife
    "{font=HelpMe.ttf}{cps=10}{size=50}A knife.{/size}{/cps}{/font}"

    "There's a playfulness to the way he holds it."
    "Like you would a stick you find walking a trail as a young child."

    show cadmus smirking with dis
    cadmus "Darling, don't look so afraid."
    "He doesn't seem the least bit concerned for the way this looks."
    show cadmus tongueOut with dis
    cadmus "I wouldn't be so bold as to cause the being of my affections harm, would I?"

    menu:
        "You tied me to a chair.":
            if remember:
                show cadmus questioning with dis
                cadmus "You asked me to, don't you remember?"
                "He tilts his head, playing with the blade in his hand."
                cadmus "Does your head hurt? I hope you're alright, my love."
            else:
                show cadmus confused with dis
                cadmus "Did I?"
                "He tilts his head, running his fingers delicately along the blade."
                cadmus "You seem disoriented, how can you be so sure {i}you{/i} didn't ask to be tied to the chair?"
            $ fearing += 1

        "Why'd you take it out then?":
            show cadmus smileteeth with dis
            cadmus "Wouldn't you, if you had a knife in your pocket?"
            "He grins as he uses the tip of his knife to pick under his nails."
            $ caring += 1

        "{glitch=15.5}You're not going to use it again are you?{/glitch}" if (persistent.onReplay and persistent.runNumber >= 3):
            play music basement channel "music_CH1" volume 0.0
            play music corrupted channel "music_CH2" volume music_vol

            $ _history = False
            show vignette
            show cadmus quiveringEyes armsHK smilecreepyTeeth shadowTD at leanSnap
            show black at eyesShakingLean
            show cadmusblinkingneutral:
                zoom 1.0
                yalign 0.2
                xoffset -260
            show hair:
                zoom 1.0
                yalign 0.2
                xoffset -260
            "{cps=10}{sc=1.5}His smile is unnaturally wide,{p}holding the knife to your throat.{/sc}"
            cadmus "{cps=10}{sc=1.5}{font=HelpMe.ttf}{size=50}Wouldn't you like to find out...{/size}{/font}{/sc}{nw}"
            $ _history = True

            play music basement channel "music_CH1" volume music_vol
            play music corrupted channel "music_CH2" volume 0.0

            show vignette zorder 4
            hide black
            hide hair
            hide cadmusblinkingneutral
            show cadmus armsKP concern at default
            cadmus "Again?"
            cadmus "Why, I'd never dream of doing it once, let alone multiple times, my love."
            $ chaos += 1

    show cadmus regularE with dis
    "Cadmus' eyes trail up and down your figure- the way he looks at you...it unnerves you."
    show cadmus lick with dis
    "Like being eaten alive by his eyes."
    show cadmus neutral with dis

    if persistent.onReplay:
        "You know trying to move is entirely worthless."
        "It pisses you off."
    else:
        camera at shakeOnceNoBlur
        play sound moveInRope
        "Again, you try to move your limbs, but the ropes against you are tight."
        "You haven't lost feeling in them- which you hope to be a blessing rather than a curse."

    show cadmus smileopenNU with dis
    cadmus "Now, now, now."
    cadmus "We don't want you getting hurt."
    "His eyes return to staring directly into yours."

    menu:
        "What about you?":
            show cadmus confused with dis
            cadmus "Me?"
            show cadmus smirkingSoft with dis
            cadmus "Oh, how sweet, I promise you, I know my way around a knife."
            $ caring += 1
        
        "Why me?":
            show cadmus smirking with dis
            cadmus "You're my darling dearest of course."
            cadmus "Being treated oh so well. Don't you think?"
            $ fearing += 1

        "{glitch=15.5}Get this over with.{/glitch}" if (persistent.onReplay and persistent.runNumber >= 3):
            show cadmus annoyed with dis
            cadmus "Such {cps=20}{sc=2}impatience{/sc}."
            $ _history = False
            cadmus "{sc=3}We will have playtime soon enough.{/sc}{nw}"
            $ _history = True
            cadmus "Don't rush me darling~"
            show cadmus smirking with dis
            cadmus "But...I'll forgive you for it."
            $ chaos += 1

    cadmus "Now..."
    show cadmus regularE with dis
    cadmus "{cps=20}Be still."

    camera:
        subpixel True 
        blur 0.0 
        linear 0.50*(not renpy.is_skipping()) blur 5.0 

    centered "{cps=10}Everything suddenly goes out of focus."
    camera:
        subpixel True
        linear 0.5*(not renpy.is_skipping()) matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.15)*HueMatrix(0.0) 
    show black zorder 5 at closeEyes
    pause 1.0
    centered "{cps=10}Your head is pounding again."
    stop music channel "music_CH1" fadeout 1.0
    stop music channel "music_CH2"
    centered "{cps=10}The silence returns."
    $_skipping = False
    pause(3.0)

    ## Sets you on your route
    ## If you mainly select 1 option, thats the route you get
    ## Otherwise, you get the amnesia route
    if caring >= 3:
        $_skipping = True
        jump caring
    if fearing >= 3:
        $_skipping = True
        jump fearing
    if chaos >= 3:
        $_skipping = True
        jump chaos
    $_skipping = True
    jump amnesia


    return
