from tkinter import * # tkinder 안에 모든것을 쓰겠다

root = Tk()
root.title("GUI")
# root.geometry("640x480") # 가로 * 세로 
root.geometry("640x480+300+100") 
# 나타나는 위치 : 가로*세로 + x좌표 + y 좌표


root.resizable(False, False) # x(너비), y(높이) 값 변경 불가 (창 크기 변경 불가)



root.mainloop()