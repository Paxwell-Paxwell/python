data = "This Is A cAt"
date = "26/05/2022"

length = len(data)
words = data.split(" ") # split with space
date_split = date.split("/")

print(length)
print(words)
print(f"words count = {len(words)}")
print(date_split)
print(f"{date_split[2]}-{date_split[1]}-{date_split[0]}")

print("///////////////////////////")

print(data.upper())
print(data.lower())
print(data.capitalize())

print("///////////////////////////")

print(data.islower())
print(data.isascii())

print("///////////////////////////")

print(data[0])
print(data[len(data)-1])
print(data[-3])
print(data[1:8])

for ch in data:
    print(ch)





