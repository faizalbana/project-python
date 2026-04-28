# Konversi fahrenheit ke kelvin
print("\nFAHRENHEIT KE KELVIN\n")

fahrenheit = float(input("Masukkan suhu: "))

celcius = 5 / 9 * (fahrenheit - 32)
kelvin = celcius + 273

print("Suhu dalam kelvin ialah: ", kelvin, ("Kelvin"))

#Konversi kelvin ke fahrenheit
print("\nKELVIN KE FAHRENHEIT\n")

kelvin = float(input("Masukkan suhu: "))

celcius = kelvin - 273
fahrenheit = ((9 / 5) * celcius) + 32

print("Suhu dalam fahrenheit ialah: ", fahrenheit, ("Fahrenheit"))
