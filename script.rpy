#Use shortcuts for names 
define a = Character("[player_name]")  
define l = Character("Logan", color="#F3B123" )
define m = Character("Mark", color="#484A47" )
define w = Character("Wyatt", color="#132E07")
define j = Character("Jennifer", color="#967AC9")
define o = Character("Olive", color="#D53451")

#resize images
image car_road = Transform("car_road.jpg", size=(1920, 1080))
image hallway = Transform("hallway.jpg", size=(1920, 1080))
image cozy_room = Transform("cozy_room.jpg", size=(1920, 1080))
image empty_boxes = Transform("empty_boxes.jpg", size=(1920, 1080))
image empty_furniture = Transform("empty_furniture.jpg", size=(1920, 1080))
image just_empty = Transform("just_empty.jpg", size=(1920, 1080))
image minimalist_room = Transform("minimalist_room.jpg", size=(1920, 1080))
image modern_room = Transform("modern_room.jpg", size=(1920, 1080))
image apartment_outside = Transform("apartment_outside.jpg", size=(1920, 1080))
image jennifer_door = Transform("jennifer_door.jpg", size=(1920, 1080))
image loading_screen = Transform("loading_screen.jpg", size=(1920, 1080))

#makes it nighttime 
transform nighttime:
    matrixcolor TintMatrix("#333355") * SaturationMatrix(0.5) * BrightnessMatrix(-0.4)

transform nighttime_light:
    matrixcolor TintMatrix("#333355") * SaturationMatrix(0.5) * BrightnessMatrix(-0.05)

transform jennifer_night_position:
    xalign 0.5
    yalign 1.0
    yoffset 150
    zoom 0.7
    matrixcolor TintMatrix("#445577") * BrightnessMatrix(-0.1)


init python:
    renpy.music.register_channel("sound2", mixer="sfx", loop=False)
    
# Character positioning
transform character_position:
    xalign 0.5
    yalign 1.0
    yoffset 150
    zoom 0.7

# Set up relationship points for the neighbors
default logan_points = 0
default wyatt_points = 0
default olive_points = 0
default jennifer_points = 0
default money_points = 42
default stress_points = 4
default apartment_style = "" 

