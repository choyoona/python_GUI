from tkinter import * # tkinder 안에 모든것을 쓰겠다

root = Tk()
root.title("GUI")
root.geometry("640x480+1000+500") 

label1 = Label(root, text="안녕하세요")
label1.pack()

photo = PhotoImage(file="/Users/yoona/Documents/Python/python_GUI/kitten.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="또 만나요")

    global photo2 # 함수 내에서 레이블의 이미지를 바꾸기 위해 photo를 전역변수로 만들어줘야함
    photo2 = PhotoImage(file="/Users/yoona/Documents/Python/python_GUI/x.png")
    label2.config(image=photo2)

btn = Button(root, text="클릭", command=change)
btn.pack()

root.mainloop()