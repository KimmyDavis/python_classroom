# while True:
#     reply = input("Enter a digit: ")
#     if reply == "Done":
#         break
#     try:
#         newnum = float(reply)
#     except:
#         print("we can't do that!")
#     else:
#         if newnum < 20:
#             print("low")
#         else:
#             print(newnum ** 2)
# print("bye!")

y = 101
x = (y ** 0.5) // 1
print(x)
while x > 1:
    if y % x == 0:
        print("composite", x)
        break
    x -= 1
else:
    print("prime")