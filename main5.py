def faqat_sonlarni_chiqaruvchi_function(royxat):
    butun_sonlar = [x for x in royxat if isinstance(x, int) and x >= 0]
    return butun_sonlar

# Test qilish
original_royxat = [1, -2, 'salom', 3.5, 0, 'world', -7, 10]
yangi_royxat = faqat_sonlarni_chiqaruvchi_function(original_royxat)

print("Asl ro'yxat:", original_royxat)
print("Yangi ro'yxat:", yangi_royxat)

