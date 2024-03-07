my_list =[]

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

my_list.insert(1, 15)

ext_list = [50, 60, 70]

my_list.extend(ext_list)

my_list.remove(70)

my_list.sort()

indx = my_list.index(30)

print(my_list)
print(indx)