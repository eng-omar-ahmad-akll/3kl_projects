# عمر احمد احمد الحسانين عقل
# 231031
import tkinter as tk
from tkinter import messagebox
from gtts import gTTS
import os

# إنشاء نافذة التطبيق
window = tk.Tk()
window.title("Text to Speech")
window.geometry("400x200")

# تسمية النافذة
tk.Label(window, text="Text to Speech", font=("Arial", 16)).pack(pady=10)

# إدخال النص
entry = tk.Entry(window, width=40, font=("Arial", 14))
entry.pack(pady=10)

# وظيفة زر Play
#تقةم بتحويل النص المدخل في مربع الانتري الي كلام و تشغيله كملف صوت باستخدام (gTTS)
def play_text():
    text = entry.get()
    if text.strip():
        # تحويل النص إلى صوت
        tts = gTTS(text=text, lang='en')
        tts.save("speech.mp3")
        os.system("start speech.mp3")
    else:
        messagebox.showwarning("تحذير", "يرجى إدخال نص للتحويل إلى صوت!")

# وظيفة زر Set
#تحذف النص وخلاص 
def clear_text():
    entry.delete(0, tk.END)

# وظيفة زر Exit
#تغلق التطبيق نهائيا 
def exit_app():
    window.destroy()

# زر Play
#يربط بالدالة الخاصة ب التشغيل (play) ليحولها الي نص
btn_play = tk.Button(window, text="Play", font=("Arial", 12), bg="gray", command=play_text)
btn_play.pack(side=tk.LEFT, padx=10, pady=20)

# زر Exit
btn_exit = tk.Button(window, text="Exit", font=("Arial", 12), bg="red", fg="white", command=exit_app)
btn_exit.pack(side=tk.LEFT, padx=10)

# زر Set
#يربط بالدالة الخاصة بالمسح ليمسح كل ما في الانتري 
btn_set = tk.Button(window, text="Set", font=("Arial", 12), bg="blue", fg="white", command=clear_text)
btn_set.pack(side=tk.LEFT, padx=10)

# تشغيل التطبيق
window.mainloop()