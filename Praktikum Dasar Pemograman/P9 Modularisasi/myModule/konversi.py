# function untuk mengkonversi suhu

def celcius_ke_fahrenheit(c):
    """fungsi untuk mengkonversi suhu dari celcius ke fahrenheit"""
    return (c * 9/5) + 32

def fahrenheit_ke_celcius(f):
    """fungsi untuk mengkonversi suhu dari fahrenheit ke celcius"""
    return (f - 32) * 5/9

def celcius_ke_kelvin(c):
    """fungsi untuk mengkonversi suhu dari celcius ke kelvin"""
    return c + 273.15

def kelvin_ke_celcius(k):
    """fungsi untuk mengkonversi suhu dari kelvin ke celcius"""
    return k - 273.15
