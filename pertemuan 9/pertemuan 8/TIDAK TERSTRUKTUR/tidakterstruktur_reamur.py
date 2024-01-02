import tkinter as tk

def konversi_suhu():
    suhu_reamur = entry_suhu.get()

    F = (9/4 * float(suhu_reamur)) + 32
    C = (5/4 * float(suhu_reamur))
    K = (5/4 * float(suhu_reamur)) + 273

    label_hasil.config(text=f"{suhu_reamur} Reamur sama dengan:\n"
                           f"{F} Fahrenheit\n"
                           f"{C} Celcius\n"
                           f"{K} Kelvin")

# Membuat window
window = tk.Tk()
window.title("Konversi Suhu Reamur")

# Label dan Entry
label_suhu = tk.Label(window, text="Masukkan Suhu Reamur:")
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
