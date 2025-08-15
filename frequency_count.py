string = input("Please enter any thing : ")
freq = {}

for char in string:
    if char != " ":  
        freq[char] = freq.get(char, 0) + 1

print("Character frequencies:")
for char, count in freq.items():
    print(f"{char} : {count}")
