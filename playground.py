print(type(str(eval(".123"))))
str_a = "1+2+3"
str_b = "+"
str_c = "-100"


str_total = str_a + str_b
str_total += str_c
print(str_total)
print(eval(str_total))
if not "":
    print("true")
