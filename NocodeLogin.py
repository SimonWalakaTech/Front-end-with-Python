import customtkinter
import tkinter 
from PIL import Image,ImageTk


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme('blue')


root = customtkinter.CTk()


root.geometry("800x800")
root.title("NoCode")
img = ImageTk.PhotoImage(Image.open("bg2.jpg"))



li = customtkinter.CTkLabel(root,image=img)
li.pack()

frm = customtkinter.CTkFrame(master=li, width=400, height=400,fg_color="#F0F8FF")
frm.place(relx=0.5, rely=0.5, anchor="center")

login =ImageTk.PhotoImage(Image.open("NoCode.jpeg").resize((400,400), Image.ANTIALIAS))


n = customtkinter.CTkLabel(master=frm, text="N", text_color="red",font=("Arial", 25,"bold"))

n.place(x=200, y=5.32)
o = customtkinter.CTkLabel(master=frm, text="o", text_color="aqua",font=("Arial", 25,"bold"))

o.place(x=215, y=5.32)
c = customtkinter.CTkLabel(master=frm, text="C", text_color="gold",font=("Calligraffitti", 25,"bold"))

c.place(x=230, y=5.32)
o = customtkinter.CTkLabel(master=frm, text="o", text_color="aqua",font=("Arial", 25,"bold"))

o.place(x=245, y=5.32)

d = customtkinter.CTkLabel(master=frm, text="d", text_color="blue",font=("Arial", 25,"bold"))

d.place(x=260, y=5.32)
e = customtkinter.CTkLabel(master=frm, text="e", text_color="green",font=("Arial", 25,"bold"))

e.place(x=275, y=5.32)


logo =ImageTk.PhotoImage(Image.open("NoCode.jpeg").resize((40,40), Image.ANTIALIAS))

#lebo = customtkinter.CTkLabel(master=frm, image=login)
#lebo.pack()

#leb = customtkinter.CTkLabel(master=lebo,image=logo)
#leb.pack()

entry1 = customtkinter.CTkEntry(master=frm, width=275,placeholder_text="Username",placeholder_text_color="black",corner_radius=4.532, fg_color="aliceblue")
entry1.place(x=5.2, y=170.1, )
entry2 = customtkinter.CTkEntry(master=frm, width=275,placeholder_text="Password",placeholder_text_color="black",corner_radius=4.532,fg_color="aliceblue")
entry2.place(x=5.2, y=240.1, )

logo1 = ImageTk.PhotoImage(Image.open("index.png").resize((20,20),Image.ANTIALIAS))
logo2 = ImageTk.PhotoImage(Image.open("iG.jpeg").resize((20,20),Image.ANTIALIAS))
logo3 = ImageTk.PhotoImage(Image.open("Facebook-logo.png").resize((20,20),Image.ANTIALIAS))
logo4 = ImageTk.PhotoImage(Image.open("NoCode.jpeg").resize((100,100),Image.ANTIALIAS))

button0 = customtkinter.CTkButton(master=frm, image=logo4, fg_color="white",text=" " ,width=100, height=100,corner_radius=3.5,compound="left", text_color="black")
button0.place(x=125, y=40)

button1 = customtkinter.CTkButton(master=frm, image=logo1, text="Google", fg_color="#F0F8FF", width=110, height=20,corner_radius=3.5,compound="left", text_color="black", hover_color="aqua")
button1.place(x=12, y=345)
button2 = customtkinter.CTkButton(master=frm, image=logo2, text="Instagram", width=110,fg_color="#F0F8FF", height=20,corner_radius=3.5,compound="left", text_color="black", hover_color="aqua")
button2.place(x=130, y=345)
button3 = customtkinter.CTkButton(master=frm, image=logo3, text="Facebook", width=110,fg_color="#F0F8FF", height=20,corner_radius=3.5,compound="left", text_color="black", hover_color="blue")
button3.place(x=245, y=345)

button4 = customtkinter.CTkButton(master=frm, text="login", fg_color="silver",width=65, height=30, corner_radius=2.456, text_color="black",hover_color="green")
button4.place(x=165, y=300)
button5 =  customtkinter.CTkButton(master=frm, text="Forgot Password?", fg_color="#F0F8FF",width=65, height=30, corner_radius=2.456, text_color="black",hover_color="#F0F8FF")
button5.place(x=165, y=375)
root.mainloop()
