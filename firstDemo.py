import random

secret = random.randint(1, 10)
print(secret)

if 1 < 3:
 print("对了")
else:
 print("错了")

# guess = 2
# while guess != 8:
#      guess = int(input("猜错了,再猜一遍:"))
#
gpa_dict ={"小明":3.251,"小花":3.869,"小李":2.683,"小张":3.685}
for name,gpa in gpa_dict.items():
  print("{0}你好,你的当前绩点为:{1:.2f}".format(name,gpa))