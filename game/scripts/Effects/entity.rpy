image snakeC:
    subpixel True
    blur 2
    zoom 0.3
    rotate 180
    ypos 400
    glitch("images/Entity/snake_cluster.png", offset=40, randomkey=None)
    pause 0.2
    glitch("images/Entity/snake_cluster.png", offset=50, randomkey=None)
    pause 0.2
    repeat

image snakeH:
    subpixel True
    blur 2
    zoom 0.2
    xpos 500
    yalign 0
    glitch("images/Entity/snake_hanging.png", offset=60, randomkey=None)
    pause 0.2
    glitch("images/Entity/snake_hanging.png", offset=90, randomkey=None)
    pause 0.2
    repeat

image snakeS:
    subpixel True
    zoom 0.3
    blur 2
    pos (0.77, 0.97)
    rotate 54
    glitch("images/Entity/snake_slither.png", offset=30, randomkey=None)
    pause 0.2
    glitch("images/Entity/snake_slither.png", offset=40, randomkey=None)
    pause 0.2
    repeat


default previousEntity = -1
init python:
    imageList = ["snakeC", "snakeH", "snakeS"]

    def showRandSnake():
        indexes = [0,1,2]
        global previousEntity
        if previousEntity >= 0:
            renpy.hide(imageList[previousEntity])
            indexes.remove(previousEntity)

        currentEntity = indexes[renpy.random.randint(0,len(indexes)-1)]
        
        if renpy.random.randint(1,100) < 30:
            previousEntity = currentEntity
            renpy.show(imageList[currentEntity])

## TODO: find spot to put this in the code, and add a check for being on subsequent run
screen entityEffect():
    ## TODO: find a way to have these occur at the same time, but the HIDE waits 3 seconds before occuring
    timer 60 repeat True action Function(showRandSnake)

