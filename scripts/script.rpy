# The script of the game goes in this file.

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    jump mageStart
    scene Corridor

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    show Chand at pendulum
    with dissolve

    show Bella childhappy2 at right
    with moveinright

    # These display lines of dialogue.
    Ar "Look, mom! I’m flying!"

    show Eve angry at left
    with moveinleft

    Ev "Arabella Dummont! Get down right in this instant!"

    Ar child sad "But, mom!" with dissolve

    Ev "You are to be the dutchess of these lands."
    Ev "I can’t have you breaking an arm or something."
    Ev "Get down.{w} I won’t say it twice."
    Ar "Yes, mother."

    hide Chand
    with dissolve

    Ar child angry2 "My mom always says things like this. People may think she’s worried about me…"
    Ar "But all I can see is her worry about our family's reputation."
    Ev angry2 "Now, let’s get started with your etiquette lesson. You seem to be needing it the most."
    Ev "How is a nobleman going to ask for your hand in marriage if you’re to act this way?"
    Ar child angry "I don’t want to get married..."
    Ev angry "... For now.{p}I’m sure you are going to change your mind when the time arrives."
    Ar child sad "If you say so…"

    hide Bella
    hide Eve
    with dissolve

    Ar "Well…"

    Ar "Time came…"

    Ar "And I still don’t want to get married."

    scene Dinner
    with fade

    $ point = 0

    Ad "...bella?{p}Arabella?"

    show Bella date happy2 with dissolve

    Ar "Yes? I'm sorry... {w} I got caught thinking about the past."
    Ad date happy "Oh, sweetie… {w}Are you nervous? I can understand it."
    Ad date bored"To be around someone as magnificent as me can cause ordinary people to get bashful."

    hide Bella with dissolve

    menu:
     "How should I answer him? Do I please the archduke for the sake of politics?"
     "Smile shyly.":
        show Bella date happy2 with dissolve
        Ar "Of course..."
        $ point = +1
        pass
        
     "“... Actually, I got bored.”":
        show Bella date bored2
        $ point = -1
        pass

    Ad date bored "So, dear Bella. May I call you Bella?"
    Ar date surprise "Actually-"
    Ad date bored "Wonderful. As I was saying, Bella…"
    Ad "I am quite positive that you have heard about my past conquers before, haven’t you?"
    Ar date happy2 "Oh, yes. I’ve heard that you have an impressive background."
    Ad date happy "More than impressive, in fact. The Luxembourg family always had been among the most noble families."
    Ad "{i}I{/i}, of course, am not behind our name as {i}I{/i} acquired abilities worthy of envy."
    Ar date happy2 "It seems that your life is always full of adventures."
    Ad date happy "Definitely. But, I'm curious, let me ask you a question… Are you the jealous type?"
   
    hide Bella

    menu:
        "Yes":
            $ point = -1
            pass
        "No":
            $ point = +1
            pass

    show Bella date bored with dissolve
    
    Ad "I’m asking because it is hard for ladies all around the world to resist the enchants of someone as grand as myself."
    Ar date bored2 "Do you travel frequently?"
    Ad date happy "Yes, of course. Traveling is one of my passions."
    Ad "I know the finest places around this world."
    Ar date happy2 "You must have had wonderful experiences."
    Ad date happy "Not only I but also the people around me, since, wherever I go..."
    Ad date bored "... my presence alone turns simple places into wonderful sceneries worthy of fairy tale narratives."
    Ar date bored2 "You seem to have a high self-esteem."

    hide Bella with dissolve

    menu:
     "Ignore his comments":
        $ point = +1

        show Bella date happy2 with dissolve

        Ar "Talking about transform places, {w}have you already visited the art exposition that is happening downtown?"
        Ad date happy "Oh, yes, I have been there."
        Ad date bored "I must admit, the exposed art did not impress me, they are not equal to my refined taste, of course."
        Ar date bored2 "Art is so subjective, isn’t it? Maybe if you looked at it from another perspective…"
        Ad date bored "But, frankly, I believe that my discernment is superior to the common folk."
        pass
     "Point out his flaws":
        $ point = -1

        show Bella date bored2 with dissolve

        Ar "With all due respect, archduke, it is quite arrogant to assume that your opinions are the ones that matter."
        Ad date bored "Arrogant! Me?!{w} How dare you?!"
        Ar date surprise "Just saying… Humility is a virtue valued by many."
        Ar "Maybe there is more to be admired in someone who recognizes the greatness of others."
        Ad date bored "Humility is not something expected from someone as important as an archduke."
        Ar date bored2 "I believe that it is best for everyone if we finish the dinner here. Have a good evening, sir."
        pass

    hide Bella with dissolve
    jump travel
    # This ends the game.
    return

label travel:

 scene Street
 with None
 show CarBody
 show WeelB
 show WeelF
 with dissolve

 Ar sbored2 "Curse that archduke!"
 Ar "No way I am going to get married to him!"

 show Paper with moveinleft
 Ar ssurprise "What is that?"

 menu:
  "Take the paper":
   hide Paper
   show Flyer
   pass

 Ar ssurprise "A... circus?"
 Ar "Maybe I could...?"
 Ar shappy2 "I better keep it for later... A small visit wouldn't make me harm"
 Ar ssurprise "Would it?"

 scene Corridor
 with fade

 show Eve worry:
  xpos 0.5
  xzoom -1
 with dissolve

 Ev "So… How did it go?"

 show Eve worry2 with dissolve

 Ar ssurprise "The epigraph of a disaster."
 Ev worry "Please, try a little bit harder."
 Ev "It is going to be a blessing to our family if we get to create ties with the Luxembourg family."
 
 show Eve worry2 with dissolve

 Ar sbored2 "A blessing indeed."
 Ar "I'm going to my room pitty my own future."
 Ar "Please, do not interrupt me."

 hide Eve
 hide Bella
 show Flyer
 with fade

 Ar sworry "I wish I could have some fun…"

 jump circus
 return
 
label circus:

 scene CircusOut with zoomout
 show Ring happy with dissolve

 Rm "Come and see! Come and see!{p}The Shadow Circus from the Red Sea!"
 Rm "Take a bow and sit down,{p}‘cause we just came into the town!"

 Ar shappy2 "Now, this may be a thing!"
 Ar "Let's see whats inside..."

 hide Ring happy
 show Mage happy
 with pixellate

 Ma "Welcome to the Shadow Circus, where the darkness reigns supreme!"
 Ma "Today we shall present our most mesmerizing act"
 Ma dance "Tell me, dear viewers, do you like to dance?" with dissolve
 Ma "For today we shall showcase our play “Danse Macabre”."
 Ma "Are you ready to transport your mind to places beyond imagination?"
 Ma "Tonight, you are about to see acts that defy the laws of reality…"
 Ma happy "… and witness secrets as ancient as the shadows that surround us." with dissolve

 jump mageStart
 return