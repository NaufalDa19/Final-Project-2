import PengolahData as baca

filename = 'dataset1.csv'
keluaran = 'dataout.csv'

nim=baca.bacaKolomList(filename,0)
tugas1=baca.bacaKolomList(filename,1)
tugas2=baca.bacaKolomList(filename,2)
quiz1=baca.bacaKolomList(filename,3)
quiz2=baca.bacaKolomList(filename,4)
uts=baca.bacaKolomList(filename,5)
uas=baca.bacaKolomList(filename,6)
header=baca.bacaHeaderList(filename)

pindah1=baca.pindahData(nim,tugas1)
pindah2=baca.pindahData(nim,tugas2)
pindah3=baca.pindahData(nim,quiz1)
pindah5=baca.pindahData(nim,uts)

tugas1_int=baca.gantiListInteger(tugas1)
tugas2_int=baca.gantiListInteger(tugas2)
quiz1_int=baca.gantiListInteger(quiz1)
quiz2_int=baca.gantiListInteger(quiz2)
uts_int=baca.gantiListInteger(uts)
uas_int=baca.gantiListInteger(uas)

hasil=[]
hasil.append(header)
for i in range(len(nim)):   
  hasil.append([nim[i],tugas1_int[i],tugas2_int[i],quiz1_int[i],quiz2_int[i],uts_int[i],uas_int[i]])
baca.simpanFileList(keluaran,hasil)
baca.bacaData(keluaran)

# Eca

'''Soal No 1'''
print("Soal No 1")
maxUTS=uts_int.index(max(uts_int))
print(f'Nilai UTS Tertinggi diraih oleh NIM {nim[maxUTS]} dengan nilai {max(uts_int)}')
print("\n")

'''Soal No 2'''
print("Soal No 2")
minUAS=uas_int.index(min(uas_int))
print(f'Nilai UAS Terendah diraih oleh NIM {nim[minUAS]} dengan nilai {min(uas_int)}')
print("\n")

# Eca

# Caca

'''Soal No 3'''
print("Soal No 3")
hasil_mean=baca.meanKolom(quiz1_int)
print(f"Hasil mean(rata-rata) dari kolom QUIZ 1 adalah {hasil_mean}")
gabNilai_mean=baca.namaList(nim,quiz1_int)
hasil_nilaimean=[list(x) for x in zip(*gabNilai_mean)]
nim_masuk_Rata_rata=baca.cariHasilindexdata_diatas_hasil(hasil_nilaimean,hasil_mean)
print(f"NIM yang nilainya di atas rata rata ada {len(nim_masuk_Rata_rata)} anak, yang mana NIM-nya sebagai berikut : {nim_masuk_Rata_rata}")
print("\n")

'''Soal No 4'''
print("Soal No 4")
hasil_median=baca.cariMedian(quiz2_int)
print(f"Hasil median(nilai-tengah) dari kolom QUIZ 2 adalah {hasil_median}")
gabNilai_median=baca.namaList(nim,quiz2_int)
hasil_nilaimedian=[list(x) for x in zip(*gabNilai_median)]
nim_Masuk_median=baca.cariHasilindexdata_dibawah_hasil(hasil_nilaimedian,hasil_median)
print(f"Setelah melewati proses sorted untuk mencari median maka, NIM yang nilainya di bawah median ada {len(nim_Masuk_median)} anak, yang mana NIM-nya sebagai berikut : {nim_Masuk_median}")
print("\n")

# Caca

# Ali

'''Soal No 5'''
print("Soal No 5")
hasil_median2=baca.cariMedian(tugas1_int)
print(f"Hasil median(nilai-tengah) dari kolom TUGAS 1 adalah {hasil_median2}")
gabNilai_median2=baca.namaList(nim,tugas1_int)
hasil_nilaimedian2=[list(x) for x in zip(*gabNilai_median2)]
nim_Masuk_median2=baca.cariHasilindexdata_dibawah_hasil(hasil_nilaimedian2,hasil_median2)
print(f"Setelah melewati proses sorted untuk mencari median maka, NIM yang nilainya di bawah median ada {len(nim_Masuk_median2)} anak, yang mana NIM-nya sebagai berikut : {nim_Masuk_median2}")
print("\n")

'''Soal No 6'''
print("Soal No 6")
hasil_mean2=baca.meanKolom(tugas2_int)
print(f"Hasil mean(rata-rata) dari kolom TUGAS 2 adalah {hasil_mean2}")
gabNilai_mean2=baca.namaList(nim,tugas2_int)
hasil_nilaimean2=[list(x) for x in zip(*gabNilai_mean2)]
nim_masuk_Rata_rata2=baca.cariHasilindexdata_diatas_hasil(hasil_nilaimean2,hasil_mean2)
print(f"NIM yang nilainya di atas rata rata ada {len(nim_masuk_Rata_rata2)} anak, yang mana NIM-nya sebagai berikut : {nim_masuk_Rata_rata2}")
print("\n")

# Ali

tugas1_int=baca.gantiListInteger(tugas1)
tugas2_int=baca.gantiListInteger(tugas2)
quiz1_int=baca.gantiListInteger(quiz1)
quiz2_int=baca.gantiListInteger(quiz2)
uts_int=baca.gantiListInteger(uts)
uas_int=baca.gantiListInteger(uas)

# Naufal

'''Soal No 8'''
print("Soal No 8")
endValue=baca.namaList(tugas1_int,tugas2_int,quiz1_int,quiz2_int,uts_int,uas_int)
hasil_endValue=[list(x) for x in zip(*endValue)]
value=baca.sumNilai(hasil_endValue)

hasil_finalScore=baca.meanAkhir(value)
print(f"Hasil dari mean(rata-rata) akhirnya adalah : {round(hasil_finalScore)}")

gabNilai_meanAkhir=baca.namaList(nim,value)
hasil_meanAkhir=[list(x) for x in zip(*gabNilai_meanAkhir)]
hasilAkhir=baca.cariHasilindexdata_dibawah_hasil(hasil_meanAkhir,hasil_finalScore)
print(f"NIM yang nilainya di bawah rata rata ada {len(hasilAkhir)} anak, yang mana NIM-nya sebagai berikut : {hasilAkhir}")
print("\n")

'''Soal No 7'''
print("Soal No 7")
Q1=baca.Qtl_1(value)
print(f"Nilai dari Quartile 1 adalah {round(Q1)}")
Q3=baca.Qtl_3(value)
print(f"Nilai dari Quartile 3 adalah {round(Q3)}")
L=baca.L(Q1,Q3)
print(f"Nilai dari L adalah {round(L)}")

Pencilan_bawah=Q1-L
Pencilan_atas=Q3+L
print(f"Nilai dari Pencilan atas adalah : {round(Pencilan_atas)} dan Nilai dari Pencilan Bawah adalah : {round(Pencilan_bawah)}")
Pengecekan=baca.PencilanCheck(Pencilan_atas, Pencilan_bawah, hasil_meanAkhir)
print(Pengecekan)

# Naufal






