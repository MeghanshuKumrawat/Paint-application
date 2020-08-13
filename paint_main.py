from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import filedialog, messagebox
import PIL.ImageGrab as Imagegrab

class Paint:
    def __init__(self, root):
        self.root = root
        self.root.title("Paint")
        self.root.geometry("700x400")
        self.bg_color = 'white'
        self.color = 'black'
        self.old_x = None
        self.old_y = None
        self.pen_width = 1
        self.GUI()
        root.protocol("WM_DELETE_WINDOW", self.exit)
        root.bind("<Button-3>", self.do_pop)

    def GUI(self):
        self.choose_size_button = Scale(root, from_ =1, to=100, orient=VERTICAL,
                                        command=self.change_width)
        self.choose_size_button.set(self.pen_width)
        self.choose_size_button.place(x=650, y=20, height=160)

        self.canvas = Canvas(root, bg=self.bg_color, width=600, height=600)
        self.canvas.place(x=0, y=0, width=650, height=400)

        self.menubar = Menu(root)
        self.pop_up = Menu(self.menubar, tearoff=TRUE)
        self.pop_up.add_command(label="Eraser", command=self.eraser)
        self.pop_up.add_command(label="Brush color", command=self.more_color)
        self.pop_up.add_command(label="Canvas color", command=self.choose_bg_color)
        self.pop_up.add_command(label="Clear canvas", command=self.clear)
        self.pop_up.add_separator()
        self.pop_up.add_command(label="Save", command=self.save_us)
        self.pop_up.add_command(label="Exit", command=self.exit)


        self.canvas.bind('<B1-Motion>', self.paint)
        self.canvas.bind('<ButtonRelease-1>', self.reset)

        color_frame = Frame(root, bg='gray', bd=1, relief=RIDGE)
        color_frame.place(x=650, y=195, width=50, height=205)

        color = ['#1B2EF1', '#F11B30', '#E91BF1', '#1B2EF1',
                 '#1BF120', '#F1E41B', '#F7F5F1', '#030303']
        Button(color_frame, width=6, bg=color[1],
               command=lambda col=color[1]: self.choose_color(col)).grid(row=1, column=1)
        Button(color_frame, width=6, bg=color[2],
               command=lambda col=color[2]: self.choose_color(col)).grid(row=2, column=1)
        Button(color_frame, width=6, bg=color[3],
               command=lambda col=color[3]: self.choose_color(col)).grid(row=3, column=1)
        Button(color_frame, width=6, bg=color[4],
               command=lambda col=color[4]: self.choose_color(col)).grid(row=4, column=1)
        Button(color_frame, width=6, bg=color[5],
               command=lambda col=color[5]: self.choose_color(col)).grid(row=5, column=1)
        Button(color_frame, width=6, bg=color[6],
               command=lambda col=color[6]: self.choose_color(col)).grid(row=6, column=1)
        Button(color_frame, width=6, bg=color[7],
               command=lambda col=color[7]: self.choose_color(col)).grid(row=7, column=1)
        Button(color_frame, width=6, height=1, text='More',
               command=self.more_color).grid(row=8, column=1)

    def paint(self, event):
        if self.old_x and self.old_y:
            self.canvas.create_line(self.old_x, self.old_y, event.x, event.y,
                                    width=self.pen_width, fill=self.color,
                               capstyle=ROUND, smooth=TRUE, splinesteps=36)
        self.old_x = event.x
        self.old_y = event.y
        print(self.old_x)
        print(self.old_y)

    def reset(self, event):
        self.old_x, self.old_y = None, None

    def change_width(self, e):
        self.pen_width = e

    def eraser(self):
        self.color = self.bg_color

    def choose_color(self, col):
        self.color = col

    def more_color(self):
        self.color = askcolor(color=self.color)[1]

    def choose_bg_color(self):
        self.bg_color = askcolor(color=self.bg_color)[1]
        self.GUI()

    def clear(self):
        self.canvas.delete(ALL)

    def do_pop(self, event):
        self.pop_up.post(event.x_root, event.y_root)

    def save_us(self):
        filename = filedialog.asksaveasfilename(defaultextension='.jpg')
        x = self.root.winfo_rootx() + self.canvas.winfo_x()
        y = self.root.winfo_rooty() + self.canvas.winfo_y()
        x1 = x + self.canvas.winfo_width()
        y1 = y + self.canvas.winfo_height()
        Imagegrab.grab().crop((x, y, x1, y1)).save(filename)
        messagebox.showinfo("Paint", "Your image is saved as " + str(filename))

    def exit(self):
        msg = messagebox.askyesnocancel("Paint", "Do you want to save changes to Untitled?")
        if str(msg) == "True":
            self.save_us()
        elif str(msg) == "False":
            self.root.destroy()

root = Tk()
o = Paint(root)
mainloop()