label caring:
    ## For when he asks if he's your first
    define areFirst = False
    define pickedQuestionFirst = False
    ## For BadBranchB
    define CBBB = False

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
    play music basement channel "music_CH1" fadein 0.5
    play music corrupted channel "music_CH2" volume 0.0
    hide black
    show blank zorder 5 at blink
    "Struggling to refocus, you noticed Cadmus is still across from you, smiling."

    camera:
        subpixel True
        linear 0.50*(not renpy.is_skipping()) blur 0.0 

    cadmus "Good morning, little mouse~"
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

    show cadmus
    show chair
    "You take the moment to get reoriented with the space."


    camera:
        subpixel True
        ease 4.0*(not renpy.is_skipping()) xpos -297 ypos 738 xzoom 1.0 zoom 1.72 

    "Due to the dim light, it's extremely hard to see if there's anything of note in this room."
    "It feels like the edges of your vision are just pure darkness."

    camera:
        subpixel True
        ease_expo 3.00*(not renpy.is_skipping()) xpos 1818

    "Is it because your head is pounding?"
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
    cadmus "Did I do something wrong?"

    "The last thing you want is him to be upset."
    "For your safety, {i}obviously{/i}."
    "You don't know what he's capable of."
    
    camera at shakeHead
    show cadmus normalSmile with dis
    "You shake your head at his question, his face immediately brightens."

    show cadmus smileopenNU with dis
    cadmus "I thought so, good."

    "His hand continues to linger on your face, his fingertips gently resting behind your ear."
    show cadmus normalSmile with dis
    "There's something calming about it...maybe even a tad bit comforting."
    "Like it was meant to be."
    show cadmus resetArms at sit

    if persistent.onReplay:
        "Everything is a bit familiar, in a weird way."
        "As his hand pulls away, you realize there is much you still don't understand."
        "Yet you know you can't ask what you actually want..."
        "But there are some that wouldn't hurt. Questions about him."
    else:
        "As he pulls his hand away, you realize you don't know much about him."
        "Let alone the circumstance you're both in."
        "Perhaps he wouldn't mind some questions."

    menu:
        "Am I your first?":
            $ pickedQuestionFirst = True
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
                    "Happy that he's giddy over someone he's kidnapped?"
                    "Ick."
                    $ areFirst = True
                
                "No":
                    show cadmus regularE with dis
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
                    "You nod."
                    show cadmus at sit
                    "Then Cadmus pulls away from you."
                    "Conflicted between feeling bad for how sad he looked, and scared from his implied threat."
                    "Though...why would you feel bad for him?"
                    "Yuck."
        
        "Are you eating enough?":
            show cadmus confused with dis
            "Cadmus looks at you, completely taken off guard by the question."
            show cadmus eyesSld with dis
            "You almost think he looks...sad."
            show cadmus smirkingSoft with dis
            "Whatever he was feeling quickly leaves, he looks at you confidently."

            cadmus "Of course darling, why are you so concerned?"
            cadmus "I take care of you so well, obviously I can handle us both, don't you think?"
            "You suppose that's true, you don't feel like your life is entirely in danger."
            "Well...outside of his foreboding presence, and being tied to a chair."

        "What do you do when I'm sleeping?":
            cadmus "Watch over you of course."
            cadmus "I have to make sure you're safe and no one takes you from me."

            menu:
                "When do you sleep?":
                    "It's obvious enough he seems to always be awake when you are..."
                    "If he's always awake even when you're not...that's...concerning."

                    show cadmus embarassed with dis
                    cadmus "Worried about me? Oh aren't you sweet~"
                    show cadmus eyesS smileopenNU with dis
                    cadmus "I'm flattered."

                    "You" "You didn't answer my question..."

                    "He continues to smile."
                    "Clearly, he has no interest in giving you a proper answer."

                "You don't cuddle me while I sleep?":
                    show cadmus regularE with dis
                    "Cadmus stares, his expression unreadable."
                    "His fingers drum against the chair."
                    "{cps=10}..."
                    "{cps=10}..."
                    "You suppose...he isn't going to answer that."
                    "Wouldn't that be something he'd want to answer?"
                    "Guess there is much you don't understand."

        "Do you know where we are?":
            show cadmus shock with dis
            "He looks caught off guard by the question."
            show cadmus concern with dis
            cadmus "Well...of course I do, I brought you here."
            cadmus "This place is mine. Why would we be somewhere I didn't know?"

            menu:
                "You seem uncertain":
                    cadmus "You're imagining things dear."
                    cadmus "Don't worry about unnecessary things."
                    cadmus "Just focus on me, yea?"

                    "The quickness in which he avoids a direct answer unnerves you."
                    "At the same time...he has yet to do anything to harm you."
                    "Maybe you could let this go for now."

                "Are we both trapped here?":
                    ## TODO: make his face no longer confused here
                    "Cadmus' gaze holds firm, whatever emotional turmoil the initial question put him in, is now gone."
                    cadmus "Such nonsense, I trapped you with me, how can we both be trapped?"

                    "You" "You seemed worried that I asked where we are."
                    "You" "Is it wrong of me to ask?"

                    "His gaze softens slightly."

                    cadmus "No. It's not."
                    cadmus "I promise...I'll protect you."

                    "He's resolute with his words, and doesn't say anything else."
                    "What exactly is he even protecting you from?"
    
    hide cadmus with dis
    play sound "<from 0 to 5>audio/sound effects/footsteps.mp3" fadeout 0.5
    "Cadmus stands from his seat, walking just out of your view."
    "Is he going somewhere?"
    "What is he doing?"

    menu:
        "Where are you going?":     
            camera at headPat
            "He laughs, placing his hand on your head."
            cadmus "I'm just stretching my legs, no need to panic."
            cadmus "Just going to walk the room. I'll be quick."
            play sound footSteps fadeout 1.0
            "He starts to walk, his footsteps filling your ears."

        "Don't leave me.":
            show cadmus at default with dis
            "He plops himself down in the chair, if only for a moment."
            show cadmus smileopenNU with dis
            cadmus "Silly mouse~ I'm just stretching my legs, I'll be back shortly."
            hide cadmus with dis
            play sound "<from 0 to 5>audio/sound effects/footsteps.mp3" fadeout 0.5
            "He once again stands, and sounds like he's stepping away."

            menu:
                "Beg him to stay":
                    "Cadmus stops, heading back to sit."
                    show cadmus questioning at default with dis
                    cadmus "Sure...if you're that concerned, I wasn't going to be long..."
                    "You" "I don't wanna be alone..."

                    show cadmus regularE with dis
                    "His expression is hard to read, but he stays where he is."
                    jump CareBadBranchA
                
                "Let him go.":
                    play sound footSteps fadeout 1.0
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
    "You can vaguely make out Cadmus' presence on the other side of the room, but you can't see him."
    "The feeling of his presence fades back into the darkness just as quickly as it was felt."
    "Trying to comprehend all this...it hurts your head."
    # screen shake and blur
    camera at continuousShake
    "That pounding sensation returns."
    "He hasn't tried to hurt you- the ropes aren't even tight."
    "So why does your head hurt so much?"
    "It feels like something eating away at you."

    cadmus "Hey, darling...hey, over here."
    camera at cameraReset
    show cadmus concern at default with dis
    "He suddenly comes into view across from you, pulling your focus from the pain."
    show cadmus sweating with dis

    cadmus "There we are."
    show cadmus smileopenNU with dis
    cadmus "It's all okay little mouse, I'm right here."

    "He eyes you carefully, that weird sensation disappearing again."
    show cadmus neutral with dis
    "You watch his eyes dance across your face, his expression hard to discern."
    "There's...sweat on his brow."
    "Did he run to you?"

    show cadmus smileopenNU with dis
    cadmus "Good, you're okay."
    cadmus "Told you I wouldn't be long, right?"

    show cadmus normalSmile with dis
    "He quickly wipes his forehead, eyes focusing back on yours, smiling slightly."
    "...does he know something you don't?"
    "How did he even know something was wrong?"
    "It's so hard to even see in here, you didn't even know where he was."

    menu:
        "You saved me...":
            ## Bad route B
            "You" "You're the reason that stopped right?"
            show cadmus questioning with dis
            cadmus "The...reason?"
            cadmus "I wouldn't call it-"
            "You" "So you're like...a hero."
            show cadmus eyebrowsR with dis
            "You state it, perhaps a bit more excitedly than you thought you would."
            
            "Clearly, he does love you, how else would the horrible pain in your head go away?"
            "He isn't holding you hostage."
            "He's protecting you."
            "You" "...You're my hero."
            show cadmus regularE with dis
            "Your words escape you in a longing whisper."
            "It startles you slightly, but you just can't help it."

            show cadmus eyebrowsC with dis
            "Cadmus watches you, a bit curious...perhaps worried..."
            "But he saved you, he must be worried for you!"

            cadmus "You feel alright?"
            "He places his hand on your forehead."
            show black with swipeDown
            "Though it falls over your eyes."

            "You" "Yes! Much better now that you're here!"

            "The smile on your face comes so naturally."
            "You feel safe with him."
            "He's truly wonderful."

            cadmus "Ok...good."
            show cadmus regularE with dis
            hide black with dis
            "His hand pulls from your eyes, he looks just as he always does."
            "Just lovely and perfect."

            jump CareBadBranchB


        "How did you know?":
            ## Good route
            show cadmus regularE with dis
            show cadmus eyebrowsTD with dis
            "Cadmus' smile slips away, brows knitting together."
            "Did you say something wrong?"
            show black at swipeDown
            "His hand reaches out to you, and covers your eyes."

            "You" "Cad-"

            cadmus "Shh."

            "A silence stretches between you two."
            "You can feel his hand quivering against your eyes."

            cadmus "If I ask you to believe in me..."
            cadmus "Will you?"

            menu:
                "Yes":
                    show cadmus concern
                    hide black with dis
                    "He takes his hand away, his expression is difficult to understand."

                    cadmus "You're so good to me."
                    $ _history = False
                    cadmus "You deserve so much better than this.{nw}"
                    $ _history = True
                    show cadmus normalSmile with dis
                    cadmus "I'm happy to have you here, little mouse."

                    "You could've sworn you heard something else."
                    jump CareGoodBranchA

                "No":
                    "You feel his fingers grip the side of your face."

                    "You" "I would appreciate an answer."
                    "You" "Anything at all."
                    cadmus "Will you believe in me if I do?"
                    "You" "Answer first."

                    "There's a hesitation thick in the air."

                    cadmus "I felt it too."
                    "No extra quips."
                    "You feel that he isn't lying, you're not sure why."

                    "You" "I believe you."
                    show cadmus normalSmile
                    hide black with dis
                    "He pulls his hand away, a small smile on his face."

                    cadmus "Thank you..."
                    $ _history = False
                    show cadmus concern with dis
                    cadmus "I'm so grateful that you believe me.{nw}"
                    $ _history = True
                    show cadmus normalSmile with dis
                    show cadmus smileopenNU with dis
                    cadmus "My little mouse is just the best~"

                    "Did he say something else?"
                    jump CareGoodBranchA

