label chaos:
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
    show cadmus annoyed at default
    show cadmus armsKP

    play music basement channel "music_CH1" fadein 0.5
    play music corrupted channel "music_CH2" volume 0.0

    hide black
    camera:
        subpixel True
        blur 0.0
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    show blank zorder 5 at blink
    "Inhaling a sharp breath, you open your eyes."
    "Cadmus sits across from you, like he always has."
    "No tricks this time."
    "Thank goodness for that."
    "The light behind him catches on the knife he holds in his hand."

    cadmus "Nice of you to wake up."
    show cadmus -angryMark
    cadmus "Took you less than last time."

    menu:
        "Last time?":
            "He sighs, seemingly unimpressed."
            cadmus "Whatever."
            "What the hell does he mean?"
        
        "Good morning.":
            show cadmus lidsS with dis
            "He narrows his eyes at you, clearly unamused."
            cadmus "Morning indeed little mouse."
            show cadmus questioning with dis
            cadmus "Are you even sure that's the time?"
            "You suppose that's true...this place has no windows."

        "Stay silent":
            show cadmus lidsS with dis
            "He watches you carefully, only the sound of you both breathing fills the space."
            cadmus "You {i}really{/i} know how to lighten a mood."
            "It's not entirely important if the mood is light or not."
            "Especially given how poorly lit this room is to begin with."

    "He plays with the knife, it seems to have vague remnants of blood, though it's hard to see."
    "You wonder if it's yours, if it's his, perhaps both."
    show cadmus armsD with dis
    "Cadmus haphazardly puts the knife back into his pocket"
    show cadmus normalSmile armsR at lean
    extend ", and wipes his fingers on your cheek."
    "You can feel something wet and cold as he does so."

    cadmus "How beautiful..."
    show cadmus smirk with dis
    cadmus "You'd make such a lovely painting."

    "It's hard to tell if he's entirely serious or speaking his usual nonsense."
    "In a way, it wasn't important one way or the other."
    "His nails dig into your cheek suddenly."

    menu:
        "Bite his fingers":
            camera at shakeOnceNoBlur
            "You tilt your head slightly and chomp on one of his fingers."
            show cadmus angie with dis
            $ _history = False
            cadmus "YOU BASTARD!{nw}"
            $ _history = True
            show cadmus annoyed armsD -hand at sit
            cadmus "OW!"

        "Move your head away":
            camera at tiltHead
            "You tilt your head away from his hand."
            $ _history = False
            camera at cameraReset
            "He grabs your hair and moves it back."
            show cadmus angie with dis
            cadmus "Ungrateful. After all this and you STILL SQUIRM?{nw}"
            $ _history = True
            show cadmus -eyeBS
            show cadmus concern with dis
            cadmus "Awe darling...I thought you liked it when I caressed your cheek."
            show cadmus armsD -hand at sit

        "Kiss his palm":
            "You tilt your head towards his hand, kissing his palm"
            show cadmus armsD -hand at sit
            extend " as he moves his hand away."
            cadmus "How sweet...sickening and sweet."
            show cadmus smirking with dis
            cadmus "You are {i}such{/i} a damned fool."

    show cadmus regularE with dis
    cadmus "You should be glad you're in those damn ropes."

    "There's a jitter in your vision, your head is pounding."
    camera at continuousShake
    "The whole room feels like it's on stilts and shaking, but you know you aren't moving."
    hide cadmus
    "Cadmus vanishes from your view."
    "You feel nauseous."
    "Trying to move out of the ropes is futile- you know that."
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
    "{cps=10}{font=HelpMe.ttf}H E ' S  R I G H T  T H E R E {/font}{nw}"
    $ _history = True

    camera at cameraReset
    show cadmus concern at default
    cadmus "Why the face darling?"
    "He is sat in his chair, as though he never moved."
    cadmus "We quite genuinely have all the time in the universe."

    "He sighs, bored out of his mind."
    "You're still struggling with whatever sensation just came over you."
    "His eyes watch you, a lingering sense of curiosity."
    show cadmus normalSmile with dis
    "It quickly vanishes."

    show cadmus annoyed with dis
    cadmus "You could at least be more entertaining...so still."

    menu:
        "I moved earlier didn't I?":
            show cadmus questioning with dis
            cadmus "Did you?"
            show cadmus at cadFidget
            "He shuffles, causing the chair to creak."
            cadmus "It's hard to say."
            show cadmus at lean
            "Cadmus leans forward."
            $ _history = False
            show cadmus armsHK with dis
            "W I T H  T H E  K N I F E{nw}"
            $ _history = True
            show cadmus armsR
            "Touching your face."
            show cadmus smirkingSoft with dis
            cadmus "Maybe you did. Maybe I did."
            cadmus "Who cares."
            jump ChaosBadBranchA

        "You could untie me.":
            "He tilts his head in thought-"
            "Is he actually considering it?"
            "His hand slithers under the ropes."
            "The chair squeals."
            show cadmus at jumpscare
            "His face fills your vision."
            show cadmus angie with dis
            cadmus "I don't understand what 'it's for your safety' isn't clicking with you?"
            show cadmus -eyeBS
            jump ChaosBadBranchB

        "And what about you?":
            show cadmus smirking with dis
            cadmus "As if."
            cadmus "Silly silly, little mouse."
            jump ChaosGoodBranchA

        "You stay still":
            show cadmus frowning with dis
            "Cadmus frowns, pursing his lips."
            cadmus "Disappointing, but unsurprising, dear."
            "He twitches."
            $ _history = False
            show cadmus smirking with dis
            show cadmus armsHK
            "Your eyes catch the knife dancing in his fingers.{nw}"
            $ _history = True
            show cadmus armsHair -shadowTD
            "His hand runs through his hair, looking a bit unamused."
            show cadmus normalSmile armsD -hairUp with dis
            cadmus "...doesn't matter."
            jump ChaosGoodBranchB


