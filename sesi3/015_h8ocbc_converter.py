def to_celcius_kelvin(angka, tujuan):
    '''
    Fungsi untuk mengkonversi celcius ke kelvin, atau kelvin ke celcius
    :param angka: nilai yang ingin dikovenrsi | int or float
    :param tujuan: tujuan temperature yang dikonversi | 'celcius' or 'kelvin' string
    
    :return: output: hasil konversi nilai ke tujuan temperature | int or float
    '''

    if (tujuan == 'celcius'):
        return angka - 273.15
    if (tujuan == 'kelvin'):
        return angka + 273.15
