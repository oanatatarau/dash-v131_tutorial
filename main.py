@namespace
class StatusBarKind:
    Progress = StatusBarKind.create()

def on_up_pressed():
    if in_game:
        jump(sprite_player, gravity2, constants_tiles_high_jump)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_hit_wall(sprite, location):
    global jumps
    if gravity2 > 0:
        if sprite.is_hitting_tile(CollisionDirection.BOTTOM):
            jumps = 0
    else:
        if sprite.is_hitting_tile(CollisionDirection.TOP):
            jumps = 0
scene.on_hit_wall(SpriteKind.player, on_hit_wall)

def level_4():
    tiles.set_small_tilemap(tilemap("""
        level_4
        """))
    scene.set_background_color(13)
def level_5():
    tiles.set_small_tilemap(tilemap("""
        level_5
        """))
    scene.set_background_color(13)

def on_overlap_tile(sprite2, location2):
    global gravity2
    gravity2 = abs(gravity2) * 1
    sprite_player.ay = gravity2
    
    def on_throttle():
        
        def on_background():
            color.start_fade(color.poke, color.black, 200)
            color.pause_until_fade_done()
            color.start_fade(color.black, color.original_palette, 200)
        timer.background(on_background)
        
    timer.throttle("fade", 400, on_throttle)
    
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        gravity_down
        """),
    on_overlap_tile)

def on_a_pressed():
    if in_game:
        jump(sprite_player, gravity2, constants_tiles_high_jump)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_overlap_tile2(sprite3, location3):
    global gravity2
    gravity2 = abs(gravity2) * -1
    sprite_player.ay = gravity2
    
    def on_throttle2():
        
        def on_background2():
            color.start_fade(color.original_palette, color.black, 200)
            color.pause_until_fade_done()
            color.start_fade(color.black, color.poke, 200)
        timer.background(on_background2)
        
    timer.throttle("fade", 400, on_throttle2)
    
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        gravity_up0
        """),
    on_overlap_tile2)

def on_overlap_tile3(sprite4, location4):
    sprite4.destroy(effects.disintegrate, 100)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        top_spike
        """),
    on_overlap_tile3)

def win():
    global won
    sprite_player_cam.set_velocity(0, 0)
    won = True
    
    def on_after():
        game_over(True)
    timer.after(2000, on_after)
    
def create_status_bar(sprite5: Sprite, tilemap_length: number):
    global sprite_progress_bar
    sprite_progress_bar = statusbars.create(127, 4, StatusBarKind.Progress)
    sprite_progress_bar.set_flag(SpriteFlag.RELATIVE_TO_CAMERA, True)
    sprite_progress_bar.left = 4
    sprite_progress_bar.top = 2
    sprite_progress_bar.value = 0
    sprite_progress_bar.max = tilemap_length
    sprite_progress_bar.set_color(7, 15)
    sprite_progress_bar.set_bar_border(1, 15)
    
    def on_background3():
        global percent_traveled
        while True:
            sprite_progress_bar.value = sprite5.right
            percent_traveled = Math.round(Math.map(sprite5.right, 0, tilemap_length, 0, 100))
            if percent_traveled < 10:
                sprite_progress_bar.set_label("" + str(percent_traveled) + "%" + "  ", 15)
            elif percent_traveled < 100:
                sprite_progress_bar.set_label("" + str(percent_traveled) + "%" + " ", 15)
            else:
                sprite_progress_bar.set_label("" + str(percent_traveled) + "%", 15)
            pause(100)
    timer.background(on_background3)
    
def game_over(win2: bool):
    info.set_score(Math.constrain(Math.round(sprite_player.right), 0, constants_length))
    if info.score() > high_scores[selected_level - 1]:
        high_scores[selected_level - 1] = info.score()
    blockSettings.write_number_array("high_scores", high_scores)
    
    def on_after2():
        game.over(win2)
    timer.after(2000, on_after2)
    

def on_overlap_tile4(sprite6, location5):
    if not (won):
        win()
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        flag_bottom
        """),
    on_overlap_tile4)