label ChaosGoodBranchA:
    show cadmus normalSmile armsHair with dis
    "Cadmus runs his fingers through his hair."
    cadmus "There is so little you understand."
    show cadmus armsD -hairUp at lean
    "He leans in close to you, carefully watching your face."
    show cadmus questioning with dis
    cadmus "I'm trying to protect you, dear. Do you realize that? Is that getting in your head?"

    menu:
        "I do realize it.":
            show cadmus smirkingSoft with dis
            cadmus "Good."
            cadmus "Not that I doubted your intelligence."

            "You" "What's that supposed to mean?"

            show cadmus frowning with dis
            cadmus "Hey hey, don't get upset with me."
            cadmus "I'm not trying to offend you. You try keeping track of all this shit."
        
        "I don't":
            show cadmus annoyed with dis
            cadmus "Must be nice to be clueless."

            "You" "Maybe you could explain it to me?"

            show cadmus frowning with dis
            cadmus "...it's better if I don't."
            show cadmus eyesSld with dis
            "His eyes aren't looking at you anymore."
            cadmus "Trying to keep track of all this nonsense is too much even for me. I'm doing this to save you from it."

    "You" "You could at least be less vague than this."
    "It's hard not to feel annoyed by him."
    "You" "I'm also involved in this aren't I?"

    show cadmus annoyed eyesS with dis
    cadmus "We don't have enough time!" 
    "His hand bangs into the chair before falling back to his side."
    show cadmus at sit
    cadmus "If you remember enough you must realize it's limited."

    "You" "If you keep avoiding answering, of course we'd run out of time."
    "You" "As if being TRAPPED in this room we don't HAVE time!"
    "You" "Not to mention what you just said entirely goes against what you said before!"

    show cadmus lidsS with dis
    "He glares at you, clearly annoyed by your insistence."
    cadmus "It was a figure of speech."
    "Even then...there's something else there you can't quite place."

    show cadmus regularE with dis
    cadmus "I'm doing you a favour by not explaining, eventually you'll realize that."

    "You" "Nothing you're doing is making any sense!"

    cadmus "Well neither is you being here."
    show cadmus pout armsR at lean
    cadmus "You shouldn't BE here, darling."

    "You" "You literally trapped me in here, how should I not even be here?"

    hide cadmus with dis
    play sound "<from 0 to 10>audio/sound effects/footsteps.mp3"
    "Cadmus stands, moving towards the darkness. His footsteps are easily heard, he didn't go far."
    "As much as you want to repeat yourself, it's clear enough from his huffing; he's either struggling or a bit annoyed."

    if persistent.lastRoute == "FG":
        cadmus "You quite literally ran out of the room."
        cadmus "You freed yourself from the ropes, stole my knife, and booked it out the door."
        cadmus "Darling...you never came back."

    elif persistent.lastRoute == "FB":
        cadmus "All I was doing was just to try and protect you, and you tried to get out of the ropes!"
        cadmus "I just...I was so scared about what would happen...I attacked you..."
        cadmus "You were dead."

    elif persistent.lastRoute == "CG":
        cadmus "You said that you loved me, and we enjoyed our time together...didn't we?"
        cadmus "But then you just...drifted away..."
        cadmus "And no matter how hard I tried you were in such a deep sleep..."

    elif persistent.lastRoute == "CB":
        cadmus "You were so obsessed with me, entirely out of nowhere."
        cadmus "If I stayed, I don't know what you would've done."
        cadmus "So I walked out...I'm not even sure how long I left for."
        cadmus "But when I came back you were just...gone."

    elif persistent.lastRoute == "CS":
        cadmus "You...said you didn't love me."
        cadmus "I don't know what came over me I was...so distressed and hurt."
        cadmus "I don't even remember what I did, but when I came to...you were on the floor..."
        cadmus "Dead."

    elif persistent.lastRoute == "AG":
        cadmus "You managed to get free from the ropes...and you killed me."
        cadmus "...you became someone you weren't...it still haunts me."

    elif persistent.lastRoute == "AB":
        cadmus "I wanted so badly to get us both out of this...cycle."
        cadmus "But I couldn't keep myself together...and when I freed you I just..."
        cadmus "I couldn't let you escape..."

    "You" "...what?"

    show cadmus concern at default with dis
    cadmus "You can't tell me you don't remember. You {i}must{/i} remember, don't you?"
    "His eyes search your face, hoping for something."

    "It takes you a moment, sitting and really thinking about what he said."
    if persistent.lastRoute == "FG":
        hide vignette with slowdis
        show image fearGood with slowdis:
            zoom 1.065
            matrixcolor TintMatrix("#e4c986") * SaturationMatrix(0.0, (0.2126, 0.7152, 0.0722))

    elif persistent.lastRoute == "FB":
        hide vignette with slowdis
        show image fearBad with slowdis:
            zoom 1.065
            matrixcolor TintMatrix("#e4c986") * SaturationMatrix(0.0, (0.2126, 0.7152, 0.0722))

    elif persistent.lastRoute == "CG":
        hide vignette with slowdis
        show image careGood with slowdis:
            zoom 1.065
            matrixcolor TintMatrix("#e4c986") * SaturationMatrix(0.0, (0.2126, 0.7152, 0.0722))

    elif persistent.lastRoute == "CB":
        hide vignette with slowdis
        show image careBad with slowdis:
            zoom 1.065
            matrixcolor TintMatrix("#e4c986") * SaturationMatrix(0.0, (0.2126, 0.7152, 0.0722))

    elif persistent.lastRoute == "CS":
        hide vignette with slowdis
        show image careSpecial with slowdis:
            zoom 1.065
            matrixcolor TintMatrix("#e4c986") * SaturationMatrix(0.0, (0.2126, 0.7152, 0.0722))

    elif persistent.lastRoute == "AG":
        hide vignette with slowdis
        show image amnesiaGood with slowdis:
            zoom 1.065
            matrixcolor TintMatrix("#e4c986") * SaturationMatrix(0.0, (0.2126, 0.7152, 0.0722))

    elif persistent.lastRoute == "AB":
        hide vignette with slowdis
        show image amnesiaBad with slowdis:
            zoom 1.065
            matrixcolor TintMatrix("#e4c986") * SaturationMatrix(0.0, (0.2126, 0.7152, 0.0722))

    "The sensations of memories that don't feel like yours come back to you."
    hide fearGood with slowdis
    hide fearBad with slowdis
    hide careGood with slowdis
    hide careBad with slowdis
    hide careSpecial with slowdis
    hide amnesiaGood with slowdis
    hide amnesiaBad with slowdis
    show vignette zorder 4 with slowdis:
        xpos -100
        ypos -270
    "{i}He's telling the truth.{/i}"

    show cadmus normalSmile with dis
    cadmus "There's the recognition..."

    "You" "But how?"

    cadmus "I quite seriously, cannot explain it to you."
    cadmus "It's simply to protect you."

    "You" "For what reason?!"

    show cadmus annoyed with dis
    cadmus "I don't get what you don't understand!"
    show cadmus blush with dis
    cadmus "You are my one true love- the being of my affections- and I want to protect you."

    "You" "That line isn't a bit??"

    show cadmus concern with dis
    show cadmus -blush
    cadmus "You thought I was joking...?"
    show cadmus frowning with dis
    cadmus "God that's even more insulting than you not understanding the gravity of the situation we're in."

    "You" "I literally haven't even met you until just...today?...now?...being in this room with you??"
    "You" "I don't even know anymore...this is all so confusing!"

    show cadmus eyesSld with dis
    cadmus "There is no time in the world for me to info dump you on all this crap."
    show cadmus armsHair with dis
    cadmus "I'm gonna pretend you didn't think I cared about you and just move on."
    cadmus "There are much bigger things to deal with right now."
    jump ChaosGoodConverged

