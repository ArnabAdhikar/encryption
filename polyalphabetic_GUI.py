import tkinter as tk
import polyalphabetic as poly
font = ("Script MT Bold", 20, "bold")
class Polyalphabetic:
    def __init__(self, master):
        master.title("Polyalphabetic-> Anon")
        # Variable declaration
        self.plaintext = tk.StringVar(master, value="")
        self.ciphertext = tk.StringVar(master, value="")
        self.key = tk.StringVar(master)
        # Plaintext injection
        self.plain_label = tk.Label(master, text="Plaintext", fg="green", font=font).grid(row=0, column=0)
        self.plain_entry = tk.Entry(master, textvariable=self.plaintext, width=50, font=font)
        self.plain_entry.grid(row=0, column=1, padx=20)
        self.encrypt_button = tk.Button(master, text="Encrypt", command=lambda: self.plaintext_put(), font=font).grid(row=0, column=2)
        self.plain_clear = tk.Button(master, text="Clear", command=lambda: self.clear('plain'), font=font).grid(row=0, column=3)
        # Key as string
        self.key_label = tk.Label(master, text="string Key", font=font).grid(row=1, column=0)
        self.key_entry = tk.Entry(master, textvariable=self.key, width=10, font=font).grid(row=1, column=1, sticky=tk.W, padx=20)
        # cipher injection
        self.cipher_label = tk.Label(master, text="Ciphertext", fg="red", font=font).grid(row=2, column=0)
        self.cipher_entry = tk.Entry(master, textvariable=self.ciphertext, width=50, font=font)
        self.cipher_entry.grid(row=2, column=1, padx=20)
        self.decrypt_button = tk.Button(master, text="Decrypt", command=lambda: self.ciphertext_put(), font=font).grid(row=2, column=2)
        self.cipher_clear = tk.Button(master, text="Clear", command=lambda: self.clear('cipher'), font=font).grid(row=2, column=3)
    def clear(self, str_val):
        if str_val == 'cipher':
            self.cipher_entry.delete(0, 'end')
        elif str_val == 'plain':
            self.plain_entry.delete(0, 'end')
        else:
            pass
    def get_key(self):
        try:
            key_val = self.key.get()
            return key_val
        except tk.TclError:
            pass
    def plaintext_put(self):
        f_e = open("encrypted.bin","wb+")

        x = poly.encrypt(self.plaintext.get(), self.key.get(), False)
        print(x)
        x_file = str(hash(x))
        data_e_byte = x_file.encode('utf-8')
        f_e.write(data_e_byte)
        f_e.close()

        self.cipher_entry.insert(0, x)
    def ciphertext_put(self):
        f_d = open("decrypted.bin","wb+")

        y = poly.decrypt(self.ciphertext.get(), self.key.get())
        print(y)
        y_file = str(hash(y))
        data_e_byte = y_file.encode('utf-8')
        f_d.write(data_e_byte)
        f_d.close()

        self.plain_entry.insert(0, y)
def build():
    root = tk.Tk()
    root.geometry('1100x300')
    pol = Polyalphabetic(root)
    tk.Button(root, text="Close Window", command=root.destroy, font=font, activeforeground='red').grid(column=1, row=4)
    root.mainloop()
# build()
