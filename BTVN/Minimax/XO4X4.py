#Giải thuật minimax - Game XO 4x4
from tkinter import *
from tkinter import messagebox
root = Tk()
root.title('Game XO 4x4')
# Nguoi choi 1 (X) di truoc, Nguoi choi 2 (0) tiep theo sau
clicked = True
count = 0

def disableButtons():
    button1.config(state=DISABLED)
    button2.config(state=DISABLED)
    button3.config(state=DISABLED)
    button4.config(state=DISABLED)
    button5.config(state=DISABLED)
    button6.config(state=DISABLED)
    button7.config(state=DISABLED)
    button8.config(state=DISABLED)
    button9.config(state=DISABLED)
    button10.config(state=DISABLED)
    button11.config(state=DISABLED)
    button12.config(state=DISABLED)
    button13.config(state=DISABLED)
    button14.config(state=DISABLED)
    button15.config(state=DISABLED)
    button16.config(state=DISABLED)

def checkWinner():
    global win
    win = False
    # Cac dieu kien ma nguoi choi 1 (X) chien thang
    if button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X" and button4["text"] == "X":
        button1.config(bg="#80ffaa")
        #[X] [X] [X] [X]
        button2.config(bg="#80ffaa")
        #[0][0][]
        button3.config(bg="#80ffaa")
        button4.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button5["text"] == "X" and button6["text"] == "X" and button7["text"] == "X" and button8["text"] == "X":
        button5.config(bg="#80ffaa")
        #[0] [0] [0] []
        button6.config(bg="#80ffaa")
        #[X] [X] [X] [X]
        button7.config(bg="#80ffaa")
        button8.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button9["text"] == "X" and button10["text"] == "X" and button11["text"] == "X" and button12["text"] == "X":
        button9.config(bg="#80ffaa")
        button10.config(bg="#80ffaa")
        #[0] [0] [11]
        button11.config(bg="#80ffaa")
        #[X] [X] [X] [X]
        button12.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button13["text"] == "X" and button14["text"] == "X" and button15["text"] == "X" and button16["text"] == "X":
        button13.config(bg="#80ffaa")
        button14.config(bg="#80ffaa")
        #[○] [○][]
        button15.config(bg="#80ffaa")
        button16.config(bg="#80ffaa")
        #[X] [X] [X] [X]
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X" and button13["text"] == "X":
        button1.config(bg="#80ffaa")
        # [X] [0] []
        button5.config(bg="#80ffaa")
        #[X][0][]
        button9.config(bg="#80ffaa")
        #[X][]
        button13.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button2["text"] == "X" and button6["text"] == "X" and button10["text"] == "X" and button14["text"] == "X":
        button2.config(bg="#80ffaa")
        # [X] [0] []
        button6.config(bg="#80ffaa")
        #[X] [0] []
        button10.config(bg="#80ffaa")
        #[X][]
        button14.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button3["text"] == "X" and button7["text"] == "X" and button11["text"] == "X" and button15["text"] == "X":
        button3.config(bg="#80ffaa")
        #[X][0][]
        button7.config(bg="#80ffaa")
        #[X][0][]
        button11.config(bg="#80ffaa")
        #[X][]
        button15.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button4["text"] == "X" and button8["text"] == "X" and button12["text"] == "X" and button16["text"] == "X":
        button4.config(bg="#80ffaa")
        #[X] [0][]
        button8.config(bg="#80ffaa")
        #[X] [○][]
        button12.config(bg="#80ffaa")
        #[X][]
        button16.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button1["text"] == "X" and button6["text"] == "X" and button11["text"] == "X" and button16["text"] == "X":
        button1.config(bg="#80ffaa")
        button6.config(bg="#80ffaa")
        button11.config(bg="#80ffaa")
        button16.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button4["text"] == "X" and button7["text"] == "X" and button10["text"] == "X" and button13["text"] == "X":
        button4.config(bg="#80ffaa")
        #[X] [0] []
        button7.config(bg="#80ffaa")
        #[X] [0][]
        button10.config(bg="#80ffaa")
        #[X][]
        button13.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    # Cac dieu kien nguoi choi 2 [0] chien thang
    if button1["text"] == "0" and button2["text"] == "0" and button3["text"] == "0" and button4["text"] == "0":
        button1.config(bg="#80ffaa")
        # [0] [0] [0] [0]
        button2.config(bg="#80ffaa")
        #[0][0][]
        button3.config(bg="#80ffaa")
        button4.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button5["text"] == "0" and button6["text"] == "0" and button7["text"] == "0" and button8["text"] == "0":
        button5.config(bg="#80ffaa")
        # [0] [0] [0][]
        button6.config(bg="#80ffaa")
        # [0] [0] [0] [0]
        button7.config(bg="#80ffaa")
        button8.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button9["text"] == "0" and button10["text"] == "0" and button11["text"] == "0" and button12["text"] == "0":
        button9.config(bg="#80ffaa")
        button10.config(bg="#80ffaa")
        #[0][0][]
        button11.config(bg="#80ffaa")
        # [0] [0] [0] [0]
        button12.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button13["text"] == "0" and button14["text"] == "0" and button15["text"] == "0" and button16["text"] == "0":
        button13.config(bg="#80ffaa")
        button14.config(bg="#80ffaa")
        # [0][0][]
        button15.config(bg="#80ffaa")
        button16.config(bg="#80ffaa")
        # [0] [0] [0] [0]
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button1["text"] == "0" and button5["text"] == "0" and button9["text"] == "0" and button13["text"] == "0":
        button1.config(bg="#80ffaa")
        # [0][0][]
        button5.config(bg="#80ffaa")
        # [0][0][]
        button9.config(bg="#80ffaa")
        #[○][]
        button13.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button2["text"] == "0" and button6["text"] == "0" and button10["text"] == "0" and button14["text"] == "0":
        button2.config(bg="#80ffaa")
        # [0][0][]
        button6.config(bg="#80ffaa")
        # [0] [0][]
        button10.config(bg="#80ffaa")
        #[○][]
        button14.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button3["text"] == "0" and button7["text"] == "0" and button11["text"] == "0" and button15["text"] == "0":
        button3.config(bg="#80ffaa")
        # [0] [0] []
        button7.config(bg="#80ffaa")
        # [0] [0] []
        button11.config(bg="#80ffaa")
        button15.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button4["text"] == "0" and button8["text"] == "0" and button12["text"] == "0" and button16["text"] == "0":
        button4.config(bg="#80ffaa")
        # [0] [0] []
        button8.config(bg="#80ffaa")
        # [0] [0] []
        button12.config(bg="#80ffaa")
        #[○][]
        button16.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button1["text"] == "0" and button6["text"] == "0" and button11["text"] == "0" and button16["text"] == "0":
        button1.config(bg="#80ffaa")
        button6.config(bg="#80ffaa")
        button11.config(bg="#80ffaa")
        button16.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button4["text"] == "0" and button7["text"] == "0" and button10["text"] == "0" and button13["text"] == "0":
        button4.config(bg="#80ffaa")
        # [0] [0] []
        button7.config(bg="#80ffaa")
        # [0] [0] []
        button10.config(bg="#80ffaa")
        #[○][]
        button13.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()