label ChaosGoodBranchB:
    "You" "Maybe this would be more entertaining if you explained things."
    "You eye him cautiously, as much as you want answers as to what the hell is going on."
    "You also don't want to put yourself in immediate danger."

    show cadmus questioning at lean
    cadmus "What do you think is happening here then?"

    menu:
        "You kidnapped me.":
            "You" "And now I'm trapped here 'cause of you."
            show cadmus armsHair with dis
            "He quickly brushes his hand through his hair, sighing."

            show cadmus smirkingSoft armsD -hairUp at sit
            cadmus "If only it were that simple darling."

            "You" "I mean you seem obsessed with me, why isn't it that simple?"
            show cadmus frowning with dis
            "You" "What someone told you to kidnap me? Is that it?"

            show cadmus eyesSld with dis
            cadmus "You are somehow so close and so far away."
            cadmus "You'd think being here again you'd realize it."

            "You" "...again?...What do you mean again?"

            "How is that even possible? You've never been here before..."

        "Something I don't understand.":
            show cadmus annoyed with dis
            cadmus "Have you bothered trying to understand it?"

            "You" "What do you think I'm trying to do smartass?"

            show cadmus smirkingSoft at sit
            cadmus "You are quite different than some other times, I'll give you that"

            "You" "Other...times? What other times?"
            "You feel even more lost than you were before."

        "You're toying with me.":
            show cadmus shock with dis
            cadmus "Oh? Toying, that's a new one."
            show cadmus confused with dis
            cadmus "What makes you so sure?"

            "You" "Well you tied me to a chair, and keep speaking vague nonsense."
            "You" "Clearly you find this so amusing and I'm entirely missing the point as to why."

            show cadmus smirkingSoft with dis
            cadmus "It is amusing, but not because I think it is."
            show cadmus at sit
            "The way his face relaxes almost seems forced, but the look in his eyes tells you otherwise."
            cadmus "Honestly I was hoping you'd realize this all seems familiar by now."

            "You" "...Familiar? How could that be possible?"

            "Implying you've been here before in some way? That can't be true..."

    show cadmus smirkingSoft eyesS at cadFidget
    "He doesn't seem in any rush to respond, fidgeting in his seat."

    "You" "Hellooo? Earth to Cadmus?"

    show cadmus annoyed armsSH with dis
    "He holds his finger up to you, looking a bit annoyed."
    "Though perhaps he's worried?"
    camera:
        subpixel True
        ease 0.5 blur 3 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.15)*HueMatrix(0.0) 
    "Your head feels weird, the room seeming to darken."
    "You aren't entirely sure what the sensation is."
    "A thought pops into your head."

    if persistent.lastRoute == "FG":
        hide vignette with slowdis
        show image fearGood with slowdis:
            zoom 1.065
            matrixcolor TintMatrix("#e4c986") * SaturationMatrix(0.0, (0.2126, 0.7152, 0.0722))
        camera:
            subpixel True
            blur 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)

        centered "You barely managed to escape, but you were running through a seemingly endless field."
        centered "It was so exhausting you passed out."

        hide fearGood with slowdis
        show vignette zorder 4 with slowdis:
            xpos -100
            ypos -270
        camera:
            subpixel True
            blur 3 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.15)*HueMatrix(0.0) 

    elif persistent.lastRoute == "FB":
        hide vignette with slowdis
        show image fearBad with slowdis:
            zoom 1.065
            matrixcolor TintMatrix("#e4c986") * SaturationMatrix(0.0, (0.2126, 0.7152, 0.0722))
        camera:
            subpixel True
            blur 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)

        centered "You were so afraid of him, and tried so hard to escape without him noticing...but he noticed."
        centered "He was so overwhelmed with anger over trying to leave him...he killed you."

        hide fearBad with slowdis
        show vignette zorder 4 with slowdis:
            xpos -100
            ypos -270
        camera:
            subpixel True
            blur 3 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.15)*HueMatrix(0.0) 

    elif persistent.lastRoute == "CG":
        hide vignette with slowdis
        show image careGood with slowdis:
            zoom 1.065
            matrixcolor TintMatrix("#e4c986") * SaturationMatrix(0.0, (0.2126, 0.7152, 0.0722))
        camera:
            subpixel True
            blur 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)

        centered "You were both happy, and you loved him. You remember that feeling so well."
        centered "Something came over you and you just...passed out."

        hide careGood with slowdis
        show vignette zorder 4 with slowdis:
            xpos -100
            ypos -270
        camera:
            subpixel True
            blur 3 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.15)*HueMatrix(0.0) 

    elif persistent.lastRoute == "CB":
        hide vignette with slowdis
        show image careBad with slowdis:
            zoom 1.065
            matrixcolor TintMatrix("#e4c986") * SaturationMatrix(0.0, (0.2126, 0.7152, 0.0722))
        camera:
            subpixel True
            blur 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)

        centered "You recall being so fixated on him, like he was your own personal obsession."
        centered "Loving him was breathing...and he left you."

        hide careBad with slowdis
        show vignette zorder 4 with slowdis:
            xpos -100
            ypos -270
        camera:
            subpixel True
            blur 3 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.15)*HueMatrix(0.0) 

    elif persistent.lastRoute == "CS":
        hide vignette with slowdis
        show image careSpecial with slowdis:
            zoom 1.065
            matrixcolor TintMatrix("#e4c986") * SaturationMatrix(0.0, (0.2126, 0.7152, 0.0722))
        camera:
            subpixel True
            blur 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)

        centered "He asked you for the truth, and you told him you didn't love him."
        centered "He was so upset he bit you so hard you passed out."

        hide careSpecial with slowdis
        show vignette zorder 4 with slowdis:
            xpos -100
            ypos -270
        camera:
            subpixel True
            blur 3 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.15)*HueMatrix(0.0) 

    elif persistent.lastRoute == "AG":
        hide vignette with slowdis
        show image amnesiaGood with slowdis:
            zoom 1.065
            matrixcolor TintMatrix("#e4c986") * SaturationMatrix(0.0, (0.2126, 0.7152, 0.0722))
        camera:
            subpixel True
            blur 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)

        centered "You took matters into your own hands...and you killed him."
        centered "It was terrifying and yet it made you feel so much bigger than you were."
        centered "Like you...both switched places."

        hide amnesiaGood with slowdis
        show vignette zorder 4 with slowdis:
            xpos -100
            ypos -270
        camera:
            subpixel True
            blur 3 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.15)*HueMatrix(0.0) 

    elif persistent.lastRoute == "AB":
        hide vignette with slowdis
        show image amnesiaBad with slowdis:
            zoom 1.065
            matrixcolor TintMatrix("#e4c986") * SaturationMatrix(0.0, (0.2126, 0.7152, 0.0722))
        camera:
            subpixel True
            blur 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)

        centered "He kept talking madness about \"breaking the cycle\" and when he cut you free, you tried to escape..."
        centered "But he captured you and bit into you like his prey."

        hide amnesiaBad with slowdis
        show vignette zorder 4 with slowdis:
            xpos -100
            ypos -270
        camera:
            subpixel True
            blur 3 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.15)*HueMatrix(0.0) 

    "A memory that isn't yours but...you can't help but feel like it is."
    "That moment happened to you."
    "But how is that even possible?"

    show cadmus normalSmile with dis
    cadmus "...there it is."
    camera:
        subpixel True
        ease 0.5 blur 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
    "The room comes back into focus."
    "Cadmus looks almost...sad, but relieved."
    cadmus "You do realize it."

    "You" "...we've been here before?"

    cadmus "Precisely, my dear."
    show cadmus armsD with dis
    cadmus "Somehow, someway, here we are."

    "You" "But...how?"
    "You" "You must understand something if you realized it before me!"

    show cadmus frowning with dis
    cadmus "I wish I could say I do...but not really."
    show cadmus eyesSld with dis
    cadmus "Unfortunately...It would take far too much time for the two of us to catch up in knowledge, and see what page we're on."

    "You" "So how much is real? Fake? Is there a truth?"
    "You" "Have you just been playing me with the whole 'being of my affections' bit?"

    cadmus "...yikes...a {i}bit{/i}."
    cadmus "I wasn't lying-"
    show cadmus armsHair with dis
    cadmus "Ah, it's not important."
    show cadmus eyesS with dis
    cadmus "I'm going to ignore the fact you think I've been joking."
    jump ChaosGoodConverged

