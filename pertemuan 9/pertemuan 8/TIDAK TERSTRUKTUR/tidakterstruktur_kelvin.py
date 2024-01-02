import tkinter as tk

def konversi_suhu():
    suhu_kelvin = entry_suhu.get()

    F = (9/5 * float(suhu_kelvin)) - 459.67
    C = float(suhu_kelvin) - 273.15
    R = (4/5 * float(suhu_kelvin)) - 218.52

    label_hasil.config(text=f"{suhu_kelvin} Kelvin sama dengan:\n"
                           f"{F} Fahrenheit\n"
                           f"{C} Celcius\n"
                           f"{R} Reamur")

# Membuat window
window = tk.Tk()
window.title("Konversi Suhu Kelvin")

# Label dan Entry
label_suhu = tk.Label(window, text="Masukkan Suhu Kelvin:")
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
