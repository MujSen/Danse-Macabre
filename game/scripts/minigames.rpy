################################################################################
## Quick Time com barra
################################################################################
screen quick_bar():
    ####Bloquea el avance con click
    modal True
    
    ####Tiempo de espera 
    default timeout = 5.0
    
    
    ####posiciones de la bar
    bar:
        xalign 0.5
        ypos 400
        xsize 740
        value AnimatedValue(old_value=0.0, value=1.0, range=1.0, delay=timeout)
    timer timeout action Jump (timeout_label)

    #Botão que deve ser apertado e a label que te levará
    key "f" action  (ui.jumps("caverna"))

################################################################################
## Mage Minigame start here
################################################################################

label mageStart:

 Ar shappy "To win the game, you must click on the right options to raise the “fear level”."
 Ar ssurprise "Watch out for the time limit."
 $ point = 0
 $ q2 = False
 $ q3 = False

 menu:
  "{font=PARCHM.TTF} {size=+50}Question One\:{/font=PARCHM.TTF} {/size} Who is the author of the book \"Frankenstein\"?"

  "Jane Austen":
   jump js_mage01
   return
  "Mary Shelley":
    Ar shappy "Ha! That was easy..."
    $ point = +1
    jump mageQ2
    return
  "Charlotte Bronte":
   jump js_mage02
   return
 return

label mageQ2:

 menu:
  "{font=PARCHM.TTF} {size=+50}Question Two\:{/font=PARCHM.TTF} {/size} What is the name of Victor Frankenstein's creature?"

  "Frankenstein":
   $ q2 = True
   jump js_mage01
   return
  "The monster":
   Ar sbored "I remember reading about that! The monster didn't have a name..."
   $ point = +1
   jump mageQ3
  "Thing":
   $ q2 = True
   jump js_mage02
   return
 return

label mageQ3:
 $ q3 = True
 menu:
  "{font=PARCHM.TTF} {size=+50}Last question\:{/font=PARCHM.TTF} {/size} Who is the protagonist of Frankenstein?"
  "The monster":
   jump js_mage01
   return
  "Elizabeth":
   jump js_mage02
   return
  "Victor Frankenstein":
   Ar shappy "I knew it!"
   $ point = +1
   return
 return

label js_mage01:
 Ma "Behold, the dance of the shadows, where reality blurs and dreams take flight. "

 if q2 == False:
  jump mageQ2
  return

 elif q3 == False:
  jump mageQ3
  return

 elif q3 == True:
  return
 return

label js_mage02:
 Ma "Witness as the darkness itself becomes my canvas, painting scenes of wonder and terror for your entertainment."

 if q2 == False:
  jump mageQ2
  return

 elif q3 == False:
  jump mageQ3
  return

 elif q3 == True:
  return
 return
 return