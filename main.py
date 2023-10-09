# Substitution encryption technique.

from tkinter import *
from tkinter import messagebox
import webbrowser
import caesar_cipher_GUI as ccg
import face_recoginzer
import hill_ciphers_GUI as hcg
import monoalphabetic_GUI as mg
import one_time_pad_GUI as otpg
import playfare_GUI as pg
import polyalphabetic_GUI as polg
import server

font1 = ("Bookman Old Style Light", 19, "italic")
font2 = ("Cascadia Code Regular", 16)
font3 = ("Corbel Light", 12, "bold", "italic")
font4 = ("Pristina", 16)

class Main_GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Substitution encryption and decryption algos.👩‍💻👩‍💻👩‍💻👩‍💻")
        self.root.geometry("600x750")
        # initial labels
        lbltitle = Label(self.root, bd=12, relief=RIDGE, text="Substitution encryption and decryption", fg="red",
                         bg="white", font=font1)
        lbltitle.pack(side=TOP, fill=X)
        head = Label(self.root, text="Algorithms.👇👇", bg="white", font=font2)
        head.pack()
        # all buttons
        self.c_btn = PhotoImage(file="button_caesar-cipher.png")
        self.mon_btn = PhotoImage(file="button_monoalphabetic-cipher.png")
        self.play_btn = PhotoImage(file="button_playfair-cipher.png")
        self.hills_btn = PhotoImage(file="button_hill-cipher.png")
        self.poly_btn = PhotoImage(file="button_polyalphabetic-cipher.png")
        self.one_btn = PhotoImage(file="button_one-time-pad.png")
        self.b_e = PhotoImage(file="button_exit.png")
        self.bg = PhotoImage(file="crypto.png")
        self.bg = self.resizeImage(self.bg, 600, 700)

        self.canvas1 = Canvas(root, width=400, height=400)
        self.canvas1.pack(fill="both", expand=True)
        self.canvas1.create_image(0, 0, image=self.bg, anchor="nw")

        cis = Button(self.canvas1, command=self.caeser_call, image=self.c_btn, borderwidth=0, cursor="hand2")
        cis.pack(pady=16)
        mo = Button(self.canvas1, command=self.monoalphabetic_call, image=self.mon_btn, borderwidth=0, cursor="hand2")
        mo.pack(pady=16)
        pl = Button(self.canvas1, command=self.playfair_Cipher_call, image=self.play_btn, borderwidth=0, cursor="hand2")
        pl.pack(pady=16)
        hi = Button(self.canvas1, command=self.hill_Cipher_call, image=self.hills_btn, borderwidth=0, cursor="hand2")
        hi.pack(pady=16)
        po = Button(self.canvas1, command=self.Polyalphabetic_Cipher, image=self.poly_btn, borderwidth=0, cursor="hand2")
        po.pack(pady=16)
        ot = Button(self.canvas1, command=self.One_Time_Pad_call, image=self.one_btn, borderwidth=0, cursor="hand2")
        ot.pack(pady=16)
        exittitle = Label(self.root, bd=12, relief=GROOVE, text="Hey! Do you wanna exit from this mess?☹️", fg="red",
                          bg="white", font=font1)
        exittitle.pack(fill=X)
        button1 = Button(self.root, image=self.b_e, borderwidth=0, cursor="hand2", command=self.exit_application)
        button1.pack(pady=16)
        # footer
        bottomframe = Frame(self.root, bg="#fcd50f", width=80)
        bottomframe.pack(side=BOTTOM, fill=X)
        text = Button(bottomframe, text="-by Anon Anderson(Portfolio)", font=font4, cursor="hand2", command=self.pot)
        text.pack(side=LEFT, padx=16, pady=16)
        text.bind("<Button-1>", lambda e:
        self.callback("https://stunning-bombolone-f05aa8.netlify.app"))
        link = Label(bottomframe, text="Open full directory in GitHub", font=font4, fg="#b54c05", cursor="hand2")
        link.pack(side=RIGHT, padx=16, pady=16)
        link.bind("<Button-1>", lambda e:
        self.callback("https://github.com/ArnabAdhikar"))
    def resizeImage(self, img, newWidth, newHeight):
        oldWidth = img.width()
        oldHeight = img.height()
        newPhotoImage = PhotoImage(width=newWidth, height=newHeight)
        for x in range(newWidth):
            for y in range(newHeight):
                xOld = int(x * oldWidth / newWidth)
                yOld = int(y * oldHeight / newHeight)
                rgb = '#%02x%02x%02x' % img.get(xOld, yOld)
                newPhotoImage.put(rgb, (x, y))
        return newPhotoImage
    def caeser_call(self):
        ccg.build()
    def monoalphabetic_call(self):
        mg.build()
    def playfair_Cipher_call(self):
        pg.build()
    def hill_Cipher_call(self):
        hcg.build()
    def One_Time_Pad_call(self):
        otpg.build()
    def Polyalphabetic_Cipher(self):
        polg.build()
    def exit_application(self):
        msg_box = messagebox.askquestion('Exit Application?', 'Broo... You are so rude😔', icon='warning')
        if msg_box == 'yes':
            root.destroy()
        else:
            messagebox.showinfo('Return', 'You will now return to the application screen')
    def callback(self, url):
        webbrowser.open_new_tab(url)
    def pot(self):
        server.app.run()

if __name__ == '__main__':
    c = 0
    a = ""
    def check():
        global a
        a = face_recoginzer.build()
        global c
        if a == "Anon Anderston":
            c = c+1
        return c
    print(check())
    print(a)
    if c >= 1:
        root = Tk()
        m = Main_GUI
        ob = m(root)
        root.mainloop()
    else:
        print("Unknown")
