label true:
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
    centered "{cps=10}{sc=1}A sensation that has become horribly familiar to you.{/sc}"
    centered "{cps=10}{sc=1}It's almost welcoming.{/sc}"

    "The sound of a whirring fan slowly fills your ears- a tapping of a foot, shallow breaths."
    hide black
    
    camera:
        subpixel True
        blur 3
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.15)*HueMatrix(0.0) 
    
    show cadmus at default
    show blank zorder 5 at blink
    "You slowly open your eyes, struggling to adjust to the dimly lit space you find yourself in."
    show cadmus smirkingSoft with dis
    "The man you know all too well seated just in front of you."

    cadmus "Welcome back darling."
    "The casualness of his words not lost on the moment. You've been here so many times."

    show cadmus normalSmile with dis
    "Despite the straining of your eyes you glance at him, ever annoyed by the hanging bulb behind him."
    "His sharp jawline, messy dark hair, his exhausted sunken features, you wonder how he'd look without the dread."

    menu:
        "Nice to see you.":
            show cadmus smileopenNU with dis
            "He laughs, shuffling in his seat."
            cadmus "Happy to have you be honest for once."
            "Any other person would take it as him pulling their leg, but he's being truthful."

    camera:
        subpixel True
        blur 0.0
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
    "Your eyes finally adjust, Cadmus coming into focus."
    "The dull thumping pain disappears into the background. His eyes focusing on you- peering into your soul."
    show cadmus smirkingSoft with dis
    "The smirk on his face was soft- inviting."

    show cadmus concern with dis
    cadmus "We only have so much time..."
    show cadmus armsR at lean
    "His hand gently rests on your cheek."
    cadmus "But- I have a plan."

    "You smile at him, attempting to be reassuring to him."

    show cadmus questioning with dis
    cadmus "You'll believe in me, won't you?"

    menu:
        "Of course, as if there's anyone else to believe in.":
            show cadmus normalSmile armsD -hand at sit
            "He smiles, pulling his hand from your cheek."
            cadmus "Only the best, my love."

    show cadmus armsHK with dis
    play sound pullOutKnife
    "Cadmus pulls out his knife,"
    extend " to no fanfare. Just to look at, or perhaps to fidget."
    "The tightness of his grip on the knife, the way his muscles tense holding it, causing his hand to quiver."
    show cadmus armsD with dis
    "He just as quickly puts the knife away."

    cadmus "I'm surprised you don't have any questions,"
    cadmus "I feel like normally you have some comments to make...perhaps it wasn't even you that had those comments to make."

    menu:
        "Did you want me to?":
            "You" "I still could ask you questions if you'd like."
            cadmus "It's better you don't...I think."
            cadmus "The less we both talk and think about things the better it is."
            "You" "So it's kept hidden?"
            show cadmus smileopenNU with dis
            cadmus "Exactly!"
            show cadmus smirkingSoft with dis
            extend " You truly are wonderful."

    "Cadmus' eyes trail up and down you- the intensity of his gaze..."
    "He truly cares so much."
    "It's so charming."

    "You adjust your wrist from beneath the ropes, you had almost forgotten they were there. Probably one of the only things here that slipped your mind."

    cadmus "I'll get you out of those soon enough." 
    "He seems determined about whatever plan he has in mind for you both."
    "You can only hope it's a good one."

    menu:
        "We'll get out of {i}here{/i} soon enough.":
            "He chuckles."
            cadmus "Yes, of course."

    cadmus "Let the game begin then, right?"
    cadmus "You'll only be out for a moment, okay?"

    "You sigh a bit, the theatrics have become a bit dull."
    "Though, you don't have much of a choice in the matter."
    "The game has to begin."
    "You" "Just like the other times."

    cadmus "Yes, just like the other times."
    "You feel his hand coming over your eyes,"
    pause 1.0
    stop music channel "music_CH1" fadeout 1.0
    stop music channel "music_CH2"
    extend " as the sounds fade away."
    $_skipping = False
    pause(3.0)

## TODO: finish true ending
## This is where the actual "True Route" begins
