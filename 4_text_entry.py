from tkinter import * # tkinder 안에 모든것을 쓰겠다

root = Tk()
root.title("GUI")
root.geometry("640x480+1000+500") 

txt = Text(root, width=30, height=5)
txt.pack()

txt.insert(END, "글자를 입력하세요") # 텍스트 레이블에 미리 문장이 들어가있음

e = Entry(root, width=30)       # enter가 안됨, 한 줄만 받을 수 있음
e.pack()
e.insert(0, "한 줄만 입력해요")     # 문장이 들어가있음 

def btncmd():
    # 내용 출력 
    print(txt.get("1.0", END))  # 처음부터 끝까지의 문장을 가져오는 것, "1.0" : 첫번째 줄 0번째 글자부터
    print(e.get())

    # 내용 삭제
    txt.delete("1.0", END)      # 모두 삭제
    e.delete(0, END)

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()