label CareGoodBranchA:
    show cadmus normalSmile at default with dis
    "You stare at him, trying to remember what he said before."
    "You {i}know{/i} he said something else."
    "But your mind is entirely blank."
    "Like there's a gap."
    "You're so sure if you focus hard enough..."

    show cadmus concern at lean
    cadmus "Pay attention."
    "You're immediately pulled from your thoughts from his harsh tone."
    cadmus "Drifting off is...dangerous."

    "You aren't entirely sure you understand, but you want to believe him."

    menu:
        "Your attitude is different.":
            show cadmus confused with dis
            show cadmus neutral with dis
            "Cadmus looks a bit confused at the statement."
            cadmus "My attitude has been the same this whole time?"
            cadmus "I'm not sure what you mean."
            cadmus "...I'm just trying to keep you safe."
        
        "You're...nice.":
            show cadmus embarassed with dis
            show cadmus smileclosedND with dis
            "Cadmus smiles, seeming a bit surprised at your comment."
            cadmus "I wouldn't be anything else to you my love."
            show cadmus eyesS with dis
            cadmus "...I want to keep you safe."
    
    "You" "You keep mentioning that...safe from what exactly?"
    show cadmus concern with dis
    show cadmus eyesSld with dis
    cadmus "I can't explain it."
    "You" "Can't? Or won't?"
    show cadmus eyesS with dis
    cadmus "You said you'd believe me didn't you?"
    cadmus "Believe me...if I could I would darling..."

    "He seems genuinely upset about lacking answers."
    camera at nodHead
    "You nod at him"
    show cadmus at sit
    extend ", and he leans back in his seat."

    $ _history = False
    show cadmus eyesSld with dis
    cadmus "I have about as much understanding as you...I think."
    show cadmus eyesS with dis
    cadmus "I don't know what I can and can't say."
    "You're immediately confused when he says that."
    "Before you get the chance to respond-"
    camera at continuousShake
    centered "{cps=10}{sc=3}...{/sc}"
    centered "{cps=10}{sc=3}Your head...{/sc}"
    centered "{cps=10}{sc=3}Why does it hurt so bad?{/sc}"
    centered "{cps=10}{sc=3}What the hell?{/sc}"
    $ _history = True
    camera at cameraReset
    show black zorder 10 at shortBlink

    cadmus "I'll make sure you stay safe."
    show cadmus smileopenNU with dis
    cadmus "You are so precious to me...nothing will harm you, darling."
    show cadmus armsR at lean
    "His hand comes to your cheek."
    "His demeanour is entirely different."
    "You feel...weirdly disoriented."
    "Did something happen just now?"

    menu:
        "Ask if he noticed anything":
            show cadmus confused with dis
            cadmus "Noticed what?"
            cadmus "I don't think anything odd happened."
            cadmus "It's just us here."
            "He rubs his thumb along your cheek."
            "Two swift motions."
            "You look at him a bit confused."
            show cadmus eyebrowsN with dis
            "He does it again."
            "...a 'Y'? As in...yes?"
            "...he did notice something, but can't acknowledge it aloud."
            "You both lock eyes."
            show cadmus normalSmile with dis
            show cadmus armsD -hand
            "He simply smiles, pulling his hand away."
            show cadmus at sit

        "Nuzzle his hand":
            jump badEndJumpPoint

        "Is something wrong?":
            show cadmus normalSmile with dis
            "Cadmus shakes his head, his smile reassuring."
            "You're startled when he rubs his thumb against your cheek."
            "Two quick swipes."
            "What is he doing?"
            "He seems to sense your confusion, and does it again."
            "...a letter? Maybe a 'Y'?"
            "Meaning...yes?"
            "...so something is wrong?"
            "Why can't he acknowledge it out loud, or even shake his head 'yes'?"
            show cadmus armsD -hand
            "He calmly pulls his hand away, as if nothing happened."
            show cadmus at sit
    
    "Even though you want to press further, you can tell from that...it'd be hard to."
    cadmus "There's much else for us to discuss."
    show cadmus inLove with dis
    cadmus "Like all the things that make you perfect~"
    cadmus "And so charming~"
    show cadmus normalSmile with dis
    show cadmus blush with dis
    cadmus "Just simply...everything."

    "You feel a bit nervous at that...does he really think so much of you?"
    "Is this some kind of ploy?"
    show cadmus smileopenNU with dis
    "He laughs, presumably at whatever face you're making, though his expression softens."

    show cadmus at lean
    cadmus "Come now, no need for that face."
    show cadmus concern with dis
    cadmus "Or...am I being too much?"
    show cadmus smileclosedND with dis
    cadmus "You are the being of my affections after all~"
    cadmus "Is that so hard to believe?"

    "He calmly stays in close proximity to you, unphased."

    show cadmus eyesSld with dis
    cadmus "Or..."
    show cadmus pout with dis
    cadmus "Do you not like me?"
    show cadmus eyesS with dis
    cadmus "...you can be honest."

    menu:
        "It's not that...":
            "You" "I'm just nervous."

            if pickedQuestionFirst:
                if areFirst:
                    show cadmus smileclosedND eyebrowsN with dis
                    cadmus "Ah, I suppose me being your first..."
                    cadmus "You would be, wouldn't you?"
                    show cadmus concern with dis
                    cadmus "I'm sorry love."
                    cadmus "I don't want to overwhelm you."
                else:
                    show cadmus smirk with dis
                    cadmus "I must cause a flutter {i}they{/i} didn't then hm?"
                    show cadmus smileopenNU eyebrowsN with dis
                    cadmus "A wonderful leg up I have~"
                    show cadmus concern with dis
                    cadmus "Though...I am sorry my love."
                    cadmus "I don't want to overwhelm you."
            else:
                show cadmus smileclosedND eyebrowsN with dis
                cadmus "You would be, wouldn't you?"
                show cadmus concern with dis
                cadmus "I'm sorry love."
                cadmus "I don't want to overwhelm you."

            "You" "...it's okay."

            show cadmus normalSmile with dis
            cadmus "It is?...good."
            cadmus "But if I'm ever too much, tell me."
            show cadmus at sit

        "I do like you.":
            show cadmus normalSmile with dis
            show cadmus smileopenNU blush with dis
            "His face brightens immediately, betraying his rough demeanor."

            cadmus "Ah...I could die right now."
            cadmus "I wouldn't though."
            show cadmus smileclosedND with dis
            cadmus "I couldn't be without you now that I have you~"

            "His dramatics catch you off guard, causing you to crack a smile."
            show cadmus smileopenNU with dis
            "Cadmus laughs, enjoying his little moment."
            show cadmus at sit

        "I don't.":
            show cadmus regularE with dis
            "His face loses expression."
            "Your words linger in the space, as the silence slowly overtakes its place."
            "What happened to his playfulness?"
            "He seemed like he was going to just...go with the punches."
            jump CareBadEndSpecial

    show cadmus concern with dis
    cadmus "I am sorry though..."
    cadmus "The ropes...they are for your safety."
    cadmus "I wish I could take them off."

    "You" "Is it really that bad?...whatever it is?"

    "He simply nods."

    "You" "Have you-"

    show cadmus eyesSld with dis
    "He nods again, the look in his eyes hard to read."

    if persistent.onReplay:
        "You suppose it makes sense..."
        "This isn't your first time here."
        "How many things has he tried at this point?"
    else:
        "But...that doesn't make any sense."
        "You only just got here...right?"
        "How could he have tried to take the ropes off...before?"
        "He has seemingly been talking as if he hasn't taken them off ever."
    
    show cadmus eyesS with dis
    cadmus "It's...better not to question."
    cadmus "But I {i}will{/i} protect you."
    show cadmus smileclosedND with dis
    cadmus "I do mean that."
    cadmus "With every fiber of my being."
    camera at cameraReset
    hide black
    hide blank

    "You have no reason to doubt him on that."
    "All you both can really do...is trust he can."
    show black zorder 5 at closeEyes
    pause 2
    jump CareGoodEnding

