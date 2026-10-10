d = {11:"apple",2:"banana",31:"cherry",94:"date"}

#sorting based on keys
sorted_dict_key = dict(sorted(d.items()))
print(sorted_dict_key)

#in reverse order based on keys
sorted_dict_key_reverse = dict(sorted(d.items(), reverse=True))
print(sorted_dict_key_reverse)

#sorting based on values
sorted_dict_value = dict(sorted(d.items(), key=lambda item: item[1]))
print(sorted_dict_value)

#using sorted with lambda function to sort based on keys
sorted_dict_key_lambda = dict(sorted(d.items(), key=lambda item: item[0]))
print(sorted_dict_key_lambda)

res = {k:v for k,v in sorted(d.items(), key= lambda item: item[0]) }
print(res)



