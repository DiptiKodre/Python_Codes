# str = "dipti"
# for ele in str[::-1]:
#     print(ele, end= " ")

string = input("Enter a string to reverse : ")
reverse_string = ""
for ele in string:
    reverse_string = ele + reverse_string
print("The reverse string is : ", reverse_string)

