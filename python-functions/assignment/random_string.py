import random
import string


def random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

data = []
for i in range(1,4):
    dict = {}
    dict["id"] = i
    dict["title"] = random_string(20)
    dict["content"] = random_string(50)
    data.append(dict)

print(data)