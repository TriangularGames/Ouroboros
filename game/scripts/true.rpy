label trueIntro:
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
    "The man you know all too well seated just in front of you."

    cadmus "Welcome back darling."
    "Cadmus says with a smile, the casualness of his words not lost on the moment. You've been here so many times."

    "Despite the straining of your eyes you glance at him, ever annoyed by the hanging bulb behind him."
    "His sharp jawline, messy dark hair, his exhausted sunken features, you wonder how he'd look without the dread."

    menu:
        "Nice to see you.":
            "He laughs, shuffling in his seat."
            cadmus "Happy to have you be honest for once."
            "He seems rather amused, any other person would take it as him pulling their leg-"
            "But he's being truthful."

    camera:
        subpixel True
        blur 0.0
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
    "Your eyes finally adjust, Cadmus coming into focus."
    "The dull thumping pain disappears into the background. His eyes focusing, peering into your soul."
    "The smirk on his face was soft- inviting."

    cadmus "We only have so much time..."
    ## TODO: add a worried expression here
    "He glances away, hand coming to your cheek."
    cadmus "but- I have a plan."

    "You smile at him, attempting to be reassuring to him."

    cadmus "You'll believe in me, won't you?"# he asks, his eyes practically begging you.

    menu:
        "Of course, as if there's anyone else to believe in.":
            "He smiles, pulling his hand from your cheek."
            cadmus "That makes me happy, my love."

    "Cadmus pulls out his knife- you're unsure why. Perhaps to fidget with it, maybe to look at."
    "The tightness of his grip on the knife, the way his muscles tense holding it, causing his hand to quiver."
    "He just as quickly puts the knife away."

    cadmus "I'm surprised you don't have more to say." #he says, even if his voice trails off,
    cadmus "I feel like normally you have so many quips..."
    cadmus "Perhaps- it wasn't even you."

    menu:
        "Did you want me to?":
            "You" "I still could ask you questions if you'd like."
            "You respond calmly, he glances away from you."
            cadmus "It's better you don't...I think." # he mutters,
            cadmus "The less we both talk and think about things the better it is."
            "You" "So it's kept hidden?"
            cadmus "Exactly..." # he smiles gently,
            extend "You truly are wonderful."

    "Cadmus' eyes trail up and down you- the intensity of his gaze..."
    "His affection oozes from it."

    "It's so charming."

    "You adjust your wrist from beneath the ropes, you had almost forgotten they were there. Probably one of the only things here that slipped your mind."

    cadmus "I'll get you out of those soon enough."
    "He seems determined about whatever plan he has in mind."

    menu:
        "We’ll get out of here soon enough.":
            "He chuckles."
            cadmus "Yes, of course."

    cadmus "Let the game begin then, right?"#he pulls in close, searching your eyes,
    cadmus "You'll only be out for a moment okay?"

    "You" "Just like the other times."

    cadmus "Yes, just like the other times."
    ## TODO: use the cover eyes thing
    centered "{cps=10}His hand delicately coming over your eyes."
    centered "{cps=10}The sounds slowly but surely fading away."

label trueRoute:
    ""