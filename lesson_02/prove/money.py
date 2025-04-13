"""
Money class

                                        Don't Change!!!!!
                                        Don't Change!!!!!
                                        Don't Change!!!!!
                                        Don't Change!!!!!
                                        Don't Change!!!!!
                                        Don't Change!!!!!
                                        Don't Change!!!!!
"""

class Money:

    def __init__(self, money_str):
        if not isinstance(money_str, str):
            raise TypeError("Input must be a string for Money() Class: ie 12345.34, -34.02, 11.00")

        self.digits = money_str.strip().replace('.', '')

    def __str__(self):
        sign = ""
        a = self.digits
        a_num = a
        if a and a[0] in ('-'):
            sign = a[0]
            a_num = a[1:]

        dollars = ''
        cents = ''

        if a_num[0] == '000':
            dollars = '0'
            cents = '00'
        elif len(a_num) == 1:
            dollars = '0'
            cents = f'0{a_num}'
        elif len(a_num) == 2:
            dollars = '0'
            cents = f'{a_num}'
        else:
            dollars = f'{a_num[:-2]}'
            cents = f'{a_num[-2:]}'

        results = f'{sign}{self.__insert_commas(dollars)}.{cents}'
        return f'${results:>15}'


    def __insert_commas(self, s):
        n = len(s)
        if n <= 3:
            return s

        result = ""
        for i in range(n - 1, -1, -1):
            digit = s[i]
            position_from_right = n - 1 - i
            if position_from_right > 0 and position_from_right % 3 == 0:
                result = "," + result
            result = digit + result

        return result        


    def __eq__(self, value):
        return self.digits == value.digits


    def __ne__(self, value):
        return self.digits != value.digits


    def __add(self, a, b):
        result = ""
        carry = 0

        i = len(a) - 1
        j = len(b) - 1

        while i >= 0 or j >= 0 or carry:
            digit_a = int(a[i]) if i >= 0 else 0
            digit_b = int(b[j]) if j >= 0 else 0
            total = digit_a + digit_b + carry
            current_digit = total % 10
            carry = total // 10
            result = str(current_digit) + result
            i -= 1
            j -= 1
        # Handle potential leading zero if result is actually 0
        return result if result else "000"


    def __sub(self, a, b):
        result = ""
        borrow = 0

        i = len(a) - 1
        j = len(b) - 1

        # Ensure a is treated as having at least as many digits as b for subtraction
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)
        i = max_len - 1
        j = max_len - 1


        while i >= 0: # Iterate through the longer length
            digit_a = int(a[i])
            digit_b = int(b[j]) if j >= 0 else 0 # Handle shorter b

            diff = digit_a - digit_b - borrow
            if diff < 0:
                diff += 10
                borrow = 1
            else:
                borrow = 0
            result = str(diff) + result
            i -= 1
            j -= 1 # Decrement j as well

        # Remove leading zeros
        k = 0
        while k < len(result) - 1 and result[k] == '0':
            k += 1
        return result[k:]

    def __fix_zero(self):
        if self.digits in ('-0', '+0'):
            self.digits = '000'

    def sub(self, other):

        a = self.digits
        b = other.digits

        a_sign = ""
        a_num = a
        if a and a[0] in ('+', '-'):
            a_sign = a[0]
            a_num = a[1:]

        b_sign = ""
        b_num = b
        if b and b[0] in ('+', '-'):
            b_sign = b[0]
            b_num = b[1:]

        # Normalize inputs (remove leading zeros from magnitude part)
        a_num = a_num.lstrip('0') if a_num else '0'
        b_num = b_num.lstrip('0') if b_num else '0'
        if a_num == '0': a_sign = "" # Treat 0 as positive
        if b_num == '0': b_sign = "" # Treat 0 as positive


        if a_sign == b_sign:
            # Case 1: (+a) - (+b) or (-a) - (-b) == (-a) + b == b - a
            # Determine which absolute value is larger
            a_is_larger = len(a_num) > len(b_num) or (len(a_num) == len(b_num) and a_num >= b_num)

            if a_is_larger:
                diff = self.__sub(a_num, b_num)
                # Result sign is the same as a's sign (or positive if a was positive)
                self.digits = a_sign + diff if a_sign == '-' else diff
            else:
                diff = self.__sub(b_num, a_num)
                # Result sign is the opposite of a's sign (or negative if a was positive)
                self.digits = diff if a_sign == '-' else "-" + diff
        else:
            # Case 2: (+a) - (-b) == a + b  OR  (-a) - (+b) == -(a + b)
            sum_val = self.__add(a_num, b_num)
            # Result sign is the same as a's sign
            self.digits = a_sign + sum_val if a_sign == '-' else sum_val

        self.__fix_zero()


    def add(self, other):

        a = self.digits
        b = other.digits

        a_sign = ""
        a_num = a
        if a and a[0] in ('+', '-'):
            a_sign = a[0]
            a_num = a[1:]

        b_sign = ""
        b_num = b
        if b and b[0] in ('+', '-'):
            b_sign = b[0]
            b_num = b[1:]

        # Normalize inputs (remove leading zeros from magnitude part)
        a_num = a_num.lstrip('0') if a_num else '0'
        b_num = b_num.lstrip('0') if b_num else '0'
        if a_num == '0': a_sign = "" # Treat 0 as positive
        if b_num == '0': b_sign = "" # Treat 0 as positive


        if a_sign == b_sign:
            # Case 1: (+a) + (+b) or (-a) + (-b) == -(a + b)
            sum_val = self.__add(a_num, b_num)
            # Result sign is the same as their common sign (or positive if both were positive)
            self.digits = a_sign + sum_val if a_sign == '-' else sum_val
        else:
            # Case 2: (+a) + (-b) == a - b  OR  (-a) + (+b) == b - a
            # Determine which absolute value is larger
            a_is_larger = len(a_num) > len(b_num) or (len(a_num) == len(b_num) and a_num >= b_num)

            if a_is_larger:
                diff = self.__sub(a_num, b_num)
                # Result sign is the same as a's sign
                self.digits = a_sign + diff if a_sign == '-' else diff
            else: # b's absolute value is larger or they are equal
                diff = self.__sub(b_num, a_num)
                # Result sign is the same as b's sign
                self.digits = b_sign + diff if b_sign == '-' else diff

        self.__fix_zero()
