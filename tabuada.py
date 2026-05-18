num = int(input("Tabuada de qual numero? "))
print(f"--- Tabuada do {num} ---")
for i in range(1, 11):
    res = num * i
    print(f"{num} x {i} = {res}")