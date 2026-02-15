def factorial(n):
    result = [n]
    for x in range(2, n+1):
        carry = 0
        for i in range(len(result)):
            prod = result[i] * x + carry
            result[i] = prod % 10
            carry = prod // 10

            while carry:
                result.append(carry % 10)
                carry //= 10

        return result[::-1]  # Reverse the result list to get the correct order
    
n= 5
print(f"factorial of {n} is : {factorial(n)}")    
        