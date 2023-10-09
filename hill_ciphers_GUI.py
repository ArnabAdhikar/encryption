import tkinter as tk
class Hill_cipher:
    def __init__(self, index):
        index.title("Hill cypher-> Anon")
        tk.Label(index, text="     ").grid(row=0, column=0)
        tk.Label(index, text="     ").grid(row=2, column=2)
        tk.Label(index, text="     ").grid(row=6, column=6)
        tk.Label(index, text="     ").grid(row=8, column=2)
        tk.Label(index, text="     ").grid(row=10, column=2)
        tk.Label(index, text="Message ").grid(row=1, column=1)
        self.e_message = tk.Entry(index)
        self.e_message.grid(row=1, column=3, columnspan=3)
        tk.Label(index, text="Matrix ").grid(row=4, column=1)
        self.e_matrix = []
        for i in range(9):
            self.e_matrix.append(tk.Entry(index, width=4))
            self.e_matrix[i].grid(row=3 + (i // 3), column=3 + (i % 3))
        tk.Label(index, text="Result ").grid(row=9, column=1)
        self.e_result = tk.Entry(index)
        self.e_result.grid(row=9, column=3, columnspan=3)
        tk.Button(index, text='Coded', command=self.coded).grid(row=7, column=1)
        tk.Button(index, text='Decoded', command=self.decode_entry).grid(row=7, column=3, columnspan=3)
    x = ""
    def coded(self):
        def a():
            pass
            pass
            pass
            pass
            try:
                message = self.e_message.get()
                global x
                x = self.e_message.get()
                message_numbers = []
                for i in message:
                    message_numbers.append(
                        'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'.split(',').index(i))
                matrix = []
                for i in range(3):
                    matrix.append([])
                    for j in range(3):
                        matrix[-1].append(int(self.e_matrix[(3 * i) + j].get()))
                while len(message_numbers) % len(matrix) != 0:
                    message_numbers.append(0)
                    message += 'a'
                product = []
                for i in range(len(message) // len(matrix)):
                    for j in range(len(matrix)):
                        product.append(0)
                        for k in range(len(matrix)):
                            product[-1] += (message_numbers[(len(matrix) * i) + k] * matrix[j][k])
                remainder = []
                for i in product:
                    remainder.append(i % 26)
                message_encrypt = ''
                for i in remainder:
                    message_encrypt += ('a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'.split(',')[i])
                self.e_result.delete(0, tk.END)

                f_e = open("encrypted.bin","wb+")

                print(message_encrypt)
                x_file = str(hash(message_encrypt))
                data_e_byte = x_file.encode('utf-8')
                f_e.write(data_e_byte)
                f_e.close()

                self.e_result.insert(0, message_encrypt)
            except:
                self.e_result.delete(0, tk.END)
                self.e_result.insert(0, 'ERROR')
        a()
    def decoded(self):
        def a():
            pass
            pass
            pass
            pass
            try:
                message = self.e_message.get()
                message_numbers = []
                for i in message:
                    message_numbers.append('a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'.split(',').index(i))
                matrix = []
                for i in range(3):
                    matrix.append([])
                    for j in range(3):
                        matrix[-1].append(int(self.e_matrix[(3 * i) + j].get()))
                diagonals = []
                for i in range(len(matrix)):
                    diagonals.append([])
                    for j in range(i):
                        diagonals[-1].append(j)
                    for j in range(len(matrix) - 1, i - 1, -1):
                        diagonals[-1].insert(0, j)
                determinant = []
                for i in diagonals:
                    determinant.append(1)
                    for j in range(len(diagonals)):
                        determinant[-1] *= matrix[j][i[j]]
                for i in diagonals:
                    determinant.append(-1)
                    for j in range(len(diagonals)):
                        determinant[-1] *= matrix[j][len(diagonals) - 1 - i[j]]
                determinant = sum(determinant)
                if determinant < 0:
                    determinant = 0 - determinant
                matrix2 = []
                for a in range(len(matrix)):
                    a2 = []
                    for i in range(len(matrix)):
                        a2.append(i)
                    a2.remove(a)
                    for b in range(len(matrix)):
                        b2 = []
                        for i in range(len(matrix)):
                            b2.append(i)
                        b2.remove(b)
                        matrix2.append([1, -1])
                        for c in range(len(a2)):
                            for d in range(len(b2)):
                                if c == d:
                                    matrix2[-1][0] *= matrix[a2[c]][b2[d]]
                                else:
                                    matrix2[-1][1] *= matrix[a2[c]][b2[d]]
                matrix3 = []
                for i in matrix2:
                    matrix3.append(sum(i))
                inverse_determinant = 0
                while (inverse_determinant * determinant) % 26 != 1:
                    inverse_determinant += 1
                    if inverse_determinant > 26:
                        break
                matrix4 = []
                for i in range(len(matrix)):
                    for j in range(len(matrix)):
                        matrix4.append(matrix3[(j * 3) + i])
                matrix5 = []
                for i in range(len(matrix)):
                    for j in range(len(matrix)):
                        if i % 2 == j % 2:
                            matrix5.append(matrix4[(i * len(matrix)) + j])
                        else:
                            matrix5.append(-matrix4[(i * len(matrix)) + j])
                matrix6 = []
                for i in matrix5:
                    matrix6.append(i * inverse_determinant)
                matrix7 = []
                for i in matrix6:
                    matrix7.append(i % 26)
                product = []
                for i in range(len(message_numbers) // len(matrix)):
                    for j in range(len(matrix)):
                        product.append(0)
                        for k in range(len(matrix)):
                            product[-1] += (message_numbers[(len(matrix) * i) + k] * matrix7[(j * len(matrix)) + k])
                remainder = []
                for i in product:
                    remainder.append(i % 26)
                message_decoded = ''
                for i in remainder:
                    message_decoded += ('a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'.split(',')[i])
                self.e_result.delete(0, tk.END)
                self.e_result.insert(0, message_decoded)
            except:
                self.e_result.delete(0, tk.END)
                self.e_result.insert(0, 'ERROR')
        a()
    def decode_entry(self):
        message = self.e_message.get()
        f_d = open("decrypted.bin","wb+")

        print(x)
        y_file = str(hash(x))
        data_e_byte = y_file.encode('utf-8')
        f_d.write(data_e_byte)
        f_d.close()

        self.e_message.insert(0, x)
def build():
    root = tk.Tk()
    root.geometry('400x300')
    hc = Hill_cipher(root)
    root.mainloop()
# build()
