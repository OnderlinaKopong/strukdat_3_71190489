teks = input("Tuliskan teks: ").lower()
x = teks.split()
y = {}
print("Output: ")
for item in x:
    if item in y:
        y[item] += 1
        print(item)
    else:
        y[item] = 1
        print(item)

total = sum(y.values())
print("Total kata = ",total)
print("Kata unik = ",len(y))



