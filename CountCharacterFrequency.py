def count_character_frequency(s):
    frequency = {}
    for ch in s:
        frequency[ch]= frequency.get(ch,0)+1
    return frequency

s = "hello world"
print(count_character_frequency(s))