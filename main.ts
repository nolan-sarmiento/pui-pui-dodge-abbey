controller.right.onEvent(ControllerButtonEvent.Repeated, function () {
    Abbey.setImage(assets.image`Abby-Right`)
    Abbey.x += 2
    IsOutOfFrame(Abbey)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Projectile, function (sprite, otherSprite) {
    sprite.startEffect(effects.fire, 1000)
    game.gameOver(false)
    game.splash("You Lose!")
})
function IsOutOfFrame (mySprite: Sprite) {
    if (mySprite.y >= 120) {
        mySprite.y = 119
        return true
    } else if (mySprite.x <= 0) {
        mySprite.x = 1
        return true
    } else if (mySprite.x >= 160) {
        mySprite.x = 159
        return true
    } else {
        return false
    }
}
function SetupBrick () {
    Bricks = sprites.create(assets.image`Brick`, SpriteKind.Projectile)
    Bricks.setPosition(randint(0, 160), 1)
    BrickSpeed = randint(1, 3)
}
controller.left.onEvent(ControllerButtonEvent.Repeated, function () {
    Abbey.setImage(assets.image`Abby-Left`)
    Abbey.x += -2
    IsOutOfFrame(Abbey)
})
let BrickSpeed = 0
let Bricks: Sprite = null
let Abbey: Sprite = null
scene.setBackgroundColor(8)
game.splash("Welcome to Pui Pui Dodge")
Abbey = sprites.create(assets.image`Abby-Right`, SpriteKind.Player)
Abbey.setPosition(73, 101)
SetupBrick()
forever(function () {
    if (IsOutOfFrame(Bricks)) {
        SetupBrick()
    } else {
        Bricks.y += BrickSpeed
    }
})
