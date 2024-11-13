layeredimage cadmus:

    group base:
        attribute base default:
            "base"
        attribute baseAU:
            "base 2 hu"

    group shadow:
        attribute shadowN:
            "eyebrows shadow"
        attribute shadowTD:
            "eyebrows tilted down shadows"
        attribute shadowTU:
            "eyebrows tilted up shadows"
        attribute shadowR:
            "eyebrows raised shadows"
        attribute shadowC:
            "eyebrows confusion shadows"

    group eyebacks:
        attribute eyeW default:
            "eye whites"
        attribute eyeB:
            "eye blacks"
        attribute eyeBS:
            "eye bloodshot"

    group pupils:
        attribute eyesS default:
            "pupils_snake"
        attribute eyesSld:
            "pupils_snake_ld"
        attribute eyesH:
            "pupils_heart"
        attribute eyesHld:
            "pupils_heart_ld"
        attribute eyesCRE:
            "pupils_creepy"
        attribute eyesCREld:
            "pupils_creepy_ld"
        attribute eyesCRA:
            "pupils_crazy"
        attribute eyesCRAld:
            "pupils_crazy_ld"
        attribute emptyEyes:
            "images/Cadmus/emptySprite.png"

    group eyes:
        attribute lidsR default:
            "cadmusblinkingneutral"
        attribute lidsS:
            "cadmusblinkingsquint"
        attribute lidsC:
            "lids closed"
        attribute lidsE:
            "images/Cadmus/emptySprite.png"
    
    group eyebrows:
        attribute eyebrowsN default:
            "eyebrows"
        attribute eyebrowsR:
            "eyebrows raised"
        attribute eyebrowsC:
            "eyebrows confusion"
        attribute eyebrowsTD:
            "eyebrows tilted down"
        attribute eyebrowsTU:
            "eyebrows tilted up"

    group mouth:
        attribute neutral default:
            "nd frown"
        attribute lick:
            "nd lick"
        attribute smileclosedND:
            "nd smile closed"
        attribute tongueOut:
            "nd tongue out"
        attribute disgust:
            "nu disgust"
        attribute gasp:
            "nu gasp"
        attribute pout:
            "nu pout"
        attribute smirk:
            "nu smile closed"
        attribute smileopenNU:
            "nu smile open"
        attribute smileteeth:
            "nu smile teeth"
        attribute smilecreepy:
            "nd smile no teeth creepy"
        attribute smilecreepyTeeth:
            "nd smile teeth creepy"
        attribute frown:
            "nd frown"
    
    group nosering:
        attribute ND default:
            "nd nose ring"
        attribute NU:
            "nu nose ring"

    group hair:
        attribute hair default:
            "hair"
        attribute hairUp:
            "hair up"
        attribute HAHABALD:
            "images/Cadmus/emptySprite.png"

    group arms:
        attribute armsD default:
            "armsd"
        attribute armsHK:
            "armshk"
        attribute armsKP:
            "armspk"
        attribute armsSH:
            "armssh"
        attribute armsHair:
            "armshair"
        attribute armsHighSH:
            "armshighsh"
        attribute armsR:
            "armsr"
        attribute armsT:
            "armstied"

    group hand:
        attribute hand:
            "hand"

    group extras multiple:
        attribute angryMark:
            "angy mark"
        attribute sweating:
            "sweating"
        attribute uglyTears:
            "ugly tears"
        attribute uglyTearsNU:
            "ugly tears nu"
        attribute blush:
            "blushing"

    group blood:
        attribute bloodyarmsHair:
            "base 2 hair up arms bloody"
        attribute bloodyarmsD:
            "base arms down bloody"
        attribute bloodyarmsHK:
            "base holding knife bloody"
        attribute bloodyarmsKP:
            "base playing w knife bloody"
        attribute bloodyarmsR:
            "base reach out n touch face 1 bloody"
        attribute bloodyarmsSH:
            "base shoosh bloody"
        attribute bloodyarmsSHH:
            "base shoosh higher bloody"
    
    group handBlood:
        attribute bloodyHand:
            "base reach out n touch face 2 bloody"

    group faces:
        attribute confused:
            "images/Cadmus/emptySprite.png"
        attribute confusedLD:
            "images/Cadmus/emptySprite.png"
        attribute annoyed:
            "images/Cadmus/emptySprite.png"
        attribute inLove:
            "images/Cadmus/emptySprite.png"
        attribute embarassed:
            "images/Cadmus/emptySprite.png"
        attribute crazy:
            "images/Cadmus/emptySprite.png"
        attribute playfulK:
            "images/Cadmus/emptySprite.png"
        attribute regularE:
            "images/Cadmus/emptySprite.png"
        attribute questioning:
            "images/Cadmus/emptySprite.png"
        attribute normalSmile:
            "images/Cadmus/emptySprite.png"
        attribute angie:
            "images/Cadmus/emptySprite.png"
        attribute smirking:
            "images/Cadmus/emptySprite.png"
        attribute smirkingSoft:
            "images/Cadmus/emptySprite.png"
        attribute disappointed:
            "images/Cadmus/emptySprite.png"
        attribute concern:
            "images/Cadmus/emptySprite.png"
        attribute questioningA:
            "images/Cadmus/emptySprite.png"
        attribute creepy:
            "images/Cadmus/emptySprite.png"
        attribute quiveringEyes:
            "images/Cadmus/emptySprite.png"
        attribute frowning:
            "images/Cadmus/emptySprite.png"
        attribute shock:
            "images/Cadmus/emptySprite.png"
        attribute scared:
            "images/Cadmus/emptySprite.png"

    group remove multiple:
        attribute removeExtras:
            "images/Cadmus/emptySprite.png"
        attribute removeShadows:
            "images/Cadmus/emptySprite.png"
        attribute removeLids:
            "images/Cadmus/emptySprite.png"
        attribute removeBlood:
            "images/Cadmus/emptySprite.png"
        attribute resetArms:
            "images/Cadmus/emptySprite.png"


