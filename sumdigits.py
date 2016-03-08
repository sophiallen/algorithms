

sumDigits_1(n):
    total = 0
    str_num = str(n)
    for i in str_num:
      total += int(i)
  return total


sumDigits_2(n):
    total = 0
    while n:
      total += n%10
      n //=10
  return total
  
