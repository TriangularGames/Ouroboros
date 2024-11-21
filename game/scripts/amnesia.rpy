label amnesia:
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

    show cadmus smileopenNU at default
    camera:
        subpixel True 
        blur 5.0
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 

    "You aren't sure how long it's been since you fell unconscious."
    "Feeling slightly off kilter."
    play music basement channel "music_CH1" fadein 0.5
    play music corrupted channel "music_CH2" volume 0.0
    hide black
    show blank zorder 5 at blink
    "Struggling to refocus, you noticed Cadmus is still across from you, smiling."

    camera:
        subpixel True
        linear 0.50*(not renpy.is_skipping()) blur 0.0 

    cadmus "Good morning, little mouse~"
    camera at cameraReset
    show cadmus smileclosedND with dis
    cadmus "I was starting to worry you weren't going to wake up."

    "You feel...glad to see him."
    "It's kind of reassuring for some reason."

    menu:
        "I wouldn't leave my darling behind":
            show cadmus smirkingSoft with dis
            cadmus "Oh, I'm simply charmed."
            cadmus "I'm happy that you wouldn't abandon me. To be without you would be devastating."

        "I'll always wake to you":
            show cadmus smirkingSoft with dis
            cadmus "And I you, dear."

    "You take the moment to get reoriented with the space."
    
    camera:
        subpixel True
        ease 4.0*(not renpy.is_skipping()) xpos -297 ypos 738 zoom 1.72

    "Due to the dim light, it's extremely hard to see if there's anything of note in this room."
    camera:
        subpixel True
        xpos -297 ypos 738 zoom 1.72
    "It feels like the edges of your vision are just pure darkness."

    camera:
        subpixel True
        ease_expo 3.00*(not renpy.is_skipping()) xpos 1818

    "Is it because your head is pounding?"
    camera:
        subpixel True
        xpos 1818
    "Why does your head hurt anyway?"

    camera:
        subpixel True
        ease_expo 3.0*(not renpy.is_skipping()) xpos 650

    "You feel a hand on your cheek."

    camera:
        subpixel True
        ease_expo 0.5*(not renpy.is_skipping()) xpos 0 ypos 0 zoom 1.0

    show cadmus concern armsR at lean with dis
    cadmus "Is everything else that much more interesting than me?"
    camera at cameraReset
    cadmus "Did I do something wrong?"

    camera at shakeHead
    "You shake your head firmly"
    show cadmus armsD -hand normalSmile with dis
    extend ", and he smiles, relaxed by your prompt response."
    camera at cameraReset
    cadmus "Good, you aren't uncomfortable are you?"
    show cadmus concern with dis
    cadmus "Are the ropes bothering you?"
    "Though you want to question his sudden concern...it's best not to."

    menu:
        "So you'll untie me?":
            show cadmus questioning with dis
            cadmus "Untie you? And lose you again? Nonsense my dear."
            show cadmus normalSmile at sit
            "He returns to his seat."
            show cadmus confused with dis
            cadmus "Why do you need to be anywhere else?"
            cadmus "I can take care of you right here."

            menu:
                "But what if I need to sleep?":
                    cadmus "The ropes aren't that tight are they?"
                    "Cadmus tugs at them, tilting his head curiously."
                    show cadmus normalSmile with dis
                    cadmus "Seems just fine to me, I don't know what you're so concerned about."
                
                "What if I want to hold you?":
                    show cadmus smirking with dis
                    show cadmus eyesH with dis
                    cadmus "I'm already holding you dear! There's no need to return the favour."
                    "You suppose he doesn't mean holding you {i}literally{/i}...the thought makes you immensely uncomfortable."
                    show cadmus smileopenNU blush eyebrowsN -shadowTD with dis
                    cadmus "You're so silly~ but thoughtful."
        
        "Stay silent":
            show cadmus neutral with dis
            "You both stare at each other."
            "{cps=10}..."
            "{cps=10}..."
            "{cps=10}..."
            show cadmus smileteeth with dis
            cadmus "I'm so happy..."
            "He checks the rope binding you, before taking a seat."
            show cadmus at sit

    camera at shakeOnceNoBlur
    "There's a jitter in your vision, your head is pounding."
    camera at continuousShake
    "The whole room feels like it's on stilts and shaking, but you know you aren't moving."
    hide cadmus
    show black zorder 5 at shortBlink
    "Cadmus vanishes from your view."
    "You feel nauseous."
    "Like something is worming it's way to you."
    "Trying to move out of the ropes is futile- you know that."
    "You can't calm yourself down."
    "You feel a lingering sensation against your neck."
    $ _history = False
    "Is it the bite?{nw}"
    $ _history = True
    "Like a snake squirming against your skin."
    $ _history = False
    "It's so hard to breathe.{nw}"
    $ _history = True
    "You struggle to even focus."
    $ _history = False
    "He's holding onto your neck.{nw}"
    $ _history = True
    "Where did he go?"
    $ _history = False
    "{cps=10}{font=HelpMe.ttf}H E ' S   R I G H T   T H E R E {/font}{nw}"
    $ _history = True
    camera at cameraReset
    show cadmus concern at default
    cadmus "Why the face darling?"
    "He seems rather calm, sitting in his seat as though he never moved."
    
    menu:
        "Does something feel weird?":
            show cadmus confused with dis
            cadmus "Weird? Weird how?"
            cadmus "Am I not doing good enough taking care of you?"

            "It almost irritates you, his {i}act{/i} of concern."
            "You find it hard to respond."
            "Or rather, you have no reason to respond."
            "The silence carries for longer than it should."
            "Clearly he was waiting for you to verbalize a response."
            "Why the hell should you?"

            show cadmus concern with dis
            cadmus "I'm sorry..."
            show cadmus armsR at lean
            "You feel his hand rest on your cheek."
            cadmus "I'll do better, I promise. I'm going to keep you safe and comfortable."
            jump AmnesiaGoodBranch

        "Stay quiet":
            show cadmus disappointed with dis
            cadmus "Ah- not talktive."
            "Despite his disappointment with your silence, he pulls himself together."
            "As though what turmoil your silence brought him didn't exist."
            show cadmus regularE with dis
            cadmus "That's okay, I'm right here."
            jump AmnesiaBadBranch

