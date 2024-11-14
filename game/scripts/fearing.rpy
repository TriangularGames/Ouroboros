label fearing:

    ## for when the jump to Good Choice 1 occurs in BadBranchA
    define BadBranchA = False

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

    "You aren't sure how long it's been since you fell unconscious."
    play music basement channel "music_CH1" fadein 0.5
    play music corrupted channel "music_CH2" volume 0.0
    hide black
    camera:
        subpixel True 
        blur 5.0
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    show blank zorder 5 at blink
    "Struggling to refocus again, you notice Cadmus is no longer sitting in front of you."
    camera:
        subpixel True 
        linear 0.5*(not renpy.is_skipping()) blur 0.0

    "What the hell did that man DO to you?"
    "Were you drugged?"
    "Have you been drugged?"
    "Will you die here?"

    "Uncertainty invades your mind."

    menu:
        "Pull on the ropes.":
            camera at shakeOnce
            "Try as you might the ropes never budge."
            camera at cameraReset
            "Though the motion of your struggle scoots the chair about a centimeter."
            "You're uncertain as to how to unravel yourself from the binds...maybe you'll figure something out eventually."

        "Take a look around.":
            "This room is entirely barren, outside of yourself, the chair you are on, the ropes that bind you, and the empty chair across from you."
            "With the lone light hanging from the ceiling, and how darkly coloured the walls are, it's impossible to tell the scale of this place."

        "Listen for him.":
            "It's entirely too quiet here."
            "Cadmus must be somewhere, the idea of your captor leaving you entirely to your own devices seems unlikely."

    show black zorder 5 at shortBlink
    show cadmus normalSmile at default with dis
    cadmus "My little mouse is awake~!"
    camera at shakeOnce
    "His voice startles you straight."
    camera at cameraReset
    "He is sitting in the chair in front of you...as if he never left."

    cadmus "You missed me?"
    show cadmus smileopenNU with dis
    cadmus "I'm sure you did!"
    show cadmus inLove with dis
    cadmus "I missed you~"

    "His fingers excitedly drum his thighs as he speaks."

    cadmus "Not that there's anyone else here...it's just you. and. me."
    show cadmus smirkingSoft with dis
    cadmus "All of our love captured in a single place. Isn't that divine?"

    show cadmus at lean
    "Cadmus stands from the chair, leaning close to you."
    "His eyes search you hungrily."
    show cadmus lick with dis
    "His tongue dancing across his lips."

    show cadmus inLove with dis
    cadmus "You truly are the most beautiful being for my affections."

    "His whispering breath dancing across your cheeks."

    cadmus "We have all the time in the world to fawn over each other."

    menu:
        "So you'll untie me?":
            show cadmus normalSmile with dis
            cadmus "Untie you? And lose you again? Nonsense my dear."
            show cadmus at sit
            "He returns to his seat, acting in mock concern."
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

    show cadmus regularE removeExtras with dis
    cadmus "I suppose...I should get you something to drink."
    show cadmus armsR at lean
    "His hand reaches for your face."
    "Even though you try to pull back from him, it's entirely in vain."
    "His index finger captures your chin- thumb gently rubbing your bottom lip."
    cadmus "Your lips are dry...I'll fix this darling."

    hide cadmus with dis
    "He starts moving away, but his hand on your chin is the last thing to leave your vision."
    "Footsteps echoing throughout the space- not as much as you expected it would."
    "The room must be much smaller than it appears, the minimal light is doing wonders to cause you panic over the sheer scale of the darkness surrounding you."

    "There's an itching at the back of your neck...you can't shake it."
    "This feeling of unease enveloping you."
    "You're trapped."
    "How did you get here?{nw=180}"
    "How will you get out?{nw=180}"
    "Does anyone miss you?{nw=180}"
    camera:
        subpixel True
        linear 0.5*(not renpy.is_skipping()) matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.15)*HueMatrix(0.0) 
    $ _history = False
    centered "The itchy feeling is getting so much worse."
    centered "It's so itchy."
    centered "It's so itchy."
    centered "It's {size=50}whERE HE BIT YOU.{nw}"
    $ _history = True
    camera at cameraReset
    "It's where the rope burns, you assume."

    "You hear running water off in the corner."
    "While he's not around, you decide to reassess the ropes."
    "{cps=10}..."
    "{cps=10}..."
    "There's a loose spot near your right hand."

    define FearbadRoute = False
    menu:
        "Wiggle to free your hand.":
            "You shouldn't take chances."
            "{cps=10}..."
            "You manage to free your hand."
            "Of course, keeping it concealed within the ropes."
            "The last thing you need is him realizing you've done this."
            $ FearbadRoute = True
        
        "Keep your hand there.":
            "It'll be a good thing to know you can free your hand in a pinch."
            "You're sure if you free it now...he might notice it."

    show cadmus normalSmile at default with dis
    "Cadmus promptly returns, cupped in his hands is a chipped teacup, lacking a handle."
    "He sits in front of you again."
    show cadmus smirkingSoft with dis
    cadmus "Your drink of water, my beloved!"
    "He holds the cup out towards you."
    cadmus "Ah- of course, you can't actually drink it yourself."
    cadmus "Let me help you~"

    "He brings the cup to your lips."
    "What if he poisoned the water?"
    "Is the cup even full of water?"
    "What in the world is he giving to you?!"
    $ _history = False
    "You try to keep your lips shut-{nw}"
    "You can't drink it!{nw}"
    "...You're so thirsty-{nw}"
    "Your lips are so dry...{nw}"
    "No! No!{nw}"
    "He's trying to kill you!{nw}"
    $ _history = True
    show cadmus smileopenNU with dis
    "He's trying to{fast} help you."
    "You happily drink the water...it feels so nice."
    "It's like you haven't had anything to drink in so long."

    show cadmus smileteeth with dis
    cadmus "Good little mouse~"
    cadmus "Much better, right?"

    "He pulls the cup away from your lips."
    "You follow the cup- desperately wanting more."
    show cadmus armsR at lean
    "He gently places his hand on your chin."
    "Wiping your lips with his thumb, smiling as he does so."

    show cadmus smirkingSoft with dis
    cadmus "I'll be faster next time, I promise."

    if FearbadRoute:
        jump FearBadBranchA
    
    ## GOOD ROUTE
    ## Bad Route stuff will be after the entire good route
    show cadmus regularE armsD -hand at sit
    "Cadmus sets the cup down on the floor, immediately going back to staring at you."
    "His eyes feel like they're reading every minute detail about you."
    "You can only wonder what he's able to decipher from you."
    "His gaze is illegible."

