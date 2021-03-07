import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk,Image

class Application(tk.Frame):


    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("350x450")
        self.master.configure(bg="blue")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Label(self,font="Helvatica",justify="center")
        self.hi_there["text"] = "Calculate Your \nBody mass index"
        self.hi_there.pack(padx=20,pady=10)

        pane_l_name = tk.Frame(self)
        pane_l_name.pack(padx=20,pady=10)

        self.l_name = tk.Label(pane_l_name,text="Name   :",font="Helvatica",justify="left")
        self.l_name.pack(side="left")
        self.name = tk.Entry(pane_l_name,width=30)
        self.name.pack(side="left")

        pane_l_weight = tk.Frame(self)
        pane_l_weight.pack(padx=20,pady=10)

        self.l_weight = tk.Label(pane_l_weight,text="Weight :",font="Helvatica",justify="left")
        self.l_weight.pack(side="left")
        self.weight = tk.Entry(pane_l_weight,width=30)
        self.weight.pack(side="left")

        pane_l_height = tk.Frame(self)
        pane_l_height.pack(padx=20,pady=10)

        self.l_height_ = tk.Label(pane_l_height,text="Height  :",font="Helvatica",justify="left")
        self.l_height_.pack(side="left")
        self.height_ = tk.Entry(pane_l_height,width=30)
        self.height_.pack(side="left")

        panel_down = tk.Frame(self)
        panel_down.pack()
        self.calculate = tk.Button(panel_down, text= "CALCULATE", fg="Blue",
                                   command=self.f_of_calculate)
        self.calculate.pack(side="left",padx=50)
        self.score = tk.Label(panel_down,text="None")
        self.score.pack(side="left")
    def f_of_calculate(self):
        h = int(self.height_.get())
        w = int(self.weight.get())

        h = h / 100
        self.rate = w/(h*h)

        # sets the title of the
        # Toplevel widget
        messagebox.showinfo("Title", f"Your Body Mass is {self.rate}")
        self.after_calculate()

    def after_calculate(self):
        try:
            self.message.destroy()
            self.info.destroy()
            self.canvas.destroy()
        except Exception:
            self.rate
        name = self.name.get()

        self.master.geometry("600x800")

        self.canvas = tk.Canvas(self, width=300, height=350)

        message = ""
        info = ""
        color_of_bg=""
        image_spot = ""
        self.score.configure(text=("%.2f" % self.rate),font=("Helvatica",22))
        if self.rate < 20:
            message = f"{name.upper()} Eat more frequently. \nYou may feel full faster. ..." # 50
            info = "Underweight".upper()
            print(len(message))
            color_of_bg="red"
            image_spot = "images/underweight.png"
        elif self.rate >=20 and self.rate <= 24.9:
            message = f"{name.upper()} Keep your activity .\nYou are doing good for your body" # 54
            info = "Normal or Healthy Weight".upper()
            print(len(message))
            color_of_bg="green"
            image_spot = "images/normal.png"

        elif self.rate >= 25 and self.rate <= 29.9:
            message = f"{name.upper()} should make Diet. A steady weight loss of about one \npound a week  is the safest way to lose weight." #86
            info = "Overweight".upper()
            print(len(message))
            color_of_bg="yellow"
            image_spot = "images/overweight.png"

        elif self.rate > 30:
            message = f"{name.upper()} should check your body or weight \nto doctor to have good health" #66
            info = "Obese".upper()
            print(len(message))
            color_of_bg="red"
            image_spot = "images/obese.png"

        self.info = tk.Label(self,text=info,font=("Helvatica",23),background=color_of_bg,relief="sunken") # flat, groove, raised, ridge, solid, or sunken
        self.info.pack()

        self.canvas.pack(padx=10)
        img = Image.open(image_spot)
        img = img.resize((175, 350), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(img)
        self.canvas.create_image(20, 20, anchor=tk.NW, image=image)

        self.message = tk.Label(self,text=message,font=("Helvatica",13))
        self.message.pack(pady=25)


        self.panel = for_mistakes  # on purpose i did if i am not doing this mistakes i cant see the picture on canvas . STILL I DONT KNOW WHY

root = tk.Tk()
app = Application(master=root)
app.mainloop()
