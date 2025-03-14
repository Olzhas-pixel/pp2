# regex - asdAsd -> asd_asd
# count file
word = "ad ad"
for i in word:
    with open(f"file{i}.txt","w",encoding="utf-8") as f:
        f.write(word)
import re
text = "asdAsd"
a = re.sub(r"Asd","_asd",text).lower()
print(a)