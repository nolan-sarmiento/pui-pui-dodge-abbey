def on_right_repeated():
    Abbey.set_image(assets.image("""
        Abby-Right
    """))
    Abbey.x += 2
    IsOutOfFrame(Abbey)
controller.right.on_event(ControllerButtonEvent.REPEATED, on_right_repeated)

def on_on_overlap(sprite, otherSprite):
    sprites.destroy(Abbey, effects.fire, 5000)
    game.game_over(False)
    game.splash("You Lose!")
sprites.on_overlap(SpriteKind.player, SpriteKind.projectile, on_on_overlap)

def IsOutOfFrame(mySprite: Sprite):
    if mySprite.y >= 120:
        mySprite.y = 119
        return True
    elif mySprite.x <= 0:
        mySprite.x = 1
        return True
    elif mySprite.x >= 160:
        mySprite.x = 159
        return True
    else:
        return False
def SetupBrick():
    global Bricks, BrickSpeed
    Bricks = sprites.create(assets.image("""
        Brick
    """), SpriteKind.projectile)
    Bricks.set_position(randint(0, 160), 1)
    BrickSpeed = randint(1, 3)

def on_left_repeated():
    Abbey.set_image(assets.image("""
        Abby-Left
    """))
    Abbey.x += -2
    IsOutOfFrame(Abbey)
controller.left.on_event(ControllerButtonEvent.REPEATED, on_left_repeated)

BrickSpeed = 0
Bricks: Sprite = None
Abbey: Sprite = None
scene.set_background_color(8)
game.splash("Welcome to Pui Pui Dodge")
Abbey = sprites.create(assets.image("""
    Abby-Right
"""), SpriteKind.player)
Abbey.set_position(73, 101)
SetupBrick()

def on_forever():
    if IsOutOfFrame(Bricks):
        SetupBrick()
    else:
        Bricks.y += BrickSpeed
forever(on_forever)
