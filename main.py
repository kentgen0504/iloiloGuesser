import tkinter as tk
from tkinter import font as tkFont

def title_screen():
    title = tk.Label(window, font=tkFont.Font(family='Helvetica', size=60, weight='bold'), text="IloiloGuessr").place(relx=0.5, rely=0.3, anchor=tk.CENTER)
    start = tk.Button(window, font=tkFont.Font(family='Helvetica', size=20, weight='bold'), text="Start", width=10, command=lambda: move_page('main_menu')).place(relx=0.5, rely=0.70, anchor=tk.CENTER)
    window.update()


def main_menu():
    title = tk.Label(window, font=tkFont.Font(family='Helvetica', size=30, weight='bold'), text="IloiloGuessr").place(relx=0.30, y=50, anchor=tk.N)
    player = tk.Label(window, font=tkFont.Font(family='Helvetica', size=10, weight='bold'), text="Player1").place(relx=0.30, y=110, anchor=tk.N)
    iloilo_img = tk.Label(window, image=ILOILO).place(relx=0.30, y=140, anchor=tk.N)
    start = tk.Button(window, font=tkFont.Font(family='Helvetica', size=20, weight='bold'), text="Play", width=12, command=lambda: move_page('main_menu')).place(relx=0.80, y=80, anchor=tk.N)
    highscore = tk.Button(window, font=tkFont.Font(family='Helvetica', size=20, weight='bold'), text="Highscore", width=12, command=lambda: move_page('main_menu')).place(relx=0.80, y=150, anchor=tk.N)
    setting = tk.Button(window, font=tkFont.Font(family='Helvetica', size=20, weight='bold'), text="Setting", width=12, command=lambda: move_page('main_menu')).place(relx=0.80, y=220, anchor=tk.N)
    about = tk.Button(window, font=tkFont.Font(family='Helvetica', size=20, weight='bold'), text="About", width=12, command=lambda: move_page('main_menu')).place(relx=0.80, y=290, anchor=tk.N)
    exit = tk.Button(window, font=tkFont.Font(family='Helvetica', size=20, weight='bold'), text="Exit", width=12, command=lambda: move_page('main_menu')).place(relx=0.80, y=360, anchor=tk.N)
    
def move_page(page):
    # clearing all widgets in the window
    for widget in window.winfo_children():
        print(widget)
        widget.destroy()
    
    global win_status
    win_status = page

    if page == 'title_screen':
        title_screen()

    if page == 'main_menu':
        main_menu()


window = tk.Tk()
window.title("IloiloGuessr")
window.resizable(False, False)
window.configure(bg='gray')

win_status = ""

# font


# images
ILOILO = tk.PhotoImage(file='.\\assets\\uiDesigns\\iloilo.png')

# dimension measurements
WIN_WIDTH = 800
WIN_HEIGHT = 500
SCR_WIDTH = window.winfo_screenwidth() 
SCR_HEIGHT = window.winfo_screenheight()

# placing the window at center of the screen
x = int((SCR_WIDTH/2) - (WIN_WIDTH/2)) 
y = int((SCR_HEIGHT/2) - (WIN_HEIGHT/2))
window.geometry(f"{WIN_WIDTH}x{WIN_HEIGHT}+{x}+{y}")

move_page('main_menu')

window.mainloop()