label start:

    scene car_road 

    play music "audio/daymusicKontraaPixabay.mp3" fadein 2.0 volume 0.5

    play sound "car_driving.mp3" 
    
    "The scenery changes in the corner of my eyes. This is one of those moments where I wish that I was a kid again"

    "Being able to look at nature without having to focus on the road"

    "I'm 5 minutes away from my new apartment. My new life. It's unbelievable"
    
    scene apartment_outside

    stop sound
    
    "I stop the car at the apartment and turn the motor off, the car goes silent"

    "{i}It's strange to imagine that I live here now. I was excited at first but now I'm kind of nervous. And tired{/i}"

    "{i}I'm SO SO tired. Who knew that moving could be THIS exhausting?{/i}"

    "I step out of the car and nervously make my way up to my apartment on the third floor. Number 303"

    scene just_empty

    "When I step inside of my apartment my eyes wander around the space. It looks very empty, the walls are beige and there's nothing in it" 
    
    "It has a lot of potential though...."

    "I put my bag down and walk back out to get the boxes in my car."

    scene hallway

    "When I step into the hallway, though, I see a guy. He's taller than me, has blond messy hair and blue playful eyes. He's wearing a hoodie and smells like..... weed?"

    show logan_character at character_position 
    
    l "Well hello..... who might you be darling?"
    
    "His eyes trail a lazy path over me"

    $ player_name = renpy.input("What is your name?") 
    $ player_name = player_name.strip()

    if not player_name:
        $ player_name = "Twiddledeedumb"

    a "I'm [player_name], I just moved in here"

    l "Aahh... a new addition to our neighbourhood. I see. Welcome. I'm Logan. If you ever want me to hook you up with the good stuff I'll give you a deal" 

    l "Consider it a welcome gift"

    hide logan_character

    "He walks off. I don't know what he meant with 'the good stuff' and I don't think that I want to know" 

    scene empty_boxes

    "Boxes pile up in my apartment as I move them from my car to my apartment"

    scene hallway 
    
    "While on my second trip I notice a girl staring at me. She's wearing a red shirt with a star on it and looks suspicious of me"

    show olive_character at character_position

    "Our eyes meet and I give her a confused look"

    hide olive_character 

    "When she notices me looking at her she quickly goes back inside and closes the door. I don't know what THAT was about."
    
    "I bring up the second to last box and stop in my tracks when I see a man waiting in front of my apartment. His arms are crossed, he's tall, has an athletic figure and looks kind of terrifying"

    show wyatt_character

    w "And who might you be?"

    "He inspects me with a serious look, his forest green eyes piercing through me"

    a "I- uuh- I'm uuh [player_name], I j-just moved in here"

    w "[player_name], huh?"

    "He looks me up and down and again, as if he's trying to find something off or wrong about me"

    w "I'm Wyatt"

    w "Got many more boxes?"
    
    "I nod"

    a "Just one more"

    w "In your car? Your cars downstairs?"

    a "Yeah the yellow one..."

    "His eyebrows raise when I mention my car but he doesn't say anything." 

    w "I'll help yu. May I have your key? To open the car."

    a "Oh no you don't have to, it's fine, I only have one box left"

    w "Then let me get that box"

    "He holds his hand outstreched. Do you give him the key"

    menu:
        "Do you give him the key, or not?"

        "Give him the key":
            $ wyatt_points += 1 
            a "Okay. Thank you. I appreciate it."
            "He nods, looking determined"
            w "No problem"
            "I hand him my car keys and he leaves to go get the last box"
            hide wyatt_character
            "I go back into my apartment"
            scene empty_boxes
            "He comes back with the box not long after and places it down"
            show wyatt_character at character_position
            a "Thank you"
            w "No problem"
            hide wyatt_character
            "He nods again and then leaves"
            jump apartment_boxes_unpacked


        "Don't give him the key":
            a "No, I'd rather do it myself"
            "His face tightens"
            w "All right then."
            hide wyatt_character
            "He goes back into his house"
            scene empty_boxes
            "I go get the last box and place it down in my apartment"
            jump apartment_boxes_unpacked
            


    label apartment_boxes_unpacked:
        scene empty_furniture 


    "When all boxes are inside I unpack them and put all the stuff away. Once that and all the other maintenance things have been arranged I lie down on the mattress"

    "The kitchen is calling my name but I can't bring myself to get up. All of my limbs hurt. So instead I reach for my phone and check my bank account. I must be able to afford take out once, right?"

    "Bank balance: 42 euros"

    "The number that pops up isn't exactly....... comforting."

    "The hunger isn't either tough. So the question is.... is it worth it or not?"

    menu:
        "Are you going to order food or not?"
        
        "Order food anyway, YOLO, right?":
            $ money_points -= 15
            $ stress_points -= 1 
            "What the heck, I'll order something"
            "I lie on the mattress and wait for my food to arrive"
            "Afterwards I put something on the TV and let myself doze off"

        "Cook something, we need to be responsible":
            $ stress_points += 2 
            "Since my bank account doesn't think that ordering food is a good idea I just decide to cook anyway"
            "I grab some ingredients, walk to the kitchen and whip up a decent meal"
            "Affter eating and stacking the dishes I lie back down on the mattress, turn on the TV and let myself doze off"

        "I'm too tired to cook and too broke to order out, I'll just do intermittent fasting":
            $ stress_points += 1
            "You know what, let me just go to bed"
            "Though distracting myself with a comedy was a good plan originally, it doesn't seem to work"
            "The hunger is making it difficult to focus or fall asleep"
            "I debate whether I should order something anways but before I can come to a decision sleep claims me"

    scene empty_furniture at nighttime
    stop music fadeout 2.0 
    play music "audio/nightmusicAbsoluteSoundPixabay.mp3" fadein 2.0 volume 0.2


    play sound "audio/baby_crying.mp3" volume 0.5 fadein 2.0 loop 
    
    "I jump up in my bed to the sudden sound of... loud.. crying?"

    "My phone screen lights up, kindly informing me that it's 2 in the morning."

    "2 in the morning...? Really...?"

    "As much as I would love to text someone, that isn't an option unfortunately since I don't have anyone's number yet"

    menu: 
        "Do you do anything about it or just ignore it?"

        "I get up, march over there and INSIST that the human spawn gets silenced AT ONCE":
            $ jennifer_points -= 2
            jump dominance 

        
        "I go over there and ask kindly if maybe they can quiet down....?":
            $ jennifer_points += 2
            jump kindly

        "I just ignore it and suck it up, I don't like confrontation":
            $ jennifer_points += 1 
            jump ignore
        
    
    label dominance:
    "I decide to march over there and assert dominance. Better that they know that I don't mess around so that they don't try again"

    scene jennifer_door at nighttime_light

    play sound2 "audio/door_knock.mp3"

    "I walk up to the door and knock on it loudly"

    "When the door opens a stressed out woman in her late thirties appears, she has bags under her eyes, her hair is in a messy bun and she's bouncing a crying baby"

    show jennifer_character at jennifer_night_position
    
    "Before she can get a word in I interrupt her"
    
    a "I'm trying to sleep, can you quiet it down?"

    "She looks upset but also annoyed"

    j "I'm so sorry but he won't stop crying"

    a "Can't you like- feed him or something?"

    j "He's not hungry."

    a "Yeah well he must be something, right?"

    "Now she starts to look really annoyed"

    j "I think that I can take care of my own child just fine, thank you very much"

    a "Yeah well clearly"

    a "You know what? Forget about it."

    hide jennifer_character

    "I storm off and she closes the door"

    stop sound 

    jump back_sleep


    label kindly:

    "Wanting to sleep while also not making enemies on day one, I decide to ask them kindly if they can maybe be a bit quieter."
    
    "I put on a robe, shoes and go outside. I follow the noise and it leads me to door number 301"

    scene jennifer_door at nighttime_light

    "I walk up to the door and knock on it"

    play sound2 "door_knock.mp3"

    "When the door opens I see a stressed out woman in her late thirties, she has bags under her eyes, her hair is in a messy bun and she's bouncing a crying baby"

    show jennifer_character at jennifer_night_position

    j "I'm SO sorry if I woke you up, he just won't quiet down, I don't know what to do, I'm sorry"

    a "Oh, it's fine. I just- I was wondering if uuhm.. can I help you? Maybe? I don't know..."

    jump help_her 


    label ignore:

    "Not wanting to bother anyone, I try to ignore it. The wailing, the screaming, the kicking"

    "When it doesn't work I put on noise canceling headphones to drown out the sound, but that doesn't seem to work either"

    "Eventually I decide to get up and go over there anyway"

    "I put on a robe, shoes and go outside. I follow the noise and it leads me to door number 301"

    scene jennifer_door at nighttime_light

    "I walk up to the door and knock on it"

    play sound2 "door_knock.mp3"

    "When the door opens I see a stressed out woman in her late thirties, she has bags under her eyes, her hair is in a messy bun and she's bouncing a crying baby"

    show jennifer_character at jennifer_night_position

    j "I'm SO sorry if I woke you up, he just won't quiet down, I don't know what to do, I'm sorry"

    a "Oh... it's- it's fine. Nevermind. I don't know what uuhm-"

    a "Do you... do you need help?"

    jump help_her

    label help_her: 

    j "Oh, uuh, one thing. Really quickly. Sorry. The tap in the bathroom is running. Can you turn it off? I'm scared that it'll overflow"

    a "Yeah, sure. Where's your bathroom?"

    j "Just at the end of the hall there"

    hide jennifer_character 

    scene black

    play sound2 "audio/zeroisnebulous_bathroom_pixabay.mp3" fadein 0.5

    "I walk into the house, over to the bathroom and turn off the tap. It has indeed overflown a bit already, the bathroom floor is slightly wet"

    stop sound2

    scene jennifer_door at nighttime_light

    show jennifer_character at jennifer_night_position

    "When I come back I see her smile at me"

    j "Thank you so much. I haven't seen you before, are you new?"

    a "Yeah, I just moved in here. I'm [player_name]" 

    j "[player_name], nice to meet you"

    a "It's nice to meet you too"

    hide jennifer_character 

    scene empty_furniture at nighttime 
    
    jump back_sleep
    
    label back_sleep: 

    "I go back to my apartment and try to get some sleep"

    stop sound fadeout 2.0

    scene empty_furniture 

    stop music 

    play music "audio/daymusicKontraaPixabay.mp3" fadein 2.0 volume 0.5

    "My eyes open to the bright light of the sun. I check my phone, 6AM."
    
    "The emptyiness of the apartment is kind of depressing. I should decorate it today"
    
    "First, though, breakfast. I doubt that the people at YKEJA would like it if I showed up there hungry"  
    
    "I tiredly pad over to the kitchen and whip up a quick breakfast, then I sit down behind my laptop and open pinterest"
    
    "All kinds of pictures of apartment decorations pop up, I go to my board titled 'Apartment inspo' and scroll through it"
    
    "I can't decide between these styles."

