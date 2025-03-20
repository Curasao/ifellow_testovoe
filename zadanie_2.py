

word = "Hello"
seen = ""

for i in word:
    if i not in seen:
        print(f"{i}: {word.count(i)}")
        seen += i
