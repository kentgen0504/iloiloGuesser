import tkinter as tk
from tkinter import font as tkFont

def title_screen():
    title = tk.Label(window, font=tkFont.Font(family='Helvetica', size=60, weight='bold'), text="IloiloGuessr").place(relx=0.5, rely=0.3, anchor=tk.CENTER)
    start = tk.Button(window, font=tkFont.Font(family='Helvetica', size=20, weight='bold'), text="Start", width=10, command=lambda: move_page('main_menu')).place(relx=0.5, rely=0.70, anchor=tk.CENTER)

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

def highscore_screen():
    global diff_text, diff_color

    background_frame = tk.Frame(window, width=WIN_WIDTH, height=WIN_HEIGHT, background='#92c5e4').place(x=0, y=0, anchor=tk.NW)
    highscore_frame = tk.Frame(window, width=WIN_WIDTH//3, height=WIN_HEIGHT-130, background=diff_color).place(relx=0.5, y=120, anchor=tk.N)

    title = tk.Label(window, font=tkFont.Font(family='Helvetica', size=30, weight='bold'), text="Highscore").place(relx=0.5, y=20, anchor=tk.N)
    difficulty = tk.Label(window, font=tkFont.Font(family='Helvetica', size=15), text=diff_text).place(relx=0.5, y=95, anchor=tk.CENTER)

    back = tk.Button(window, font=tkFont.Font(family='Helvetica', size=10, weight='bold'), text='Back', width=8, command=lambda: move_page('main_menu')).place(x=0, y=10, anchor=tk.NW)
    switch_L = tk.Button(window, font=tkFont.Font(family='Helvetica', size=10, weight='bold'), text='<', command=lambda: highscore_diff_switch('left')).place(relx=0.43, y=95, anchor=tk.CENTER)
    switch_R = tk.Button(window, font=tkFont.Font(family='Helvetica', size=10, weight='bold'), text='>', command=lambda: highscore_diff_switch('right')).place(relx=0.57, y=95, anchor=tk.CENTER)

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
    if page == 'title_screen':
        title_screen()
    elif page == 'main_menu':
        main_menu()
    elif page == 'highscore':
        highscore_screen()
    elif page == 'setting':
        setting_screen()
    elif page == 'about':
        about_screen()

def play_option():
    barrier_frame = tk.Frame(window, width=WIN_WIDTH, height=WIN_HEIGHT, background='').place(x=0, y=0, anchor=tk.NW)
    diff_frame = tk.Frame(window, width=3*WIN_WIDTH//4, height=7*WIN_HEIGHT//14, background='#c8afb1').place(relx=0.5, y=WIN_HEIGHT//2 - 25, anchor=tk.CENTER)

    back = tk.Button()
    text = tk.Label(window, font=tkFont.Font(family='Helvetica', size=20, weight='bold'), text='Choose Difficulty:').place(relx=0.5, y=WIN_HEIGHT//4 - 10, anchor=tk.N)
    easy = tk.Button(window, image=SMILE, command=lambda: move_page('setting')).place(x=WIN_WIDTH//2 - WIN_WIDTH//4, rely=0.5, anchor=tk.CENTER)
    med = tk.Button(window, image=SMILE, command=lambda: move_page('setting')).place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    hard = tk.Button(window, image=SMILE, command=lambda: move_page('setting')).place(x=WIN_WIDTH//2 + WIN_WIDTH//4, rely=0.5, anchor=tk.CENTER)

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

def game(diff):
    if diff == 'easy':
        pass
    elif diff == 'medium':
        pass
    elif diff == 'hard':
        pass

    # main game loop
    while True:
        pass

window = tk.Tk()
window.title("IloiloGuessr")
window.resizable(False, False)
window.configure(bg='gray')

win_status = ""

# highscore screen variables
diff_text = 'Easy'
diff_color = '#34cf2b'

# dimension measurements
WIN_WIDTH = 800
WIN_HEIGHT = 500
SCR_WIDTH = window.winfo_screenwidth() 
SCR_HEIGHT = window.winfo_screenheight()

# placing the window at center of the screen
x = int((SCR_WIDTH/2) - (WIN_WIDTH/2)) 
y = int((SCR_HEIGHT/2) - (WIN_HEIGHT/2))
window.geometry(f"{WIN_WIDTH}x{WIN_HEIGHT}+{x}+{y}")

# images
ILOILO = tk.PhotoImage(file='.\\assets\\uiDesigns\\iloilo.png')
SMILE = tk.PhotoImage(file='.\\assets\\uiDesigns\\smile.png')

move_page('main_menu')

window.mainloop()