# contoh penggunaan list
a = [5,10,15,20,25,30,35,40]
# a[2] = 15
print("a[2] = ", a[2])
# a[0:3] = [5, 10, 15]
print("a[0:3] = ", a[0:3])
# a[5:] = [30, 35, 40]
print("a[5:] = ", a[5:])

# contoh penggunaan tuple
white = (255,255, 255)
red = (255,0,0)
print(white)
print(red[0])
print(red[1])

# set integer
my_set = {1,2,3}
print(my_set)

# set dengan menggunakan fungsi set()
my_set = set([1,2,3])
print(my_set)

# set data campuran
my_set = {1, 2.0, "Python", (3,4,5)}
print(my_set)

# bila kita mengisi duplikasi, set akan menghilangkan salah satu
# output: {1,2,3}
my_set = {1,2,2,3,3,3}
print(my_set)

# set tidak bisa berisi anggota list
# contoh berikut akan muncul error TypeError
my_set = {1,2,[3,4,5]}

d = {1:'satu', 2:'dua', 'tiga':3}
print(type(d))
print("d[1] = ", d[1])
print("d['tiga'] = ", d['tiga'])
