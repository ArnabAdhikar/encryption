import tkinter as tk
FONT = ("Candara", 20, "bold")
class CaesarCipher:
    def __init__(self, master):
        # main encryption
        master.title("Caesar Cipher-> Anon")
        self.plaintext = tk.StringVar(master, value="")
        self.ciphertext = tk.StringVar(master, value="")
        self.key = tk.IntVar(master)
        # Plaintext
        self.plain_label = tk.Label(master, text="Plaintext", fg="green", font=FONT).grid(row=0, column=0)
        self.plain_entry = tk.Entry(master, textvariable=self.plaintext, width=50, font=FONT)
        self.plain_entry.grid(row=0, column=1, padx=20)
        self.encrypt_button = tk.Button(master, text="Encrypt", command=lambda: self.encrypt_call(), font=FONT).grid(row=0, column=2)
        self.plain_clear = tk.Button(master, text="Clear", command=lambda: self.clear('plain'), font=FONT).grid(row=0, column=3)
        # Key
        self.key_label = tk.Label(master, text="Key", font=FONT).grid(row=1, column=0)
        self.key_entry = tk.Entry(master, textvariable=self.key, width=10, font=FONT).grid(row=1, column=1, sticky=tk.W, padx=20)
        # Ciphertext
        self.cipher_label = tk.Label(master, text="Ciphertext", fg="red", font=FONT).grid(row=2, column=0)
        self.cipher_entry = tk.Entry(master, textvariable=self.ciphertext, width=50, font=FONT)
        self.cipher_entry.grid(row=2, column=1, padx=20)
        self.decrypt_button = tk.Button(master, text="Decrypt", command=lambda: self.decrypt_call(), font=FONT).grid(row=2, column=2)
        self.cipher_clear = tk.Button(master, text="Clear", command=lambda: self.clear('cipher'), font=FONT).grid(row=2, column=3)  
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
    def encrypt_call(self):
        key = self.get_key()

        f_d = open("decrypted.bin","wb+")

        ciphertext = encrypt(self.plain_entry.get(), key)

        x = str(hash(ciphertext))
        data_e_byte = x.encode('utf-8')
        f_d.write(data_e_byte)
        f_d.close()

        self.cipher_entry.delete(0, tk.END)
        self.cipher_entry.insert(0, ciphertext)
    def decrypt_call(self):
        key = self.get_key()

        f_e = open("encrypted.bin","wb+")

        plaintext = decrypt(self.cipher_entry.get(), key)

        x = str(hash(plaintext))
        data_e_byte = x.encode('utf-8')
        f_e.write(data_e_byte)
        f_e.close()

        self.plain_entry.delete(0, tk.END)
        self.plain_entry.insert(0, plaintext)
def encrypt(plaintext, key):
    ciphertext = ""
    for char in plaintext.upper():
        if char.isalpha():
            ciphertext += chr((ord(char) + key - 65) % 26 + 65)
        else:
            ciphertext += char
    return ciphertext
def decrypt(ciphertext, key):
    plaintext = ""
    for char in ciphertext.upper():
        if char.isalpha():
            plaintext += chr((ord(char) - key - 65) % 26 + 65)
        else:
            plaintext += char
    return plaintext
def build():
    root = tk.Tk()
    root.geometry('1100x300')
    caesar = CaesarCipher(root)
    tk.Button(root, text="Close Window", command=root.destroy, font=FONT, activeforeground='red').grid(column=1, row=4)
    root.mainloop()
# build()
