import tkinter as tk
from tkinter import scrolledtext, messagebox
import pyperclip
import threading
import time

clipboard_history = []
a = True
remove_newlines = False  # akan diatur lewat prompt

def monitor_clipboard():    
    last_text = ""
    while True:
        try:
            current_text = pyperclip.paste()
            if remove_newlines:
                current_text = current_text.replace("\n", " ")
            if current_text != last_text and current_text.strip() != "":
                last_text = current_text
                clipboard_history.insert(0, current_text)
                update_display()
        except:
            pass
        time.sleep(1)

def update_display():
    text_area.config(state='normal')
    text_area.delete("1.0", tk.END)
    global a
    if a is True:
        if clipboard_history:
            clipboard_history.pop(0)
        a = False
    for item in reversed(clipboard_history):
        text_area.insert(tk.END, f"{item}\n")
    text_area.config(state='disabled')

def clear_clipboard():
    clipboard_history.clear()
    pyperclip.copy('')
    update_display()

# GUI setup
root = tk.Tk()
root.title("Riwayat Clipboard")
root.geometry("500x400")

# Prompt pengguna
remove_newlines = messagebox.askyesno(
    "Hapus Newline?",
    "Apakah nantinya anda ingin menghapus karakter baris baru (\\n) dari setiap teks yang disalin?"
)

# Label atas
label = tk.Label(root, text="Riwayat Clipboard (otomatis merekam teks):")
label.pack(pady=5)

# Area teks
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled', height=18)
text_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 5))

# Tombol hapus riwayat
clear_button = tk.Button(
    root,
    text="🧹 Hapus Riwayat",
    command=clear_clipboard,
    bg="blue",
    fg="white",
    font=('Arial', 10, 'bold'),
    relief=tk.RAISED,
    padx=10,
    pady=5
)
clear_button.pack(pady=(5, 10))

# Jalankan monitoring clipboard
thread = threading.Thread(target=monitor_clipboard, daemon=True)
thread.start()

root.mainloop()