label ChaosGoodConverged:
    show cadmus armsD -hairUp at cadFidget
    "He takes a second to adjust himself in his seat, before he speaks again."
    show cadmus concern with dis
    cadmus "We're on a bit of a timer."
    cadmus "We can only be so entertaining."

    "You" "{cps=10}{b}We?{/b}"
    "You" "Are you implying...som-"

    show cadmus frown armsHighSH at lean
    cadmus "SHH!"
    "Cadmus immediately closes the distance between you, holding his finger to your lips, he looks worried...and scared."
    cadmus "Don't. We're just having a normal conversation."

    "You eye him, a bit freaked out by his sudden movement"
    camera at nodHead
    extend ", but you nod at him."
    show cadmus normalSmile -armsHighSH at sit
    "He seems to relax, looking relieved."

    "You" "So what do we do then?"
    "You" "Ideas? Plans? Anything?"

    show cadmus frowning with dis
    cadmus "Wish I could say I have any...but I don't."
    "He sinks a bit into his seat."
    cadmus "It's a bit difficult. Given the space. I'm not entirely sure we're exactly in a real location."

    "He pulls himself up as you try to process what he said."
    "I mean it's already weird enough to seemingly be stuck in...a loop?"
    "But not in a real place? That's pushing the boundaries of your understanding."

    show cadmus at cadFidget
    cadmus "Trust me, I barely understand it myself."
    "He is carefully watching the look on your face as he speaks."
    cadmus "I'm just barely able to keep my wits each time...I think it comes with the territory."

    "You" "Being in here however long we have or...?"

    show cadmus eyesSld with dis
    "Cadmus looks upset, not meeting your eyes anymore."
    "Clearly he's reluctant to give you information, though it's hard to get why."
    "Without talking about the bigger picture...dancing around topics like this, how are you supposed to get all this?"

    cadmus "Regardless of everything..."
    show cadmus eyesS with dis
    "He returns his gaze to you, trying to be comforting."
    show cadmus normalSmile with dis
    cadmus "I don't know what other things you might've been through...but I'll get us out of here."
    show cadmus at cadFidget
    "He fidgets in his seat, trying his best to smile."
    show cadmus smileopenNU with dis
    cadmus "You mean so much to me, I have to do my best."

    menu:
        "Why can't I help?":
            "You" "If we're both in this, shouldn't we both be trying?"
            show cadmus frowning with dis
            "He looks conflicted about your question."

            cadmus "I don't think you have that luxury, or I guess the curse of being able to try."

            "You" "What do you mean?"

            show cadmus confused at lean
            cadmus "Did you realize any other time we're vaguely repeating things?"

            "You didn't really."
            "Of course something always felt a bit weird but it was never something you could truly place."
            "If you only really realized now...would there be another chance to notice?"
            "How could you help if you couldn't remember..."

            show cadmus concern with dis
            cadmus "I don't mean to make you feel bad, love."
            show cadmus at sit
            cadmus "I would be happy to have your help. I just...don't know if it's possible."

        "I'm sorry you're doing so much.":
            "You" "I don't really...get why but, I'm appreciative."
            show cadmus embarassed with dis
            show cadmus smileteeth
            "He smiles brightly, a faint blush on his cheeks."

            cadmus "Aren't you just the sweetest..."
            show cadmus smileclosedND with dis
            cadmus "Your appreciation is more than enough. I'll keep going knowing I have your support."

            "You" "Even if I don't remember giving it to you?"

            cadmus "Even if you don't..."
            show cadmus eyesS with dis
            "He gently pats your knee, smiling softly."
            show cadmus smileopenNU with dis
            cadmus "It'll be one of the greatest gifts you've given me. I'll never forget it."
    
    "You" "So what do we do now?"

    show cadmus confusedLD -blush with dis
    show cadmus at cadFidget
    "He seems to carefully consider the question, fidgeting in his seat."
    "It's not like there's much you can do...you are tied to the chair."
    "Untying you is probably out of the question, he must have a reason for it."
    "You don't fully understand how time passes here either."

    cadmus "Well..."
    show cadmus eyesS with dis
    cadmus "I could at least try explaining a bit of what I know?"

    "You" "I thought you were worried about the amount of time we have and even talking about anything?"

    show cadmus normalSmile with dis
    cadmus "I think it's worth a risk."
    cadmus "I will have to dance around a few things...so I'm sorry about that."

    "You" "Whatever you can give me, maybe I'll be able to help or at least retain something?"

    show cadmus concern with dis
    "He looks concerned at that, you aren't sure if it's because he knows you won't remember, or he isn't sure you can help."
    "You can't help but feel a bit bad...what is he shouldering all on his own?"
    "This entire situation is so bizarre."
    "Most people would be afraid of the guy who kidnapped them."

    show cadmus regularE with dis
    cadmus "There's more to this place than even I understand, I've been outside all of about four times."
    show cadmus eyesSld with dis
    cadmus "It's just an inescapably endless field. Which is why I think we aren't exactly in a tangible place. This place is impossible."

    if persistent.lastRoute == "FG":
        "That makes sense, when you did manage to escape it just went on forever until you passed out from sheer exhaustion."
    else:
        "That sounds horrifying, just watching the field constantly extending out before you...no end in sight..."

    show cadmus eyesS with dis
    cadmus "It's like...an infection."

    "You" "What is? The field?"

    cadmus "No...it-"
    show cadmus concern at lean
    cadmus "I...I really don't know how much I can say."

    "You" "Just say it, it's better to speak it, right?"
    "You don't totally understand where this is coming from."
    "You" "It'll be fine right?"

    show cadmus eyesSld with dis
    "Cadmus still hesitates."
    camera:
        subpixel True
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.15)*HueMatrix(0.0) 
    "What is {font=HelpMe.ttf}{b}it{/b}{/font}?"
    "Why won't he tell you what {font=HelpMe.ttf}{b}it{/b}{/font} is?"
    "Is {font=HelpMe.ttf}{b}it{/b}{/font} that...scary?"

    show cadmus shock with dis
    camera at shakeOnce
    cadmus "Stop!"
    "He suddenly grasps your shoulders."
    camera at cameraReset
    show cadmus scaredNoTears with dis
    cadmus "Stop it! Clear your mind, please."

    "You" "Huh- what-"

    cadmus "Stop thinking!"

    "You don't totally understand why, or even how he knows where your mind is."
    "It's probably better to just focus on him."
    "You and Cadmus are in this room."
    "He is worried about you."
    show cadmus normalSmile at sit
    "He relaxes, and pulls away from you again."

    show cadmus pout with dis
    cadmus "There's more than us here."
    "He mumbles as he pulls himself together."
    cadmus "I can't do much about that...God I wish I could."

    "You" "Because of how impossible this place is?"

    cadmus "Suppose you could say that..."

    "There's a silence that is put between you both."
    "You aren't entirely sure what to say."
    jump ChaosConvergedEnding

