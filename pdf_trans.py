import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfReader


def select_pdf_and_convert():
    # tkinter 기본 창 숨기기
    root = tk.Tk()
    root.withdraw()

    # 파일 선택 팝업
    pdf_path = filedialog.askopenfilename(
        title="PDF 파일 선택",
        filetypes=[("PDF files", "*.pdf")]
    )

    if not pdf_path:
        return  # 파일 선택 취소

    try:
        reader = PdfReader(pdf_path)
        text = ""

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

        # 저장 파일명 생성 (확장자만 txt로 변경)
        base_name = os.path.splitext(pdf_path)[0]
        txt_path = base_name + ".txt"

        with open(txt_path, "w", encoding="utf-8") as f:
            f.write(text)

        messagebox.showinfo(
            "완료",
            f"텍스트 추출이 완료되었습니다.\n\n저장 위치:\n{txt_path}"
        )

    except Exception as e:
        messagebox.showerror("오류", str(e))


if __name__ == "__main__":
    select_pdf_and_convert()
