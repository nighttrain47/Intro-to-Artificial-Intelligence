#Giải thuật minimax - Game XO 6x6
from tkinter import *
from tkinter import messagebox
root = Tk()
root.title('Game XO 6x6')
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
    button17.config(state=DISABLED)
    button18.config(state=DISABLED)
    button19.config(state=DISABLED)
    button20.config(state=DISABLED)
    button21.config(state=DISABLED)
    button22.config(state=DISABLED)
    button23.config(state=DISABLED)
    button24.config(state=DISABLED)
    button25.config(state=DISABLED)
    button26.config(state=DISABLED)
    button27.config(state=DISABLED)
    button28.config(state=DISABLED)
    button29.config(state=DISABLED)
    button30.config(state=DISABLED)
    button31.config(state=DISABLED)
    button32.config(state=DISABLED)
    button33.config(state=DISABLED)
    button34.config(state=DISABLED)
    button35.config(state=DISABLED)
    button36.config(state=DISABLED)

def checkWinner():
    global win
    win = False
    
    # Rows - Player 1 (X)
    if button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X" and button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X":
        button1.config(bg="#80ffaa")
        button2.config(bg="#80ffaa")
        button3.config(bg="#80ffaa")
        button4.config(bg="#80ffaa")
        button5.config(bg="#80ffaa")
        button6.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X" and button10["text"] == "X" and button11["text"] == "X" and button12["text"] == "X":
        button7.config(bg="#80ffaa")
        button8.config(bg="#80ffaa")
        button9.config(bg="#80ffaa")
        button10.config(bg="#80ffaa")
        button11.config(bg="#80ffaa")
        button12.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button13["text"] == "X" and button14["text"] == "X" and button15["text"] == "X" and button16["text"] == "X" and button17["text"] == "X" and button18["text"] == "X":
        button13.config(bg="#80ffaa")
        button14.config(bg="#80ffaa")
        button15.config(bg="#80ffaa")
        button16.config(bg="#80ffaa")
        button17.config(bg="#80ffaa")
        button18.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button19["text"] == "X" and button20["text"] == "X" and button21["text"] == "X" and button22["text"] == "X" and button23["text"] == "X" and button24["text"] == "X":
        button19.config(bg="#80ffaa")
        button20.config(bg="#80ffaa")
        button21.config(bg="#80ffaa")
        button22.config(bg="#80ffaa")
        button23.config(bg="#80ffaa")
        button24.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button25["text"] == "X" and button26["text"] == "X" and button27["text"] == "X" and button28["text"] == "X" and button29["text"] == "X" and button30["text"] == "X":
        button25.config(bg="#80ffaa")
        button26.config(bg="#80ffaa")
        button27.config(bg="#80ffaa")
        button28.config(bg="#80ffaa")
        button29.config(bg="#80ffaa")
        button30.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button31["text"] == "X" and button32["text"] == "X" and button33["text"] == "X" and button34["text"] == "X" and button35["text"] == "X" and button36["text"] == "X":
        button31.config(bg="#80ffaa")
        button32.config(bg="#80ffaa")
        button33.config(bg="#80ffaa")
        button34.config(bg="#80ffaa")
        button35.config(bg="#80ffaa")
        button36.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    # Columns - Player 1 (X)
    elif button1["text"] == "X" and button7["text"] == "X" and button13["text"] == "X" and button19["text"] == "X" and button25["text"] == "X" and button31["text"] == "X":
        button1.config(bg="#80ffaa")
        button7.config(bg="#80ffaa")
        button13.config(bg="#80ffaa")
        button19.config(bg="#80ffaa")
        button25.config(bg="#80ffaa")
        button31.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button2["text"] == "X" and button8["text"] == "X" and button14["text"] == "X" and button20["text"] == "X" and button26["text"] == "X" and button32["text"] == "X":
        button2.config(bg="#80ffaa")
        button8.config(bg="#80ffaa")
        button14.config(bg="#80ffaa")
        button20.config(bg="#80ffaa")
        button26.config(bg="#80ffaa")
        button32.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button3["text"] == "X" and button9["text"] == "X" and button15["text"] == "X" and button21["text"] == "X" and button27["text"] == "X" and button33["text"] == "X":
        button3.config(bg="#80ffaa")
        button9.config(bg="#80ffaa")
        button15.config(bg="#80ffaa")
        button21.config(bg="#80ffaa")
        button27.config(bg="#80ffaa")
        button33.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button4["text"] == "X" and button10["text"] == "X" and button16["text"] == "X" and button22["text"] == "X" and button28["text"] == "X" and button34["text"] == "X":
        button4.config(bg="#80ffaa")
        button10.config(bg="#80ffaa")
        button16.config(bg="#80ffaa")
        button22.config(bg="#80ffaa")
        button28.config(bg="#80ffaa")
        button34.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button5["text"] == "X" and button11["text"] == "X" and button17["text"] == "X" and button23["text"] == "X" and button29["text"] == "X" and button35["text"] == "X":
        button5.config(bg="#80ffaa")
        button11.config(bg="#80ffaa")
        button17.config(bg="#80ffaa")
        button23.config(bg="#80ffaa")
        button29.config(bg="#80ffaa")
        button35.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button6["text"] == "X" and button12["text"] == "X" and button18["text"] == "X" and button24["text"] == "X" and button30["text"] == "X" and button36["text"] == "X":
        button6.config(bg="#80ffaa")
        button12.config(bg="#80ffaa")
        button18.config(bg="#80ffaa")
        button24.config(bg="#80ffaa")
        button30.config(bg="#80ffaa")
        button36.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    # Diagonals - Player 1 (X)
    elif button1["text"] == "X" and button8["text"] == "X" and button15["text"] == "X" and button22["text"] == "X" and button29["text"] == "X" and button36["text"] == "X":
        button1.config(bg="#80ffaa")
        button8.config(bg="#80ffaa")
        button15.config(bg="#80ffaa")
        button22.config(bg="#80ffaa")
        button29.config(bg="#80ffaa")
        button36.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button6["text"] == "X" and button11["text"] == "X" and button16["text"] == "X" and button21["text"] == "X" and button26["text"] == "X" and button31["text"] == "X":
        button6.config(bg="#80ffaa")
        button11.config(bg="#80ffaa")
        button16.config(bg="#80ffaa")
        button21.config(bg="#80ffaa")
        button26.config(bg="#80ffaa")
        button31.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    # Rows - Player 2 (0)
    elif button1["text"] == "0" and button2["text"] == "0" and button3["text"] == "0" and button4["text"] == "0" and button5["text"] == "0" and button6["text"] == "0":
        button1.config(bg="#80ffaa")
        button2.config(bg="#80ffaa")
        button3.config(bg="#80ffaa")
        button4.config(bg="#80ffaa")
        button5.config(bg="#80ffaa")
        button6.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button7["text"] == "0" and button8["text"] == "0" and button9["text"] == "0" and button10["text"] == "0" and button11["text"] == "0" and button12["text"] == "0":
        button7.config(bg="#80ffaa")
        button8.config(bg="#80ffaa")
        button9.config(bg="#80ffaa")
        button10.config(bg="#80ffaa")
        button11.config(bg="#80ffaa")
        button12.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button13["text"] == "0" and button14["text"] == "0" and button15["text"] == "0" and button16["text"] == "0" and button17["text"] == "0" and button18["text"] == "0":
        button13.config(bg="#80ffaa")
        button14.config(bg="#80ffaa")
        button15.config(bg="#80ffaa")
        button16.config(bg="#80ffaa")
        button17.config(bg="#80ffaa")
        button18.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button19["text"] == "0" and button20["text"] == "0" and button21["text"] == "0" and button22["text"] == "0" and button23["text"] == "0" and button24["text"] == "0":
        button19.config(bg="#80ffaa")
        button20.config(bg="#80ffaa")
        button21.config(bg="#80ffaa")
        button22.config(bg="#80ffaa")
        button23.config(bg="#80ffaa")
        button24.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button25["text"] == "0" and button26["text"] == "0" and button27["text"] == "0" and button28["text"] == "0" and button29["text"] == "0" and button30["text"] == "0":
        button25.config(bg="#80ffaa")
        button26.config(bg="#80ffaa")
        button27.config(bg="#80ffaa")
        button28.config(bg="#80ffaa")
        button29.config(bg="#80ffaa")
        button30.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button31["text"] == "0" and button32["text"] == "0" and button33["text"] == "0" and button34["text"] == "0" and button35["text"] == "0" and button36["text"] == "0":
        button31.config(bg="#80ffaa")
        button32.config(bg="#80ffaa")
        button33.config(bg="#80ffaa")
        button34.config(bg="#80ffaa")
        button35.config(bg="#80ffaa")
        button36.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    # Columns - Player 2 (0)
    elif button1["text"] == "0" and button7["text"] == "0" and button13["text"] == "0" and button19["text"] == "0" and button25["text"] == "0" and button31["text"] == "0":
        button1.config(bg="#80ffaa")
        button7.config(bg="#80ffaa")
        button13.config(bg="#80ffaa")
        button19.config(bg="#80ffaa")
        button25.config(bg="#80ffaa")
        button31.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button2["text"] == "0" and button8["text"] == "0" and button14["text"] == "0" and button20["text"] == "0" and button26["text"] == "0" and button32["text"] == "0":
        button2.config(bg="#80ffaa")
        button8.config(bg="#80ffaa")
        button14.config(bg="#80ffaa")
        button20.config(bg="#80ffaa")
        button26.config(bg="#80ffaa")
        button32.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button3["text"] == "0" and button9["text"] == "0" and button15["text"] == "0" and button21["text"] == "0" and button27["text"] == "0" and button33["text"] == "0":
        button3.config(bg="#80ffaa")
        button9.config(bg="#80ffaa")
        button15.config(bg="#80ffaa")
        button21.config(bg="#80ffaa")
        button27.config(bg="#80ffaa")
        button33.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button4["text"] == "0" and button10["text"] == "0" and button16["text"] == "0" and button22["text"] == "0" and button28["text"] == "0" and button34["text"] == "0":
        button4.config(bg="#80ffaa")
        button10.config(bg="#80ffaa")
        button16.config(bg="#80ffaa")
        button22.config(bg="#80ffaa")
        button28.config(bg="#80ffaa")
        button34.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button5["text"] == "0" and button11["text"] == "0" and button17["text"] == "0" and button23["text"] == "0" and button29["text"] == "0" and button35["text"] == "0":
        button5.config(bg="#80ffaa")
        button11.config(bg="#80ffaa")
        button17.config(bg="#80ffaa")
        button23.config(bg="#80ffaa")
        button29.config(bg="#80ffaa")
        button35.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button6["text"] == "0" and button12["text"] == "0" and button18["text"] == "0" and button24["text"] == "0" and button30["text"] == "0" and button36["text"] == "0":
        button6.config(bg="#80ffaa")
        button12.config(bg="#80ffaa")
        button18.config(bg="#80ffaa")
        button24.config(bg="#80ffaa")
        button30.config(bg="#80ffaa")
        button36.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    # Diagonals - Player 2 (0)
    elif button1["text"] == "0" and button8["text"] == "0" and button15["text"] == "0" and button22["text"] == "0" and button29["text"] == "0" and button36["text"] == "0":
        button1.config(bg="#80ffaa")
        button8.config(bg="#80ffaa")
        button15.config(bg="#80ffaa")
        button22.config(bg="#80ffaa")
        button29.config(bg="#80ffaa")
        button36.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button6["text"] == "0" and button11["text"] == "0" and button16["text"] == "0" and button21["text"] == "0" and button26["text"] == "0" and button31["text"] == "0":
        button6.config(bg="#80ffaa")
        button11.config(bg="#80ffaa")
        button16.config(bg="#80ffaa")
        button21.config(bg="#80ffaa")
        button26.config(bg="#80ffaa")
        button31.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()

