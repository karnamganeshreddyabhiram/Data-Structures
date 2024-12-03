"""
Convert integer to roman
"""

m = [ "", "M", "MM", "MMM" ]
c = [ "", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM "]
x = [ "", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC" ]
i = [ "", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

num=831
thousands = m[num // 1000]
hundereds = c[(num % 1000) // 100]
tens =  x[(num % 100) // 10]
ones = i[num % 10]
    
ans = (thousands + hundereds + tens + ones)
ans=ans.replace(" ","")
ans=ans.strip()
print(ans)            
