def count_vowels_consonents(s):
    vowels = "aeiou"
    v_count = 0
    c_count = 0
    for char in s:
        if char.isalpha():
            if char in vowels:
                v_count += 1
            else:
                c_count +=1
    return v_count, c_count
v, c = count_vowels_consonents("raviteja")
print("vowels: ",v)
print("consonents: ",c)
