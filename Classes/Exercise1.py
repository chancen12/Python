class py_solution:
    def int_to_Roman(self, num):
        a = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        b= [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num = ''
        i = 0
        while  num > 0:
            for _ in range(num // a[i]):
                roman_num += b[i]
                num -= a[i]
            i += 1
        return roman_num


print(py_solution().int_to_Roman(1))
print(py_solution().int_to_Roman(560))