label AmnesiaGoodBranch:
    "You almost wanna ask if he's keeping you safe from {i}him{/i}."
    show cadmus regularE -armsR -hand at sit
    play sound drummingFingers
    "He pulls his hand away, continuing to drum against the chair."
    "Leavng you to wonder what the best course of action is."
    "You know you could free your hand if you wanted to- but you don't know where his knife is."
    "Glancing at his legs, it's hard to see."
    "The room is too dark to get a good look as to where his pockets might be."
    "Even if you manage to leave the ropes, get his knife- who knows what else he has on him."
    "That's not to mention..."
    "You don't even know {i}where{/i} the exit is."

    "It's hard to understand the situation you're even in."
    "Perhaps he wouldn't mind some questions?"
    "Whatever things come to mind should work."

    menu:
        "Am I your first?":
            show cadmus inLove with dis
            cadmus "I've only ever had eyes for you dear."
            cadmus "Why would I need anyone else? You're perfect for me~"
            cadmus "What about me? I'm your first aren't I?"

            menu:
                "Yes":
                    show cadmus smirkingSoft with dis
                    cadmus "Lucky me then~"
                    show cadmus eyesH blush with dis
                    cadmus "Have eyes for me and only me darling~"
                    "You can't help but smile a bit just at how excited he is."
                    "Though, you quickly come back to your senses."
                    "How bizarre, to feel any sense of happiness for someone who kidnapped you."
                    "Disgusting."
                
                "No":
                    show cadmus concern with dis
                    cadmus "Oh..."
                    show cadmus at lean
                    "He suddenly leans in closer to you."
                    show cadmus questioningA with dis
                    cadmus "Who were they? Got a name?"
                    cadmus "Actually."
                    show cadmus smileopenNU with dis
                    cadmus "Don't tell me. I'm sure I'll figure it out eventually~"
                    show cadmus eyesH blush with dis
                    cadmus "You'll have eyes for only me now, right?"
                    "As he stares, his smile is a tad bit unnerving."
                    camera at nodHead
                    "You nod"
                    show cadmus normalSmile at sit
                    extend ", he seems to relax."
                    "He looked so pathetic- as though it matters if he's the only one for you."
                    "His threat barely means anything now that you're already caught in his trap."
                    "What a weirdo."
        
        "Are you eating enough?":
            show cadmus confused with dis
            "Cadmus looks at you, completely taken off guard by the question."
            show cadmus eyesSld with dis
            "His eyes drift from being locked on yours."
            "You almost think he looks...sad."
            show cadmus smirkingSoft with dis
            "Whatever he was feeling quickly leaves, he looks at you confidently."

            cadmus "Of course darling, why are you so concerned?"
            show cadmus inLove with dis
            cadmus "I take care of you so well, obviously I can handle us both, don't you think?"
            "You suppose that's true, you don't feel like your life is entirely in danger."
            "Well...outside of his foreboding presence, and being tied to a chair."

        "What do you do when I'm sleeping?":
            show cadmus inLove with dis
            cadmus "Watch over you of course."
            cadmus "I have to make sure you're safe and no one takes you from me."
            "You can't help but feel unnerved by his response."
            "Though, the fact you even expected him to say something more {i}normal{/i}..."
            "That's entirely on you."

        "Do you know where we are?":
            show cadmus shock with dis
            "He looks caught off guard by the question."
            show cadmus concern with dis
            "Struggling to put his emotions in check, you assume."
            cadmus "Well...of course I do, I brought you here."
            cadmus "This place is mine. Why would we be somewhere I didn't know?"
            "He's probably just trying to pull your leg."
            "Cadmus {i}definitely{/i} knows something you don't."

    show cadmus normalSmile removeExtras with dis
    cadmus "Such a curious little mouse."
    cadmus "I'm appreciative of your curiosity."

    "He watches you closely, seemingly occupied by you."
    show cadmus at cadFidget
    "Fidgeting in his chair a bit."
    "It's hard to focus on anything, your mind feels so fuzzy."
    "Why are you here?"
    "Is he just taunting you?"

    show cadmus concern with dis
    cadmus "Darling?"
    cadmus "Are you worried about me? You seem so concerned."

    "You have no idea how he got that from anything you've done."
    "I guess asking him a question did do something."
    "You suppose...it might work to just play along with him."

    menu:
        "Is there anyway I can help you?":
            show cadmus frowning with dis
            cadmus "I don't think you have that luxury, or I guess the curse of being able to try."

            "You didn't really, you are tied to the chair."
            "If you actually {i}wanted{/i} to help him-"
            "Which you don't."

            cadmus "I don't mean to make you feel bad, love."
            show cadmus eyesSld with dis
            cadmus "I would be happy to have your help. I just...don't know if it's possible."


        "I'm sorry you're doing so much.":
            show cadmus embarassed with dis
            show cadmus smileclosedND
            "He smiles brightly, a faint blush on his cheeks."

            cadmus "Aren't you just the sweetest..."
            cadmus "I'll keep going knowing I have your support."

            "He's so sappy..."

    show cadmus normalSmile with dis
    "As he is seemingly lost in thought about what to do to help make you feel better."
    "It gives you time to think."
    "You focus on the ropes surrounding you."
    "There seems to be a loose spot near your hand."
    "It would be best to think of a game plan."
    "You could rid yourself of this situation"
    extend ", get out of here, leave it all behind."
    "You just have to get out of the ropes."
    "{b}Grab his knife.{/b}"
    "{b}End it all.{/b}"
    "{b}Be free.{/b}"
    "{b}It'll be so easy.{/b}"