# Hàm checkDraw nêu hòa nhau
def checkDraw():
    global count, win
    if count == 36 and win == False:
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
    global button1, button2, button3, button4, button5, button6, button7, button8, button9, button10
    global button11, button12, button13, button14, button15, button16, button17, button18, button19, button20
    global button21, button22, button23, button24, button25, button26, button27, button28, button29, button30
    global button31, button32, button33, button34, button35, button36
    global clicked, count
    clicked = True
    count = 0
    
    # Xây dựng các nút cho trò chơi
    button1 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace", command=lambda: buttonClicked(button1))
    button2 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace", command=lambda: buttonClicked(button2))
    button3 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace", command=lambda: buttonClicked(button3))
    button4 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace", command=lambda: buttonClicked(button4))
    button5 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace", command=lambda: buttonClicked(button5))
    button6 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace", command=lambda: buttonClicked(button6))
    button7 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace", command=lambda: buttonClicked(button7))
    button8 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace", command=lambda: buttonClicked(button8))
    button9 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace", command=lambda: buttonClicked(button9))
    button10 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace", command=lambda: buttonClicked(button10))
    button11 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace", command=lambda: buttonClicked(button11))
    button12 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace", command=lambda: buttonClicked(button12))
    button13 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace", command=lambda: buttonClicked(button13))
    button14 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace", command=lambda: buttonClicked(button14))
    button15 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace", command=lambda: buttonClicked(button15))
    button16 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace", command=lambda: buttonClicked(button16))
    button17 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace", command=lambda: buttonClicked(button17))
    button18 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace", command=lambda: buttonClicked(button18))
    button19 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace", command=lambda: buttonClicked(button19))
    button20 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace", command=lambda: buttonClicked(button20))
    button21 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace", command=lambda: buttonClicked(button21))
    button22 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace", command=lambda: buttonClicked(button22))
    button23 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace", command=lambda: buttonClicked(button23))
    button24 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace", command=lambda: buttonClicked(button24))
    button25 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace", command=lambda: buttonClicked(button25))
    button26 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace", command=lambda: buttonClicked(button26))
    button27 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace", command=lambda: buttonClicked(button27))
    button28 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace", command=lambda: buttonClicked(button28))
    button29 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace", command=lambda: buttonClicked(button29))
    button30 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace", command=lambda: buttonClicked(button30))
    button31 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace", command=lambda: buttonClicked(button31))
    button32 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace", command=lambda: buttonClicked(button32))
    button33 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace", command=lambda: buttonClicked(button33))
    button34 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace", command=lambda: buttonClicked(button34))
    button35 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace", command=lambda: buttonClicked(button35))
    button36 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace", command=lambda: buttonClicked(button36))
    
    # sắp xếp các nút trên màn hình cho trò chơi
    button1.grid(row=0, column=0)
    button2.grid(row=0, column=1)
    button3.grid(row=0, column=2)
    button4.grid(row=0, column=3)
    button5.grid(row=0, column=4)
    button6.grid(row=0, column=5)
    button7.grid(row=1, column=0)
    button8.grid(row=1, column=1)
    button9.grid(row=1, column=2)
    button10.grid(row=1, column=3)
    button11.grid(row=1, column=4)
    button12.grid(row=1, column=5)
    button13.grid(row=2, column=0)
    button14.grid(row=2, column=1)
    button15.grid(row=2, column=2)
    button16.grid(row=2, column=3)
    button17.grid(row=2, column=4)
    button18.grid(row=2, column=5)
    button19.grid(row=3, column=0)
    button20.grid(row=3, column=1)
    button21.grid(row=3, column=2)
    button22.grid(row=3, column=3)
    button23.grid(row=3, column=4)
    button24.grid(row=3, column=5)
    button25.grid(row=4, column=0)
    button26.grid(row=4, column=1)
    button27.grid(row=4, column=2)
    button28.grid(row=4, column=3)
    button29.grid(row=4, column=4)
    button30.grid(row=4, column=5)
    button31.grid(row=5, column=0)
    button32.grid(row=5, column=1)
    button33.grid(row=5, column=2)
    button34.grid(row=5, column=3)
    button35.grid(row=5, column=4)
    button36.grid(row=5, column=5)
    
    # Tạo menu trò chơi
    gameMenu = Menu(root)
    root.config(menu=gameMenu)
    
    # Tạo menu tùy chọn trò chơi
    optionMenu = Menu(gameMenu, tearoff=False)
    gameMenu.add_cascade(label="Options", menu=optionMenu)
    optionMenu.add_command(label="Restart Game", command=start)

start()
root.mainloop()