label FearBadChoice1:
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

            if BadBranchA:
                jump FearBranchACont
        
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

            if BadBranchA:
                jump FearBranchACont
    
    show cadmus concern with dis
    cadmus "Well, there must be something I can do to quell any possible concerns you might have..."
    "His fingers drum against the back of the chair as he ponders."
    show cadmus armsHighSH at lean
    "Just as you go to speak, he presses a finger to your lips."
    show cadmus smirk with dis
    cadmus "Ah ah ah~ Those ropes {i}must{/i} stay."
    cadmus "It's to keep you safe."

    "You almost wanna ask if he's keeping you safe from {i}him{/i}, but given how sharp he is about things..."
    "It's best you don't tempt the devil."
    show cadmus regularE -armsHighSH at sit
    "He pulls his hand away, continuing to drum against the chair."
    "Leavng you to wonder what the best course of action is."
    "You know you could free your hand if you wanted to- but you don't know where his knife is."
    "Glancing at his legs, it's hard to see."
    "The room is too dark to get a good look as to where his pockets might be."
    "Even if you manage to leave the ropes, get his knife- who knows what else he has on him."
    "That's not to mention..."
    "You don't even know {i}where{/i} the exit is."

    show cadmus eyebrowsR with dis
    cadmus "Hmm...ah!"
    "Cadmus suddenly stands, startling you."
    hide cadmus with dis
    cadmus "I'll be right back my love~"

    "Once again, wandering off somewhere, scooping the cup off the ground as he makes his way out of sight."
    "You could only wish he'd be out of mind."
    $ _history = False
    "{size=50}{font=HelpMe.ttf}WITHOUT HIS VENOM IN YOUR NECK{/font}{nw}"
    "{size=50}{font=HelpMe.ttf}IT ITCHES SO MUCH{/font}{nw}"
    $ _history = True
    "Your head hurts so much...what even was in that drink anyways?"
    "That's not important, at least not right now."
    "Trying to figure out what he's up to is more pressing."
    "Straining to listen to whatever odd sounds you can..."
    "{cps=10}..."
    "There's nothing."
    "{cps=10}..."
    "{cps=10}..."
    "You can't hear a single thing."
    "There's no running water, no clanging of metal, no sound of a door, not even any sounds that'd be from him."
    "The room is completely silent."
    "Honestly...maybe you should free your hand now."
    "Who knows what in the world Cadmus is planning."

    menu:
        "Free your hand":
            "Taking chances leaving it now can only mean bad things for you."
            "It takes a few second but you get your hand free."
            "Doing your best to leave it concealed within the ropes."
            "If he came back and noticed...you'd be in deep shit."
            jump FearBadBranchB

        "Leave it be":
            "As much as it's tempting...you have no idea what he's doing right now."
            "You can always try pulling it free later."
            "Taking this opportunity to do it now might end terribly."
    
    ##Landing point for "Bad Choice 2"