label AmnesiaGoodEnding:
    camera at shakeOnce
    "You just barely manage to wrangle yourself free from the ropes."
    camera at cameraReset
    show cadmus scared at default with dis
    cadmus "Wait! Hold on!"
    "Cadmus looks horrified as you reach for his knife."

    "You" "Absolutely not!"
    camera:
        subpixel True
        ease 0.5*(not renpy.is_skipping()) zoom 1.5 xpos 500 ypos 500
    "You scream out, driving the knife into him."
    play sound stab
    show blank with flash
    show cadmus frown bloodyarmsD lidsC

    "You stab him a few times, his screaming echoing in the room."
    show cadmus at fallOff
    play sound silencepoint5
    queue sound bodyFall
    stop music channel "music_CH1" fadeout 1.0
    stop music channel "music_CH2" 
    "You're both covered in blood."
    hide cadmus
    hide black
    camera at cameraReset
    "It's...horrifying..."
    "But you feel so...in control."
    show black zorder 5 at closeEyes
    hide blank
    "Your head starts pounding, causing you to forcibly shut your eyes."
    "It hurts so bad."
    hide bg basement
    show bg wall
    show cadmus lidsC armsT at default:
        subpixel True matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.16)*HueMatrix(0.0) 
    "Everything feels like it's moving and shaking."
    hide black
    play music basement channel "music_CH1" volume music_vol
    show blank zorder 5 at blink
    "When you open them, everything looks different."
    "As your eyes focus, Cadmus sits limply in a chair in front of you."
    "Ropes hold him there."
    "He's against the wall you just were."
    show cadmus lidsR gasp shadowTU eyeBS with dis
    "He opens his eyes, and looks horrified."

    cadmus "...why did you let {b}it{/b} in?"

    stop music channel "music_CH1" fadeout 1.0

    ## fade out, title "Amnesia: Good Ending?"
    if persistent.onReplay == False:
        $ persistent.onReplay = True
    $ persistent.AmnesiaGoodEnd = True
    $ persistent.lastRoute = "AG"
    $ persistent.runNumber += 1
    $ renpy.save_persistent()
    scene black with fade
    pause (0.5)
    show text "{font=HelpMe.ttf}{sc=2}Amnesia: Good Ending?{/sc}{/font}" with Dissolve(1.5)
    pause (2.0)
    hide text
    return