def on_overlap_tile5(sprite7, location6):
    
    def on_throttle3():
        global jumps
        jump(sprite_player, gravity2, constants_tiles_high_jump)
        jumps = 0
    timer.throttle("auto_jump", 100, on_throttle3)
    
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        auto_jump
        """),
    on_overlap_tile5)

def prepare_level():
    tiles.place_on_random_tile(sprite_player, assets.tile("""
        start
        """))
    tiles.place_on_random_tile(sprite_player_cam, assets.tile("""
        start
        """))
    tiles.set_tile_at(tiles.get_tiles_by_type(assets.tile("""
            start
            """))[0],
        assets.tile("""
            transparency8
            """))
    sprite_player.set_velocity(48, 0)
    sprite_player_cam.set_velocity(48, 0)
    create_status_bar(sprite_player, tiles.tilemap_columns() * tiles.tile_width())
    scene.camera_follow_sprite(sprite_player_cam)
    tiles.cover_all_tiles(assets.tile("""
            auto_jump
            """),
        assets.tile("""
            blank
            """))
    tiles.cover_all_tiles(assets.tile("""
            from
            """),
        assets.tile("""
            blank
            """))
    tiles.cover_all_tiles(assets.tile("""
            to0
            """),
        assets.tile("""
            blank
            """))

def on_overlap_tile6(sprite8, location7):
    if not (won):
        win()
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        flag_top
        """),
    on_overlap_tile6)

def on_overlap_tile7(sprite9, location8):
    tiles.place_on_random_tile(sprite_player, assets.tile("""
        to0
        """))
    tiles.place_on_random_tile(sprite_player_cam, assets.tile("""
        to0
        """))
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        from
        """),
    on_overlap_tile7)

def level_2():
    tiles.set_small_tilemap(tilemap("""
        level_2
        """))
    scene.set_background_color(13)
def make_player():
    global sprite_player, sprite_player_cam
    sprite_player = sprites.create(assets.image("""
        character
        """), SpriteKind.player)
    sprite_player_cam = sprites.create(assets.image("""
            camera_reference
            """),
        SpriteKind.player)
    sprite_player.set_flag(SpriteFlag.AUTO_DESTROY, True)
    sprite_player_cam.set_flag(SpriteFlag.GHOST, True)
    sprite_player.ay = gravity2
def in_simulator_or_rpi():
    return control.device_dal_version() == "sim" or control.device_dal_version() == "linux"

def on_overlap_tile8(sprite10, location9):
    sprite10.destroy(effects.disintegrate, 100)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        bottom_spike
        """),
    on_overlap_tile8)

def select_level():
    color.set_palette(color.black)
    blockMenu.set_colors(1, 15)
    blockMenu.show_menu(menu, MenuStyle.GRID, MenuLocation.BOTTOM_HALF)
    blockMenu.set_controls_enabled(False)
    scene.set_background_color(13)
    tiles.set_small_tilemap(tilemap("""
        demo
        """))
    tiles.place_on_random_tile(sprite_player, assets.tile("""
        start
        """))
    tiles.set_tile_at(tiles.get_tiles_by_type(assets.tile("""
            start
            """))[0],
        assets.tile("""
            transparency8
            """))
    tiles.cover_all_tiles(assets.tile("""
            from
            """),
        assets.tile("""
            blank
            """))
    tiles.cover_all_tiles(assets.tile("""
            to0
            """),
        assets.tile("""
            blank
            """))
    tiles.cover_all_tiles(assets.tile("""
            auto_jump
            """),
        assets.tile("""
            blank
            """))
    sprite_player.set_velocity(48, 0)
    scene.camera_follow_sprite(sprite_player)
    fade(False, 2000, True)
    blockMenu.set_controls_enabled(True)
    wait_for_select()
    fade(True, 2000, True)
    color.set_palette(color.black)
    return parse_float(blockMenu.selected_menu_option())
