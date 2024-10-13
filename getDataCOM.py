import serial
import time

# Sesuaikan 'COMx' dan baud rate dengan yang digunakan di Proteus
ser = serial.Serial('COM6', 9600)  # Contoh untuk Windows
time.sleep(2)  # Delay untuk memastikan koneksi

try:
    while True:
        if ser.in_waiting > 0:  # Periksa apakah ada data yang masuk
            line = ser.readline().decode('utf-8').rstrip()
            print(line)  # Menampilkan data yang diterima
except KeyboardInterrupt:
    print("Program dihentikan.")
finally:
    ser.close()