label AmnesiaBadBranch:
    show cadmus armsR smileopenNU at lean
    "He places his hand against your cheek, his grin wide as he stares intently at you."
    cadmus "My beautiful dear, you are irreplaceable~"

    "Letting it linger there, without him talking- you can pay attention to the way it feels."
    "{cps=15}His hand is cold."
    show cadmus smirk with dis
    $ _history = False
    "Maybe he's cold blooded.{nw}"
    $ _history = True
    "Maybe he{fast} has bad blood flow?"
    "His entire hand feels like ice against your face."

    show cadmus armsD -hand at sit
    "Cadmus pulls his hand away, shaking it off dramatically before letting it drop to his side."

    show cadmus lidsS with dis
    cadmus "You should be far more wary than you are. Don't you think?"

    "You don't even bother answering."
    "It's clear enough he's just asking it, not expecting much of an answer."
    "It's not like you really have much to give anyway."
    "Plus you can't even really avoid anything."
    "You quite literally can't move."

    cadmus "There is much time for you to consider your actions, my love."
    show cadmus smileteeth -lidsS with dis
    "He smiles as he swipes his feet against the concrete floor."
    show cadmus confused with dis
    cadmus "Or I suppose your words. Perhaps both. Wouldn't that be amusing?"

    "You" "Why should I even play your game?"

    show cadmus questioning with dis
    cadmus "Why so scared?"
    show cadmus at lean
    "He leans towards you, eyeing you curiously."
    show cadmus concern with dis
    cadmus "Am I really oh so frightening? I couldn't hurt a fly~"

    menu:
        "You aren't scary":
            cadmus "I'm not?"
            show cadmus smirk eyebrowsN with dis
            cadmus "Good."
            show cadmus at sit
            "He leans back into his seat, eyes still trained on you."
            show cadmus lidsR with dis
            cadmus "I'd be worried if you were, we are partners after all."
            show cadmus smileclosedND with dis
            cadmus "Communication is {i}very{/i} important darling."

            "You can't tell if he added that last part in as a joke, given you both haven't spoken very much since you...arrived?"
            "Given how cloudy your head is, you aren't exactly sure {i}when{/i} it was that you got here."
            "A stark reminder of how wrapped up in his lies you are."
        
        "You're frightening":
            show cadmus smirking with dis
            "He cocks his head curiously, lingering close to you."
            cadmus "How could I be?"
            cadmus "You always told me you {i}adored{/i} my smile, darling."
            show cadmus concern with dis
            "He pouts, clearly a bit upset. Doing what you can only assume to be puppy eyes at you."
            cadmus "I'm a well behaved young man, I promise~"

            show cadmus smileteeth eyebrowsN with dis
            show cadmus at sit
            "With a grin he proceeds to lean back away from you, giving you back your precious breathing room."
            "Much needed breathing room."

    hide cadmus with dis
    "Cadmus stands from his seat, walking just out of your view."
    "Is he going somewhere?"
    "What is he doing?"

    menu:
        "Where are you going?":
            ## add headpat effect perhaps?
            "He laughs, placing his hand on your head."
            cadmus "I'm just stretching my legs, no need to panic."
            cadmus "Just going to walk the room. I'll be quick."
            "He starts to walk, his footsteps filling your ears."

        "Don't leave me.":
            show cadmus at default with dis
            "He plops himself down in the chair, if only for a moment."
            show cadmus smileopenNU with dis
            cadmus "Silly mouse~ I'm just stretching my legs, I'll be back shortly."
            hide cadmus with dis
            "He once again stands, and sounds like he's stepping away."

            menu:
                "Beg him to stay":
                    cadmus "I have to go dear, I'll be back."
                    "He simply continues to walk away from you."
                
                "Let him go.":
                    "{nw}"

    
    "Him not being directly across from you gives you a moment to breathe."
    "In a weird way, still being able to hear his footsteps is comforting."
    "Finding your captor...comforting."
    "How strange."
    "You are no closer to understanding what his goal is, but even still."
    "You are safe, in some unexplainable way."
    "He's looking after you, he isn't hurting you."
    "He cares for you."
    "He loves you."
    "Cadmus comes into view, on the other side of the room, just barely visible."
    "He disappears back into the darkness just as quickly as he appeared."
    "Trying to comprehend all this...it hurts your head."
    
    camera at continuousShake
    "That pounding sensation returns."
    "He hasn't tried to hurt you- the ropes aren't even tight."
    "So why does your head hurt so much?"
    "It feels like something eating away at you."
    camera at cameraReset

    show cadmus normalSmile at default with dis
    cadmus "I'm back, darling."
    "He suddenly appears in front of you, that feeling in your head immediately vanishing."
    cadmus "Hope you didn't miss me too much."

    "You feel glad to see him...but..."
    "Everything feels so strange."
    hide cadmus with dis
    "He stands up, pacing just nearby."
    "Muttering to himself."
    "Nonsense you can't understand."
    "What is he doing?"
    show cadmus angie at default
    "He sits back down abruptly."

    "You" "{cps=15}...Cadmus?"
    jump AmnesiaBadEnding

