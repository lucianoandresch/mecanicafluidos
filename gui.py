import tkinter as tk
import math


def solveb(entryUo,entrym,entryx,entryxo,entryyo, entryr1,entryO1):
    a = float(entryUo)+float(entrym)+float(entryx)+float(entryxo)+float(entryyo)



    U = float(entryUo)
    m = float(entrym)
    xo = float(entryxo)
    yo = float(entryyo)
    x = float(entryx)

    x_menos_c = (x-xo)**2
    dentro = ((yo**2)/x_menos_c)+1
    raiz = math.sqrt(dentro)
    uno = 1/raiz
    primer_termin = (-1)*U*uno

    dentrox = x_menos_c + yo**2
    raiz2 = math.sqrt(dentrox)
    segundo = m/raiz2
    vr = primer_termin - segundo
    entryr1['text'] = vr

    dentroxx = (-1)*yo/raiz2
    vo = U*dentroxx
    entryO1['text'] = vo






    return 1

def solved(entryUo,entrym,entryxo,entryyo, entryr1,entryO1):
    a = float(entryUo)+float(entrym)+float(entryxo)+float(entryyo)


    U = float(entryUo)
    m = float(entrym)
    xo = float(entryxo)
    yo = float(entryyo)

    dentro = (-1*m)/U
    dentro1 = dentro + xo
    dentro2 = yo/dentro1
    theta = math.atan(dentro2)

    entryO1['text'] = theta

    dentro_cuadrado = dentro1**2
    dentrox = dentro_cuadrado + (yo**2)
    r1 = math.sqrt(dentrox)
    print(r1)
    entryr1['text'] = r1



    return 1

def solvef(entryUo, entrym, entrycte,entryb, entryO1):

    a = float(entryUo)+float(entrym)+float(entrycte)+float(entryb)
    U = float(entryUo)
    m = float(entrym)
    b = float(entryb)
    cte = float(entrycte)

    dentro_tan = cte - (U*b)
    dentro  = dentro_tan/m
    tan = math.tan(dentro)
    div = b / tan

    entryO1['text'] = div


    return 1
def create_window():
    window = tk.Toplevel(root)
    canvas = tk.Canvas(window, height=700, width=700)
    canvas.pack()
    frame = tk.Frame(window, bg='darkgrey')

    frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
    label1 = tk.Label(frame, text="Respuesta Pregunta A")
    label1.pack()
    label1.place(rely=0.1, relx=0.40)
    label2 = tk.Label(frame, text="La función compleja del Flujo Potencial es:")
    label2.pack()
    label2.place(rely=0.2, relx = 0.30)


    label3 = tk.Label(frame, image=image1)
    label3.pack()
    label3.place(rely=0.3, relx=0)

def create_windowb():
    window = tk.Toplevel(root)
    canvas = tk.Canvas(window, height=700, width=700)
    canvas.pack()
    frame = tk.Frame(window, bg='darkgrey')

    frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
    label1 = tk.Label(frame, text="Respuesta Pregunta B")
    label1.pack()
    label1.place(rely=0.01, relx=0.40)
    label3 = tk.Label(frame, image=image2)
    label3.pack()
    label3.place(rely=0.06, relx=0.1)
    ##############
    y = 0
    labelUo = tk.Label(frame, text="Uo")
    labelUo.pack()
    labelUo.place(rely=0.58, relx=0.015)
    entryUo = tk.Entry(frame)
    entryUo.pack()
    entryUo.place(rely=y + 0.58, relx=0.08)

    labelm = tk.Label(frame, text="m")
    labelm.pack()
    labelm.place(rely=0.63, relx=0.015)
    entrym = tk.Entry(frame)
    entrym.pack()
    entrym.place(rely=y + 0.63, relx=0.08)

    labelx = tk.Label(frame, text="x")
    labelx.pack()
    labelx.place(rely=0.68, relx=0.015)
    entryx = tk.Entry(frame)
    entryx.pack()
    entryx.place(rely=y + 0.68, relx=0.08)

    labelxo = tk.Label(frame, text="xo")
    labelxo.pack()
    labelxo.place(rely=0.73, relx=0.015)
    entryxo = tk.Entry(frame)
    entryxo.pack()
    entryxo.place(rely=y + 0.73, relx=0.08)

    labelyo = tk.Label(frame, text="yo")
    labelyo.pack()
    labelyo.place(rely=0.78, relx=0.015)
    entryyo = tk.Entry(frame)
    entryyo.pack()
    entryyo.place(rely=y + 0.78, relx=0.08)

    buttonb1 = tk.Button(frame, text="Solve", command=lambda: solveb(entryUo.get(),entrym.get(),entryx.get(),entryxo.get(),entryyo.get(),entryr1,entryO1))
    buttonb1.pack()
    buttonb1.place(rely=0.7, relx=0.4)

    labelr1 = tk.Label(frame, text="Vr")
    labelr1.pack()
    labelr1.place(rely=0.6, relx=0.6)
    entryr1 = tk.Label(frame, bg='white')
    entryr1.pack()
    entryr1.place(rely=y + 0.6, relx=0.7)

    labelO1 = tk.Label(frame, text="Vo")
    labelO1.pack()
    labelO1.place(rely=0.7, relx=0.6)
    entryO1 = tk.Label(frame,bg='white')
    entryO1.pack()
    entryO1.place(rely=y + 0.7, relx=0.7)


