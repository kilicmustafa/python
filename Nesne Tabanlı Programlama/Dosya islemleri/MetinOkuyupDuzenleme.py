with open("metin.txt" ,"r" ,encoding = "utf-8") as file:
    
    dosya_icerigi = file.read()
    for i in dosya_icerigi:
        kelimeler = i.strip("\n")
        

    