label ChaosBadBranchA:
    "You" "If it doesn't really matter...what does then?"

    show cadmus at sit
    cadmus "Does anything in the universe matter, love?"
    show cadmus armsHair with dis
    "He fusses with his hair."
    cadmus "Does anything matter here? We are simply two people in a room."

    "You" "One person freely in a room and the other tied to a chair."
    show cadmus questioningA armsD -hairUp with dis
    cadmus "Are you so certain of those facts? Or are they just your delusions?"

    menu:
        "How am I delusional?":
            "You" "I am tied to a chair and you clearly aren't."
            "His questions honestly confound you, why is he even asking?"
            "What is he playing at?"

            show cadmus at lean
            cadmus "Who said I was free?"
            show cadmus smirking with dis
            cadmus "You truly think you know everything."
            show cadmus at sit
            cadmus "Fascinating little mind you have, darling mouse~"

        "That's what I'm seeing.":
            show cadmus smirking with dis
            cadmus "Have you been given reasons to trust your eyes?"
            show cadmus at lean
            "He approaches you looking quite amused."

            "You" "I-"

            show cadmus smileopenNU with dis
            cadmus "You haven't have you?"
            show cadmus at sit
            cadmus "Silly mouse you are~"
    
    cadmus "You are just so amusing~"
    cadmus "Shouldn't you be a bit more aware?"

    "You" "Maybe I would if you were being so damn vague!"

    show cadmus frowning with dis
    cadmus "Oh no...my dear lover is upset."
    show cadmus pout with dis
    cadmus "How can I ever make it up to you?"

    "You" "By telling me what your game is instead of just toying with me?!"

    show cadmus normalSmile with dis
    cadmus "Toying? Me? Hilarious."
    cadmus "Are you sure it's me?"

    "You" "What is your deal!"

    show cadmus smirking with dis
    cadmus "How about...we play a word game, darling?"
    show cadmus playfulK with dis
    "He is entirely changing the subject, pulling his knife out to play with."
    cadmus "I say a word, and you tell me what comes to mind. Doesn't that sound fun?"

    "You" "I don't have a choice do I?"

    cadmus "Good, you understand the rules."
    show cadmus regularE with dis
    cadmus "Let's play."
    show cadmus armsD with dis

    if persistent.lastRoute == "FG":
        cadmus "Murder."
        "What he'd probably do to you if he didn't love you so much."
        "No...he wouldn't..."
        "But...he did, didn't he?"
        "You tried to leave."
        "It's hard to forget the pain in your torso."

    elif persistent.lastRoute == "FB":
        cadmus "Escape."
        "You'd love nothing more than to get out of here."
        "You can see the open sky now..."
        "And the endless...field."
        "Your throat feels hoarse just thinking about it."
        "There was no escape."

    elif persistent.lastRoute == "CG":
        cadmus "Lover."
        "Of course Cadmus immediately comes to mind, if only because of how much he keeps calling you that."
        "But something pops into your mind, a memory you don't fully recognize."
        "He took care of you."
        "You loved him."
        "You feel disoriented."

    elif persistent.lastRoute == "CB":
        cadmus "Abandoned."
        "A lost kitten perhaps? Left out in the rain?"
        "Suddenly this room comes into your mind."
        "The chair across from you is empty."
        "He left you."
        "You loved him and he left you."
        "You feel so hurt."

    elif persistent.lastRoute == "CS":
        cadmus "Heartbroken."
        "How he will feel when he realizes you don't love him."
        "...but you told him that."
        "He did get so upset with you."
        "He even bit you."
        "It still hurts."

    elif persistent.lastRoute == "AG":
        cadmus "Killer."
        "Like a kidnapper serial killer, maybe he's one of them."
        "I mean if you could you would..."
        "...kill him."
        "Why are your hands shaking?"
        "His screams still echo in your mind."
        "...did you kill him?"

    elif persistent.lastRoute == "AB":
        cadmus "Break."
        "Like a bone? Maybe a broken heart?"
        "Or...a cycle."
        "He wanted to be free."
        "Both of you, to be free."
        "It didn't work."

    show cadmus smirking with dis
    cadmus "Even without words it's written on your face."
    show cadmus at lean
    "He leans in, studying your expression carefully."
    cadmus "What do you think now?"

    "You" "...how is-"

    cadmus "Any of this real? Wish I could tell you, dear."
    show cadmus at sit
    cadmus "I was worried nothing was going to come into your mind, given how stubborn you're being."

    "You" "You...knew that was going to trigger something?"

    show cadmus confused with dis
    cadmus "It was more of a guess than an assured fact."
    show cadmus normalSmile with dis
    cadmus "I was hopeful, and it seems my trust was placed correctly."

    "You" "How much more do you know? About all this?"

    cadmus "Well we're stuck here, and in a loop, and I care deeply and want to protect you."
    cadmus "The simple facts and truths."

    "You" "But...you tied me to a chair, you trapped me here..."

    "You can't help but feel so overwhelmed and confused."

    "You" "You're my enemy...right?"

    show cadmus confused with dis
    cadmus "You're still on that?"
    show cadmus eyesSld with dis
    cadmus "I am not your enemy. Maybe I can't convince you, but I will keep saying it if I must."

    "You" "...so if I take you at your word, what do we do then?"

    show cadmus normalSmile with dis
    show cadmus pout eyesSld with dis
    cadmus "I suppose I could attempt to fill you in, though-"
    show cadmus eyesS with dis
    "He pauses a moment, returning his gaze to you."
    cadmus "You will come to realize we don't have as much time as you or I could hope for."

    jump ChaosBadConverged

