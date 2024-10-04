temperature = float(input("Entrez la température: "))
if temperature < 0:
    print("Très froid")
elif temperature < 15:
    print("Froid")
elif temperature < 30:
    print("Tiède")
else:
    print("Chaud")