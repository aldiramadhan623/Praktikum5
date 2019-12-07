data = {}
while True:
    print("")
    c = input("T)ambah, U)bah, H)apus, L)ihat, C)ari, K)eluar: ")
    if c.lower() == 'k':
        break

    elif c.lower() == 'l':
        if data.items ():
            print("||^^^^^^^^^^^^^^^^^^^^^^^Daftar Nilai Mahasiswa^^^^^^^^^^^^^^^^^^^^||")
            
            print("_____________________________________________________________________")
            print()
            print()
            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<..>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print("| No |   NAMA   |    NIM    |  Tugas  |  UTS  |  UAS  | Nilai Akhir |")
            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<..>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            i=0
            for x in data.items():
                i+=1
                print("|{6:2}| {0:10s} |{1:11}|{2:9d}|{3:7d}|{4:7d}|{5:13.2f}|"\
                      .format(x[0], x[1][0], x[1][1], x[1][2], x[1][3], x[1][4],i))
                print("_________________________________________________________________")
                print("")
                
        else:
            print("||^^^^^^^^^^^^^^^^^^^^^^^Daftar Nilai Mahasiswa^^^^^^^^^^^^^^^^^^^^||")
            print("_____________________________________________________________________")
            print()
            print()
            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<..>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print("| No |   NAMA   |   NIM  |  Tugas  |  UTS   | UAS |   Nilai Akhir   |")
            
            print("|                     Tidak Ada Data Mahasiswa                      |")
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("")

        
    elif c.lower() == 't':
        print("=============== |Tambah Daftar Mahasiswa| ===============")
        nama    = input         ("Nama        :")
        nim     = int(input     ("Nim         :"))
        tugas   = int(input     ("Nilai Tugas :"))
        uts     = int(input     ("Nilai UTS   :"))
        uas     = int(input     ("Nilai UAS   :"))
        akhir =((tugas)*30/100 + (uts)*35/100 + (uas)*35/100)
        data[nama] = nim, tugas, uts, uas, akhir

    elif c.lower() == 'u':
        print("=============== |Ubah Data Mahasiswa| ===============")
        nama = input                ("Nama        : ")
        if nama in data.keys():
            nim     = input         ("Nim         :")
            tugas   = int(input     ("Nilai Tugas :"))
            uts     = int(input     ("Nilai UTS   :"))
            uas     = int(input     ("Nilai UAS   :"))
            akhir   =((tugas)*30/100 + (uts)*35/100 + (uas)*35/100)
            data[nama] = nim, tugas, uts, uas, akhir
            
        else:
            print(" Data Mahasiswa {0} tidak ada".format(nama))



    elif c.lower()=='h':
        print("=============== |Hapus data Mahasiswa| ===============")
        nama = input ("Nama: ")
        if nama in data.keys():
            del data[nama]
        else :
            print("Data Mahasiswa Tidak Ada".format(nama))

    elif c.lower ()== 'c':
        print("=============== |Cari Data Mahasiswa| ===============")
        nama = input ("Nama   : ")
        if nama in data.keys():
            print ("Data Nilai Mahasiswa",nama, "adalah ={0}".format(data[nama]))
        else:
            print("=============== |Data Mahasiswa Tidak Ada| ===============")