label FearGoodBranchHalf:
    "You aren't sure how long you're stuck in the silence."
    "With how disorienting this space is- could be mere seconds, could be hours."
    "It almost makes you..."
    "{cps=15}Miss...him."
    "Miss him?"
    "There's a weird thought."
    "Suddenly the sound of footsteps- he's coming back."
    "It's almost reassuring."
    "Are you...worrying about him?"
    "That's complete nonsense."
    "You {i}really{/i} need to get out of here."

    show cadmus smileopenNU at default with dis
    cadmus "There you are~"

    $ _history = False
    "He takes his rightful place{nw}"
    $ _history = True
    "He takes his place{fast} back in front of you."

    show cadmus concern with dis
    cadmus "Oh darling, you look so sad...I'm sorry for being gone so long."

    "Did you look sad?"
    "He must be toying with you."
    "There's no way you feel that way about {i}him{/i}."

    show cadmus pout eyesSld eyebrowsTD with dis
    cadmus "Unfortunately, as you can see, I return empty handed."
    "He seems genuinely disappointed at this fact."
    cadmus "My idea- despite it being so brilliant...I don't have what I'm looking for anymore."

    "{cps=15}Anymore?"

    cadmus "Either way~"
    cadmus "I have you, no need for any other fanciful things."
    cadmus "My love is right here."

    "Cadmus leans on his arm, staring at you once again."
    "He seems to have no interest in going anywhere."
    "...Now might be your chance."

    menu fearloop:
        "Not yet":
            "You shouldn't."
            "Not yet anyway."

            "He continues to stare at you."
            "Eyes piercing your very being."
            "No sudden movements..."
            "Just the sounds of you both breathing."
            jump fearloop

        "Now!":
            "You pull your hand free-"
            "The sudden motion shifting the ropes, allowing you more movement than you expected."
            "For a guy so proud of these stupid things, he sure didn't do that well tying you."
            "Cadmus is shocked, trying to speak but his words failing him."
            ## TODO: have a zoom towards him?
            "Reaching for one of his pockets, you manage to find the knife."

    cadmus "W-wait!"
    "He sounds...genuinely scared."
    "You cut yourself free from the ropes, holding the knife towards him."

    "You" "The exit."
    "You" "Where is it?"

    "You command his attention, despite the fact your voice is shaking."

    "He simply points off to the side-"
    "You book it without looking back."
    ## TODO: zoom into the door?
    play sound doorOpen
    "It's a short struggle to find the knob in the darkness, but the second your hand finds purchase- you keep moving."
    stop music channel "music_CH1" fadeout 1.0
    stop music channel "music_CH2"
    show black zorder 5 with dis

    "Stopping now would be a horrible mistake."
    "Cadmus is going to find you."
    "He's definitely going to come after you once the shock wears off."
    "You cannot allow yourself to slow down- even for a second."

    show bg not_bliss
    "There's light at the end of this corridor- a completely welcome sight to behold."
    hide black with dis

    "Reaching the outside- you find yourself in a field."
    "An endless field of grass."
    "Is this place...a bunker?"
    "In the middle of nowhere?"
    "Now's not the time to wonder that!"
    "Shaking the thought from your mind, you continue to run."
    "Civilization must be close, you just know it."
    "{cps=10}..."
    "{cps=10}..."
    "Is this grass truly never ending?"
    "You haven't seen a road, a sign, a vehicle, or even a person."
    "{cps=10}..."
    "How long have you been running?"
    "Your throat is burning."
    "{cps=10}..."
    "It's so hard to breathe..."
    "You can't stop."
    "You know you can't."
    "{cps=10}..."
    "He's {i}going{/i} to find you, Cadmus {i}must{/i} be right behind you."
    "...He's got to be."
    "{cps=10}..."
    "Your foot catches on itself-"
    play sound bodyFall
    "Tumbling to the ground-"
    "Your head is pounding."
    "You can't breathe anymore."
    "...someone will find you."
    "You'll be home soon."
    "You're sure of it."
    "{cps=10}Home is just around the corner."
    scene black with fade

    cadmus "Back so soon, love?"
    cadmus "I wonder how long you'll be resting for this time..."

    ##add a fade out, title "Fear: Good Ending?"
    if persistent.onReplay == False:
        $ persistent.onReplay = True
    $ persistent.FearGoodEnd = True
    $ persistent.lastRoute = "FG"
    $ persistent.runNumber += 1
    $ renpy.save_persistent()
    pause (0.5)
    show text "{font=HelpMe.ttf}{sc=2}Fear: Good Ending?{/sc}{/font}" with Dissolve(1.5)
    pause (2.0)
    hide text
    return


## BAD ROUTE

