print("konversi suhu celsius")
def get_fahrenheit(suhu):
    F = (9/5 * float(suhu)) + 32
    return F

def get_reamur(suhu):
    R = (4/5 * float(suhu))
    return R

def get_kelvin(suhu):
    K = float(suhu) + 273
    return K

# Entry
suhu = input("masukkan suhu dalam celcius:")

#rumus
F = get_fahrenheit(suhu)
R = get_reamur(suhu)
K = get_kelvin(suhu)