label ChaosBadBranchB:
    show cadmus frowning at sit
    "Cadmus pulls his hand away, shaking it off dramatically before letting it drop to his side."

    show cadmus lidsS with dis
    cadmus "You should be far more wary than you are. Don't you think?"

    "You don't even bother answering."
    "It's clear enough he's just asking it, not expecting much of an answer."
    "It's not like you really have much to give anyway."
    "Plus you can't even really avoid anything."
    "You quite literally can't move."

    cadmus "There is much time for you to consider your actions, my love."
    show cadmus smileopenNU -lidsS -eyebrowsTU with dis
    "He smiles as he swipes his feet against the concrete floor."
    cadmus "Or I suppose your words. Perhaps both. Wouldn't that be amusing?"

    "You" "Why should I even play your game?"

    show cadmus smirking with dis
    cadmus "Oh darling, you don't have much of a choice in the matter. I'm sure you realize that."
    show cadmus playfulK with dis
    "He pulls his knife from his pocket once more."
    "He presses the tip of it into a finger, chuckling to himself."
    "The knife has seemingly occupied him for now, twirling it around and inspecting it."
    "All of this feels familiar, it's so hard to place exactly why."
    "This room, this space, the feeling of the ropes."
    "{b}{i}Him.{/i}{/b}"
    "Something pops into your head."

    menu:
        "I escaped here already..." if persistent.lastRoute == "FG":
            show cadmus confused with dis
            cadmus "Those ropes? You've always been here."
            cadmus "It's not possible you left."

            "You" "The field went on forever, I know it did."

            show cadmus concern with dis
            "His face softens, almost...like he's sorry."
            "Why would he feel sorry?"
            $ _history = False
            "Is he seriously concerned?{nw}"
            $ _history = True
            "Is he{fast} even taking you seriously?"
            show cadmus armsD with dis
            "You doubt he'd explain."

        "Will you kill your lover again?" if persistent.lastRoute == "FB":
            show cadmus questioning with dis
            cadmus "Kill you? My my, such an imagination you have darling."
            cadmus "You think I'm keeping you here to harm you?"

            "You" "You did before."

            show cadmus normalSmile with dis
            "He continues to laugh, offering no other comments on the matter."
            show cadmus armsD with dis
            "Despite this...he puts the knife away after you said that."
            $ _history = False
            "Did he do that so as not to worry you?{nw}"
            $ _history = True
            "Did he do that{fast} to give you a false sense of security?"
            "...nothing makes any sense."

        "You weren't like this before." if persistent.lastRoute == "CG":
            show cadmus confused with dis
            cadmus "Like what?"
            "He doesn't seem to have a clue what you're talking about."
            "But there's this look in his eyes..."

            $ _history = False
            show cadmus frowning with dis
            "{cps=5}Pain{nw}"
            "{cps=5}Suffering{nw}"
            "{cps=5}Worry{nw}"
            $ _history = True

            "Regret..."
            "Your head is killing you."

            "You" "Nevermind."

            show cadmus normalSmile armsD with dis
            "Cadmus smiles, clearly amused as he puts the knife away."

        "You abandoned me." if persistent.lastRoute == "CB":
            show cadmus confused with dis
            cadmus "Me? Abandon you? Why I'd never think about it."

            "He looks a bit miffed, at least at first glance..."
            "But there's something distinct-"

            $ _history = False
            show cadmus frowning with dis
            "{cps=5}Recognition{nw}"
            "{cps=5}Sorrow{nw}"
            "{cps=5}Understanding{nw}"
            $ _history = True

            show cadmus confused
            "Confusion..."
            "What was all that?"
            "It hurts so much."

            "You" "Of course...you wouldn't think that."
            show cadmus armsD with dis
            "Cadmus still looks a bit confused, before putting the knife away."

        "You were so upset I didn't love you." if persistent.lastRoute == "CS":
            cadmus "What an interesting suggestion."
            show cadmus smirking with dis
            cadmus "As if you don't love me. You are my entire world, don't be so silly."

            "But there's something there."
            show cadmus frowning armsD with dis
            "A genuine sadness."

        "Didn't I kill you?" if persistent.lastRoute == "AG":
            show cadmus at lean
            cadmus "What an interesting thought."
            show cadmus confused with dis
            cadmus "You're tied to a chair, how could you possibly have killed me when I'm right here?"

            "You" "They aren't exactly tight on me."

            show cadmus at sit
            "He eyes you carefully."
            "But there's a moment."

            $ _history = False
            show cadmus concern with dis
            "{cps=5}Fear{nw}"
            "{cps=5}Concern{nw}"
            $ _history = True

            show cadmus normalSmile with dis
            "He doesn't seem that confused by it."
            show cadmus at sit
            "...what is going on?"

        "You tried to end all this." if persistent.lastRoute == "AB":
            show cadmus confused with dis
            cadmus "All of what darling?"
            cadmus "I love having you here with me, why wouldn't I want that?"

            show cadmus concern armsD with dis
            "As you're about to respond his expression softens."
            "He looks...defeated."
            "And so sad."

    show cadmus normalSmile with dis
    "You" "You're just going to act like this isn't a repeat then?"
    show cadmus smileopenNU at lean
    "He smiles happily at you."

    cadmus "Oh I'm not acting, but I appreciate you thinking I'm talented."

    show cadmus lidsC frown at sit
    "You blow in his eyes, causing him to back away."
    show cadmus pout -lidsC with dis
    "Cadmus is quite annoyed at that."
    "Or...at least he seems to be at first."
    show cadmus regularE armsD with dis
    "His face relaxes as he adjusts himself in his seat."

    cadmus "Though it seems you're more conscious than you were before."
    "He rubs his palms against his pants as he speaks."
    cadmus "That's at least a bit of a start."

    "You" "More conscious? What do you mean?"

    cadmus "Well you realized this isn't your first time here."
    show cadmus concern with dis
    show cadmus smileclosedND
    cadmus "Which is more than I can say you did before."

    "You" "Am I not supposed to realize that? What are you going to do now that I know?"

    show cadmus frowning with dis
    show cadmus eyesSld
    cadmus "...you still think I'm your enemy."
    "Does he feel bad?"
    "Why would he feel bad? He's clearly...evil...isn't he?"

    cadmus "I've done this to try and protect you...whether you believe that or not I suppose it's not my business."
    show cadmus eyesS with dis
    cadmus "But I'm not your real enemy. I don't know all that you've really seen before me here."

    "You" "Are you implying if I've been here more than once...not every you is...you?"

    cadmus "In a way-"
    "His voice trails off, seemingly not wanting to say more than that."

    "You" "I feel like I'm missing details here. You're going to explain to me aren't you?"
    "You watch him closely, hoping desperately for answers."
    "You" "...won't you?"

    cadmus "It's not like there's much else to do than that but...our time like this might be shorter than either of us would like."
    show cadmus normalSmile with dis
    "He smiles gently, you only wish he'd be like that more often."
    jump ChaosBadConverged

