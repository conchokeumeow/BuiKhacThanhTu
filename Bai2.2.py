GNY = int(input("Nhap gia niem yet: "))
CK = int(input("Nhap chiet khau: "))
VAT = (GNY - CK)*0.01
GB = GNY - CK + VAT
print("Gia ban:", GB)