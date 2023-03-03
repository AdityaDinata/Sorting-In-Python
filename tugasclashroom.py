import random
import time as time
import os

datasort = []
for i in range(10):
    datasort.append(random.randint(1, 100))


def mulai():
    os.system("cls")
    print("\t------Selamat Datang Di Program Sorting------")
    print("\tAngka Random Yang Muncul")
    time.sleep(0.5)
    print("\t", datasort)
    print("\tpilihan shorting\n\t1. Merge Sort\n\t2. Quick Sort ")
    while True:
        try:
            sort = int(input("Plih : "))
            if sort == 1:
                os.system("cls")
                merge()
                while True:
                    try:
                        pilih = input(
                            "\nApakah anda ingin merandom angka lagi?\ny/t Pilih : ")
                        if pilih == "y":
                            os.system("cls")
                            datasort.clear()
                            for i in range(10):
                                datasort.append(random.randint(1, 100))
                            mulai()
                        elif pilih == "t":
                            break
                        else:
                            print("\tMASUKAN PILIHAN DENGAN BENAR")
                    except:
                        print("\tMASUKAN PILIHAN DENGAN BENAR")
                break
            elif sort == 2:
                os.system("cls")
                quick()
                while True:
                    try:
                        pilih = input(
                            "\nApakah anda ingin merandom angka lagi?\ny/t Pilih : ")
                        if pilih == "y":
                            os.system("cls")
                            datasort.clear()
                            for i in range(10):
                                datasort.append(random.randint(1, 100))
                            mulai()
                        elif pilih == "t":
                            break
                        else:
                            print("\tMASUKAN PILIHAN DENGAN BENAR")
                    except:
                        print("\tMASUKAN PILIHAN DENGAN BENAR")
                break
            else:
                print("\tMASUKAN PILIHAN DENGAN BENAR")
        except:
            print("\tMASUKAN PILIHAN DENGAN BENAR")


def merge():
    def mergeSort(datasort):
        if len(datasort) > 1:
            mid = len(datasort) // 2
            left_data = datasort[:mid]
            right_data = datasort[mid:]
            mergeSort(left_data)
            mergeSort(right_data)
            h = i = j = 0
            while h < len(left_data) and i < len(right_data):
                if left_data[h] < right_data[i]:
                    datasort[j] = left_data[h]
                    h += 1
                else:
                    datasort[j] = right_data[i]
                    i += 1
                j += 1
            while h < len(left_data):
                datasort[j] = left_data[h]
                h += 1
                j += 1
            while i < len(right_data):
                datasort[j] = right_data[i]
                i += 1
                j += 1

    if __name__ == "__main__":
        print("Data sebelum di mergeshort adalah :")
        print(datasort)
        mergeSort(datasort)
        print("Data sesudah di mergeshort adalah :")
        print(datasort)


def quick():
    def quick(datasort):
        if len(datasort) <= 1:
            return datasort
        else:
            pivot = datasort[0]
            left = [x for x in datasort[1:] if x <= pivot]
            right = [x for x in datasort[1:] if x > pivot]
            return quick(left) + [pivot] + quick(right)
    print(f" List sebelum di qucksort {datasort}")
    result = quick(datasort)
    print(f" List sesudah di quicksort {result}")


mulai()
