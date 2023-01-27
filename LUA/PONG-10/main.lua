WINDOW_WIDTH=1280
WINDOW_HEIGHT=720
push=require 'push'
Class=require 'class'
require 'Ball' 
require 'Paddle'

VIRTUAL_WIDTH=432
VIRTUAL_HEIGHT=243

PADDLE_SPEED=200




function love.load()
    love.graphics.setDefaultFilter('nearest','nearest')

    love.window.setTitle('Pong')

    math.randomseed(os.time())


    smallFont=love.graphics.newFont('font.ttf',8)
    scoreFont=love.graphics.newFont('font.ttf',32)
    largeFont=love.graphics.newFont('font.ttf',16)

    love.graphics.setFont(smallFont)


    push:setupScreen(VIRTUAL_WIDTH,VIRTUAL_HEIGHT,WINDOW_WIDTH,WINDOW_HEIGHT,{
            fullscreen=false,
            resizable=false,
            vsync=true
    })
    player1Score=0
    player2Score=0

    player1=Paddle(10,30,5,20)
    player2=Paddle(VIRTUAL_WIDTH-10,VIRTUAL_HEIGHT-30,5,20)

    ball=Ball(VIRTUAL_WIDTH/2-2,VIRTUAL_HEIGHT/2-2,4,4)
    gameState='start'
end



function love.update(dt)
    if love.keyboard.isDown('w')then
        player1.dy=-PADDLE_SPEED
    elseif love.keyboard.isDown('s') then
        player1.dy=PADDLE_SPEED
    else
        player1.dy=0
    end

    if love.keyboard.isDown('up')then
        player2.dy=-PADDLE_SPEED 
    elseif love.keyboard.isDown('down') then
        player2.dy=PADDLE_SPEED
    else
        player2.dy=0
    end

    if gameState=='serve' then
        if servingPlayer==1 then
            ball.dx=math.random(140,200)
        else
            ball.dx=-math.random(140,200)
        end
        ball.dy=math.random(-50,50)
    elseif gameState=='play' then

        if ball:collides(player1) then
            ball.dx = -ball.dx*1.03
            ball.x=player1.x+5

            if ball.dy<0 then 
                ball.dy=-math.random(10,150)
            else
                ball.dy=math.random(10,150)
            end
        end

        if ball:collides(player2) then
            ball.dx = -ball.dx*1.03
            ball.x=player2.x-5

            if ball.dy<0 then 
                ball.dy=-math.random(10,150)
            else
                ball.dy=math.random(10,150)
            end
        end

        if ball.y<=0 then
            ball.y=0
            ball.dy=-ball.dy
        end
        if ball.y>= VIRTUAL_HEIGHT-4 then
            ball.y=VIRTUAL_HEIGHT-4
            ball.dy=-ball.dy
        end

        if ball.x<0 then
            player2Score=player2Score+1
            servingPlayer=2
            if player2Score==3 then
                winningPlayer=2
                gameState='done'
            else 
                ball:reset()
                gameState='serve'
            end
        end
        if ball.x>VIRTUAL_WIDTH then
            player1Score=player1Score+1
            servingPlayer=1
            if player1Score==3 then
                winningPlayer=1
                gameState='done'
            else 
                ball:reset()
                gameState='serve'
            end
        end 
    end

    player1:update(dt)
    player2:update(dt)
    if gameState=='play' then
        ball:update(dt)
    end
end


function love.keypressed(key)
    if key=='escape' then
        love.event.quit()
    elseif key=='enter' or key=='return' then
        if gameState=='start' then
            gameState='serve'
        elseif gameState == 'serve' then
            gameState='play'
        elseif gameState == 'done' then
            ball:reset()
            gameState='serve'
            player1Score=0
            player2Score=0
            if winningPlayer==1 then
                servingPlayer=2
            else
                servingPlayer=1
            end
        end   
    end 
end


function love.draw()
    push:apply('start')

    love.graphics.clear(40,45,52,225)
    if gameState == 'start' then
        love.graphics.setFont(smallFont)
        love.graphics.printf('Welcome to Pong!', 0, 10, VIRTUAL_WIDTH, 'center')
        love.graphics.printf('Press Enter to begin!', 0, 20, VIRTUAL_WIDTH, 'center')
    elseif gameState == 'serve' then
        love.graphics.setFont(smallFont)
        love.graphics.printf('Player ' .. tostring(servingPlayer) .. "'s serve!", 
            0, 10, VIRTUAL_WIDTH, 'center')
        love.graphics.printf('Press Enter to serve!', 0, 20, VIRTUAL_WIDTH, 'center')
    elseif gameState == 'play' then
        -- no UI messages to display in play
    elseif gameState=='done' then
        love.graphics.setFont(largeFont)
        love.graphics.printf('Player ' .. tostring(winningPlayer) .. ' wins!',
            0, 10, VIRTUAL_WIDTH, 'center')
        love.graphics.setFont(smallFont)
        love.graphics.printf('Press Enter to restart!', 0, 30, VIRTUAL_WIDTH, 'center')
    end
    love.graphics.setFont(scoreFont)
    love.graphics.print(tostring(player1Score), VIRTUAL_WIDTH / 2 - 50, VIRTUAL_HEIGHT / 3)
    love.graphics.print(tostring(player2Score), VIRTUAL_WIDTH / 2 + 30, VIRTUAL_HEIGHT / 3)
    player1:render()
    player2:render()
    ball:render()
    push:apply('end')
end

function displayFPS()
    -- simple FPS display across all states
    love.graphics.setFont(smallFont)
    love.graphics.setColor(0, 255, 0, 255)
    love.graphics.print('FPS: ' .. tostring(love.timer.getFPS()), 10, 10)
end