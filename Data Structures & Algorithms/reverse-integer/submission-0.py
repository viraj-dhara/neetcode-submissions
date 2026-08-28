class Solution:
    def reverse(self, x: int) -> int:
        
        number = str(x)

        negative = False
        if number[0] == '-' : 
            number = number[1:]
            negative = True


        print(number)

        reverse = number[::-1]

        def generate_highest_integer () -> str :
            
            num = str(2 ** 30)
            carry = 0
            result = ""
            for n in reversed(num) :
                result = str((carry + int(n) * 2) % 10) + result
                carry = (carry + int(n) * 2) // 10

            if carry : result += str(carry) + result

            print(result)

            return result


        high = generate_highest_integer()

        if len(high) == len(reverse) :
            for h, n in zip(high, reverse) :
                if n > h : 
                    reverse = "0"
                    negative = False
                    break
                if n < h :
                    break
            

        if negative :
            reverse = '-' + reverse

        return int(reverse)