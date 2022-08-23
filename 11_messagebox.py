import tkinter.messagebox as msgbox
from tkinter import * # tkinder 안에 모든것을 쓰겠다

root = Tk()
root.title("GUI")
root.geometry("640x480+1000+500") 

# 메세지 박스 : 메세지가 팝업으로 나오는 것 

# 기차 예매 시스템이라고 가정
def info():
    msgbox.showinfo("알림", "정상적으로 예매 완료되었습니다.")  
    # 알림은 창의 이름, 정상적---은 실제로 보여지는 메세지 

def warn():
    msgbox.showwarning("경고", "해당 자석은 매진되었습니다.")  

def error():
    msgbox.showerror("에러", "결제 오류가 발생했습니다.")  

def okcancel():
    msgbox.askokcancel("확인 / 취소", "해당 좌석은 유아동반석입니다. 에매하시겠습니까?")  
    # 확인 취소 버튼이 창에 생김 

def retrycancel():
    response = msgbox.askretrycancel("재시도 / 취소", "일시적인 오류입니다. 다시 시도하시겠습니까?")  
    if response == 1:  
        print("재시도")
    elif response == 0:
        print("취소")
  

def yesno():
    msgbox.askyesno("예 / 아니오", "해당 좌석은 역방향입니다. 예매하시겠습니까?") 

def yesnocancel():
    response = msgbox.askyesnocancel(title=None, message="예매 내역이 저장되지 않았습니다. \n \
        저장 후 프로그램을 종료하시겠습니까?")   
    # 녜 : 저장 후 종료
    # 아니오 : 저장 하지 않고 종료
    # 취소 : 프로그램 종료 취소 (현재 화면에서 계속 작업)
    print("응답:", response)  # Ture, False, None -> 예 1, 아니오 0, 그 외 
    if response == 1:  # 네 , ok
        print("예")
    elif response == 0:
        print("아니오")
    else:
        print("취소")

Button(root, command=info, text="알림").pack()
Button(root, command=warn, text="경고").pack()
Button(root, command=error, text="경고").pack()

Button(root, command=okcancel, text="확인 취소").pack()
Button(root, command=retrycancel, text="재시도 취소").pack()
Button(root, command=yesno, text="예 아니오").pack()
Button(root, command=yesnocancel, text="예 아니오 취소").pack()


root.mainloop()