# Hàm checkDraw nêu hòa nhau
def checkDraw():
    global count, win
    if count == 16 and win == False:
        messagebox.showerror("OX Game", "DRAW!!")
        start()
        
# Để xác định các nút mà Người chơi 1 hoặc Người chơi 2 đã nhấp vào
def buttonClicked(button):
    global clicked, count
    if button["text"] == " " and clicked == True:
        button["text"] = "X"
        clicked = False
        count += 1
        checkWinner()
        checkDraw()
    elif button["text"] == " " and clicked == False:
        button["text"] = "0"
        clicked = True
        count += 1
        checkWinner()
        checkDraw()
    else:
        messagebox.showerror("OX Game", "LỖI!! Vui lòng chọn lại")
        
# Để bắt đầu hoặc chơi lại
def start():
    global button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11, button12, button13, button14, button15, button16
    global clicked, count
    clicked = True
    count = 0
    
    # Xây dựng các nút cho trò chơi
    button1 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=7, bg="SystemButtonFace", command=lambda: buttonClicked(button1))
    button2 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=7, bg="SystemButtonFace", command=lambda: buttonClicked(button2))
    button3 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=7, bg="SystemButtonFace", command=lambda: buttonClicked(button3))
    button4 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=7, bg="SystemButtonFace", command=lambda: buttonClicked(button4))
    button5 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=7, bg="SystemButtonFace", command=lambda: buttonClicked(button5))
    button6 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=7, bg="SystemButtonFace", command=lambda: buttonClicked(button6))
    button7 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=7, bg="SystemButtonFace", command=lambda: buttonClicked(button7))
    button8 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=7, bg="SystemButtonFace", command=lambda: buttonClicked(button8))
    button9 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=7, bg="SystemButtonFace", command=lambda: buttonClicked(button9))
    button10 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=7, bg="SystemButtonFace", command=lambda: buttonClicked(button10))
    button11 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=7, bg="SystemButtonFace", command=lambda: buttonClicked(button11))
    button12 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=7, bg="SystemButtonFace", command=lambda: buttonClicked(button12))
    button13 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=7, bg="SystemButtonFace", command=lambda: buttonClicked(button13))
    button14 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=7, bg="SystemButtonFace", command=lambda: buttonClicked(button14))
    button15 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=7, bg="SystemButtonFace", command=lambda: buttonClicked(button15))
    button16 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=7, bg="SystemButtonFace", command=lambda: buttonClicked(button16))
    
    # sắp xếp các nút trên màn hình cho trò chơi
    button1.grid(row=0, column=0)
    button2.grid(row=0, column=1)
    button3.grid(row=0, column=2)
    button4.grid(row=0, column=3)
    button5.grid(row=1, column=0)
    button6.grid(row=1, column=1)
    button7.grid(row=1, column=2)
    button8.grid(row=1, column=3)
    button9.grid(row=2, column=0)
    button10.grid(row=2, column=1)
    button11.grid(row=2, column=2)
    button12.grid(row=2, column=3)
    button13.grid(row=3, column=0)
    button14.grid(row=3, column=1)
    button15.grid(row=3, column=2)
    button16.grid(row=3, column=3)
    
    # Tạo menu trò chơi
    gameMenu = Menu(root)
    root.config(menu=gameMenu)
    
    # Tạo menu tùy chọn trò chơi
    optionMenu = Menu(gameMenu, tearoff=False)
    gameMenu.add_cascade(label="Options", menu=optionMenu)
    optionMenu.add_command(label="Restart Game", command=start)

start()
root.mainloop()