label ChaosBadConverged:
    "You" "Why exactly is our time limited?"
    "You" "Like do we only have a set number of minutes or something?"

    show cadmus confused with dis
    cadmus "No, nothing that simple."
    show cadmus pout with dis
    cadmus "Honestly things would be much easier if it was just a set time, set everything...but it's not."

    "You" "What is it then?"

    cadmus "It's...hard to explain..."
    show cadmus concern with dis
    cadmus "Whenever we stop being entertaining."

    "You" "Entertaining?...We?"
    "You" "Like...to who, how do we know if we are?"

    show cadmus eyesSld with dis
    cadmus "And that's part of the problem, isn't it?"
    cadmus "I don't know. Sometimes I get a feeling."
    cadmus "Like something is itching in my mind."
    cadmus "But I can't guarantee anything."

    show cadmus at cadFidget
    "He fidgets in his seat, seemingly struggling to think."
    show cadmus regularE with dis
    "Cadmus didn't exactly answer part of your question though..."
    "So does that mean someone else is here?"
    camera:
        subpixel True
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.15)*HueMatrix(0.0) 
    "Is {b}it{/b} even a person?"
    "What is {b}it{/b} anyways?"
    "How can we stop {b}it{/b}?"

    show cadmus concern with dis
    cadmus "STOP IT!"
    camera:
        subpixel True
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
    camera at shakeOnce
    "He suddenly yells, voice firm and full of worry, if it weren't for the ropes you would've fallen out of the chair."
    camera at cameraReset
    show cadmus angie with dis
    cadmus "Don't think, stop thinking, focus here. Focus on me. Now."

    "You have no idea where this is coming from."
    "With how panicked he is, it's best to listen."
    show cadmus -eyeBS
    "You're tied to a chair, in a room."
    "Cadmus is in front of you."
    "Cadmus is worried."
    show cadmus normalSmile with dis
    "He finally relaxes, sighing heavily."

    show cadmus pout with dis
    cadmus "That was really stupid of you."
    show cadmus frown with dis
    cadmus "I know you don't know a lot but...please...be careful."

    menu:
        "How did you know what I was doing?":
            show cadmus eyesSld with dis
            cadmus "I told you, sometimes I get a feeling."
            cadmus "I meant that just in general."
            cadmus "I don't fully know why, like there's some connection, telepathic or something."
            show cadmus eyesS with dis
            cadmus "Between us...{b}all{/b} of us."

            "You" "I would call bullshit, but given this entire situation..."

            show cadmus normalSmile with dis
            cadmus "It's hard to, isn't it?"

            "You" "...yeah."
        
        "Well {i}sorry{/i}.":
            "You" "You act like I was supposed to know!"

            show cadmus pout with dis
            cadmus "I didn't think you would be that concerned!"
            cadmus "I should know better, I'm sorry."

            show cadmus concern with dis
            "His face softens, he definitely looks like he feels badly."
            "As much as you want to stay mad at your captor..."
            "You can't."

    "You" "So...can I even do anything?"

    show cadmus pout with dis
    show cadmus eyesSld
    "There's a silence that stretches between you both as he seems lost in thought."
    "It at the very least gives you an opportunity to take in what you've been told."
    "You're both stuck here, neither of you know why..."
    "Who even trapped you both."
    "And he loves you."
    "You're a bit surprised of all things to be true, that one seems to be."
    "Does that mean you know each other outside of this?"
    "But how?"

    cadmus "That I'm not sure..."
    show cadmus eyesS with dis
    cadmus "You didn't exactly seem to be aware of all this most other times I've seen you."

    "You" "Other times...do you also pass out at points?"

    show cadmus confused with dis
    cadmus "More like a blip in reality? That's a better way of putting it."
    cadmus "I think there's a large difference between your connection to this space and mine."

    "You" "Is your connection different from mine?"

    show cadmus pout with dis
    cadmus "I could only assume that's the case."
    cadmus "I think maybe...we aren't always in the same continuity..."

    "You" "...like different realities?"

    cadmus "Yeah...like...you seem the most like the one I remember."
    show cadmus smirkingSoft with dis
    cadmus "You feel real to me."
    cadmus "I don't know how I come across to you..."

    menu:
        "I'm not sure either.":
            "You" "I don't really feel like I remember all that much...outside of being here."

            show cadmus concern at lean
            "He looks genuinely sad and concerned, leaning close to you."

            cadmus "...that's okay, we'll...we'll figure this out,."
            show cadmus normalSmile armsR with dis
            "He gently cups your cheek, trying his best to smile at you."
            cadmus "I'll make sure of it."
        
        "You seem real to me.":
            cadmus "That's good...good."
            show cadmus normalSmile at lean
            cadmus "I'll get us both out of here...I promise."

            "You" "...what if I forget your promise?"

            cadmus "I'll remember for us both, how about that?"
            show cadmus smileopenNU armsR with dis
            "He laughs gently, cupping your cheek."
            cadmus "It's our little secret."

        
        "Like a weird guy.":
            show cadmus concern with dis
            cadmus "Haha, ouch."
            show cadmus normalSmile at lean
            "He looks hurt, but clearly he's joking around."
            cadmus "Well if I'm weird, what does that make you?"

            "You" "The most normal person you've ever met."
            
            show cadmus smileopenNU armsR with dis
            "He laughs, putting his hand to your cheek and smiling brightly."

            cadmus "What about the love of my life, instead? I'd like that more."

            "You" "...we'll see."
    
    show cadmus normalSmile armsD -hand at sit
    "He seems to admire you carefully."

    cadmus "Either way, I'll do my best to protect you, that much I know I can do."

    "You" "What about you? Shouldn't...someone protect you?"

    show cadmus smirkingSoft with dis
    cadmus "Are you offering?"

    "You" "Well I don't see anyone else in here do you?"

    show cadmus smileopenNU with dis
    "He laughs, his smile lighting up the room."
    jump ChaosConvergedEnding

