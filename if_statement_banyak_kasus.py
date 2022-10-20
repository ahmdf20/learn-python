huruf = input("Masukkan 1 huruf : ")

if huruf != "a":
    if huruf != "i":
        if huruf != "u":
            if huruf != "e":
                if huruf != "o":
                    print("Huruf ",huruf," adalah huruf konsonan")
                else:
                    print("Huruf ",huruf," adalah huruf vocal")
            else:
                print("Huruf ",huruf," adalah huruf vocal")
        else:
            print("Huruf ",huruf," adalah huruf vocal")
    else:
        print("Huruf ",huruf," adalah huruf vocal")
else:
    print("Huruf ",huruf," adalah huruf vocal")