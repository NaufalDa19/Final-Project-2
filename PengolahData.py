import csv
'''digunakan untuk melakukan prepocessing data csv'''

def namaList(*li):
    data=[]
    for j in li:
        data.append(j)
    return data

# program utama

# Caca

def simpanFileList(fOut,data):
    '''untuk menyimpan file dari data yang sudah di olah dari data awal'''
    with open(fOut, "w", newline="") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerows(data)

def bacaKolomList (f,kolom):
    '''untuk membaca file csv kolom dalam bentuk list'''
    data=[]
    with open(f, 'r') as csv_file:
        dataReader = csv.reader(csv_file)
        header = next(dataReader)
        for row in dataReader:
            content = list(row[i] for i in [kolom])
            data += content
    return data

# Caca

# Eca

def bacaHeaderList (f):
    '''untuk membaca file csv kolom dalam bentuk list'''
    with open(f, 'r') as csv_file:
        dataReader = csv.reader(csv_file)
        return next(dataReader)
    
def gantiListInteger(l):
    '''digunakan untuk merubah tipe data dari suatu list'''
    for a in range(len(l)):
        l[a] = int(l[a])
    return l

# Eca

# Ali

def pindahData(l1,l2):
    '''untuk memindahkan sebuah nilai dari suatu header ke lainnya'''
    for i in range(len(l1)):
        for x in range(len(l2)):
            if len(l1[x]) == 2 and len(l2[x]) == 10:
                l1[x],l2[x] = l2[x],l1[x]
    return list(l1),list(l2)

# Ali

# Naufal
    
def bacaData(fBaru):
    dataout = []
    with open(fBaru) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for row in csv_reader:
            dataout.append(row)
    labels = dataout.pop(0)
    print(f'{labels[0]}     \t {labels[1]}\t {labels[2]}\t {labels[3]}\t {labels[4]}\t {labels[5]}\t {labels[6]}')
    print("-"*60)
    for data in dataout:
        print(f'{data[0]} \t {data[1]} \t {data[2]} \t {data[3]} \t {data[4]} \t {data[5]} \t {data[6]}')

# Naufal
       
# program utama
   
def meanKolom(kolom):
    '''Untuk mencari nilai dari mean(rata-rata)'''
    mean=sum(kolom)/len(kolom)
    a=round(mean)
    return a

def cariHasilindexdata_diatas_hasil(kolom,hasil_data):
    '''Untuk mencari nim yang masuk diatas hasil data'''
    hasil=[]
    for i in kolom:
        if i[1] > hasil_data:
            hasil.append(i[0])
    return hasil

def cariHasilindexdata_dibawah_hasil(kolom,hasil_data):
    '''Untuk mencari nim yang masuk dibawah hasil data'''
    hasil=[]
    for i in kolom:
        if i[1] < hasil_data:
            hasil.append(i[0])
    return hasil

def cariMedian(data):
    '''Untuk mencari nilai median(nilai tengah dari data)'''
    data.sort()
    panjang_data=len(data)
    nilai_tengah=panjang_data//2 #Hasil pembagian agar hasilnya dibulatkan kebawah
    if panjang_data % 2 == 1:
        return data[nilai_tengah]
    return (data[nilai_tengah-1] + data[nilai_tengah]) / 2

def sumNilai(data):
    '''Untuk Mencari Jumlah Nilai'''
    hasil=[]
    for x in data:
        nilai=sum(x) / len(x)
        hasil.append(nilai)
    return hasil

def meanAkhir(data):
    '''Untuk Mencari Mean Akhir'''
    nilai=sum(data)/len(data)
    return nilai

def Qtl_1(data):
    '''Mencari Data Quartil 1'''
    pengurutan = sorted(data)
    Q1 = (len(pengurutan) + 1) / 4
    idx = (pengurutan[int(Q1)] + pengurutan[int(Q1) + 1]) / 2
    return idx

def Qtl_3(data):
    '''Mencari Data Q3'''
    pengurutan = sorted(data)
    Q3 = 3 * (len(pengurutan) + 1) / 4
    idx = (pengurutan[int(Q3)] + pengurutan[int(Q3) + 1]) / 2
    return idx

def L(data1,data2):
    '''Mencari Nilai L'''
    nilai_L = (3 / 2) * (data2 - data1)
    return nilai_L
    
def PencilanCheck(Pencilan_a,Pencilan_b,data):
    '''Untuk Mengecek Data Pencilan Yang Ada Di Pencilan Atas Maupun Bawah'''
    Pencilanatas=[]
    Pencilanbawah=[]
    for nilai in data:
        if nilai[1] > Pencilan_a:
            Pencilanatas.append(nilai)
            return Pencilanatas,Pencilanbawah
        elif nilai[1] < Pencilan_b:
            Pencilanbawah.append(nilai)
            return Pencilanbawah,Pencilanatas
    return "Tidak ada data Pencilan Atas Maupun Bawah"        
    
    


    
            
    
    
    
    