image cadmusblinkingneutral:
    "lids open"
    function blinky
    "lids closed"
    pause 0.2
    repeat

image cadmusblinkingsquint:
    "lids squint"
    function blinky
    "lids closed"
    pause 0.2
    repeat


transform default:
    xalign 0.4
    xoffset 0
    zoom 0.45

## was not fuckin prepared for that
transform jumpscare:
    yalign 0.2
    xoffset -800
    zoom 2.5

transform lean:
    ease 0.5 zoom 1.0 yalign 0.2 xoffset -200

transform leanSnap:
    zoom 1.0 yalign 0.2 xoffset -200

transform sit:
    ease 1.0 zoom 0.45 xalign 0.4 xoffset 0



##stuff for blinks
default blink_timer = renpy.random.randint(2,8) #min and max gap between blinks in seconds

init python:
    def blinky(trans,st,at):
        global blink_timer
        if st >= blink_timer:
            blink_timer = renpy.random.randint(2,8)
            return None
        else:
            return 0

## Stuff for grouping emoting together!!! yay!!!
init python:
    def cadmus_expressions(tagged_attributes):
        t_attrib = list(tagged_attributes)

    # Just for mouth movements ONLY, auto puts correct nosering

        if 'neutral' in t_attrib:
            t_attrib.append('ND')

        if 'lick' in t_attrib:
            t_attrib.append('ND')

        if 'smileclosedND' in t_attrib:
            t_attrib.append('ND')
        
        if 'tongueOut' in t_attrib:
            t_attrib.append('ND')

        if 'disgust' in t_attrib:
            t_attrib.append('NU')

        if 'gasp' in t_attrib:
            t_attrib.append('NU')

        if 'pout' in t_attrib:
            t_attrib.append('NU')

        if 'smirk' in t_attrib:
            t_attrib.append('NU')

        if 'smileopenNU' in t_attrib:
            t_attrib.append('NU')

        if 'smileteeth' in t_attrib:
            t_attrib.append('NU')
        
        if 'smilecreepyTeeth' in t_attrib:
            t_attrib.append('ND')
        
        if 'smilecreepy' in t_attrib:
            t_attrib.append('ND')
        
        if 'frown' in t_attrib:
            t_attrib.append('ND')

        # eyebrow shadows

        if 'shadowTD' in t_attrib:
            t_attrib.append('eyebrowsTD')

        if 'shadowTU' in t_attrib:
            t_attrib.append('eyebrowsTU')

        if 'shadowN' in t_attrib:
            t_attrib.append('eyebrowsN')
        
        if 'shadowR' in t_attrib:
            t_attrib.append('eyebrowsR')

        if 'shadowC' in t_attrib:
            t_attrib.append('eyebrowsC')

        ## arms to face
        if 'armsD' in t_attrib:
            t_attrib.append('base')

        if 'armsR' in t_attrib:
            t_attrib.append('hand')

        if 'armsHair' in t_attrib:
            t_attrib.append('baseAU')
            t_attrib.append('hairUp')

        # FOR EYE SHAKING:
        if 'quiveringEyes' in t_attrib:
            t_attrib.append('lidsE')
            t_attrib.append('emptyEyes')
            t_attrib.append('HAHABALD')

        # FACES
        # remember to put all extras as things to remove if they aren't in use!
        # as well as include EVERY major piece of expression + arms!

        # this one is the default expression
        if 'regularE' in t_attrib:
            t_attrib.append('-blush')
            t_attrib.append('-angryMark')
            t_attrib.append('-sweating')
            t_attrib.append('-uglyTears')
            t_attrib.append('-uglyTearsNU')
            t_attrib.append('-shadowTD')
            t_attrib.append('-shadowTU')
            t_attrib.append('-shadowN')
            t_attrib.append('-lidsS')
            t_attrib.append('-lidsC')
            t_attrib.append('-lidsE')
            t_attrib.append('-HAHABALD')

            t_attrib.append('eyebrowsN')
            t_attrib.append('eyesS')
            t_attrib.append('neutral')
            t_attrib.append('ND')

        if 'angie' in t_attrib:
            t_attrib.append('-blush')
            t_attrib.append('-angryMark')
            t_attrib.append('-sweating')
            t_attrib.append('-uglyTears')
            t_attrib.append('-uglyTearsNU')
            t_attrib.append('-shadowTU')
            t_attrib.append('-shadowN')
            t_attrib.append('-lidsC')
            t_attrib.append('-lidsE')
            t_attrib.append('-HAHABALD')

            t_attrib.append('shadowTD')
            t_attrib.append('eyebrowsTD')
            t_attrib.append('lidsS')
            t_attrib.append('eyeBS')
            t_attrib.append('frown')
            t_attrib.append('ND')

        if 'frowning' in t_attrib:
            t_attrib.append('-blush')
            t_attrib.append('-angryMark')
            t_attrib.append('-sweating')
            t_attrib.append('-uglyTears')
            t_attrib.append('-uglyTearsNU')
            t_attrib.append('-shadowTD')
            t_attrib.append('-shadowTU')
            t_attrib.append('-shadowN')
            t_attrib.append('-lidsS')
            t_attrib.append('-lidsC')
            t_attrib.append('-lidsE')
            t_attrib.append('-HAHABALD')

            t_attrib.append('eyebrowsTU')
            t_attrib.append('frown')
            t_attrib.append('ND')

        if 'normalSmile' in t_attrib:
            t_attrib.append('-blush')
            t_attrib.append('-angryMark')
            t_attrib.append('-sweating')
            t_attrib.append('-uglyTears')
            t_attrib.append('-uglyTearsNU')
            t_attrib.append('-shadowTD')
            t_attrib.append('-shadowTU')
            t_attrib.append('-shadowN')
            t_attrib.append('-lidsS')
            t_attrib.append('-lidsC')
            t_attrib.append('-lidsE')
            t_attrib.append('-HAHABALD')

            t_attrib.append('eyebrowsN')
            t_attrib.append('eyesS')
            t_attrib.append('smileclosedND')
            t_attrib.append('ND')

        if 'smirking' in t_attrib:
            t_attrib.append('-blush')
            t_attrib.append('-angryMark')
            t_attrib.append('-sweating')
            t_attrib.append('-uglyTears')
            t_attrib.append('-uglyTearsNU')
            t_attrib.append('-shadowTU')
            t_attrib.append('-shadowN')
            t_attrib.append('-lidsS')
            t_attrib.append('-lidsC')
            t_attrib.append('-lidsE')
            t_attrib.append('-HAHABALD')

            t_attrib.append('shadowTD')
            t_attrib.append('eyebrowsTD')
            t_attrib.append('eyesS')
            t_attrib.append('smirk')
            t_attrib.append('NU')

        if 'smirkingSoft' in t_attrib:
            t_attrib.append('-blush')
            t_attrib.append('-angryMark')
            t_attrib.append('-sweating')
            t_attrib.append('-uglyTears')
            t_attrib.append('-uglyTearsNU')
            t_attrib.append('-shadowTD')
            t_attrib.append('-shadowTU')
            t_attrib.append('-shadowN')
            t_attrib.append('-lidsS')
            t_attrib.append('-lidsC')
            t_attrib.append('-lidsE')
            t_attrib.append('-HAHABALD')

            t_attrib.append('eyebrowsN')
            t_attrib.append('eyesS')
            t_attrib.append('smirk')
            t_attrib.append('NU')

        if 'confused' in t_attrib:
            t_attrib.append('-blush')
            t_attrib.append('-angryMark')
            t_attrib.append('-sweating')
            t_attrib.append('-uglyTears')
            t_attrib.append('-uglyTearsNU')
            t_attrib.append('-shadowTD')
            t_attrib.append('-shadowTU')
            t_attrib.append('-shadowN')
            t_attrib.append('-lidsS')
            t_attrib.append('-lidsC')
            t_attrib.append('-lidsE')
            t_attrib.append('-HAHABALD')

            t_attrib.append('eyesS')
            t_attrib.append('eyebrowsC')
            t_attrib.append('frown')
            t_attrib.append('ND')
        
        if 'confusedLD' in t_attrib:
            t_attrib.append('-blush')
            t_attrib.append('-angryMark')
            t_attrib.append('-sweating')
            t_attrib.append('-uglyTears')
            t_attrib.append('-uglyTearsNU')
            t_attrib.append('-shadowTD')
            t_attrib.append('-shadowTU')
            t_attrib.append('-shadowN')
            t_attrib.append('-lidsS')
            t_attrib.append('-lidsC')
            t_attrib.append('-lidsE')
            t_attrib.append('-HAHABALD')

            t_attrib.append('eyesSld')
            t_attrib.append('eyebrowsC')
            t_attrib.append('frown')
            t_attrib.append('ND')

        if 'concern' in t_attrib:
            t_attrib.append('-blush')
            t_attrib.append('-angryMark')
            t_attrib.append('-sweating')
            t_attrib.append('-uglyTears')
            t_attrib.append('-uglyTearsNU')
            t_attrib.append('-shadowTD')
            t_attrib.append('-shadowTU')
            t_attrib.append('-shadowN')
            t_attrib.append('-lidsS')
            t_attrib.append('-lidsC')
            t_attrib.append('-lidsE')
            t_attrib.append('-HAHABALD')

            t_attrib.append('eyesS')
            t_attrib.append('eyebrowsTU')
            t_attrib.append('pout')
            t_attrib.append('NU')

        if 'shock' in t_attrib:
            t_attrib.append('-blush')
            t_attrib.append('-angryMark')
            t_attrib.append('-sweating')
            t_attrib.append('-uglyTears')
            t_attrib.append('-uglyTearsNU')
            t_attrib.append('-shadowTD')
            t_attrib.append('-shadowTU')
            t_attrib.append('-shadowN')
            t_attrib.append('-lidsS')
            t_attrib.append('-lidsC')
            t_attrib.append('-lidsE')
            t_attrib.append('-HAHABALD')

            t_attrib.append('eyesS')
            t_attrib.append('eyebrowsR')
            t_attrib.append('gasp')
            t_attrib.append('NU')

        if 'scared' in t_attrib:
            t_attrib.append('-blush')
            t_attrib.append('-angryMark')
            t_attrib.append('-sweating')
            t_attrib.append('-shadowTD')
            t_attrib.append('-shadowTU')
            t_attrib.append('-shadowN')
            t_attrib.append('-lidsS')
            t_attrib.append('-lidsC')
            t_attrib.append('-lidsE')
            t_attrib.append('-HAHABALD')

            t_attrib.append('eyesS')
            t_attrib.append('eyebrowsTU')
            t_attrib.append('uglyTearsNU')
            t_attrib.append('gasp')
            t_attrib.append('NU')
        
        if 'disappointed' in t_attrib:
            t_attrib.append('-blush')
            t_attrib.append('-angryMark')
            t_attrib.append('-sweating')
            t_attrib.append('-uglyTears')
            t_attrib.append('-uglyTearsNU')
            t_attrib.append('-shadowTD')
            t_attrib.append('-shadowTU')
            t_attrib.append('-shadowN')
            t_attrib.append('-lidsS')
            t_attrib.append('-lidsC')
            t_attrib.append('-lidsE')
            t_attrib.append('-HAHABALD')

            t_attrib.append('eyesS')
            t_attrib.append('eyebrowsTD')
            t_attrib.append('frown')
            t_attrib.append('ND')

        if 'annoyed' in t_attrib:
            t_attrib.append('-blush')
            t_attrib.append('-sweating')
            t_attrib.append('-uglyTears')
            t_attrib.append('-uglyTearsNU')
            t_attrib.append('-shadowTD')
            t_attrib.append('-shadowTU')
            t_attrib.append('-shadowN')
            t_attrib.append('-lidsS')
            t_attrib.append('-lidsC')
            t_attrib.append('-lidsE')
            t_attrib.append('-HAHABALD')

            t_attrib.append('eyesS')
            t_attrib.append('eyebrowsTD')
            t_attrib.append('pout')
            t_attrib.append('NU')
            t_attrib.append('angryMark')

        if 'inLove' in t_attrib:
            t_attrib.append('-angryMark')
            t_attrib.append('-sweating')
            t_attrib.append('-uglyTears')
            t_attrib.append('-uglyTearsNU')
            t_attrib.append('-shadowTD')
            t_attrib.append('-shadowTU')
            t_attrib.append('-shadowN')
            t_attrib.append('-lidsS')
            t_attrib.append('-lidsC')
            t_attrib.append('-lidsE')
            t_attrib.append('-HAHABALD')

            t_attrib.append('blush')
            t_attrib.append('eyebrowsN')
            t_attrib.append('eyesH')
            t_attrib.append('smileteeth')
            t_attrib.append('NU')

        if 'embarassed' in t_attrib:
            t_attrib.append('-angryMark')
            t_attrib.append('-sweating')
            t_attrib.append('-uglyTears')
            t_attrib.append('-uglyTearsNU')
            t_attrib.append('-shadowTD')
            t_attrib.append('-shadowTU')
            t_attrib.append('-shadowN')
            t_attrib.append('-lidsS')
            t_attrib.append('-lidsC')
            t_attrib.append('-lidsE')
            t_attrib.append('-HAHABALD')

            t_attrib.append('blush')
            t_attrib.append('eyebrowsN')
            t_attrib.append('eyesSld')
            t_attrib.append('pout')
            t_attrib.append('NU')

        if 'playfulK' in t_attrib:
            t_attrib.append('-blush')
            t_attrib.append('-angryMark')
            t_attrib.append('-sweating')
            t_attrib.append('-uglyTears')
            t_attrib.append('-uglyTearsNU')
            t_attrib.append('-shadowTD')
            t_attrib.append('-shadowTU')
            t_attrib.append('-shadowN')
            t_attrib.append('-lidsS')
            t_attrib.append('-lidsC')
            t_attrib.append('-lidsE')
            t_attrib.append('-HAHABALD')

            t_attrib.append('armsKP')
            t_attrib.append('eyebrowsN')
            t_attrib.append('eyesS')
            t_attrib.append('smileopenNU')
            t_attrib.append('NU')

        if 'questioning' in t_attrib:
            t_attrib.append('-blush')
            t_attrib.append('-angryMark')
            t_attrib.append('-sweating')
            t_attrib.append('-uglyTears')
            t_attrib.append('-uglyTearsNU')
            t_attrib.append('-shadowTD')
            t_attrib.append('-shadowTU')
            t_attrib.append('-shadowN')
            t_attrib.append('-HAHABALD')

            t_attrib.append('lidsS')
            t_attrib.append('eyebrowsC')
            t_attrib.append('eyesS')
            t_attrib.append('pout')
            t_attrib.append('NU')

        if 'questioningA' in t_attrib:
            t_attrib.append('-blush')
            t_attrib.append('-angryMark')
            t_attrib.append('-sweating')
            t_attrib.append('-uglyTears')
            t_attrib.append('-uglyTearsNU')
            t_attrib.append('-shadowTU')
            t_attrib.append('-shadowN')
            t_attrib.append('-HAHABALD')

            t_attrib.append('shadowTD')
            t_attrib.append('lidsS')
            t_attrib.append('eyebrowsTD')
            t_attrib.append('eyesS')
            t_attrib.append('smirk')
            t_attrib.append('NU')

        if 'creepy' in t_attrib:
            t_attrib.append('-angryMark')
            t_attrib.append('-sweating')
            t_attrib.append('-uglyTears')
            t_attrib.append('-uglyTearsNU')
            t_attrib.append('-shadowTU')
            t_attrib.append('-shadowN')
            t_attrib.append('-blush')
            t_attrib.append('-HAHABALD')

            t_attrib.append('lidsS')
            t_attrib.append('bloodyarmsD')
            t_attrib.append('shadowTD')
            t_attrib.append('eyebrowsTD')
            t_attrib.append('eyesCRA')
            t_attrib.append('smilecreepy')
            t_attrib.append('ND')

        if 'crazy' in t_attrib:
            t_attrib.append('-angryMark')
            t_attrib.append('-sweating')
            t_attrib.append('-uglyTears')
            t_attrib.append('-uglyTearsNU')
            t_attrib.append('-shadowTU')
            t_attrib.append('-shadowN')
            t_attrib.append('-blush')
            t_attrib.append('-lidsS')
            t_attrib.append('-lidsC')
            t_attrib.append('-lidsE')
            t_attrib.append('-HAHABALD')

            t_attrib.append('bloodyarmsD')
            t_attrib.append('shadowTD')
            t_attrib.append('eyebrowsTD')
            t_attrib.append('eyesCRA')
            t_attrib.append('eyeB')
            t_attrib.append('smilecreepyteeth')
            t_attrib.append('ND')

        ## thing to remove all the extras!!
        if 'removeExtras' in t_attrib:
            t_attrib.append('-blush')
            t_attrib.append('-angryMark')
            t_attrib.append('-sweating')
            t_attrib.append('-uglyTears')
            t_attrib.append('-uglyTearsNU')
            t_attrib.append('-eyeBS')
            t_attrib.append('-eyeB')
        
        if 'removeShadows' in t_attrib:
            t_attrib.append('-shadowTD')
            t_attrib.append('-shadowTU')
            t_attrib.append('-shadowN')
            t_attrib.append('-shadowR')
            t_attrib.append('-shadowC')

        if 'removeLids' in t_attrib:
            t_attrib.append('-lidsS')
            t_attrib.append('-lidsC')

        if 'removeBlood' in t_attrib:
            t_attrib.append('-bloodyarmsD')
            t_attrib.append('-bloodyarmsHair')
            t_attrib.append('-bloodyarmsHK')
            t_attrib.append('-bloodyarmsKP')
            t_attrib.append('-bloodyarmsR')
            t_attrib.append('-bloodyarmsSH')
            t_attrib.append('-bloodyarmsSHH')

        if 'resetArms' in t_attrib:
            t_attrib.append('-armsHair')
            t_attrib.append('-armsHK')
            t_attrib.append('-armsKP')
            t_attrib.append('-armsR')
            t_attrib.append('-armsSH')
            t_attrib.append('-armsSHH')
            t_attrib.append('-hand')



        return tuple(t_attrib)


# definitions
define config.adjust_attributes = {
    "cadmus": cadmus_expressions
}