label FearBadBranchA:
    "Cadmus tosses the cup aside."
    "The porcelain shattering pierces your ears."
    $ _history = False
    "Would he do that to you?{nw}"
    $ _history = True
    "Why did he do that?"
    "Your muscles tense at the sound."

    cadmus "Don't worry about that my love."
    cadmus "Cups are easy to replace..."
    cadmus "But you?"
    "He places his hand against your cheek, his grin wide as he stares intently at you."
    cadmus "My beautiful dear, you are irreplaceable~"

    "Letting it linger there, without him talking- you can pay attention to the way it feels."
    "{cps=15}His hand is cold."
    $ _history = False
    "Maybe he's cold blooded.{nw}"
    $ _history = True
    "Maybe he{fast} has bad blood flow?"
    "His entire hand feels like ice against your face."

    $ BadBranchA = True
    jump FearBadChoice1

label FearBranchACont:
    cadmus "You're so lovely to look at."
    "His hand finally releases your cheek."
    cadmus "I want to stay with your forever."

    "He chuckles, amused at his own statement."

    cadmus "Of course, that's what we're going to do."

    "He drums his fingers against the chair, lost in his own thoughts."
    "Given he seems a bit distracted...now might be your chance."
    "You could grab his knife and run...right?"

    menu:
        "Try to grab the knife":
            "With your hand free, you try to reach for his pockets."
            "Your arm snags."
            "{cps=10}Shit."
            "His attention snaps to you immediately, grabbing your wrist."
            "Nails digging into your skin, so hard it starts to bleed."
            jump FearBadConverged

        "Wait for another opening":
            "Cadmus seems to always be decently attentive..."
            "It might not be a good idea to trust he's actually distracted."

            cadmus "Ah!"
            cadmus "I have an idea!"

            "He seems quite excited, abruptly standing."

            cadmus "I'll be back in just a moment, darling~"

            "He promptly walks off, disappearing out of your vision."

            jump FearGoodBranchHalf

label FearBadBranchB:
    "The sound of footsteps echo through the space."
    "He's returning."
    "You try to prepare yourself for anything- good, bad, and awful."
    "He has nothing with him."
    "{cps=10}..."
    "Nothing?"

    cadmus "I return my little mouse~"
    "He excitedly plops himself back across from you."
    cadmus "Did you miss me?"

    "Knowing he truly believes you're in love, you nod at him."
    "His eyes glimmer with excitement."

    cadmus "Oh how divine! How precious!"
    "His laughter fills your ears, it's almost comforting."
    "{cps=10}But his face contorts."

    cadmus "It's a shame...you think you're pulling a fast one on me."

label FearBadConverged:
    show cadmus armsHK with dis
    play sound ropeFalls
    "Brandishing his knife, he slices through the ropes with ease."
    $ _history = False
    "{cps=10}JuSt LiKe He WiLl YoUr FlEsH{nw=3}"
    $ _history = True
    "You're horrified at what's coming for you."
    ## TODO: add movement here so that he looks like he's holding you up
    "Cadmus' hand firmly grasps your neck, lifting you from the chair with ease."
    $ _history = False
    "Not even giving you a second to react to being free from his tail's suffocation.{nw}"
    $ _history = True
    "Not even giving you a second to react to being free from{fast} the winding ropes."

    cadmus "I'VE DONE ALL THIS TO PROTECT YOU!"
    "He sounds...sad...why?"
    cadmus "CAN'T YOU SEE THAT I LOVE YOU?"

    "You gasp-"
    camera at shakeOnce
    play sound bloodSplat
    show cadmus bloodyarmsHK
    "He drove the knife into your side."

    cadmus "I LOVE YOU I LOVE YOU I LOVE YOU I LOVE YOU I LOVE YOU-"

    "Cadmus keeps incessantly repeating the phrase with each stab, blood gushing from your stomach."
    camera:
        subpixel True
        blur 5
    "Your mind is clouded."
    "You're going to die here."
    "God...you're going to die here."
    "You're {i}dying{/i} here."
    stop music channel "music_CH1" fadeout 1.0
    stop music channel "music_CH2"
    "His voice begins to fade..."
    camera:
        subpixel True
        linear 0.5*(not renpy.is_skipping()) matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.15)*HueMatrix(0.0) 
    show black zorder 5 at closeEyes
    "Along with your vision."
    "It's over."
    "{cps=15}Why did it have to be like this?"

    scene black with fade
    pause (0.5)

    cadmus "I just...want to protect you..."
    cadmus "Believe in me...please..."

    ## fade out, title "Fear: Bad Ending?"
    if persistent.onReplay == False:
        $ persistent.onReplay = True
    $ persistent.FearBadEnd = True
    $ persistent.lastRoute = "FB"
    $ persistent.runNumber += 1
    $ renpy.save_persistent()
    pause (0.5)
    show text "{font=HelpMe.ttf}{sc=2}Fear: Bad Ending?{/sc}{/font}" with Dissolve(1.5)
    pause (2.0)
    hide text
    return