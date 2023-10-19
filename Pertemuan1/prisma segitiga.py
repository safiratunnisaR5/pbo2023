#variabel
alas_segitiga = 10
tinggi_segitiga = 5
tinggi_prisma = 5

#rumus
luas_segitiga = (1/2) * alas_segitiga * tinggi_segitiga
luas_prisma = (2 * alas_segitiga * tinggi_segitiga) + (3 * alas_segitiga * tinggi_prisma)
volume_prisma = luas_segitiga * tinggi_prisma

#output
print("luas prisma:", luas_prisma)
print("volume prisma:", volume_prisma)
