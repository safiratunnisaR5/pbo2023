import tkinter as tk

def konversi_suhu():
    suhu_fahrenheit = entry_suhu.get()

    R = (4/9 * float(suhu_fahrenheit)) - 32
    C = (5/9 * float(suhu_fahrenheit)) - 32
    K = (4/9 * float(suhu_fahrenheit)) - 32 + 273

    label_hasil.config(text=f"{suhu_fahrenheit} Fahrenheit sama dengan:\n"
                           f"{R} Reamur\n"
                           f"{C} Celcius\n"
                           f"{K} Kelvin")

# Membuat window
window = tk.Tk()
window.title("Konversi Suhu Fahrenheit")

# Label dan Entry
label_suhu = tk.Label(window, text="Masukkan Suhu Fahrenheit:")
label_suhu.pack()

entry_suhu = tk.Entry(window)
entry_suhu.pack()

# Tombol Konversi
tombol_konversi = tk.Button(window, text="Konversi", command=konversi_suhu)
tombol_konversi.pack()

# Label Hasil
label_hasil = tk.Label(window, text="")
label_hasil.pack()

# Menjalankan aplikasi
window.mainloop()
