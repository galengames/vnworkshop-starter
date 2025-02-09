# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define fboy = Character("Flowerboy", image="fboy", who_color="F0B50B")
define you = Character("You")



###Cursor code --ignore
define config.mouse = {"default":[ ("gui/cursor.png", 1, 1) ] }

#A label is equivalent to a scene.
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene garden_edifice

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #this displays the sprite
    show fboy at center

    #this is a line of dialogue, you want to insert your script here and translate it to Ren'Py code.
    fboy b_normal m_smile "Greetings fellow traveller, how do you do?"

    #you can specify what emotion he will show, combine different brows and mouth images and see what you get.
    # mouths - frown, normal, smile, open
    # brows - normal, sad, angry, curious

    #here we will enact a choice
    menu:
        "Do you want to be my valentine?"   #dialogue that shows up
        "Yes": #choice 1
            #what happens after you select it
            fboy b_normal m_smile blush "I'm so happy I could die...."
        "Sorry bruh":
            fboy b_sad m_frown "Sad face"
                

    return
