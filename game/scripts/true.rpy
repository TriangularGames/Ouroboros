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

    cadmus "Welcome back darling." ## have him smiling here
    "The casualness of his words not lost on the moment. You've been here so many times."

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
    ## FIXME: add a worried expression here
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
    "You adjust your wrist from beneath the ropes, you had almost forgotten they were there."
    extend "Probably one of the only things here that slipped your mind."

    cadmus "I'll get you out of those soon enough."

    "He seems determined about whatever plan he has in mind."

    menu:
        "We'll get out of here soon enough.":
            "He chuckles."
            cadmus "Yes, of course."

    cadmus "Let the game begin then, right?"#he pulls in close, searching your eyes,
    cadmus "You'll only be out for a moment okay?"

    "You" "Just like the other times."

    cadmus "Yes, just like the other times."
    ## TODO: use the cover eyes thing
    centered "{cps=10}His hand delicately coming over your eyes."
    centered "{cps=10}{i}See you soon.{/i}" ## this line is spoken by him
    centered "{cps=10}The sounds slowly but surely fading away."
    hide cadmus

label trueRoute:
    ## open eyes anim thing
    ## maybe add some slight coloration to the background to indicate the difference
    "You struggle to open your eyes, as if weighed down by a force."
    "The room looks the same as it always has."
    "Though Cadmus is not in front of you as you'd expect."
    "You try to adjust yourself in your seat- but your limbs refuse to move."
    "The sensation is so odd, like you're paralyzed."
    "This hasn't happened before."
    "Why is it suddenly different?"
    "For the first time in a long time it feels...different."
    "You take another glance around the room."
    "It...{i}is{/i} the same room...right?"
    ## add door slamming sound
    "The sound of a door slamming startles you- only then are you able to move."
    ## footstep sounds
    "The radiating aura of the person approaching you is unlike anything you've experienced."
    show cadmus smirking at default
    "Cadmus sits across from you, like always."
    "{i}It is him right?{/i}"

    ## TODO: add effect to him having black scaleras
    cadmus "Darling, how lovely to see you."
    
    menu:
        "What's going on?":
            pass
        "Where were you?":
            pass
        "Are you alright?":
            pass

    "Though you try to speak, nothing escapes your lips."
    "He seems to find it rather amusing, as he closes the gap."

    cadmus "Oh my, did I simply take your breath away?" ## he chuckles
    "There's a deepness to his voice that..."
    extend "doesn't sound right."

    "His hand comes to your face"
    extend "- it's ice cold."
    "The sensation messes with your vision again, that force weighing on you only gets worse."
    "Something is definitely off."
    "So much for his {i}plan{/i}..."
    "What the hell is going on?"

    cadmus "Now now, don't give me that look."
    "His hand runs along your cheek, as he regards you lovingly."
    cadmus "You're perfectly safe with me."
    cadmus "You haven't forgotten that...have you?"

    menu:
        "I haven't.":
            ""
        "I don't know who you are.":
            ""
        "It would seem so.":
            ""
    
    "You're honestly surprised your voice even came out that time."
    "As he returns to his seat, you try to speak again."
    "And find you can't."
    "Was his hand being there somehow allowing you to talk?"
    "But..."
    extend "that's never been an issue before."

    menu:
        "Try to scream":
            pass
        "Try to move":
            pass