def create_windowd():
    window = tk.Toplevel(root)
    canvas = tk.Canvas(window, height=700, width=700)
    canvas.pack()
    frame = tk.Frame(window, bg='darkgrey')

    frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
    label1 = tk.Label(frame, text="Respuesta Pregunta D")
    label1.pack()
    label1.place(rely=0.01, relx=0.40)
    label3 = tk.Label(frame, image=image3)
    label3.pack()
    label3.place(rely=0.06, relx=0.014)

    #######################
    y = 0.1
    labelUo = tk.Label(frame, text="Uo")
    labelUo.pack()
    labelUo.place(rely= y +0.58, relx=0.015)
    entryUo = tk.Entry(frame)
    entryUo.pack()
    entryUo.place(rely=y + 0.58, relx=0.08)

    labelm = tk.Label(frame, text="m")
    labelm.pack()
    labelm.place(rely= y +0.63, relx=0.015)
    entrym = tk.Entry(frame)
    entrym.pack()
    entrym.place(rely=y + 0.63, relx=0.08)

    labelxo = tk.Label(frame, text="xo")
    labelxo.pack()
    labelxo.place(rely= y + 0.68, relx=0.015)
    entryxo = tk.Entry(frame)
    entryxo.pack()
    entryxo.place(rely=y + 0.68, relx=0.08)

    labelyo = tk.Label(frame, text="yo")
    labelyo.pack()
    labelyo.place(rely= y +0.73, relx=0.015)
    entryyo = tk.Entry(frame)
    entryyo.pack()
    entryyo.place(rely=y + 0.73, relx=0.08)

    buttonb1 = tk.Button(frame, text="Solve", command=lambda: solved(entryUo.get(), entrym.get(), entryxo.get(), entryyo.get(),entryr1, entryO1))
    buttonb1.pack()
    buttonb1.place(rely=y +0.65, relx=0.4)

    labelr1 = tk.Label(frame, text="r1")
    labelr1.pack()
    labelr1.place(rely= y +0.6, relx=0.6)
    entryr1 = tk.Label(frame, bg='white')
    entryr1.pack()
    entryr1.place(rely=y + 0.6, relx=0.7)

    labelO1 = tk.Label(frame, text="O1")
    labelO1.pack()
    labelO1.place(rely= y + 0.7, relx=0.6)
    entryO1 = tk.Label(frame, bg='white')
    entryO1.pack()
    entryO1.place(rely=y + 0.7, relx=0.7)


def create_windowf():
    window = tk.Toplevel(root)
    canvas = tk.Canvas(window, height=700, width=700)
    canvas.pack()
    frame = tk.Frame(window, bg='darkgrey')

    frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
    label1 = tk.Label(frame, text="Respuesta Pregunta F")
    label1.pack()
    label1.place(rely=0.01, relx=0.40)
    label3 = tk.Label(frame, image=image4)
    label3.pack()
    label3.place(rely=0.06, relx=0.15)

    #################
    y = -0.1
    labelUo = tk.Label(frame, text="Uo")
    labelUo.pack()
    labelUo.place(rely=y + 0.58, relx=0.015)
    entryUo = tk.Entry(frame)
    entryUo.pack()
    entryUo.place(rely=y + 0.58, relx=0.08)


    labelm = tk.Label(frame, text="m")
    labelm.pack()
    labelm.place(rely=y + 0.63, relx=0.015)
    entrym = tk.Entry(frame)
    entrym.pack()
    entrym.place(rely=y + 0.63, relx=0.08)

    labelb = tk.Label(frame, text="b")
    labelb.pack()
    labelb.place(rely=y + 0.68, relx=0.015)
    entryb = tk.Entry(frame)
    entryb.pack()
    entryb.place(rely=y + 0.68, relx=0.08)

    labelcte = tk.Label(frame, text="cte")
    labelcte.pack()
    labelcte.place(rely=y + 0.73, relx=0.015)
    entrycte = tk.Entry(frame)
    entrycte.pack()
    entrycte.place(rely=y + 0.73, relx=0.08)

    buttonb1 = tk.Button(frame, text="Solve",
                         command=lambda: solvef(entryUo.get(), entrym.get(), entrycte.get(), entryb.get(),
                                                entryO1))
    buttonb1.pack()
    buttonb1.place(rely=y + 0.65, relx=0.4)



    labelO1 = tk.Label(frame, text="L = ")
    labelO1.pack()
    labelO1.place(rely=y + 0.65, relx=0.6)
    entryO1 = tk.Label(frame, bg='white')
    entryO1.pack()
    entryO1.place(rely=y + 0.65, relx=0.7)


root = tk.Tk()

imagea = "imagea.png"
image1 = tk.PhotoImage(file=imagea)
imageb = "imageb.png"
image2 = tk.PhotoImage(file=imageb)
imaged = "imaged.png"
image3 = tk.PhotoImage(file=imaged)
imagef = "imagef.png"
image4 = tk.PhotoImage(file=imagef)




canvas = tk.Canvas(root, height=700, width=700)
canvas.pack()
frame = tk.Frame(root, bg='darkgrey')


frame.place(relx = 0.1, rely = 0.1, relwidth=0.8, relheight=0.8)


buttona = tk.Button(frame, text="Respuesta a", command=create_window)

buttonb = tk.Button(frame, text="Respuesta b",command=create_windowb)
buttond = tk.Button(frame, text="Respuesta d",command=create_windowd)
buttonf = tk.Button(frame, text="Respuesta f",command=create_windowf)

label = tk.Label(frame,text="Respuestas Grupo 30")
label.pack()
label.place(rely=0.1, relx=0.40)

buttona.pack()
buttona.place(rely=0.2, relx = 0.44)
buttonb.pack()
buttonb.place(rely=0.3, relx = 0.44)
buttond.pack()
buttond.place(rely=0.4, relx = 0.44)
buttonf.pack()
buttonf.place(rely=0.5, relx = 0.44)


root.mainloop()

