piso = int(input("¿En que piso te encuentras en estos momentos?: "))

for i in range(piso, 0, -1):
    if i != 1:
        print(f"vvv-- Bajas por el piso {i}")
    else:
        print("!!!-- Llegaste al primer piso")