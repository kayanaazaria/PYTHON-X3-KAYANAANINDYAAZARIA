# konversi bilangan biner ke desimal
def konversi(biner):
    if biner == 0:
        return 0
    else:
        return (biner % 10 + 2*konversi(biner // 10))
biner = int(input("input nilai biner : "))
print(konversi(biner)) 