if True:
    root = 'C:\Users\\realx\OneDrive\Documents\codingstuff\pythonstuff\pygame\spacegame\spacegame current\\'
#opening
    option = ''
    buthlosanger=0

    from winsound import PlaySound as play
    from winsound import Beep as beep
    import winsound
    from time import sleep
    import os
    print(os.getcwd())
    print("\n\n\nHey! You there!\n(Press ENTER to continue when the three dots appear)")
    play(root + "sounds\line1.wav", winsound.SND_FILENAME)
    input('...')
    print("Hello and Welcome to Scrounger!\nYou're about to begin your new life as an interplanetary scavenger.\nBefore you head out into the cosmos, you'll need to learn what you'll face out there.")
    play(root + "sounds\line2.wav", winsound.SND_FILENAME)
    input('...')
    print("As a Scrounger, your job is to extract the valuable gemstones that we leave behind.")
    play(root + "sounds\line3.wav", winsound.SND_FILENAME)
    input('...')
    print("Think of it as being the last line of defense against our shrinking profit marg- *cough*")
    play(root + "sounds\line4.wav", winsound.SND_FILENAME)
    input('...')
    input('...')
    print("There are four main types of gemstones:")
    print("Hoplitite, Janidite, Dynomite, and Aurelite.")
    play(root + "sounds\line5.wav", winsound.SND_FILENAME)
    print("Any questions so far?")
    play(root + "sounds\line6.wav", winsound.SND_FILENAME)
    option = input("Options:\n(Type the first word of whichever option you choose.)\n  Hoplitite | Janidite | Dynomite | Aurelite | No thanks\n").lower()
    while option != 'no':
        if option == 'hoplitite':
            print('Hoplitite is a SKY BLUE gemstone. It is known to have a HEALING effect when held near the heart.')
            play(root + "sounds\hoplitite.wav", winsound.SND_FILENAME)
            input('...')
        elif option == 'janidite':
            print("Janidite is a GREEN gemstone. It doesn't do much, but it's worth good money.")
            play(root + "sounds\janidite.wav", winsound.SND_FILENAME)
            input('...')
        elif option == 'dynomite':
            print("Dynomite is an ORANGE gemstone. It's name is suspiciously similar to a certain explosive, and with good reason too! Dynomite is HIGHLY EXPlOSIVE.\nMore than that, Dynomite catalyses nearby Janidite, resulting in more money lost than gained.")
            play(root + "sounds\dynomite.wav", winsound.SND_FILENAME)
            input('...')
        elif option == 'aurelite':
            print("Aurelite is a YELLOW gemstone with an other-worldly glow due to the barely visible Caeseum impurities within.\ndue to those Caeseum impurities within, it both sells for a lot of money, and explodes like a grenade when disturbed.\nif you have the hull integrity to store it, you might just survive with your new found riches.")
            play(root + "sounds\\aurelite.wav", winsound.SND_FILENAME)
            input('...')
        elif buthlosanger == 1:
            print('What did you say to me?')
            play(root + "sounds\\buthloswhat.wav", winsound.SND_FILENAME)
            buthlosanger =2
            print('[Buthlos will remember this]')
            input('...')
        elif buthlosanger == 2:
            print("The fuck did you just call me!?")
            play(root + "sounds\\buthlostf.wav", winsound.SND_FILENAME)
            buthlosanger =3
            print("[Buthlos will remember this]")
            input('...')
        elif buthlosanger == 3:
            print("Get the fuck out of this station and onto your ship right now or so help me!")
            play(root + "sounds\\buthlosgetout.wav", winsound.SND_FILENAME)
            print('[Buthlos will remember this]')
            option = 'no'
            break
        else:
            print("Pardon?")
            buthlosanger = 1
            play(root + "sounds\\buthlospardon.wav", winsound.SND_FILENAME)
            print("[Buthlos will remember this]")
            input('...')
        option = input("Options:\n  Hoplitite | Janidite | Dynomite | Aurelite | No thanks\n").lower()


    option = ''
    while True:
        print('You done with your questions? Do you even know how to fly?\nOptions:\n  Yes | No')
        play(root + "sounds\\flightquestioning.wav",winsound.SND_FILENAME)
        option = input().lower()
        if option == 'yes':
            print('At least you know that much.')
            play(root + "sounds\\flightyes.wav",winsound.SND_FILENAME)
            input('...')
            break
        else:
            print("I guess you don't know then")
            play(root + "sounds\\flightno1.wav",winsound.SND_FILENAME)
            print("You only have a few controls,\nthere's the steering ( ◀ / ▶ ),\nThe accelerator (Space + ◀ / ▶ ),")
            play(root + "sounds\\flightno2.wav",winsound.SND_FILENAME)
            print("And, wait no that's it.")
            play(root + "sounds\\flightno3.wav",winsound.SND_FILENAME)
            input('...')
            break


    print("Tell me when you're ready to head out. ")
    play(root + "sounds\line7.wav", winsound.SND_FILENAME)
    input("(press ENTER to exit the station)")
    print("Getting things ready and...")
    play(root + "sounds\gettingthingsready.wav",winsound.SND_FILENAME)
    beep(1199, 300)
    sleep(0.3)
    beep(2718,100)
    sleep(.1)
    beep
    print("Bye!")
    play(root + "sounds\\bye.wav",winsound.SND_FILENAME)


    

    # Define desired window position
    x = 100
    y = 50

    # Set the environment variable before importing pgzrun
    os.environ['SDL_VIDEO_WINDOW_POS'] = f'{x},{y}'

    import pgzrun as pg
    from random import randint

    WIDTH = 800
    HEIGHT = 600

    #var initialisation
    score = 0
    health = 30
    g = 9.8
    falltime = -1
    gemtype = {
        1:'gemgreen',
        2:'gemred',
        3:'gemblue',
        4:'gemyellow'
    }
    gemcolour = 1
    gameover = False

    ship = Actor('playership1_blue')
    ship.x = 370
    ship.y = 550

    gem = Actor(gemtype[1])
    gem.x = randint(20, 780)
    gem.y = 0


    def gemrand():
        global falltime
        global gemtype
        global score
        global health
        global gem
        global gemcolour

        #gravity
        gem.y += falltime * g
        falltime += 1/30

    #GEM COLLISION

        #gem collision with ground
        if gem.y > 600:
            gemcolour = randint(1,3)
            gem = Actor(gemtype[gemcolour])
            gem.x = randint(20, 780)
            print(gem.x)
            gem.y = 0
            falltime = 0

            health -= 1
            print(f'{gemtype[gemcolour]} fell')
            
        if gem.colliderect(ship):
            #green gem collision with ship
            if gemcolour==1:
                gem = Actor(gemtype[gemcolour])
                gem.x = randint(20, 780)
                gem.y = 0
                falltime = 0
                score += 3
                gemcolour = randint(1,3)
                print('janidite')
                
            #red gem collision with ship
            if gemcolour==2:
                gemcolour = randint(1,4)
                gem = Actor(gemtype[gemcolour])
                gem.y = 0
                falltime = 0
                score -= 5
                health -= randint(3,8)
                gem.x = randint(20, 780)
                print('dynomite')

            #blue gem collision with ship
            if gemcolour==3:
                gemcolour = randint(1,4)
                gem = Actor(gemtype[gemcolour])
                gem.y = 0
                falltime = 0
                score += 0
                health += randint(5,10)
                gem.x = randint(20, 780)
                print('Hoplitite')

            #yellow gem collision with ship
            if gemcolour==4:
                gemcolour = randint(1,4)
                gem = Actor(gemtype[gemcolour])
                gem.y = 0
                falltime = 0
                score += 30
                health -= randint(10,18)
                gem.x = randint(20, 780)
                print('Aurelite')

    #updater
    def update():
        global score
        global g
        global falltime
        global health
        global gameover

        if health <= 0:
            gameover = True
            if keyboard.up:
                gameover = False
                health = 30
                score = 0
        else:

        #check keyboard input
            if keyboard.space:
                if keyboard.left:
                    ship.x -= 15
                if keyboard.right:
                    ship.x += 15
            if keyboard.left:
                ship.x -= 5
            if keyboard.right:
                ship.x += 5
            
            gemrand()

    def draw():

        screen.clear()
        if gameover:
            screen.draw.text("Better luck next time",(200,300),color=(255,255,255),fontsize=60)
            screen.draw.text("Score: "+str(score),(15,10),color=(255,255,255),fontsize=50)
        else:
            healthbar = '▮'
            screen.draw.text('Score: ' + str(score), (15,10), color=(255,255,255), fontsize=30)
            screen.draw.text('Health: ' + str(health), (15,40), color=(80,255,80), fontsize=30)
            screen.draw.text((healthbar), (15,40), color=(80,155,80), fontsize=30)
            gem.draw()
            ship.draw()
        


    pg.go()