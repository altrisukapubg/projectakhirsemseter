import tkinter as tk
from tkinter import messagebox
import random
import ttkbootstrap as ttk

# Fungsi untuk memulai game baru
def new_game():
    global number_to_guess
    number_to_guess = random.randint(1, 100)
    entry_guess.delete(0, tk.END)
    lbl_message.config(text="Tebak angka dari 1 hingga 100")

# Fungsi untuk memeriksa tebakan pemain
def check_guess():
    try:
        guess = int(entry_guess.get())
    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid!")
        return

    if guess < number_to_guess:
        lbl_message.config(text="Terlalu rendah! Coba lagi.")
    elif guess > number_to_guess:
        lbl_message.config(text="Terlalu tinggi! Coba lagi.")
    else:
        messagebox.showinfo("Selamat!", "Tebakan Anda benar!")
        new_game()

# Inisialisasi aplikasi
root = ttk.Window(themename="darkly")
root.title("Game Tebak Angka")

# Label untuk pesan
lbl_message = ttk.Label(root, text="Tebak angka dari 1 hingga 100", font=("Helvetica", 14))
lbl_message.pack(pady=10)

# Entry untuk input tebakan
entry_guess = ttk.Entry(root, font=("Helvetica", 14))
entry_guess.pack(pady=10)

# Tombol untuk mengecek tebakan
btn_check = ttk.Button(root, text="Cek Tebakan", command=check_guess, bootstyle="primary")
btn_check.pack(pady=5)

# Tombol untuk memulai game baru
btn_new_game = ttk.Button(root, text="Game Baru", command=new_game, bootstyle="success")
btn_new_game.pack(pady=5)

# Mulai game pertama kali
new_game()

# Menjalankan aplikasi
root.mainloop()