label CareGoodEnding:
    hide black
    show blank zorder 5 at blink

    show cadmus normalSmile with dis
    "You and Cadmus spent your time in relative comfort."
    cadmus "I'm glad we can just...be."
    cadmus "It's something I've missed. Just existing for the sake of it."
    "You" "Can you normally not?"
    show cadmus confusedLD with dis
    cadmus "That's hard to explain..."

    "There's a hesitancy, one you've become quite familiar with."
    "Topics that tend to be avoided, words that don't linger."
    "A taste of something different."

    show cadmus normalSmile with dis
    show cadmus smileopenNU
    cadmus "I can teach you something, that's what we can do today."

    "He holds his hand near your right, using his other hand to slide the ropes a bit."
    "You have a bit more room to move it."
    "Cadmus taps on your hand with his finger twice. Distinctly separated taps."

    "You" "...what are you doing?"
    cadmus "Teaching you, of course."
    show cadmus normalSmile with dis
    cadmus "You know what morse code is?"
    "You" "You're not teaching me that are you? Isn't that complicated?"

    show cadmus smirkingSoft with dis
    "He laughs, shaking his head."
    "He taps on your hand once."

    cadmus "Much simpler. Though I suppose that makes it harder, doesn't it?"
    "You" "It limits communication?"

    "He nods, tapping your hand twice."
    "Oh."
    "Twice is yes, once is no."
    "He's teaching you without speaking."

    show cadmus smileopenNU with dis
    cadmus "What a smart cookie~"

    "His eyes twinkle, staring at you with the utmost affection."

    cadmus "We'll make others I'm sure, do you have one?"

    show cadmus smirkingSoft with dis
    "As you ponder, he places your finger on top of his palm."

    menu:
        "Slide your finger on his palm":
            show cadmus smileopenNU blush with dis
            "Cadmus twitches a bit and he laughs."
            "Is he ticklish?"
            cadmus "What will that be?"
            "You" "\"I'm here.\""
            cadmus "Like saying everything's okay?"
            show cadmus -blush with dis
            cadmus "I like that."
            $ persistent.code = "slide"

        "Tap twice with two fingers":
            show cadmus smileopenNU with dis
            "He smiles as he watches you."
            cadmus "What will that mean?"
            "You" "\"Focus.\""
            cadmus "So that we stay centered?"
            cadmus "That works."
            $ persistent.code = "doubletap"

    "You both laugh, simply enjoying each other's company."
    "It's hard to imagine you used to feel uncomfortable because of him."

    cadmus "I'm going to get a drink, I'll be right back."
    hide cadmus with dis

    "He gets up every so often to walk the room."
    "You don't get those weird head pains much anymore."
    "Like you both aren't tethered, with clouded minds."
    "Sometimes it gets you wondering...when it will all go back to how it was."
    "It's hard to remember how long you've both been in this comfort."
    "As if it were a dream."
    "You hope to never wake from it."

    show cadmus at default with dis
    "He returns quickly- he still worries about losing you."
    "Even with his concerns, it seems they weren't all that warranted."
    "No matter how long he is gone for, you are both still here."
    
    show cadmus concern with dis
    cadmus "You're still here..."
    "You" "I have nowhere else to go, I don't get why it still shocks you."
    show cadmus smirk at lean
    cadmus "...I thought we would be gone by now."
    "You" "Gone?"

    "He takes your hand in his, his fingers calloused."

    "You" "Your hand seems worn."

    "You make the comment without much thought, he smiles."

    ## TODO: extend guitar convo with the new info
    show cadmus normalSmile with dis
    cadmus "I play in a band- lead guitar."
    "You" "Really?"
    show cadmus confused with dis
    cadmus "Is that surprising? Most people ask me if I'm in a band."
    show cadmus smirk with dis
    cadmus "It's the first question after \"Are you single?\""
    "You" "I'm {i}so{/i} sure you aren't just pulling my leg."

    show cadmus normalSmile with dis
    "He snickers, running his thumb on the back of your hand."

    cadmus "I do play guitar, I'm serious about that."
    "You" "And about the rest?"
    show cadmus smirkingSoft with dis
    cadmus "A secret~"

    show cadmus embarassed with dis
    cadmus "I hope I can play for you sometime."
    "You" "That would be nice."

    "Cadmus leans to your hand and kisses it, like it's the most delicate thing in the world."
    "To be with...the being of your affections."
    "Cadmus has really grown on you with the time you've spent together."
    show cadmus smileopenNU eyesS with dis
    "You know one day you will both be happier."
    show cadmus at sit
    "You are both happy right now, you're certain."
    "But you both will be happier."
    "So very soon."
    "{cps=10}..."
    camera:
        subpixel True
        blur 5.0
    "{cps=10}..."
    "Your head suddenly starts pounding."
    "Why does it hurt so much?"
    show cadmus concern with dis
    "You're trying to listen to him talk..."
    ## muffled he's saying "Hey...are you okay?" "Is something wrong?" "No no...no god." "Please, pay attention to me!" "Please..."
    stop music channel "music_CH1" fadeout 1.0
    stop music channel "music_CH2"
    "His words fail to reach your ears."
    camera:
        subpixel True
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.15)*HueMatrix(0.0) 
    "It hurts so badly."
    show cadmus at lean
    "You can see the fear in his eyes- the panic."
    show black zorder 5 at closeEyes
    "You shut your eyes, trying desperately to make it go away."
    "It will go away...won't it?"
    "{cps=10}...won't it?"

    scene black with fade
    camera at cameraReset
    pause (0.5)

    cadmus "Darling? Where did you go?"
    cadmus "...why did {b}it{/b} take you from me..."

    ## fade out, title "Care: Good Ending?"
    if persistent.onReplay == False:
        $ persistent.onReplay = True
    $ persistent.CareGoodEnd = True
    $ persistent.lastRoute = "CG"
    $ persistent.runNumber += 1
    $ renpy.save_persistent()
    pause (0.5)
    show text "{font=HelpMe.ttf}{sc=2}Care: Good Ending?{/sc}{/font}" with Dissolve(1.5)
    pause (2.0)
    hide text
    return

