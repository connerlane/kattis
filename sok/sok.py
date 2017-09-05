from decimal import Decimal

orange_juice, apple_juice, pineapple_juice = [eval(i) for i in input().split()]
o_ratio, a_ratio, p_ratio = [eval(i) for i in input().split()]

max_juice_possible = min(orange_juice / o_ratio, 
   apple_juice / a_ratio, pineapple_juice / p_ratio)

print(Decimal(str(orange_juice - 
   max_juice_possible * o_ratio)).quantize(Decimal('.000001')), end=' ')
print(Decimal(str(apple_juice - 
   max_juice_possible * a_ratio)).quantize(Decimal('.000001')), end=' ')
print(Decimal(str(pineapple_juice - 
   max_juice_possible * p_ratio)).quantize(Decimal('.000001')))