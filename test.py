import tkinter
from tkinter import messagebox

# 팝업 창 생성
def show_popup():
    messagebox.showinfo("알림", "안녕하세요")

# 메인 윈도우 생성
root = tkinter.Tk()
root.withdraw()  # 메인 윈도우 숨기기

# 팝업 표시
show_popup()