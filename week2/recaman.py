a = 0
length = int(input(print("Input of the sequence length")))
storage = []
for k in range(0,length):
    if a - k > 0 and a - k not in storage:
        a = a - k
    else:
        a = a + k
    storage.append(a)
print(storage)