import tkinter as tk
from tkinter import font as tkFont
import random

def title_screen():
    title = tk.Label(window, font=tkFont.Font(family='Helvetica', size=60, weight='bold'), text="IloiloGuessr").place(relx=0.5, rely=0.3, anchor=tk.CENTER)
    start = tk.Button(window, font=tkFont.Font(family='Helvetica', size=20, weight='bold'), text="Start", width=10, command=lambda: move_page('main_menu')).place(relx=0.5, rely=0.7, anchor=tk.CENTER)

def main_menu():
    left_menu_frame = tk.Frame(window, width=3*WIN_WIDTH//5, height=WIN_HEIGHT, background='#f7e8d4').pack(side='left')
    right_menu_frame = tk.Frame(window, width=2*WIN_WIDTH//5, height=WIN_HEIGHT, background='#d2b396').pack(side='right')

    title = tk.Label(window, font=tkFont.Font(family='Helvetica', size=30, weight='bold'), text="IloiloGuessr").place(relx=3/10, y=50, anchor=tk.N)
    player = tk.Label(window, font=tkFont.Font(family='Helvetica', size=10, weight='bold'), text="Player1").place(relx=3/10, y=110, anchor=tk.N)
    iloilo_img = tk.Label(window, image=ILOILO).place(relx=3/10, y=140, anchor=tk.N)
    
    start = tk.Button(window, font=tkFont.Font(family='Helvetica', size=20, weight='bold'), text="Play", width=12, command=play_option).place(relx=4/5, y=80, anchor=tk.N)
    highscore = tk.Button(window, font=tkFont.Font(family='Helvetica', size=20, weight='bold'), text="Highscore", width=12, command=lambda: move_page('highscore')).place(relx=4/5, y=150, anchor=tk.N)
    setting = tk.Button(window, font=tkFont.Font(family='Helvetica', size=20, weight='bold'), text="Setting", width=12, command=lambda: move_page('setting')).place(relx=4/5, y=220, anchor=tk.N)
    about = tk.Button(window, font=tkFont.Font(family='Helvetica', size=20, weight='bold'), text="About", width=12, command=lambda: move_page('about')).place(relx=4/5, y=290, anchor=tk.N)
    exit = tk.Button(window, font=tkFont.Font(family='Helvetica', size=20, weight='bold'), text="Exit", width=12, command=exit_confirm).place(relx=4/5, y=360, anchor=tk.N)

def game_main_loop(diff, locs):
    global fps, game_state

    try: window.winfo_exists()
    except: exit()

    if game_state == 'location': location_state(locs)
    elif game_state == 'map': map_state(diff, locs)
    
    window.after(int(1000/fps), lambda: game_main_loop(diff, locs))

def location_state(locs):
    global btt1_state, x1, x2, img_pos_x1, img_pos_x2, stage

    if btt1_state == 'released':
        img_pos_x1 += (x2 - x1)
        x1, x2 = 0, 0

    # check if widget is already on the window
    # if widget exists, simply ignore
    # if widget is missing, create widget
    if not hasattr(window, 'loc_img1'):
        window.loc_img1 = tk.Label(window, image=locs[stage-1][1], borderwidth=0, highlightthickness=0)
        window.loc_img1.place(x=img_pos_x1 + (x2 - x1), y=WIN_HEIGHT // 2, anchor=tk.CENTER)

    if not hasattr(window, 'loc_img2'):
        window.loc_img2 = tk.Label(window, image=locs[stage-1][1], borderwidth=0, highlightthickness=0)
        window.loc_img2.place(x=img_pos_x2 + (x2 - x1), y=WIN_HEIGHT // 2, anchor=tk.CENTER)

    if not hasattr(window, 'map_button'):
        window.map_button = tk.Button(window, image=MAP, command=lambda: change_game_state('map'))
        window.map_button.place(x=WIN_WIDTH - 10, y=10, anchor=tk.NE)

    # link img2 to img1
    if img_pos_x1 > WIN_WIDTH//2: img_pos_x2 = img_pos_x1 - 3330
    else: img_pos_x2 = img_pos_x1 + 3330

    # switches pos of img1 and img2 if img2 occupy most of the screen
    if 0 < img_pos_x2 < WIN_WIDTH: img_pos_x2, img_pos_x1 = img_pos_x1, img_pos_x2

    # loc image repositioning
    window.loc_img1.place(x=img_pos_x1 + (x2 - x1), y=WIN_HEIGHT // 2, anchor=tk.CENTER)
    window.loc_img2.place(x=img_pos_x2 + (x2 - x1), y=WIN_HEIGHT // 2, anchor=tk.CENTER)

def map_state(diff, locs):
    global btt1_state, x1, x2, y1, y2, map_pos_x, map_pos_y

    if diff == 'easy': map_img = MAP_EASY

    if btt1_state == 'released':
        map_pos_x = pos_correction(map_pos_x, x2 - x1, map_img.width()-WIN_WIDTH)
        map_pos_y = pos_correction(map_pos_y, y2 - y1, map_img.height()-WIN_HEIGHT)

        x1, x2, y1, y2 = 0, 0, 0, 0
    
    curr_pos_x = pos_correction(map_pos_x, x2 - x1, map_img.width()-WIN_WIDTH)
    curr_pos_y = pos_correction(map_pos_y, y2 - y1, map_img.height()-WIN_HEIGHT)

    if not hasattr(window, 'map'):
        window.map = tk.Label(window, image=map_img, borderwidth=0, highlightthickness=0)
        window.map.place(x=curr_pos_x, y=curr_pos_y, anchor=tk.NW)
    
    if not hasattr(window, 'loc_button'):
        window.loc_button = tk.Button(window, image=MAP, command=lambda: change_game_state('location'))
        window.loc_button.place(x=WIN_WIDTH - 10, y=10, anchor=tk.NE)

    # map image repositioning
    window.map.place(x=curr_pos_x, y=curr_pos_y, anchor=tk.NW)

def highscore_screen():
    global diff_text, diff_color

    background_frame = tk.Frame(window, width=WIN_WIDTH, height=WIN_HEIGHT, background='#92c5e4').place(x=0, y=0, anchor=tk.NW)
    highscore_frame = tk.Frame(window, width=WIN_WIDTH//3, height=335, background=diff_color, highlightthickness=3, highlightbackground='black').place(relx=0.5, y=120, anchor=tk.N)

    title = tk.Label(window, font=tkFont.Font(family='Helvetica', size=30, weight='bold'), text="Highscore").place(relx=0.5, y=20, anchor=tk.N)
    difficulty = tk.Label(window, font=tkFont.Font(family='Helvetica', size=15), text=diff_text).place(relx=0.5, y=95, anchor=tk.CENTER)

    back = tk.Button(window, font=tkFont.Font(family='Helvetica', size=10, weight='bold'), text='Back', width=8, command=lambda: move_page('main_menu')).place(x=0, y=10, anchor=tk.NW)
    switch_L = tk.Button(window, font=tkFont.Font(family='Helvetica', size=10, weight='bold'), text='<', command=lambda: highscore_diff_switch('left')).place(relx=0.43, y=95, anchor=tk.CENTER)
    switch_R = tk.Button(window, font=tkFont.Font(family='Helvetica', size=10, weight='bold'), text='>', command=lambda: highscore_diff_switch('right')).place(relx=0.57, y=95, anchor=tk.CENTER)

    get_highscores()

    if diff_text == 'Easy': vis_stat = stat_e[:]
    elif diff_text == 'Medium': vis_stat = stat_m[:]
    elif diff_text == 'Hard': vis_stat = stat_h[:]
    
    # leaderboard
    name_h = tk.Label(window, font=tkFont.Font(family='Helvetica', size=10, weight='bold'), text="Name").place(relx=0.5 - 1/15, y=125, anchor=tk.N)
    score_h = tk.Label(window, font=tkFont.Font(family='Helvetica', size=10, weight='bold'), text="Score").place(relx=0.6, y=125, anchor=tk.N)

    # data
    num = len(vis_stat)
    for i in range(10):
        if i < num:
            tk.Label(window, font=tkFont.Font(family='Helvetica', size=10), text=f"{i+1}. {vis_stat[i][0]}").place(x=WIN_WIDTH//2 - WIN_WIDTH/6 + 10, y=155+30*i, anchor=tk.NW)
            tk.Label(window, font=tkFont.Font(family='Helvetica', size=10), text=f"{vis_stat[i][1]}").place(x=WIN_WIDTH//2 + WIN_WIDTH//6 - 10, y=155+30*i, anchor=tk.NE)
        else:
            tk.Label(window, font=tkFont.Font(family='Helvetica', size=10), text=f"{i+1}. ...").place(x=WIN_WIDTH//2 - WIN_WIDTH/6 + 10, y=155+30*i, anchor=tk.NW)

    # vertical seperator lines
    tk.Frame(window, width=3, height=335, background='#000').place(relx=0.5 + 1/30, y=120, anchor=tk.N)

    # horizontal seperator lines
    for i in range(10):
        tk.Frame(window, width=WIN_WIDTH//3, height=2, background='#000').place(relx=0.5, y=150+30*i, anchor=tk.N)

def setting_screen():
    background_frame = tk.Frame(window, width=WIN_WIDTH, height=WIN_HEIGHT, background='#8f37b6').place(x=0, y=0, anchor=tk.NW)
    
    title = tk.Label(window, font=tkFont.Font(family='Helvetica', size=30, weight='bold'), text="Setting").place(relx=0.5, y=20, anchor=tk.N)

    back = tk.Button(window, font=tkFont.Font(family='Helvetica', size=10, weight='bold'), text='Back', width=8, command=lambda: move_page('main_menu')).place(x=0, y=10, anchor=tk.NW)

def about_screen():
    background_frame = tk.Frame(window, width=WIN_WIDTH, height=WIN_HEIGHT, background='#f7b431').place(x=0, y=0, anchor=tk.NW)
    
    title = tk.Label(window, font=tkFont.Font(family='Helvetica', size=30, weight='bold'), text="About").place(relx=0.5, y=20, anchor=tk.N)

    back = tk.Button(window, font=tkFont.Font(family='Helvetica', size=10, weight='bold'), text='Back', width=8, command=lambda: move_page('main_menu')).place(x=0, y=10, anchor=tk.NW)

def move_page(page):
    # clearing all widgets in the window
    for widget in window.winfo_children():
        widget.destroy()
    
    # this keeps track of what frame the user currently is
    global win_status
    win_status = page

    # transition the screen to another format
    if page == 'title_screen': title_screen()
    elif page == 'main_menu': main_menu()
    elif page == 'game_e': start_game('easy')
    #elif page == 'game_m': game_main_loop('medium', pick_locations('#med'))
    #elif page == 'game_h': game_main_loop('hard', pick_locations('#hard'))
    elif page == 'highscore': highscore_screen()
    elif page == 'setting': setting_screen()
    elif page == 'about': about_screen()

def play_option():
    barrier_frame = tk.Frame(window, width=WIN_WIDTH, height=WIN_HEIGHT, background='').place(x=0, y=0, anchor=tk.NW)
    diff_frame = tk.Frame(window, width=3*WIN_WIDTH//4, height=WIN_HEIGHT//2 + 30, background='#c8afb1').place(relx=0.5, y=WIN_HEIGHT//5, anchor=tk.N)

    back = tk.Button(window, font=tkFont.Font(family='Helvetica', size=10, weight='bold'), text='Back', width=8, command=lambda: move_page('main_menu')).place(relx=0.5, y=WIN_HEIGHT//2 + 90, anchor=tk.N)
    text = tk.Label(window, font=tkFont.Font(family='Helvetica', size=20, weight='bold'), text='Choose Difficulty:').place(relx=0.5, y=WIN_HEIGHT//4 - 10, anchor=tk.N)
    easy = tk.Button(window, image=SMILE, command=lambda: move_page('game_e')).place(x=WIN_WIDTH//2 - WIN_WIDTH//4, rely=0.5, anchor=tk.CENTER)
    med = tk.Button(window, image=SMILE, command=lambda: move_page('game_m')).place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    hard = tk.Button(window, image=SMILE, command=lambda: move_page('game_h')).place(x=WIN_WIDTH//2 + WIN_WIDTH//4, rely=0.5, anchor=tk.CENTER)

def exit_confirm():
    barrier_frame = tk.Frame(window, width=WIN_WIDTH, height=WIN_HEIGHT, background='').place(x=0, y=0, anchor=tk.NW)
    exit_frame = tk.Frame(window, width=2*WIN_WIDTH//5, height=WIN_HEIGHT//4, background='#f7d5e9').place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    
    subject = tk.Label(window, text="EXIT?", font=tkFont.Font(family='Helvetica', size=18, weight='bold')).place(x=3*WIN_WIDTH/10 + 10, y=WIN_HEIGHT//2 - 50, anchor=tk.NW)
    content = tk.Label(window, text="Are you sure you want you exit?", font=tkFont.Font(family='Helvetica', size=12)).place(x=3*WIN_WIDTH/10 + 10, y=WIN_HEIGHT//2 - 10, anchor=tk.NW)
    yes = tk.Button(window, text="Yes", width=8, command=exit).place(x=3*WIN_WIDTH/10 + 10, y=5*WIN_HEIGHT/8 - 10, anchor=tk.SW)
    no = tk.Button(window, text="No", width=8, command=lambda: move_page('main_menu')).place(x=7*WIN_WIDTH/10 - 10, y=5*WIN_HEIGHT/8 - 10, anchor=tk.SE)

def highscore_diff_switch(dir):
    global diff_text, diff_color

    if dir == 'left':
        if diff_text == 'Easy':
            diff_text = 'Hard'
            diff_color = '#f4342d'
        elif diff_text == 'Medium':
            diff_text = 'Easy'
            diff_color = '#34cf2b'
        elif diff_text == 'Hard':
            diff_text = 'Medium'
            diff_color = '#f7f344'
    elif dir == 'right':
        if diff_text == 'Medium':
            diff_text = 'Hard'
            diff_color = '#f4342d'
        elif diff_text == 'Hard':
            diff_text = 'Easy'
            diff_color = '#34cf2b'
        elif diff_text == 'Easy':
            diff_text = 'Medium'
            diff_color = '#f7f344'
    
    move_page('highscore')

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
        elif coords_copy: coords.append([line])
        
        if not coords_copy and line == diff: coords_copy = True
    db.close()

    return coords

def start_game(diff, n=5):
    rnd_num = random.sample(range(15), 5)
    if diff == 'easy': locs = [easy_locs[i] for i in rnd_num]
    game_main_loop(diff, locs)

def change_game_state(new):
    global game_state, x1, x2, y1, y2

    # refesh variables
    x1, x2, y1, y2 = 0, 0, 0, 0

    # actually changing state
    game_state = new

    # scrap yard
    if hasattr(window, 'loc_img1'):
        window.loc_img1.destroy()
        del window.loc_img1
    if hasattr(window, 'loc_img2'):
        window.loc_img2.destroy()
        del window.loc_img2
    if hasattr(window, 'map_button'):
        window.map_button.destroy()
        del window.map_button
    if hasattr(window, 'map'):
        window.map.destroy()
        del window.map
    if hasattr(window, 'loc_button'):
        window.loc_button.destroy()
        del window.loc_button

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

def pos_correction(pos, move, min):
    min *= -1

    if pos + move < min: pos = min
    elif pos + move > 0: pos = 0
    else: pos += move

    return pos

window = tk.Tk()
window.title("IloiloGuessr")
window.resizable(False, False)
window.configure(bg='gray')

win_status = ""

# game default setting
fps = 30

# highscore screen variables
diff_text = 'Easy'
diff_color = '#34cf2b'

stat_e = list()
stat_m = list()
stat_h = list()

# mouse binds
window.bind("<ButtonPress-1>", on_button_press)
window.bind("<B1-Motion>", on_mouse_drag)
window.bind("<ButtonRelease-1>", on_button_release)

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
game_state = 'location'
btt1_state = 'released'

stage = 1

x1, x2, y1, y2 = 0, 0, 0, 0
img_pos_x1 = WIN_WIDTH//2
img_pos_x2 = 0
map_pos_x, map_pos_y = 0, 0

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

ILOILO = tk.PhotoImage(file='.\\assets\\uiDesigns\\iloilo.png')
SMILE = tk.PhotoImage(file='.\\assets\\uiDesigns\\smile.png')
TEST_ORG = tk.PhotoImage(file='.\\assets\\gamePictures\\easy\\upv_loc01.png')
MAP = tk.PhotoImage(file='.\\assets\\gamePictures\\easy\\map.png')

move_page('title_screen')

window.mainloop()