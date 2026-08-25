class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        negation = False
        if a < 0 and b < 0:
            a, b = abs(a), abs(b)
            negation = True
        elif (a < 0) ^ (b < 0) :
            
            if abs(min(a, b)) > max(a, b) :
                negation = True
            
            a, b = max(abs(a), abs(b)), min(abs(a), abs(b))

            ans = 1
            borrow = 0
            while a :
                ans = ans << 1
                if (a & 1) and not (b & 1):
                    if not borrow :
                        ans |= 1
                    elif borrow :
                        borrow = 0
                elif (a & 1) and (b & 1):
                    if not borrow :
                        pass
                    elif borrow :
                        borrow = 1
                        ans |= 1
                elif not (a & 1) and not (b & 1) :
                    if not borrow :
                        pass
                    elif borrow :
                        borrow = 1
                        ans |= 1
                elif not (a & 1) and (b & 1) :
                    if not borrow :
                        borrow = 1
                        ans |= 1
                    elif borrow :
                        borrow = 1
                
                a = a >> 1
                b = b >> 1

            
            result = 0
            while ans :
                result = result << 1
                result |= (ans & 1)
                ans = ans >> 1
            result = result >> 1

            if negation : result = -1 * result

            return result
            



        ans = 1
        carry = 0
        while a or b or carry:
            ans = ans << 1
            if (a & 1) and (b & 1):
                if carry :
                    ans |= 1
                else :
                    carry = 1
            elif (a & 1) ^ (b & 1):
                if not carry :
                    ans |= 1
            else :
                if carry :
                    ans |= 1
                    carry = 0
            
            a = a >> 1
            b = b >> 1

        
        result = 0
        while ans :
            result = result << 1
            result |= (ans & 1)
            ans = ans >> 1
        result = result >> 1

        if negation : result = -1 * result

        return result


                

        