import warnings

import appgamekit as agk
from appgamekit import *

with agk.Application():
    set_virtual_resolution(1024, 768)

    character_inventory = []
    # GAME DATA
    # THE BACKGROUND IMAGES SHOULD BE PLACED HERE IN ORDER --!!!
    wallpaper = create_sprite(load_image("wallpaper.png"))
    wallpaper_home = create_sprite(load_image("wallpaperstart.png"))
    set_sprite_visible(wallpaper_home, False)

    # FURNITURES OR ITEMS
    one = create_sprite(load_image("1.png"))
    two = create_sprite(load_image("2.png"))
    three = create_sprite(load_image("3.png"))
    five = create_sprite(load_image("5.png"))
    window = create_sprite(load_image("window.png"))
    door = create_sprite(load_image("door.png"))
    door2 = create_sprite(load_image("door2.png"))
    door2_unlocked = create_sprite(load_image("door2_unlocked.png"))
    opendoor = create_sprite(load_image("opendoor.png"))
    couch = create_sprite(load_image("couch.png"))
    key = create_sprite(load_image("key.png"))
    frame = create_sprite(load_image("frame.png"))
    clothes_1 = create_sprite(load_image("clothes_1.png"))
    clothes_2 = create_sprite(load_image("clothes_2.png"))
    password_1 = create_sprite(load_image("password.png"))
    vault = create_sprite(load_image("vault.png"))
    vault_unlocked = create_sprite(load_image("vault_unlocked.png"))
    vault_screen = create_sprite(load_image("vault_screen.png"))
    plant2 = create_sprite(load_image("plant2.png"))
    computer = create_sprite(load_image("computer.png"))
    clock = create_sprite(load_image("clock.png"))
    chips = create_sprite(load_image("chips.png"))
    backpack = create_sprite(load_image("backpack.png"))
    key2 = create_sprite(load_image("key2.png"))

    # SCREEN
    screen = create_sprite(load_image("screen.png"))
    set_sprite_visible(screen, False)

    screen_2 = create_sprite(load_image("screen2.png"))
    set_sprite_visible(screen_2, False)

    text_password = create_sprite(load_image("textpassword.png"))

    COUCH_X = 1024//2
    COUCH_Y = 768//2
    DOOR_X = 380
    DOOR2_X = 650
    DOOR_Y = 235
    DOOR2_Y = 155
    CARPET_X = 200
    CARPET_Y = 680
    FRAME_X = 100
    FRAME_Y = 100
    WINDOW_X = 620
    WINDOW_Y = 70
    CLOTHES_X = 10
    CLOTHES_Y = 250
    PASSWORD1_X = 725
    PASSWORD1_Y = 10
    VAULT_X = 800
    VAULT_Y = 360
    PLANT2_X = 380
    PLANT2_Y = 100
    ONE_X = 150
    ONE_Y = 150
    THREE_X = 420
    THREE_Y = 135
    TWO_X = 125
    TWO_Y = 350
    FIVE_X = 875
    FIVE_Y = 180
    COMPUTER_X = 370
    COMPUTER_Y = 250
    CLOCK_X = 420
    CLOCK_Y = 80
    TEXTPASS_X = 350
    TEXTPASS_Y = 768 // 2
    BACKPACK_X = 900
    BACKPACK_Y = 450
    CHIPS_X = 860
    CHIPS_Y = 450
    KEY2_X = 900
    KEY2_Y = 540

    set_sprite_position(one, ONE_X, ONE_Y)
    set_sprite_visible(one, False)

    set_sprite_position(three, THREE_X, THREE_Y)
    set_sprite_visible(three, False)

    set_sprite_position(two, TWO_X, TWO_Y)
    set_sprite_visible(two, False)

    set_sprite_position(five, FIVE_X, FIVE_Y)
    set_sprite_visible(five, False)

    set_sprite_position(couch, COUCH_X, COUCH_Y)
    set_sprite_visible(couch, False)

    set_sprite_position(door, DOOR_X, DOOR_Y)
    set_sprite_visible(door, False)

    set_sprite_position(key, CARPET_X, CARPET_Y)
    set_sprite_visible(key, False)
    set_sprite_size(key, 40, 71)

    set_sprite_position(opendoor, DOOR_X, DOOR_Y)
    set_sprite_visible(opendoor, False)

    set_sprite_position(frame, FRAME_X, FRAME_Y)
    set_sprite_visible(frame, False)

    set_sprite_position(window, WINDOW_X, WINDOW_Y)
    set_sprite_visible(window, False)

    set_sprite_position(clothes_1, CLOTHES_X, CLOTHES_Y)
    set_sprite_position(clothes_2, CLOTHES_X, CLOTHES_Y)
    set_sprite_visible(clothes_1, False)
    set_sprite_visible(clothes_2, False)

    set_sprite_position(password_1, PASSWORD1_X, PASSWORD1_Y)
    set_sprite_visible(password_1, False)

    set_sprite_position(door2, DOOR2_X, DOOR2_Y)
    set_sprite_visible(door2, False)

    set_sprite_position(vault, VAULT_X, VAULT_Y)
    set_sprite_visible(vault, False)

    set_sprite_position(vault_unlocked, VAULT_X, VAULT_Y)
    set_sprite_visible(vault_unlocked, False)

    set_sprite_position(plant2, PLANT2_X, PLANT2_Y)
    set_sprite_visible(plant2, False)

    set_sprite_position(computer, COMPUTER_X, COMPUTER_Y)
    set_sprite_visible(computer, False)

    set_sprite_position(clock, CLOCK_X, CLOCK_Y)
    set_sprite_visible(clock, False)

    set_sprite_position(text_password, TEXTPASS_X, TEXTPASS_Y)
    set_sprite_visible(text_password, False)

    set_sprite_visible(vault_screen, False)

    set_sprite_position(backpack, BACKPACK_X, BACKPACK_Y)
    set_sprite_visible(backpack, False)

    set_sprite_position(chips, CHIPS_X, CHIPS_Y)
    set_sprite_visible(chips, False)

    set_sprite_position(door2_unlocked, DOOR2_X, DOOR2_Y)
    set_sprite_visible(door2_unlocked, False)

    set_sprite_position(key2, KEY2_X, KEY2_Y)
    set_sprite_visible(key2, False)

    img_font = load_image("font1.png")
    set_text_default_font_image(img_font)
    music = load_music_ogg("theme2.ogg")
    play_music_ogg(music)

    mouseclick = load_sound_ogg("mouse.ogg")

    character_stand = create_sprite(load_image("backchar.png"))
    set_sprite_visible(character_stand, False)
    character_sleeping = create_sprite(load_image("sleeping.png"))
    set_sprite_visible(character_sleeping, False)

    character = create_sprite(load_image("still1.png"))
    add_sprite_animation_frame(character, load_image("still1.png"))
    add_sprite_animation_frame(character, load_image("still2.png"))
    add_sprite_animation_frame(character, load_image("still3.png"))

    info_text = create_text("You need a key and a password to open the door...")
    set_text_size(info_text, 30)
    set_text_visible(info_text, False)

    play_sprite(character, 2, 1, 1, 3)
    set_sprite_visible(character, False)
    set_sprite_position(character, 30, 400)

    def scene4():
        pass

    def scene3():
        set_sprite_visible(clothes_2, False)
        set_sprite_visible(computer, False)
        set_sprite_visible(clock, False)
        set_sprite_visible(vault, False)
        set_sprite_visible(vault_unlocked, False)
        set_sprite_visible(door2_unlocked, False)
        set_sprite_visible(two, False)
        set_sprite_visible(five, False)
        set_sprite_visible(chips, False)
        set_sprite_visible(backpack, False)
        set_sprite_visible(key2, False)
        set_sprite_visible(password_1, False)
        set_sprite_visible(text_password, False)

        comic1 = create_sprite(load_image("comic1.png"))
        set_sprite_position(comic1, 100, 60)

        comic1_text = create_text("So this is where he hides my treats and toys hmm")
        set_text_position(comic1_text, 10, 500)
        set_text_size(comic1_text, 30)

        comic2 = create_sprite(load_image("comic2.png"))
        set_sprite_position(comic2, 650, 60)
        set_sprite_visible(comic2, False)

        comic2_text = create_text("At least I found the key to the outside world!!")
        set_text_position(comic2_text, 10, 500)
        set_text_size(comic2_text, 30)
        set_text_visible(comic2_text, False)

        comic3 = create_sprite(load_image("comic3.png"))
        set_sprite_visible(comic3, False)

        comic3_text = create_text("Let the adventures begin!")
        set_text_size(comic3_text, 50)
        set_text_visible(comic3_text, False)
        set_text_position(comic3_text, 60, 0)

        tbc = create_text("To be continued...")
        set_text_size(tbc, 50)
        set_text_position(tbc, 250, 250)
        set_text_visible(tbc, False)

        add_virtual_button(13, 900, 600, 100)
        set_virtual_button_text(13, "NEXT")
        set_virtual_button_color(13, 5, 5, 5)

        add_virtual_button(14, 900, 600, 100)
        set_virtual_button_text(14, "NEXT")
        set_virtual_button_color(14, 5, 5, 5)
        set_virtual_button_active(14, False)
        set_virtual_button_visible(14, False)

        add_virtual_button(15, 900, 600, 100)
        set_virtual_button_text(15, "NEXT")
        set_virtual_button_color(15, 5, 5, 5)
        set_virtual_button_active(15, False)
        set_virtual_button_visible(15, False)
        start = True
        while start:
            if get_virtual_button_pressed(13):
                set_sprite_visible(comic2, True)
                set_text_visible(comic1_text, False)
                set_text_visible(comic2_text, True)
                set_virtual_button_visible(13, False)
                set_virtual_button_active(13, False)
                set_virtual_button_visible(14, True)
                set_virtual_button_active(14, True)

            if get_virtual_button_pressed(14):
                set_text_visible(comic2_text, False)
                set_sprite_visible(comic3, True)
                set_text_visible(comic3_text, True)
                set_virtual_button_visible(14, False)
                set_virtual_button_active(14, False)
                set_virtual_button_visible(15, True)
                set_virtual_button_active(15, True)

            if get_virtual_button_pressed(15):
                set_sprite_visible(comic1, False)
                set_sprite_visible(comic2, False)
                set_sprite_visible(comic3, False)
                set_text_visible(comic3_text, False)
                set_virtual_button_visible(15, False)
                set_virtual_button_active(15, False)
                set_text_visible(tbc, True)
            if get_pointer_pressed():
                print(get_pointer_x())
                print(get_pointer_y())
            agk.sync()

    def computer_window():
        set_sprite_visible(screen, True)
        set_sprite_visible(text_password, True)
        set_sprite_visible(computer, False)
        set_sprite_visible(five, False)
        set_sprite_visible(two, False)
        set_sprite_visible(clothes_1, False)
        set_sprite_visible(password_1, False)
        set_sprite_visible(door2, False)
        set_sprite_visible(vault, False)
        set_sprite_visible(clock, False)
        set_sprite_active(password_1, False)
        set_sprite_visible(backpack, False)
        set_sprite_visible(chips, False)
        set_sprite_visible(key2, False)

        delete_virtual_button(5)
        delete_virtual_button(7)
        delete_virtual_button(8)
        delete_virtual_button(9)
        delete_virtual_button(10)
        delete_virtual_button(11)
        delete_virtual_button(12)

        start = True

        add_virtual_button(6, 900, 50, 100)
        set_virtual_button_text(6, "CANCEL")
        set_virtual_button_color(6, 5, 5, 5)

        editbox = create_edit_box()
        set_edit_box_position(editbox, 375, 345)
        set_edit_box_size(editbox, 250, 50)
        set_edit_box_text_size(editbox, 45)

        while start:
            if get_edit_box_text(editbox) == "1240":
                set_edit_box_active(editbox, False)
                set_edit_box_visible(editbox, False)
                set_sprite_visible(text_password, False)
                set_sprite_visible(screen, False)
                set_sprite_visible(screen_2, True)
            if get_virtual_button_pressed(6):
                set_edit_box_active(editbox, False)
                set_edit_box_visible(editbox, False)
                set_sprite_visible(text_password, False)
                set_sprite_visible(screen_2, False)
                set_sprite_visible(vault_screen, False)
                scene2()

            if get_sprite_hit_test(password_1, get_pointer_x(), get_pointer_y()):
                stop_text_input()

            agk.sync()


    def scene2():
        password_vault = ["star", "heart", "circle", "square"]
        password_input = []
        set_sprite_visible(screen, False)
        set_sprite_visible(couch, False)
        set_sprite_visible(door, False)
        set_sprite_visible(frame, False)
        set_sprite_visible(window, False)
        set_sprite_visible(opendoor, False)
        set_sprite_visible(character, False)
        set_sprite_visible(character_sleeping, False)
        set_sprite_visible(character_stand, False)
        set_sprite_visible(plant2, False)
        set_sprite_visible(one, False)
        set_sprite_visible(three, False)
        delete_virtual_button(4)
        delete_virtual_button(6)
        set_sprite_visible(computer, True)
        set_sprite_visible(five, True)
        set_sprite_visible(two, True)
        set_sprite_visible(clothes_1, True)
        set_sprite_visible(password_1, True)
        set_sprite_visible(door2, True)
        set_sprite_visible(vault, True)
        set_sprite_visible(clock, True)

        add_virtual_button(5, 100, 100, 100)
        set_virtual_button_text(5, "REWIND")

        set_text_input_max_chars(4)

        wrong_password = create_text("Wrong password! Please try again.")
        set_text_size(wrong_password, 30)
        set_text_visible(wrong_password, False)

        correct_password = create_text("You've unlocked the vault!")
        set_text_position(correct_password, 240, 500)
        set_text_size(correct_password, 30)
        set_text_visible(correct_password, False)

        start = True

        add_virtual_button(7, 180, 250, 150)
        set_virtual_button_text(7, "HEART")
        set_virtual_button_color(7, 5, 5, 5)
        set_virtual_button_active(7, False)
        set_virtual_button_visible(7, False)

        add_virtual_button(8, 380, 250, 150)
        set_virtual_button_text(8, "STAR")
        set_virtual_button_color(8, 5, 5, 5)
        set_virtual_button_active(8, False)
        set_virtual_button_visible(8, False)

        add_virtual_button(9, 580, 250, 150)
        set_virtual_button_text(9, "SQUARE")
        set_virtual_button_color(9, 5, 5, 5)
        set_virtual_button_active(9, False)
        set_virtual_button_visible(9, False)

        add_virtual_button(10, 780, 250, 150)
        set_virtual_button_text(10, "CIRCLE")
        set_virtual_button_color(10, 5, 5, 5)
        set_virtual_button_active(10, False)
        set_virtual_button_visible(10, False)

        add_virtual_button(11, 700, 500, 100)
        set_virtual_button_text(11, "CHECK")
        set_virtual_button_color(11, 5, 5, 5)
        set_virtual_button_active(11, False)
        set_virtual_button_visible(11, False)

        add_virtual_button(12, 500, 500, 100)
        set_virtual_button_text(12, "CANCEL")
        set_virtual_button_color(12, 5, 5, 5)
        set_virtual_button_active(12, False)
        set_virtual_button_visible(12, False)

        while start:
            hit_vault = get_sprite_hit_test(vault, get_pointer_x(), get_pointer_y())
            hit_screen = get_sprite_hit_test(computer, get_pointer_x(), get_pointer_y())

            if not get_sprite_exists(vault) and RuntimeWarning:
                warnings.filterwarnings("ignore", category=RuntimeWarning)
                set_sprite_visible(vault_unlocked, True)
                set_sprite_visible(chips, True)
                set_sprite_visible(backpack, True)
                set_sprite_visible(key2, True)
                set_text_visible(info_text, False)

            if hit_screen and get_pointer_pressed():
                play_sound(mouseclick, 200)
                set_sprite_visible(vault_screen, False)
                computer_window()

            if hit_vault and RuntimeWarning:
                warnings.filterwarnings("ignore", category=RuntimeWarning)
                set_sprite_visible(character_stand, True)
                set_sprite_position(character_stand, 860, 425)
                set_sprite_active(computer, False)
                set_text_visible(info_text, False)
            else:
                set_sprite_visible(character_stand, False)

            if get_virtual_button_pressed(5):
                play_sound(mouseclick, 200)
                set_sprite_visible(clothes_1, False)
                set_sprite_visible(clothes_2, False)
                set_sprite_visible(password_1, False)
                set_sprite_visible(door2, False)
                set_sprite_visible(vault, False)
                set_sprite_visible(two, False)
                set_sprite_visible(five, False)
                set_sprite_visible(computer, False)
                set_sprite_visible(clock, False)
                set_sprite_visible(vault_unlocked, False)
                set_sprite_visible(vault_screen, False)
                set_text_visible(correct_password, False)
                set_text_visible(wrong_password, False)
                set_sprite_visible(chips, False)
                set_sprite_visible(backpack, False)
                set_sprite_visible(key2, False)
                set_text_visible(info_text, False)
                delete_virtual_button(5)
                scene1()
            if get_sprite_hit_test(password_1, get_pointer_x(), get_pointer_y()):
                start_text_input()
                text = get_text_input()
                if text == "1325" and get_sprite_visible(key2):
                    print("YESSS")
                    set_sprite_visible(door2, False)
                    set_sprite_visible(door2_unlocked, True)
                    # SET REWIND BUTTON FALSE OR INACTIVE
                    set_virtual_button_active(5, False)
                    set_virtual_button_visible(5, False)
                    set_sprite_visible(clothes_1, False)
                    set_text_visible(correct_password, False)
                    set_text_visible(wrong_password, False)
                    stop_text_input()
                    scene3()
                else:
                    set_text_visible(info_text, True)
            else:
                stop_text_input()
            if get_sprite_hit_test(clothes_1, get_pointer_x(), get_pointer_y()):
                set_sprite_visible(clothes_2, True)
                set_sprite_visible(clothes_1, False)
            else:
                set_sprite_visible(clothes_2, False)
                set_sprite_visible(clothes_1, True)

            if get_sprite_hit_test(vault, get_pointer_x(), get_pointer_y()) and get_pointer_pressed():
                set_sprite_visible(computer, False)
                set_sprite_visible(clock, False)
                set_sprite_visible(vault_screen, True)
                set_virtual_button_visible(7, True)
                set_virtual_button_visible(8, True)
                set_virtual_button_visible(9, True)
                set_virtual_button_visible(10, True)
                set_virtual_button_visible(11, True)
                set_virtual_button_visible(12, True)

                set_virtual_button_active(7, True)
                set_virtual_button_active(8, True)
                set_virtual_button_active(9, True)
                set_virtual_button_active(10, True)
                set_virtual_button_active(11, True)
                set_virtual_button_active(12, True)

            if get_virtual_button_pressed(7):
                play_sound(mouseclick, 200)
                password_input.append("heart")
            if get_virtual_button_pressed(8):
                play_sound(mouseclick, 200)
                password_input.append("star")
            if get_virtual_button_pressed(9):
                play_sound(mouseclick, 200)
                password_input.append("square")
            if get_virtual_button_pressed(10):
                play_sound(mouseclick, 200)
                password_input.append("circle")
            if get_virtual_button_pressed(11) and password_input == password_vault:
                print("TRUE")
                print(password_input)
                delete_sprite(vault)
                set_sprite_visible(vault_screen, False)
                set_sprite_visible(backpack, True)
                set_sprite_visible(vault_unlocked, True)
                set_text_visible(correct_password, True)
                set_text_visible(info_text, False)
                set_virtual_button_visible(7, False)
                set_virtual_button_visible(8, False)
                set_virtual_button_visible(9, False)
                set_virtual_button_visible(10, False)
                set_virtual_button_visible(11, False)
                set_virtual_button_visible(12, False)

                set_virtual_button_active(7, False)
                set_virtual_button_active(8, False)
                set_virtual_button_active(9, False)
                set_virtual_button_active(10, False)
                set_virtual_button_active(11, False)
                set_virtual_button_active(12, False)

                set_sprite_visible(vault_screen, False)
                set_sprite_visible(computer, True)
                set_sprite_visible(clock, True)
                set_sprite_visible(chips, True)
                set_sprite_visible(key2, True)

                # ADD SOME CODES HERE....

            elif get_virtual_button_pressed(11) and password_input != password_vault:
                print("WRONG")
                set_text_visible(wrong_password, True)
                set_text_visible(info_text, False)
                password_input.clear()
                print(password_input)

            if get_virtual_button_released(12):
                play_sound(mouseclick, 200)
                set_text_visible(wrong_password, False)
                set_sprite_visible(vault_screen, False)
                set_virtual_button_visible(7, False)
                set_virtual_button_visible(8, False)
                set_virtual_button_visible(9, False)
                set_virtual_button_visible(10, False)
                set_virtual_button_visible(11, False)
                set_virtual_button_visible(12, False)

                set_virtual_button_active(7, False)
                set_virtual_button_active(8, False)
                set_virtual_button_active(9, False)
                set_virtual_button_active(10, False)
                set_virtual_button_active(11, False)
                set_virtual_button_active(12, False)

                set_sprite_visible(computer, True)
                set_sprite_visible(clock, True)

            agk.sync()

    def scene1():

        SLEEPING_X = 745
        SLEEPING_Y = 445
        STAND_X = 740
        STAND_Y = 200

        delete_virtual_button(7)
        delete_virtual_button(8)
        delete_virtual_button(9)
        delete_virtual_button(10)
        delete_virtual_button(11)
        delete_virtual_button(12)

        set_sprite_visible(wallpaper, False)
        set_sprite_visible(wallpaper_home, True)
        set_sprite_visible(couch, True)
        set_sprite_visible(door, True)
        set_sprite_visible(frame, True)
        set_sprite_visible(window, True)
        set_sprite_visible(character, True)
        set_sprite_visible(plant2, True)
        set_sprite_visible(one, True)
        set_sprite_visible(three, True)
        door_text = create_text("It is locked! He's holding me hostageee...")
        set_text_size(door_text, 30)
        set_text_visible(door_text, False)

        add_virtual_button(4, CARPET_X, CARPET_Y, 350)
        set_virtual_button_image_up(4, load_image("carpet.png"))
        set_virtual_button_image_down(4, load_image("carpet.png"))

        start = True

        while start:
            if get_virtual_button_pressed(4):
                play_sound(mouseclick, 200)
                set_sprite_visible(key, True)
                set_virtual_button_visible(4, False)
                set_virtual_button_active(4, False)
            if get_pointer_pressed():
                hit_couch = get_sprite_hit_test(couch, get_pointer_x(), get_pointer_y())
                hit_door = get_sprite_hit_test(door, get_pointer_x(), get_pointer_y())
                hit_key = get_sprite_hit_test(key, get_pointer_x(), get_pointer_y())
                hit_window = get_sprite_hit_test(window, get_pointer_x(), get_pointer_y())
                hit_frame = get_sprite_hit_test(frame, get_pointer_x(), get_pointer_y())
                hit_plant = get_sprite_hit_test(plant2, get_pointer_x(), get_pointer_y())

                if hit_plant:
                    play_sound(mouseclick, 200)
                    set_sprite_position(plant2, PLANT2_X, 25)

                if hit_couch:
                    play_sound(mouseclick, 200)
                    set_sprite_visible(character_sleeping, True)
                    set_sprite_visible(character, False)
                    set_sprite_position(character_sleeping, SLEEPING_X, SLEEPING_Y)
                    set_sprite_visible(character_stand, False)

                elif hit_door:
                    play_sound(mouseclick, 200)
                    set_text_visible(door_text, True)

                else:
                    play_sound(mouseclick, 200)
                    set_text_visible(door_text, False)
                    set_sprite_visible(character_sleeping, False)
                    set_sprite_visible(character, True)
                    set_sprite_visible(character_stand, False)

                if hit_key:
                    play_sound(mouseclick, 200)
                    set_text_visible(door_text, False)
                    set_sprite_visible(key, False)
                    set_sprite_active(key, False)
                    set_sprite_visible(door, False)
                    set_sprite_visible(opendoor, True)
                    scene2()
                    start = False
                    # OPENED DOOR SPRITE AND THEN PROCEED TO THE NEXT SCENE

                if hit_window:
                    play_sound(mouseclick, 200)
                    set_sprite_position(character_stand, STAND_X, STAND_Y)
                    set_sprite_visible(character_stand, True)
                    set_sprite_visible(character, False)
                    set_sprite_visible(character_sleeping, False)
                    set_text_visible(door_text, False)

                if hit_frame:
                    play_sound(mouseclick, 200)
                    set_sprite_position(frame, 100, 300)

            agk.sync()

    def intro2():

        start = True

        set_virtual_button_visible(1, False)
        set_virtual_button_active(1, False)

        # DIALOG

        dialog1 = create_text("I always wonder where my master goes everytime \nhe leaves the house. So I came up "
                              "with an idea of \nfollowing him...")
        set_text_size(dialog1, 30)
        set_text_position(dialog1, 10, 45)

        add_virtual_button(3, 900, 600, 100)
        set_virtual_button_text(3, "Next")
        set_virtual_button_color(3, 5, 5, 5)

        while start:
            if get_virtual_button_pressed(3):
                play_sound(mouseclick, 200)
                delete_text(dialog1)
                set_virtual_button_active(3, False)
                set_virtual_button_visible(3, False)
                scene1()
                start = False

            agk.sync()

            if agk.get_raw_key_pressed(agk.KEY_ESCAPE):
                break

    def intro1():

        start = True

        # INTRO TEXTS OR TITLE TEXTS
        title_text = create_text("Don't Leave Meow Alone!")
        set_text_size(title_text, 60)
        set_text_position(title_text, 35, 80)

        add_virtual_button(1, 500, 450, 150)
        set_virtual_button_text(1, "Start")
        set_virtual_button_color(1, 5, 5, 5)

        while start:

            if get_virtual_button_pressed(1):
                play_sound(mouseclick, 200)
                delete_text(title_text)
                intro2()
                start = False
            agk.sync()

            if agk.get_raw_key_pressed(agk.KEY_ESCAPE):
                break

    intro1()