label CareBadBranchA:
    "You both sit and stare at each other in silence."
    "Other than the sounds of his fingers drumming idly against the chair."
    "You're happy he didn't walk away from you."
    "It would be extremely lonely without him sitting across from you."
    "His deep green eyes staring at you."
    "The way his hair falls onto his face."
    "How the lightbulb backlights his beautiful features."
    "You can't help...but feel like you need him right here."
    "It would be lonely without him."
    "His sigh pulls you from your thoughts."
    "Though...he doesn't say anything."

    menu:
        "Everything ok, dear?":
            "He sits a bit straighter."
            cadmus "Of course, of course."
            show cadmus smirking with dis
            cadmus "There's just...so much to think about, darling."
            "You can't help but be curious."

            menu:
                "Like what? Me?":
                    cadmus "Only you are ever on my mind~"

                "Such as~...":
                    cadmus "So so many things~"
                    "He pokes your nose gently."
                    cadmus "Nothing your pretty little head needs to worry about."

        "Are you speechless?":
            show cadmus at cadFidget
            "He adjusts himself in his seat."
            show cadmus smileclosedND with dis
            cadmus "Ah, well you are so charming, it's easy to be at a loss for words."
            cadmus "Though that should be completely unsurprising darling."
            "You can't help but smile, he knows exactly what to say."
    
    show cadmus regularE with dis
    "Cadmus falls silent again."
    "For some reason...you feel annoyed."
    show cadmus eyesSld with dis
    "Watching his gaze drift away annoys you even more."
    "Aren't you enough to hold his attention?"
    "You can't even tell where all these emotions are coming from."
    "You {b}need{/b} his attention."

    "You" "Where are you looking?!"
    show cadmus eyesS eyebrowsR with dis
    "His head snaps back at you."
    "You suppose your voice was a bit stern...it wasn't your intention..."
    show cadmus concern with dis
    cadmus "Nowhere, dear, don't worry!"
    cadmus "I'm simply just...so overwhelmed by you."

    "Your heart swells, his words so sickening and sweet."
    show cadmus armsR at lean
    "He gently rubs his thumb against your cheek."

    cadmus "I don't know what you're so worried about, I'm right here."

    menu:
        "Nuzzle his hand":
            label badEndJumpPoint:
                "Cadmus seems entirely taken aback."
                show cadmus regularE armsD -hand at sit
                "Pulling his hand away from you."

                "You" "Something wrong?"
                cadmus "Nothing. Sorry."

                show cadmus eyesSld with dis
                "His gaze drifts away again."
                "You" "Cadmus...did I upset you?"
                cadmus "No no, darling, of course not!"
                show cadmus eyesS smileopenNU with dis
                cadmus "You could never upset me, my lovely little mouse...it's okay."
                "His words make you smile."
        
        "Kiss his palm":
            "His hand twitches when your lips touch them."
            show cadmus pout eyebrowsR with dis
            cadmus "What are you-?"
            "His reaction is {i}so{/i} cute."
            "You can't help but chuckle at him."
            show cadmus armsD -hand at sit
            "Cadmus slowly pulls his hand away."

            "You" "I didn't upset you...did I?"
        
            cadmus "No, certainly not."
            show cadmus normalSmile with dis
            cadmus "How could the lovely being of my affections ever upset me?"
            cadmus "What silly thoughts you have."

            "His little pet name for you...he is so sweet~"

    show cadmus armsHair regularE with dis
    "He runs his fingers through his hair."
    "Every movement captures your eyes."
    "He is so pretty."

    cadmus "My dear..."
    show cadmus armsD -hairUp with dis
    cadmus "I really do need to stretch my legs for the moment."

    "You" "...Do you?"
    "You can't help but feel upset, a knot twisting in your heart."

    show cadmus smileopenNU with dis
    cadmus "I really won't be long...I promise."
    "He gently pats your head, before walking off."

    "You" "Hurry back!"
    play sound "<from 0 to 15>audio/sound effects/footsteps.mp3" fadeout 1.0
    "You lean towards his direction, the ropes tightly pulling against you as his footsteps drift away."
    hide cadmus with dis

