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
    centered "{cps=10}His hand delicately comes over your eyes."
    centered "{cps=10}{i}See you soon.{/i}" ## this line is spoken by him
    centered "{cps=10}The sounds slowly but surely fading away."
    hide cadmus

label trueRoute:
    ## open eyes anim thing
    ## maybe add some slight coloration to the background to indicate the difference
    $ mus = '???'
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
    ## TODO: have him bug out here
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
            cadmus "Good."
            "There's a tone behind it that's comfortingly famliar."
            "So it is him."
            "Or...at least, somewhere that person you know is in front of you."

        "I don't know who you are.":
            cadmus "Hm."
            "He seems to ponder, almost like he'll say more."
            "But he doesn't."
            "You can faintly see tears welling up in his eyes..."
            "They're gone in an instant."

        "It would seem so.":
            cadmus "So it would."
            "The slight smile reminiscent of ones you've seen countless times."
            "Yet, somehow it feels so foreign in this moment."
    
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
    
    ## TODO: sound distorts here, and maybe just black out the screen
    "Suddenly your head is forced down, staring at the floor."
    "You gasp for air- unable to pull yourself back up."
    "He grasps your shoulders, the only things grounding you to the present."
    "Other than the feeling of the concrete floor beneath your feet."
    "There's a complete imbalance in yourself."
    "Clearly he isn't himself anymore."
    "{i}Clearly{/i} this isn't the same space anymore."
    "Or rather-"
    "This place has never existed."
    "It's been the same thing, over"
    extend ", and over"
    extend ", and over"
    extend ", and over."
    "{i}The plan must be in motion.{/i}"
    "...and if this isn't him in front of you..."

    menu:
        "Acknowledge {b}{i}IT{/b}{/i}":
            pass
    
    "You" "Let me go."
    "You can feel the way your voice struggles to escape your lips."
    "Finally able to control your own body. Looking up-"
    ## TODO: add cadmus looking posessed spooky
    extend " the man in front of you is just barely recognizable."

    cadmus "Feisty~"
    cadmus "Just like I remember."
    "Even as he pulls away, his fingers linger on your shoulders."
    "The cold sensation of his touch sticks to you through your shirt."
    "You watch as the eyes you've come to find comfort in search you."
    "All familiarity about him entirely lost in his far seeing gaze."

    cadmus "You look so beautiful." # he sighs as he says this
    "He laughs jovially, leaning back slightly in his seat as he regards you."
    cadmus "Confusion did always look best on you."

    "His compliment makes your skin crawl."
    "This is definitely not the man you hoped to see."
    "It's hard to decide what to even do now-"
    "Be Angry?"
    extend " Kick and scream?"
    "Stay calm?"
    extend " Be upset?"
    "Your overwhelmed by the whirlwind of emotions and thoughts running rampant through your mind."
    "He seems to be gleeful at your turmoil." # he is smiling creepily here
    "There's only one thing that comes to mind."

    "You" "Let him go!"
    "Pulling yourself forward, the ropes fighting to hold you to the chair."
    "A desperate plea to whatever is in front of you."
    "You feel...lost without the familiar man you've come to know."

    cadmus "Let...{i}who{/i} go?" # he chuckles
    cadmus "You see anyone else here, little mouse?"
    cadmus "Come now...you haven't lost yourself already, have you?" # he pouts mocking concern

    menu:
        "I'm completely certain.":
            pass
        "I know what I'm asking.":
            pass
        "Don't toy with me.":
            pass
    
    cadmus "You're so sure, hm?"
    cadmus "What's his name?" # change the font here perhaps?

    "Of course, you know his name."
    extend " You've been with him through thick and thin at this point!"
    "He's been there through every loop."
    "Every bout of pain-"
    "Every struggle-"
    "Every escape-"
    "...everything."
    "{cps=10}..."
    "You...know his name."
    "{cps=10}..."
    "{cps=10}..."
    pause 2.0
    "His...name."
    pause 1.0

    cadmus "Not so certain now~ are we?" # he sounds so horribly dripplingly amused
    # caresses cheek here
    cadmus "Oh there, there, mousey~"
    cadmus "It's alright, {i}I'm{/i} here for you."

    menu:
        "I don't want YOU!":
            cadmus "What a shame..."
            cadmus "Unfortunately, I don't see many options here for you, darling."
            cadmus "I'll be here for you in your time of need."

        "I {i}doubt{/i} that.":
            cadmus "Well..."
            extend "I'm in this room, and whoever this \"he\" is, isn't."
            cadmus "Clearly, I'm much better than him- since I haven't abandoned you in your time of need."
    
    "You don't bother responding, entirely too focused over the question."
    "{i}His name.{/i}"
    "How did you even forget it?"
    "How could you even forget it?"
    "It is floating somewhere in the back of your mind."
    "It's drifting right on the tip of your tongue."
    "You know it...it's right there."

    cadmus "Come now little mouse, don't lose sight of the present."
    cadmus "I can provide {i}anything{/i} your gorgeous little head desires."
    cadmus "What more would you need..."
    extend "When you have me~"

    menu:
        "Give him back then.":
            "He seem to ponder your request"
            extend "- if only for a moment, just to amuse himself."
            cadmus "I haven't the faintest idea who you're talking about, darling."
            cadmus "If {i}only{/i} there was some way to know...gosh, even a single thing about him!" # he sighs dramatically
            cadmus "Like {b}a name{/b}."
            "You" "You know who I'm referring to."
            cadmus "Hm, can't say I do, little mouse."

        "Let me leave.":
            "Adjusting himself in his seat"
            extend "- he appears to think about his response."
            cadmus "No." # he is smiling sweetly here
            cadmus "Can't have that."
            cadmus "The world is far far too dangerous. The safest place for you..."
            cadmus "is right here, with me."
            "You" "You're lying."
            cadmus "Wouldn't dream of it, little mouse."
    
    cadmus "Hm...clearly, you doubt me." # he huffs, sounding dejected but its hard to say if he's more upset or annoyed
    "As if he couldn't state something {i}more{/i} obvious."
    "His words aren't important, he's clearly trying to distract you."
    "What if you're losing sight of things the longer this continues?"
    "What else have you forgotten?"
    "Maybe it's just his name that escaped you-"
    "Escaped?!"
    "Right-"
    extend " he had a plan!"
    "Is this...part of his plan?"
    "You don't know anything for certain..."
    "But he told you to believe in him."
    "If whatever this is might be part of it"
    extend "- perhaps there's something to it."
    "To entertain the...thing...in front of you."

    cadmus "...Are you done thinking to yourself?" # he is right up in your face here
    "You're completely taken aback by his sudden closeness."
    "Though- how he got there without you even noticing matters little."
    "Especally in this \"reality.\""

    cadmus "There's that little sparkle~" # he pulls back here
    cadmus "It's {i}so{/i} unbeveliably easy to figure out when you space out, y'know?"
    cadmus "Ah...it makes me so horribly lonely..."
    cadmus "Keep your everything focused on me, alright little mouse?"

    ## TODO: the interogation scene

    if persistent.code = "slide":
        "He gently takes your hand-"
        extend " though you immediately try to pull away, his hold is firm."
        "Carefully, his finger slides down your palm."
        "His touch is..."
        extend "warm."
        "{i}He's here.{/i}"
        "Though you can't help but feel relieved, now is not the time to let it show."
        "The end of this is near..."
        extend "you can feel it."

    elif persistent.code = "doubletap":
        "He carefully moves his hand to your palm-"
        extend " trying to yank your hand away from him, though he refuses to let you go."
        "The hand that carefully holds your wrist is warm."
        "He taps his finger twice."
        "{i}It's that code you made.{/i}"
        "Focus...if you need to focus, it must almost be over, right?"
        "As much as it's reassuring, the last thing you need is for that to be obvious."

    "As you lock eyes with the man in front of you"
    extend "...he looks {i}confused{/i}."
    "He takes his hand away, seemingly struggling to contain his disbelief."

    menu:
        "Something wrong?":
            pass
        "Everything okay?":
            pass
    
    cadmus "...that's impossible."
    "The softness to his voice completely takes you off guard- like a lost child."

    centered "{cps=10}What's my name?"

    "The thought invades your mind unexpectedly-"
    "The room around you almost seems to quiver..."
    extend "as though it's moments from complete collapse."

    centered "{cps=10}What's my name?"

    cadmus "...no. NO!"
    "He almost seems to flicker between states of being."
    ## TODO: add typing of Cadmus' name here
    $ mus = 'Cadmus'
    "Watching him as the name finally returns to you feels completely surreal."
    "Though, everything about this place is a complete impossibility."
    # cadmus flickering stops here
    "Finally...the man you've longed to see falls into place in front of you."

    cadmus "Hurry! We have to go, quickly."
    "He swiftly cuts the ropes off you, holding his hand out as he stands."

    menu:
        "Take his hand":
            pass
    
    "You both make a mad rush to the door, running through the seemingly endless corridor towards the light."
    "Daring, you take a glance behind you-"
    "It's as if a black hole opened up, and you watch as the room you've been sequestered to for so long..."
    "Collapses under itself."
    "Entirely ceasing to exist."

    cadmus "Hey, stay focused here!"
    "He tightens his grip on your hand, pulling you closer as you begin climbing the stairs out."
    # show outside cg here
    pause (0.5)

    "The breeze and sunlight hitting your face is the most refreshing feeling in the world."
    "Though the rush causes you to lose your footing- Cadmus protects you as you both tumble into the grass."
    "The prison you were trapped in crushing into nothingness behind you overwhelms your senses-"
    ## TODO: black hole sound effect of somekind and a pause
    "Then silence."
    "You take some time to catch your breath."
    "There's peace in that- and the gentle breeze, the rustling of the grass."
    "You...escaped."
    "Cadmus and you escaped."
    ## show the final cg here
    "You lift yourself up to look at him, his eyes shut as he struggles to catch his breath."

    menu:
        "We...made it.":
            pass
    
    "He laughs, opening his eyes to look up at you."
    "A soft blush tickles his cheeks as his gaze is full of nothing but love and admiration."

    cadmus "Yeah...we did."
    cadmus "I'm so glad! I-I can hardly believe it."
    "You" "Me neither."
    cadmus "...there's lots I'd like to do."
    cadmus "Y'know, once we get properly away from here."
    "You" "Like...what?"
    cadmus "Like, take you out. On a date."
    cadmus "If you want."

    menu:
        "I'd love that.":
            # he laughs sweetly
            cadmus "...I love you so much."
            "You" "Me too."

        "Maybe we should hang out first.":
            "You" "We do barely know each other."
            cadmus "Heh...ya you're right."
            cadmus "We'll do whatever you want!"
            cadmus "Starting..."
            extend "right now."
            "You" "Whatever I want?"
            cadmus "Anything, just say the word."
            "You" "How about, going home?"
            cadmus "I like it! C'mon-"

    cadmus "Let's get going."
    "You both stand, and he takes your hand like it's the most natural thing in the world."
    "And you both walk through the field- back home."