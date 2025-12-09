MAX = 500000000000000000000000000000
total = 0

max_a = 1 + int((MAX).bit_length() - 1)

max_b = 1 + int(500000**(1/3.0) * 1.5)

max_c = 1 + int(500000**(1/5.0) * 1.5)
max_d = 1 + int(500000**(1/7.0) * 1.5)


current_n = 1
while current_n < MAX:
    temp_n_7_5 = current_n
    while temp_n_7_5 < MAX:
        temp_n_7_5_3 = temp_n_7_5
        while temp_n_7_5_3 < MAX:
            n = temp_n_7_5_3
            while n < MAX:
                if n != 0:
                    total += 1 / n
                
                if MAX / 2.0 <= n:
                    break
                
                n *= 2
                
            if MAX / 3.0 <= temp_n_7_5_3:
                break
                
            temp_n_7_5_3 *= 3
            
        if MAX / 5.0 <= temp_n_7_5:
            break
            
        temp_n_7_5 *= 5
        
    if MAX / 7.0 <= current_n:
        break
        
    current_n *= 7

print(f"Total sum: {total}")