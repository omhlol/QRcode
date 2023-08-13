import qrcode




print("+----+-------+----+")
print("|    |       |    |")
print("+----+       +----+")
print("|                 |")
print("|                 |")
print("+----+            |")
print("|    |            |")
print("+----+------------+")
print("")
print("Created By Ryan Nikbin")

data = input("Enter the text for the QR code: ")
filename = input("Enter the desired file name (without extension): ")

img = qrcode.make(data)
img.save(f"{filename}.png")