a = float(input('Masukkan nilai a: '))
try:
   b = float(input('Masukkan nilai b: '))
   if b == 0:
      raise ZeroDivisionError   # membangkitkan eksepsi
except ZeroDivisionError as e:
   print('Kesalahan: nilai b tidak boleh 0')
else:
   c = a / b
   print('%.3f / %.3f = %.3f' % (a, b, c))