label CareBadBranchBJump:
    "Now that he's gone everything feels..."
    "Empty."
    "He'll be back though."
    "He has nowhere to go."
    "Cadmus will be right back with you."
    "Every second that ticks by fills you with dread."
    "Even though you can still hear his footsteps."
    "You can't help but miss him."
    
    if CBBB:
        play sound runningWater volume 0.05 fadeout 2.0
        "You hear the sound of running water in the distance."
        "It stops just as quickly as it was heard."
    else:
        "You catch a glimpse of him at the other side of the room."
        "Though he disappears just as quickly as you caught him."

    "Oh how you miss him."
    "You feel like you're going to die without him."
    "You desperately need him back."
    jump CareBadEnd

label CareBadBranchB:
    $ CBBB = True
    show cadmus eyesSld with dis
    "You watch as he rubs his hands together, staring off at something."
    "What could be more interesting than you?"
    "You're right here."

    "You" "Cadmus, is something wrong?"

    show cadmus eyesS smileopenNU with dis
    cadmus "No, nothing to worry about."
    "He looks towards you and smiles, a smile you've become oh so familiar with."
    "Oh."
    "So."
    "Fond of."

    cadmus "Darling you worry far too much about trivial things."
    "You" "Worrying about you is...trivial? But that's absurd!"

    "Him saying such a thing makes your blood boil"
    "The being of {i}your{/i} affections?"
    "{i}Trivial?{/i}"

    show cadmus eyesSld frown with dis
    cadmus "Oh-"
    cadmus "I just meant you seem to worry over nothing, love. That's all."

    "You feel your muscles relax, you didn't even realize you were so tense."
    "Yes, of course that's what he meant."
    show cadmus eyesS neutral with dis
    "Why would he ever mean anything else?"
    "He loves you so much."
    "Just like you love him."
    "That isn't trivial at all."
    show cadmus eyebrowsR with dis
    "He wanted to keep you so safe he tied you to a chair."
    "Perhaps you are a danger to yourself."
    "Cadmus is so considerate of your safety and well being!"
    show cadmus frown with dis
    "He is so beautiful..."
    "And perfect..."
    "How lucky you are."

    cadmus "Um...darling?"
    "His voice pulls you from your thoughts."
    "You were on such a tangent it seems you left him confused due to your silence."

    "You" "Yes love?"
    "You wait with baited breath for whatever wonderful thing he's about to say."

    cadmus "I need to...stretch my legs again, for a moment."
    show cadmus regularE with dis
    cadmus "I'll only be a brief moment. Just to get a drink. You won't even know I was gone."

    menu:
        "You can't":
            "You" "You just left...why do you need to leave again?!"
            show cadmus eyebrowsR with dis
            "You can't help the rising volume of your voice, the panic of his absence already setting in without him even leaving."
            "You" "What if it happens again?!?! What if you don't return fast enough?!?!"

            show cadmus concern with dis
            cadmus "Darling darling, please, it's going to be just fine."
            cadmus "You need to relax~ it'll be just fine."

            hide cadmus with dis
            "You watch as he gets up, calmly leaving your view."
            "Despite how angry you feel it quickly subsides."

        
        "No!":
            show cadmus concern with dis
            cadmus "My love, you must understand...I'm just getting a drink."
            cadmus "You want me to die of thirst?"

            "You" "No no! Certainly not."
            "You feel panicked, how could you be so thoughtless!"
            "Cadmus, your beloved, would never abandon you!"
            "Dying of thirst...oh how dreadful..."
            "If only you could solve all his problems on your own."

            cadmus "I'll return before you know it."
            hide cadmus
    
    jump CareBadBranchBJump