def jump(sprite11: Sprite, gravity: number, tiles2: number):
    global jumps
    if jumps < constants_max_jumps:
        if gravity > 0:
            sprite11.vy = 0 - Math.sqrt(2 * (gravity * (tiles2 * tiles.tile_width())))
        else:
            sprite11.vy = Math.sqrt(2 * (abs(gravity) * (tiles2 * tiles.tile_width())))
        jumps += 1
        
        def on_background4():
            
            def on_throttle4():
                if in_simulator_or_rpi():
                    for index in range(36):
                        transformSprites.change_rotation(sprite_player, 10)
                        pause(10)
                else:
                    for index2 in range(8):
                        transformSprites.change_rotation(sprite_player, 45)
                        pause(45)
            timer.throttle("rotate", 100, on_throttle4)
            
        timer.background(on_background4)
        
def fade(_in: bool, duration: number, block: bool):
    if _in:
        color.start_fade(color.original_palette, color.black, duration)
    else:
        color.start_fade(color.black, color.original_palette, duration)
    if block:
        color.pause_until_fade_done()
def wait_for_select():
    global selected
    selected = False
    while not (selected):
        pause(100)
    blockMenu.close_menu()

def on_on_destroyed(sprite12):
    sprite_player_cam.set_velocity(0, 0)
    game_over(False)
sprites.on_destroyed(SpriteKind.player, on_on_destroyed)

def on_menu_option_selected(option, index3):
    global selected
    selected = True
blockMenu.on_menu_option_selected(on_menu_option_selected)

def level_1():
    tiles.set_small_tilemap(tilemap("""
        level_1
        """))
    scene.set_background_color(13)
def level_3():
    tiles.set_small_tilemap(tilemap("""
        level_3
        """))
    scene.set_background_color(13)
selected = False
percent_traveled = 0
sprite_progress_bar: StatusBarSprite = None
sprite_player_cam: Sprite = None
selected_level = 0
menu: List[str] = []
sprite_player: Sprite = None
high_scores: List[number] = []
in_game = False
won = False
jumps = 0
constants_length = 0
constants_max_jumps = 0
constants_tiles_high_jump = 0
gravity2 = 0
gravity2 = 300
constants_tiles_high_jump = 3
constants_max_jumps = 2
constants_length = 1600
constants_levels = 5
jumps = 0
won = False
in_game = False
while game.runtime() < 500:
    if controller.B.is_pressed():
        color.set_palette(color.black)
        scene.set_background_color(13)
        pause(100)
        fade(False, 2000, True)
        if game.ask("Reset high scores?"):
            blockSettings.remove("high_scores")
            blockSettings.remove("high-score")
            game.show_long_text("Successfully reset high scores!", DialogLayout.BOTTOM)
            fade(True, 2000, True)
            break
        fade(True, 2000, True)
    if controller.A.is_pressed():
        break
    pause(100)
if not (blockSettings.exists("high_scores")):
    high_scores = []
    for index4 in range(constants_levels):
        high_scores.append(0)
    blockSettings.write_number_array("high_scores", high_scores)
high_scores = blockSettings.read_number_array("high_scores")
make_player()
sprite_player.say("Dash!")
if True:
    menu = []
    index5 = 0
    while index5 <= constants_levels - 1:
        menu.append("" + str((index5 + 1)) + " (" + str(spriteutils.round_with_precision(high_scores[index5] / constants_length * 100, 2)) + "%)" + "")
        index5 += 1
    selected_level = select_level()
    pause(1000)
else:
    selected_level = constants_levels
tiles.load_map(tiles.create_map(tilemap("""
    level12
    """)))
blockSettings.write_number("high-score", high_scores[selected_level - 1])
if selected_level == 1:
    level_1()
elif selected_level == 2:
    level_2()
elif selected_level == 3:
    level_3()
elif selected_level == 4:
    level_4()
elif selected_level == 5:
    level_5()
prepare_level()
in_game = True
sprite_player.say("")
fade(False, 2000, False)

def on_on_update():
    sprite_player.vx = 48
game.on_update(on_on_update)

def on_update_interval():
    if not (won):
        if sprite_player.x > sprite_player_cam.x:
            sprite_player.x += -1
        elif sprite_player.x < sprite_player_cam.x:
            sprite_player.x += 1
game.on_update_interval(100, on_update_interval)