label style_choice:
    menu:
        "Which style am I going to pick?"
    
        "Cozy and warm":
            $ apartment_style = "cozy"
            jump cozy_confirmation

        "Minimalistic and professional":
            $ apartment_style = "minimalistic"
            jump minimalist_confirmation

        "Modern style":
            $ apartment_style = "modern"
            jump modern_confirmation


label cozy_confirmation:

    scene cozy_room 

    "Warm colours, soft blankets and plants. This feels like home."

    menu:
        "Choose this style?"

        "Yes":
            jump decorations

        "No":
            jump style_choice


label minimalist_confirmation:

    scene minimalist_room

    "White, clean, serious. The perfect environment to focus in"

    menu:
        "Choose this style?"

        "Yes":
            jump decorations

        "No":
            jump style_choice


label modern_confirmation:

    scene modern_room

    "Dark walls, wooden walls, dark furniture and led lights. Feels rich and luxury."

    menu:
        "Choose this style?"

        "Yes":
            jump decorations

        "No":
            jump style_choice

label decorations:

    scene empty_furniture 

    "I spend hours decorating my apartment"

    scene black with fade
    
    play sound "audio/liliangorini_pixabay_construction.mp3"
    
    $ renpy.pause(5.0, hard=True)
    
    stop sound fadeout 1.0

    if apartment_style == "cozy":
        scene cozy_room
    
    if apartment_style == "modern":
        scene modern_room
    
    if apartment_style == "minimalistic":
        scene minimalist_room

"After hours slaving away in my apartment trying to make it pretty I let myself fall down on the couch"

"This evening I go to the kitchen, make myself dinner and go to bed"

scene black with fade

"The next morning I wake up to the sound of arguing"

scene loading_screen with fade

"{b}Ending Chapter 1{/b}"

"Stats: \n Wyatt points: [wyatt_points] \n Logan points: [logan_points] \n Jennifer points: [jennifer_points]"
"Stats: \n Money points: [money_points] \n Stress points: [stress_points]" 


return