label CareBadEnd:
    show cadmus at default with dis
    "You stare longingly at him as he finally returns to the chair."
    
    "You" "I missed you!"
    
    "You're so excited as he returns to you, he seems to tense when you speak."

    show cadmus confusedLD with dis
    cadmus "Yes...I missed you as well."

    "There's a long silence as you watch him, his beautiful sharp features accentuated as he glances off to the side."
    show cadmus regularE with dis
    "You can't help but love looking at him."
    "He's so beautiful."
    "The being of your affections."

    ## TODO: add a conversation based on one of the topics in the Cadmus Character Info sheet in the doc

    show cadmus concern with dis
    cadmus "Look...dear, I have to...go find something."
    show cadmus regularE with dis
    cadmus "Yes, yes, there is something I thought of."
    show cadmus smileopenNU with dis
    cadmus "A uh-...a gift! Just for you."

    "You" "Just for me?"

    "You can barely even contain your glee at the thought, tugging on the ropes to get closer to him."

    cadmus "Just for you, but you'll have to be patient."
    show cadmus smirking with dis
    cadmus "So make sure you wait for me."

    "You" "Of course!"

    hide cadmus with dis
    play sound footSteps fadeout 2.0
    "You hear his footsteps fade away."
    play sound doorOpen
    "You can hear the door from the other side of the room"
    play sound doorClose
    extend ", and it promptly shut."
    "Cadmus is bringing you a gift."
    "He's getting you a present!"
    "You've been so good."
    "And you love him so much!"
    "Of course you deserve a gift!"
    "{cps=10}..."
    "{cps=10}..."
    "He'll be back any minute, he always is."
    "{cps=10}..."
    "{cps=10}..."
    "You know whatever he's getting is going to be so lovely."
    "{cps=10}..."
    "{cps=10}..."
    "A gift for his precious little mouse."
    "{cps=10}..."
    "{cps=10}..."
    stop music channel "music_CH1" fadeout 1.0
    stop music channel "music_CH2"
    "Your head starts to hurt."
    "Cadmus still isn't back yet."
    "You mustn't fall asleep, he'll be here any moment."
    "You just know it..."
    "...he's always here."
    "{cps=10}...always here."

    scene black with fade
    pause (0.5)

    cadmus "By the time I get back they'll be asleep again..."
    cadmus "...another round will begin."

    ## fade out, title "Care: Bad Ending?"
    if persistent.onReplay == False:
        $ persistent.onReplay = True
    $ persistent.CareBadEnd = True
    $ persistent.lastRoute = "CB"
    $ persistent.runNumber += 1
    $ renpy.save_persistent()
    pause (0.5)
    show text "{font=HelpMe.ttf}{sc=2}Care: Bad Ending?{/sc}{/font}" with Dissolve(1.5)
    pause (2.0)
    hide text
    return


