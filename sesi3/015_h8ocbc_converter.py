def to_celcius_kelvin(nilai, tujuan):
    '''
    Fungsi untuk mengkonversi celcius ke kelvin, atau kelvin ke celcius
    :param nilai: nilai/angka yang ingin dikovenrsi | int or float
    :param tujuan: tujuan temperature yang dikonversi | 'celcius' or 'kelvin' string
    
    :return: output: hasil konversi nilai ke tujuan temperature | int or float
    '''

    if tujuan == 'celcius':
        return nilai - 273.15
    if tujuan == 'kelvin':
        return nilai + 273.15


def to_fahrenheit(nilai, asal):
    '''
    Fungsi untuk mengkonversi celcius ke fahrenheit, atau kelvin ke farenheit
    :param nilai: nilai/angka yang ingin dikovenrsi ke fahrenheit | int or float
    :param asal: asal nilai temperature yang dikonversi | 'celcius' or 'kelvin' string
    
    :return: output: hasil konversi nilai ke fahrenheit | int or float
    '''

    if asal == 'kelvin':
        return (9 / 5) * (to_celcius_kelvin(nilai, 'celcius')) + 32
    if asal == 'celcius':
        return (9 / 5) * (nilai) + 32


def fahrenheit_converter(nilai, tujuan):
    '''
    Fungsi untuk mengkonversi fahrenheit ke celcius atau kelvin
    :param nilai: nilai/angka fahrenheit yang ingin dikovenrsi | int or float
    :param tujuan: tujuan temperature yang dikonversi | 'celcius' or 'kelvin' string

    :return: output: hasil konversi nilai dari fahrenheit ke celcius atau kelvin | int or float
    '''

    f_to_c = (5 / 9) * (nilai - 32)

    if tujuan == 'celcius':
        return f_to_c
    if tujuan == 'kelvin':
        return f_to_c + 273


print(to_fahrenheit(32, 'celcius'))
print(to_fahrenheit(322, 'kelvin'))