label AmnesiaBadEnding:
    play music basement channel "music_CH1" volume 0.0
    play music corrupted channel "music_CH2" volume music_vol
    show cadmus armsHK with dis
    "Cadmus suddenly pulls out the knife."

    cadmus "This has to end."
    play sound heartBeat
    "You can't help but be afraid."

    show cadmus armsD with dis
    "The knife slashes through the ropes, he tosses the knife to the floor."

    show cadmus eyesCRA with dis
    cadmus "I have to break it...that's the only way..."
    "He's muttering like he's lost his mind."
    cadmus "The cycle has to break...it has to break. It's going to break."

    "You don't want to stay around to find out what in the world he's mumbling about."
    "With yourself free from your shackles, you shove him away."
    camera:
        subpixel True
        ease_expo 3.00 xpos 1920 ypos 300 zoom 1.5
    "Standing and running for the door."
    cadmus "{size=50}LIKE HELL YOU'RE LEAVING!{/size}"
    camera at shakeOnce
    "You feel him grab your shoulders from behind you."
    camera:
        subpixel True
        xpos 1920 ypos 300 zoom 1.5
    "You can't move."
    "God why won't your legs move?!"
    "Run idiot!!"

    show blank with flash
    "You feel his teeth dig into your neck, and scream."
    show black at closeEyes
    "Your eyes shut from how horrible the pain is."
    "He holds you firmly as he bites harder, your legs barely keeping you standing."
    "All sensations fade away."
    stop music channel "music_CH1" 
    stop music channel "music_CH2" fadeout 1.0

    scene black with fade
    pause (0.5)

    cadmus "...we'll never be free from {b}it{/b}...will we..."

    ## fade out, title "Amnesia: Bad Ending?"
    if persistent.onReplay == False:
        $ persistent.onReplay = True
    $ persistent.AmnesiaBadEnd = True
    $ persistent.lastRoute = "AB"
    $ persistent.runNumber += 1
    $ renpy.save_persistent()
    pause (0.5)
    show text "{font=HelpMe.ttf}{sc=2}Amnesia: Bad Ending?{/sc}{/font}" with Dissolve(1.5)
    pause (2.0)
    hide text
    return