label CareBadEndSpecial:
    ## TODO: rewrite this. it's also kinda fuckin mid s m h
    "You want to try and say something, but every word is caught in your throat."
    show cadmus shadowTD frown lidsS with dis
    "His eyes stare daggers into you."
    "It tickles the back of your head in a way that just..."
    play sound heartBeat
    "Fills you with pure fear."
    "The silence stretches for longer than it should."
    show cadmus armsR at lean
    "His hand comes up to your face."
    "Nails digging into your cheeks."
    play sound pullOutKnife
    "You catch the glint of his knife being pulled from his pocket."
    "What is he doing...?"
    "{sc=3.5}You can't move.{/sc}"
    play sound ropeFalls
    "Suddenly you feel the ropes slip off you-"
    play sound knifeDrop
    "The sound of the knife clattering to the floor."
    camera at liftUp
    show cadmus smilecreepyTeeth with dis
    "Cadmus forces your head up as he bears his teeth at you."
    show black zorder 5 at closeEyes:
        yoffset -100
    "You scream as his teeth dig into the back of your neck."
    "The pounding in your head starts again."
    "{sc=3.5}You can't focus at all.{/sc}"
    stop music channel "music_CH1" fadeout 1.0
    stop music channel "music_CH2"
    "Shutting your eyes, trying to forget the pain."
    "You feel something wet against your shoulder."
    "As all sensation slips away."

    scene black with fade
    pause (0.5)

    cadmus "...I'm doing this for you."
    cadmus "Why won't you believe me?"

    ## fade out, title "Care: Lover's Quarrel Ending"
    if persistent.onReplay == False:
        $ persistent.onReplay = True
    $ persistent.CareSpecialEnd = True
    $ persistent.lastRoute = "CS"
    $ persistent.runNumber += 1
    $ renpy.save_persistent()
    pause (0.5)
    show text "{font=HelpMe.ttf}{sc=2}Care: Lover's Quarrel Ending{/sc}{/font}" with Dissolve(1.5)
    pause (2.0)
    hide text
    return




