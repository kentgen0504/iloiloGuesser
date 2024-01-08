import tkinter as tk
from tkinter import font as tkFont
import random
import math

# GUI
def move_to(page):
    window.main_canvas.delete('all')

    if page == 'title': title_screen()
    elif page == 'menu': main_menu()
    elif page == 'hs': highscore_screen()
    elif page == 'setting': setting_screen()
    elif page == 'about': about_screen()

def title_screen():
    global title_update

    if title_update:
        # bg
        window.title_bg = window.main_canvas.create_image(0, 0, anchor=tk.NW, image=TITLE_BG)
        
        # bttn
        window.title_bttn = window.start_bttn = window.main_canvas.create_image(WIN_WIDTH//2, 7*WIN_HEIGHT//10, anchor=tk.CENTER, image=START_BTTN)
        
        # bind
        window.main_canvas.tag_bind(window.start_bttn, '<Button-1>', lambda event: move_to('menu'))
        title_update = False

def main_menu():
    window.main_canvas.create_image(0, 0, anchor=tk.NW, image=UNIV_BG) # bg img

    # left side
    window.main_canvas.create_image(3*WIN_WIDTH//10, 20, anchor=tk.N, image=MENU_TITLE) # title
    window.main_canvas.create_image(3*WIN_WIDTH//10, 150, anchor=tk.N, image=MENU_IMG) # img

    # right side
    window.play_bttn = window.main_canvas.create_image(4*WIN_WIDTH//5, WIN_HEIGHT//2 - 160, anchor=tk.CENTER, image=PLAY_BTTN)
    window.hs_bttn = window.main_canvas.create_image(4*WIN_WIDTH//5, WIN_HEIGHT//2 - 80, anchor=tk.CENTER, image=HS_BTTN)
    window.setting_bttn = window.main_canvas.create_image(4*WIN_WIDTH//5, WIN_HEIGHT//2, anchor=tk.CENTER, image=SETTING_BTTN)
    window.about_bttn = window.main_canvas.create_image(4*WIN_WIDTH//5, WIN_HEIGHT//2 + 80, anchor=tk.CENTER, image=ABOUT_BTTN)
    window.exit_bttn = window.main_canvas.create_image(4*WIN_WIDTH//5, WIN_HEIGHT//2 + 160, anchor=tk.CENTER, image=EXIT_BTTN)

    # button bind
    window.main_canvas.tag_bind(window.play_bttn, '<Button-1>', lambda event: play_option())
    window.main_canvas.tag_bind(window.hs_bttn, '<Button-1>', lambda event: move_to('hs'))
    window.main_canvas.tag_bind(window.setting_bttn, '<Button-1>', lambda event: move_to('setting'))
    window.main_canvas.tag_bind(window.about_bttn, '<Button-1>', lambda event: move_to('about'))
    window.main_canvas.tag_bind(window.exit_bttn, '<Button-1>', lambda event: exit_confirm())

def highscore_screen():
    global diff_text, diff_color

    get_highscores()

    if diff_text == 'Easy': 
        vis_stat = stat_e[:]
        diff_img = HS_EASY
    elif diff_text == 'Medium':
        vis_stat = stat_m[:]
        diff_img = HS_MED
    elif diff_text == 'Hard':
        vis_stat = stat_h[:]
        diff_img = HS_HARD

    window.main_canvas.create_image(0, 0, anchor=tk.NW, image=UNIV_BG) # bg img
    window.main_canvas.create_image(WIN_WIDTH//2, 30, anchor=tk.N, image=HS_TITLE) # title
    window.main_canvas.create_image(WIN_WIDTH//2, 105, anchor=tk.CENTER, image=diff_img) # diff text
    
    #font=tkFont.Font(family='Small Fonts', size=15)

    # bttn
    window.hs_back = window.main_canvas.create_image(20, 20, anchor=tk.NW, image=UNIV_BACK)
    window.hs_left = window.main_canvas.create_image(WIN_WIDTH//2 - WIN_WIDTH//6 - 30, 302, anchor=tk.E, image=HS_LEFT)
    window.hs_right = window.main_canvas.create_image(WIN_WIDTH//2 + WIN_WIDTH//6 + 30, 302, anchor=tk.W, image=HS_RIGHT)

    # button bind
    window.main_canvas.tag_bind(window.hs_back, '<Button-1>', lambda event: move_to('menu'))
    window.main_canvas.tag_bind(window.hs_left, '<Button-1>', lambda event: highscore_diff_switch('left'))
    window.main_canvas.tag_bind(window.hs_right, '<Button-1>', lambda event: highscore_diff_switch('right'))

    # leaderboard
    # highscore bg
    window.main_canvas.create_rectangle(WIN_WIDTH//2 - WIN_WIDTH//6, 130, WIN_WIDTH//2 + WIN_WIDTH//6, 474, fill=diff_color)
    window.main_canvas.create_rectangle(WIN_WIDTH//2 - WIN_WIDTH//6 + 5, 135, WIN_WIDTH//2 + WIN_WIDTH//6 - 5, 469, fill='white')
    window.main_canvas.create_rectangle(WIN_WIDTH//2 - WIN_WIDTH//6 + 10, 140, WIN_WIDTH//2 + WIN_WIDTH//6 - 10, 464, fill=diff_color)

    # header
    window.main_canvas.create_text(WIN_WIDTH//2 - (WIN_WIDTH//3 - 20)//5, 142, font=tkFont.Font(family='Small Fonts', size=12, weight='bold'), text="Name", anchor=tk.N) # name
    window.main_canvas.create_text(WIN_WIDTH//2 + 3*(WIN_WIDTH//3 - 20)//10, 142, font=tkFont.Font(family='Small Fonts', size=12, weight='bold'), text="Score", anchor=tk.N) # score

    # data
    num = len(vis_stat)
    for i in range(10):
        if i < num:
            window.main_canvas.create_text(WIN_WIDTH//2 - WIN_WIDTH//6 + 15, 179 + i*30, font=tkFont.Font(family='Small Fonts', size=12), text=f"{i+1}. {vis_stat[i][0]}", anchor=tk.W)
            window.main_canvas.create_text(WIN_WIDTH//2 + WIN_WIDTH//6 - 15, 179 + i*30, font=tkFont.Font(family='Small Fonts', size=12), text=f"{vis_stat[i][1]}", anchor=tk.E)
        else:
            window.main_canvas.create_text(WIN_WIDTH//2 - WIN_WIDTH//6 + 15, 179 + i*30, font=tkFont.Font(family='Small Fonts', size=12), text=f"{i+1}. ...", anchor=tk.W)

    # vertical seperator lines
    window.main_canvas.create_rectangle(WIN_WIDTH//2 + (WIN_WIDTH//3 - 20)//10, 137, WIN_WIDTH//2 + (WIN_WIDTH//3 - 20)//10 + 2, 468, fill='white', outline='')

    # horizontal seperator lines
    for i in range(10):
        window.main_canvas.create_rectangle(WIN_WIDTH//2 - WIN_WIDTH//6 + 7, 164 + i*30, WIN_WIDTH//2 + WIN_WIDTH//6 - 7, 166 + i*30, fill='white', outline='')

def setting_screen():
    window.main_canvas.create_image(0, 0, anchor=tk.NW, image=UNIV_BG) # bg img
    window.main_canvas.create_image(WIN_WIDTH//2, 30, anchor=tk.N, image=SETTING_TITLE) # title

    # bttn
    window.setting_back = window.main_canvas.create_image(20, 20, anchor=tk.NW, image=UNIV_BACK)

    # button bind
    window.main_canvas.tag_bind(window.setting_back, '<Button-1>', lambda event: move_to('menu'))

def about_screen():
    window.main_canvas.create_image(0, 0, anchor=tk.NW, image=UNIV_BG) # bg img
    window.main_canvas.create_image(WIN_WIDTH//2, 30, anchor=tk.N, image=ABOUT_TITLE) # title

    # bttn
    window.about_back = window.main_canvas.create_image(20, 20, anchor=tk.NW, image=UNIV_BACK)

    # button bind
    window.main_canvas.tag_bind(window.about_back, '<Button-1>', lambda event: move_to('menu'))

def play_option():
    window.main_canvas.tag_unbind(window.play_bttn, '<Button-1>')
    window.main_canvas.tag_unbind(window.hs_bttn, '<Button-1>')
    window.main_canvas.tag_unbind(window.setting_bttn, '<Button-1>')
    window.main_canvas.tag_unbind(window.about_bttn, '<Button-1>')
    window.main_canvas.tag_unbind(window.exit_bttn, '<Button-1>')

    window.main_canvas.create_image(WIN_WIDTH//2, WIN_HEIGHT//2, anchor=tk.CENTER, image=PLAY_DIFF)

    # bttn
    window.play_easy = window.main_canvas.create_image(170, 216, anchor=tk.NW, image=PLAY_EASY)
    window.play_med = window.main_canvas.create_image(333, 216, anchor=tk.NW, image=PLAY_MED)
    window.play_hard = window.main_canvas.create_image(492, 216, anchor=tk.NW, image=PLAY_HARD)

    # bind
    window.main_canvas.tag_bind(window.play_easy, '<Button-1>', lambda event: start_game('easy'))
    window.main_canvas.tag_bind(window.play_med, '<Button-1>', lambda event: exit())
    window.main_canvas.tag_bind(window.play_hard, '<Button-1>', lambda event: exit())

def exit_confirm():
    window.main_canvas.tag_unbind(window.play_bttn, '<Button-1>')
    window.main_canvas.tag_unbind(window.hs_bttn, '<Button-1>')
    window.main_canvas.tag_unbind(window.setting_bttn, '<Button-1>')
    window.main_canvas.tag_unbind(window.about_bttn, '<Button-1>')
    window.main_canvas.tag_unbind(window.exit_bttn, '<Button-1>')

    window.main_canvas.create_image(WIN_WIDTH//2, WIN_HEIGHT//2, anchor=tk.CENTER, image=EXIT_CONF)

    # bttn
    window.exit_yes = window.main_canvas.create_image(223, 265, anchor=tk.NW, image=EXIT_YES)
    window.exit_no = window.main_canvas.create_image(436, 265, anchor=tk.NW, image=EXIT_NO)

    # binds
    window.main_canvas.tag_bind(window.exit_yes, '<Button-1>', lambda event: exit())
    window.main_canvas.tag_bind(window.exit_no, '<Button-1>', lambda event: move_to('menu'))

# GAME
def game_loop(diff, locs):
    global fps, game_state, game_running

    try: window.winfo_exists()
    except: exit()

    if game_state == 'location': location_state(locs)
    elif game_state == 'map': map_state(diff, locs)
    elif game_state == 'answer': answer_state(diff, locs)
    elif game_state == 'stage_clear': clear_state(diff)
    elif game_state == 'stop': 
        game_running = False
        move_to('menu')
    
    if game_running:
        window.after(int(1000/fps), lambda: game_loop(diff, locs))

def location_state(locs):
    global btt1_state, x1, x2, img_pos_x1, img_pos_x2, stage

    if btt1_state == 'released':
        img_pos_x1 += (x2 - x1)
        x1, x2 = 0, 0

    # check if widget is already on the window
    # if widget exists, simply ignore
    # if widget is missing, create widget
    if not hasattr(window, 'loc_img1'): window.loc_img1 = window.main_canvas.create_image(img_pos_x1 + (x2 - x1), WIN_HEIGHT // 2, anchor=tk.CENTER, image=locs[stage-1][1])
    if not hasattr(window, 'loc_img2'): window.loc_img2 = window.main_canvas.create_image(img_pos_x2 + (x2 - x1), WIN_HEIGHT // 2, anchor=tk.CENTER, image=locs[stage-1][1])
    if not hasattr(window, 'map_bttn'): window.map_bttn = window.main_canvas.create_image(WIN_WIDTH - 10, 10 // 2, anchor=tk.NE, image=MAP)
    
    # link img2 to img1
    if img_pos_x1 > WIN_WIDTH//2: img_pos_x2 = img_pos_x1 - 3330
    else: img_pos_x2 = img_pos_x1 + 3330

    # switches pos of img1 and img2 if img2 occupy most of the screen
    if 0 < img_pos_x2 < WIN_WIDTH: img_pos_x2, img_pos_x1 = img_pos_x1, img_pos_x2

    # loc image repositioning
    window.main_canvas.coords(window.loc_img1, img_pos_x1 + (x2 - x1), WIN_HEIGHT // 2)
    window.main_canvas.coords(window.loc_img2, img_pos_x2 + (x2 - x1), WIN_HEIGHT // 2)

    # bind
    window.main_canvas.tag_bind(window.map_bttn, '<Button-1>', lambda event: change_game_state('map'))

def map_state(diff, locs):
    global btt1_state, x1, x2, y1, y2, map_pos_x, map_pos_y, pin_pos_x, pin_pos_y

    if diff == 'easy': map_img = MAP_EASY

    if btt1_state == 'released':
        map_pos_x = pos_correction(map_pos_x, x2 - x1, map_img.width()-WIN_WIDTH)
        map_pos_y = pos_correction(map_pos_y, y2 - y1, map_img.height()-WIN_HEIGHT)

        x1, x2, y1, y2 = 0, 0, 0, 0
    
    curr_map_pos_x = pos_correction(map_pos_x, x2 - x1, map_img.width()-WIN_WIDTH)
    curr_map_pos_y = pos_correction(map_pos_y, y2 - y1, map_img.height()-WIN_HEIGHT)

    if not hasattr(window, 'map'): window.map = window.main_canvas.create_image(curr_map_pos_x, curr_map_pos_y, anchor=tk.NW, image=map_img)
    if not hasattr(window, 'loc_pin'): window.loc_pin = window.main_canvas.create_image(pin_pos_x + curr_map_pos_x, pin_pos_y + curr_map_pos_y, anchor=tk.S, image=PIN)
    if not hasattr(window, 'loc_conf'): window.loc_conf = window.main_canvas.create_image(pin_pos_x + curr_map_pos_x, pin_pos_y + curr_map_pos_y, anchor=tk.S, image=PIN_CONF)
    if not hasattr(window, 'loc_bttn'): window.loc_bttn = window.main_canvas.create_image(WIN_WIDTH - 10, 10 // 2, anchor=tk.NE, image=MAP)

    # bind
    window.main_canvas.tag_bind(window.loc_conf, '<Button-1>', lambda event: assess_answer(diff, locs))
    window.main_canvas.tag_bind(window.loc_bttn, '<Button-1>', lambda event: change_game_state('location'))

    # map image repositioning
    window.main_canvas.coords(window.map, curr_map_pos_x, curr_map_pos_y)
    window.main_canvas.coords(window.loc_pin, pin_pos_x + curr_map_pos_x, pin_pos_y + curr_map_pos_y)
    window.main_canvas.coords(window.loc_conf, pin_pos_x + curr_map_pos_x, pin_pos_y + curr_map_pos_y - 27)

def answer_state(diff, locs):
    global stage, pin_pos_x, pin_pos_y, map_pos_x, map_pos_y, x1, x2, y1, y2, stage_score

    if diff == 'easy': map_img = MAP_EASY

    if not hasattr(window, 'map_ans'):
        map_pos_x = pos_correction(400 - locs[stage-1][0][0], 0, map_img.width()-WIN_WIDTH)
        map_pos_y = pos_correction(250 - locs[stage-1][0][1], 0, map_img.height()-WIN_HEIGHT)
        window.map_ans = window.main_canvas.create_image(map_pos_x, map_pos_y, anchor=tk.NW, image=map_img)
    if not hasattr(window, 'dist_line'): window.dist_line = window.main_canvas.create_line(pin_pos_x + map_pos_x, pin_pos_y + map_pos_y, locs[stage-1][0][0] + map_pos_x, locs[stage-1][0][1] + map_pos_y, fill="black", dash=(6, 4), width=3)
    if not hasattr(window, 'loc_pin'): window.loc_pin = window.main_canvas.create_image(pin_pos_x + map_pos_x, pin_pos_y + map_pos_y, anchor=tk.S, image=PIN)
    if not hasattr(window, 'loc_ans'): window.loc_ans = window.main_canvas.create_image(locs[stage-1][0][0] + map_pos_x, locs[stage-1][0][1] + map_pos_y, anchor=tk.S, image=ANS)
    if not hasattr(window, 'next_bttn'): window.next_bttn = window.main_canvas.create_image(10, 50, anchor=tk.NW, image=NEXT_BTTN)
    if not hasattr(window, 'score'): window.score = window.main_canvas.create_text(10, 10, font=tkFont.Font(family='Small Fonts', size=20, weight='bold'), text=f"Score: {stage_score}", anchor=tk.NW)

    if btt1_state == 'released':
        map_pos_x = pos_correction(map_pos_x, x2 - x1, map_img.width()-WIN_WIDTH)
        map_pos_y = pos_correction(map_pos_y, y2 - y1, map_img.height()-WIN_HEIGHT)

        x1, x2, y1, y2 = 0, 0, 0, 0
    
    curr_map_pos_x = pos_correction(map_pos_x, x2 - x1, map_img.width()-WIN_WIDTH)
    curr_map_pos_y = pos_correction(map_pos_y, y2 - y1, map_img.height()-WIN_HEIGHT)

    window.main_canvas.tag_bind(window.next_bttn, '<Button-1>', lambda event: next_stage())

    # position update
    window.main_canvas.coords(window.map_ans, curr_map_pos_x, curr_map_pos_y)
    window.main_canvas.coords(window.dist_line, pin_pos_x + curr_map_pos_x, pin_pos_y + curr_map_pos_y, locs[stage-1][0][0] + curr_map_pos_x, locs[stage-1][0][1] + curr_map_pos_y)
    window.main_canvas.coords(window.loc_pin, pin_pos_x + curr_map_pos_x, pin_pos_y + curr_map_pos_y)
    window.main_canvas.coords(window.loc_ans, locs[stage-1][0][0] + curr_map_pos_x, locs[stage-1][0][1] + curr_map_pos_y)

def clear_state(diff):
    global total_score

    if diff == 'easy': bg = CLEAR_EASY

    if not hasattr(window, 'clear_bg'): window.clear_bg = window.main_canvas.create_image(0, 0, anchor=tk.NW, image=bg)
    if not hasattr(window, 'ttl_text'): window.ttl_text = window.main_canvas.create_text(WIN_WIDTH//2, WIN_HEIGHT//2 + 100, font=tkFont.Font(family='Small Fonts', size=40, weight='bold'), text='Total Score:', anchor=tk.N)
    if not hasattr(window, 'ttl_score'): window.ttl_score = window.main_canvas.create_text(WIN_WIDTH//2, WIN_HEIGHT//2 + 150, font=tkFont.Font(family='Small Fonts', size=40, weight='bold'), text=total_score, anchor=tk.N)
    if not hasattr(window, 'menu_bttn'): window.menu_bttn = window.menu_bttn = window.main_canvas.create_image(20, 20, anchor=tk.NW, image=CLEAR_BACK)

    window.main_canvas.tag_bind(window.menu_bttn, '<Button-1>', lambda event: change_game_state('stop'))

# NECESSARY computations
def assess_answer(diff, locs):
    global stage, stage_score, pin_pos_x, pin_pos_y

    if diff == 'easy': 
        min_max = EASY_MIN_MAX
        perfect = EASY_PERFECT

    dist_from_ans = math.sqrt((pin_pos_x - locs[stage-1][0][0])**2 + (pin_pos_y - locs[stage-1][0][1])**2)

    if dist_from_ans < min_max[0]: stage_score = perfect
    elif dist_from_ans > min_max[1]: stage_score = 0
    else: stage_score = int(perfect * (1 - dist_from_ans/(min_max[1]-min_max[0])))

    change_game_state('answer')

def change_game_state(new):
    global game_state, x1, x2, y1, y2

    # refesh variables
    x1, x2, y1, y2 = 0, 0, 0, 0

    # actually changing state
    game_state = new

    # scrap yard
    window.main_canvas.delete('all')

    if hasattr(window, 'loc_img1'): del window.loc_img1
    if hasattr(window, 'loc_img2'): del window.loc_img2
    if hasattr(window, 'map'): del window.map
    if hasattr(window, 'map_ans'): del window.map_ans
    if hasattr(window, 'map_bttn'): del window.map_bttn
    if hasattr(window, 'loc_ans'): del window.loc_ans
    if hasattr(window, 'loc_pin'): del window.loc_pin
    if hasattr(window, 'loc_conf'): del window.loc_conf
    if hasattr(window, 'loc_bttn'): del window.loc_bttn
    if hasattr(window, 'dist_line'): del window.dist_line
    if hasattr(window, 'next_bttn'): del window.next_bttn
    if hasattr(window, 'score'): del window.score
    if hasattr(window, 'clear_bg'): del window.clear_bg
    if hasattr(window, 'ttl_text'): del window.ttl_text
    if hasattr(window, 'ttl_score'): del window.ttl_score
    if hasattr(window, 'menu_bttn'): del window.menu_bttn

def next_stage():
    global stage, stage_score, total_score, img_pos_x1, img_pos_x2, map_pos_x, map_pos_y, pin_pos_x, pin_pos_y

    stage += 1
    total_score += stage_score

    # refresh variables
    img_pos_x1 = WIN_WIDTH//2
    img_pos_x2 = 0
    map_pos_x, map_pos_y = 0, 0
    pin_pos_x, pin_pos_y = 0, 0

    if stage <= 5: change_game_state('location')
    else: change_game_state('stage_clear')

def highscore_diff_switch(dir):
    global diff_text, diff_color

    if dir == 'left':
        if diff_text == 'Easy':
            diff_text = 'Hard'
            diff_color = '#AA4FE0'
        elif diff_text == 'Medium':
            diff_text = 'Easy'
            diff_color = '#ff0068'
        elif diff_text == 'Hard':
            diff_text = 'Medium'
            diff_color = '#a509a8'
    elif dir == 'right':
        if diff_text == 'Medium':
            diff_text = 'Hard'
            diff_color = '#AA4FE0'
        elif diff_text == 'Hard':
            diff_text = 'Easy'
            diff_color = '#ff0068'
        elif diff_text == 'Easy':
            diff_text = 'Medium'
            diff_color = '#a509a8'
    
    move_to('hs')

def get_highscores():
    stat_e.clear()
    stat_m.clear()
    stat_h.clear()
    
    dif = ''
    counter = 0

    db = open('highscore_db.txt', 'r')
    for data in db:
        line = data.rstrip('\n')

        if line in ('#easy', '#med', '#hard'): 
            dif = line
            counter = 0
            continue
        
        if dif == '#easy': stat_e.append(line.split('|'))
        elif dif == '#med': stat_m.append(line.split('|'))
        elif dif == '#hard': stat_h.append(line.split('|'))
        
        counter += 1
    db.close()

def get_loc_coords(diff):
    coords = list()

    db = open('game_db.txt', 'r')
    coords_copy = False
    for data in db:
        line = data.rstrip('\n')
        if coords_copy and line == '---': break
        elif coords_copy: coords.append([tuple(map(int, line[1:-1].split(",")))])
        
        if not coords_copy and line == diff: coords_copy = True
    db.close()

    return coords

def start_game(diff, n=5):
    global game_running

    rnd_num = random.sample(range(15), n)
    if diff == 'easy': locs = [easy_locs[i] for i in rnd_num]

    # refresh all variables
    refresh_game_var()

    game_running = True
    game_loop(diff, locs)

def refresh_game_var():
    global game_state, btt1_state, total_score, stage_score, stage, x1, x2, y1, y2, img_pos_x1, img_pos_x2, map_pos_x, map_pos_y, pin_pos_x, pin_pos_y

    game_state = 'location'
    btt1_state = 'released'
    stage = 1
    stage_score = 0
    total_score = 0
    x1, x2, y1, y2 = 0, 0, 0, 0
    img_pos_x1 = WIN_WIDTH//2
    img_pos_x2 = 0
    map_pos_x, map_pos_y = 0, 0
    pin_pos_x, pin_pos_y = 0, 0

def on_button_press(event):
    global x1, x2, y1, y2, btt1_state
    x1 = window.winfo_pointerx() - window.winfo_rootx()
    x2 = window.winfo_pointerx() - window.winfo_rootx()
    y1 = window.winfo_pointery() - window.winfo_rooty()
    y2 = window.winfo_pointery() - window.winfo_rooty()
    btt1_state = 'pressed'

def on_mouse_drag(event):
    global x2, y2, btt1_state
    x2 = window.winfo_pointerx() - window.winfo_rootx()
    y2 = window.winfo_pointery() - window.winfo_rooty()
    btt1_state = 'dragged'

def on_button_release(event):
    global btt1_state
    btt1_state = 'released'

def on_double_click(event):
    global pin_pos_x, pin_pos_y, map_pos_x, map_pos_y

    if game_state == 'map':
        pin_pos_x = window.winfo_pointerx() - window.winfo_rootx() - map_pos_x
        pin_pos_y = window.winfo_pointery() - window.winfo_rooty() - map_pos_y

def pos_correction(pos, move, min):
    min *= -1

    if pos + move < min: pos = min
    elif pos + move > 0: pos = 0
    else: pos += move

    return pos

window = tk.Tk()
window.title("IloiloGuessr")
window.resizable(False, False)

# game default setting
game_running = False

fps = 30
gui_state = 'title'

title_update = True
menu_update = True
hs_update = True

play_overlay = False
exit_overlay = False

# highscore screen variables
diff_text = 'Easy'
diff_color = '#ff0068'

stat_e = list()
stat_m = list()
stat_h = list()

# mouse binds
window.bind("<ButtonPress-1>", on_button_press)
window.bind("<B1-Motion>", on_mouse_drag)
window.bind("<ButtonRelease-1>", on_button_release)
window.bind("<Double-Button-1>", on_double_click)

# dimension measurements
WIN_WIDTH = 800
WIN_HEIGHT = 500
SCR_WIDTH = window.winfo_screenwidth() 
SCR_HEIGHT = window.winfo_screenheight()

# placing the window at center of the screen
x = int((SCR_WIDTH - WIN_WIDTH)//2) 
y = int((SCR_HEIGHT - WIN_HEIGHT)//2)
window.geometry(f"{WIN_WIDTH}x{WIN_HEIGHT}+{x}+{y}")

# game variabes
EASY_PERFECT = 1000
MED_PERFECT = 2500
HARD_PERFECT = 5000

EASY_MIN_MAX = (5, 500) # in meters
MED_MIN_MAX = (5, 500)
HARD_MIN_MAX = (5, 500)

game_state = 'location'
btt1_state = 'released'

stage = 1
stage_score = 0

total_score = 0

x1, x2, y1, y2 = 0, 0, 0, 0
img_pos_x1 = WIN_WIDTH//2
img_pos_x2 = 0
map_pos_x, map_pos_y = 0, 0
pin_pos_x, pin_pos_y = 0, 0

# setting canvas
window.main_canvas = tk.Canvas(window, width=WIN_WIDTH, height=WIN_HEIGHT, borderwidth=0, highlightthickness=0)
window.main_canvas.pack()

# images
MAP_EASY = tk.PhotoImage(file='.\\assets\\gamePictures\\easy\\upv_map.png')
#MAP_MED = tk.PhotoImage(file='.\\assets\\gamePictures\\easy\\miagao_map.png')
#MAP_HARD = tk.PhotoImage(file='.\\assets\\gamePictures\\easy\\iloilo_map.png')

# get image and coords for easy round
easy_locs = get_loc_coords('#easy')
for i in range(1, 16):
    if i < 10: num = '0' + str(i)
    else: num = str(i)
    easy_locs[i-1].append(tk.PhotoImage(file=f'.\\assets\\gamePictures\\easy\\upv_loc{num}.png'))

CLEAR_EASY = tk.PhotoImage(file='.\\assets\\gamePictures\\easy\\stage_clear.png')

# title_screen imgs
TITLE_BG = tk.PhotoImage(file='.\\assets\\uiDesigns\\title_screen\\title_bg.png')
START_BTTN = tk.PhotoImage(file='.\\assets\\uiDesigns\\title_screen\\start_bttn.png')

# menu_screen imgs
MENU_TITLE = tk.PhotoImage(file='.\\assets\\uiDesigns\\menu_screen\\title_head.png')
MENU_IMG = tk.PhotoImage(file='.\\assets\\uiDesigns\\menu_screen\\menu_img.png')

PLAY_BTTN = tk.PhotoImage(file='.\\assets\\uiDesigns\\menu_screen\\play_bttn.png')
HS_BTTN = tk.PhotoImage(file='.\\assets\\uiDesigns\\menu_screen\\highscore_bttn.png')
SETTING_BTTN = tk.PhotoImage(file='.\\assets\\uiDesigns\\menu_screen\\setting_bttn.png')
ABOUT_BTTN = tk.PhotoImage(file='.\\assets\\uiDesigns\\menu_screen\\about_bttn.png')
EXIT_BTTN = tk.PhotoImage(file='.\\assets\\uiDesigns\\menu_screen\\exit_bttn.png')

PLAY_DIFF = tk.PhotoImage(file='.\\assets\\uiDesigns\\menu_screen\\play_diff.png')
PLAY_EASY = tk.PhotoImage(file='.\\assets\\uiDesigns\\menu_screen\\play_easy.png')
PLAY_MED = tk.PhotoImage(file='.\\assets\\uiDesigns\\menu_screen\\play_med.png')
PLAY_HARD = tk.PhotoImage(file='.\\assets\\uiDesigns\\menu_screen\\play_hard.png')

EXIT_CONF = tk.PhotoImage(file='.\\assets\\uiDesigns\\menu_screen\\exit_confirm.png')
EXIT_YES = tk.PhotoImage(file='.\\assets\\uiDesigns\\menu_screen\\exit_yes.png')
EXIT_NO = tk.PhotoImage(file='.\\assets\\uiDesigns\\menu_screen\\exit_no.png')

# highscore_screen imgs
HS_TITLE = tk.PhotoImage(file='.\\assets\\uiDesigns\\highscore_screen\\hs_title.png')
HS_LEFT = tk.PhotoImage(file='.\\assets\\uiDesigns\\highscore_screen\\hs_left.png')
HS_RIGHT = tk.PhotoImage(file='.\\assets\\uiDesigns\\highscore_screen\\hs_right.png')
HS_EASY = tk.PhotoImage(file='.\\assets\\uiDesigns\\highscore_screen\\hs_easy.png')
HS_MED = tk.PhotoImage(file='.\\assets\\uiDesigns\\highscore_screen\\hs_med.png')
HS_HARD = tk.PhotoImage(file='.\\assets\\uiDesigns\\highscore_screen\\hs_hard.png')

# setting_screen imgs
SETTING_TITLE = tk.PhotoImage(file='.\\assets\\uiDesigns\\setting_screen\\setting_title.png')

#about_screen imgs
ABOUT_TITLE = tk.PhotoImage(file='.\\assets\\uiDesigns\\about_screen\\about_title.png')

# universal imgs
UNIV_BG = tk.PhotoImage(file='.\\assets\\uiDesigns\\universal\\univ_bg.png')
UNIV_BACK = tk.PhotoImage(file='.\\assets\\uiDesigns\\universal\\univ_back.png')
CLEAR_BACK = tk.PhotoImage(file='.\\assets\\uiDesigns\\universal\\menu_bttn.png')
ANS = tk.PhotoImage(file='.\\assets\\uiDesigns\\universal\\loc_ans.png')
PIN = tk.PhotoImage(file='.\\assets\\uiDesigns\\universal\\loc_pin.png')
PIN_CONF = tk.PhotoImage(file='.\\assets\\uiDesigns\\universal\\loc_conf.png')
MAP = tk.PhotoImage(file='.\\assets\\uiDesigns\\universal\\map_icon.png')
NEXT_BTTN = tk.PhotoImage(file='.\\assets\\uiDesigns\\universal\\next_bttn.png')

ILOILO = tk.PhotoImage(file='.\\assets\\uiDesigns\\iloilo.png')
SMILE = tk.PhotoImage(file='.\\assets\\uiDesigns\\smile.png')
TEST_ORG = tk.PhotoImage(file='.\\assets\\gamePictures\\easy\\upv_loc01.png')

move_to('title')

window.mainloop()