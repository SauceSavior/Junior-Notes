WINDOW_WIDTH=1280
WINDOW_HEIGHT=720
push=require 'push'

VIRTUAL_WIDTH=432
VIRTUAL_HEIGHT=243

function love.load()
    love.graphics.setDefaultFilter('nearest','nearest')

    smallFont=love.graphics.newFont('font.ttf',8)

    love.graphics.setFont(smallFont)

    push:setupScreen(VIRTUAL_WIDTH,VIRTUAL_HEIGHT,WINDOW_WIDTH,WINDOW_HEIGHT,{
            fullscreen=false,
            resizable=false,
            vsync=true
    })
end

function love.update()
end

function love.draw()
    push:apply('start')

    love.graphics.clear(40,45,52,225)

    love.graphics.printf('Hello Pong!',0,VIRTUAL_HEIGHT-235,VIRTUAL_WIDTH,'center')

    love.graphics.rectangle('fill',10,30,5,20)
    love.graphics.rectangle('fill',VIRTUAL_WIDTH-10,VIRTUAL_HEIGHT-50,5,20)

    love.graphics.rectangle('fill',VIRTUAL_WIDTH/2,VIRTUAL_HEIGHT/2,4,4)
    push:apply('end')
end

