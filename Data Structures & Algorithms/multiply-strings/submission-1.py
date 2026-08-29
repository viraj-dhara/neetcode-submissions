class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        if num1 == "0" or num2 == "0" : return "0"

        nums1, nums2 = [int(i) for i in num1], [int(i) for i in num2]

        if len(nums2) > len(nums1) : 
            nums1, nums2 = nums2, nums1

        mid_section = list()

        
        for j in reversed(range(len(nums2))) :

            line_number = len(nums2) - j - 1
            mid_section.append(list())
            mid_section[line_number].extend([0 for i in range(0,line_number)])
            # print(f"{j=} {mid_section[line_number]=}")
            carry = 0

            for i in reversed(range(len(nums1))) :
                mid_section[line_number].append((nums1[i] * nums2[j] + carry) % 10)
                carry = (nums1[i] * nums2[j] + carry) // 10

            if carry != 0 :
                mid_section[line_number].append(carry)
            carry = 0

        # print(mid_section)

        carry = 0
        col_sum = 0
        result = ""
        for i in range(len(nums1) + len(nums2)) :
            col_sum = 0
            for j in range(len(mid_section)) :
                if mid_section[j] :
                    col_sum += mid_section[j].pop(0)
            
            result += str((col_sum + carry) % 10)
            carry = (col_sum + carry) // 10

        if result[-1] == "0" : result = result[:-1]

        return "".join([c for c in reversed(result)])