label ChaosConvergedEnding:
    play music basement channel "music_CH1" volume 0.0
    play music corrupted channel "music_CH2" volume music_vol

    show cadmus at fallOff
    play sound silencepoint5
    queue sound bodyFall
    "Suddenly Cadmus falls to the floor."


    cadmus "No....no we can't be out of time..."
    cadmus "shit...shit shit shit..."

    show cadmus crazy

    "You" "What's wrong?...Cadmus?"
    "You call for him, but he's still struggling, mumbling to himself."

    show cadmus at comeUp
    "He pulls himself into the chair again"
    show cadmus armsHK bloodyarmsHK with dis
    play sound pullOutKnife
    extend ", his hand pulling the knife from his pocket."

    "You" "What are you doing? I thought we had stuff to talk about??"

    show cadmus uglyTears with dis
    "He doesn't say anything, tears falling down his cheeks."

    "You" "Cadmus! What's going on!"

    show cadmus at lean
    play sound ropeFalls
    "He approaches you, cutting you free from the ropes."

    cadmus "{cps=10}{font=HelpMe.ttf}Time. Is. Up. Little. Mouse.{/font}"

    "He sounds...different."
    "The knife comes for your throat."
    camera at shakeOnceNoBlur
    "Your hands clasp his, trying to keep the knife away from you."
    camera at cameraReset

    "You" "Please! Cadmus! Snap out of it!"

    "Despite your pleading...you know in your heart it isn't reaching him."
    "He's not the one in front of you now."
    play sound stab
    camera:
        subpixel True
        blur 1.0
    show blank with flash
    "With his free hand he pulls your hands away, slicing at your neck."
    show black with Fade(0.2, 0.0, 0.4)
    "Everything goes dark in an instant."
    stop music channel "music_CH1" 
    stop music channel "music_CH2" fadeout 1.0
    "...there has to be an escape."

    pause (0.5)

    cadmus "{cps=10}..."
    cadmus "Darling...I'm sorry, I'm so sorry..."

    ## fade out, title "Chaos"
    $ persistent.ChaosEnding = True
    $ persistent.runNumber += 1
    $ renpy.save_persistent()
    pause (0.5)
    show text "{font=HelpMe.ttf}{sc=2}Chaos{/sc}{/font}" with Dissolve(1.5)
    pause (2.0)
    hide text
    return