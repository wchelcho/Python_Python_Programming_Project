i_a = 41234
i_b = 42563
i_c = i_a + i_b
type_i_c = type(i_c)
print(f' type_i_c: {type_i_c} i_c = {i_c}')

i_d = 6537828764
i_e = 9772564773
i_f = i_d * i_e
print(f'i_f: {i_f}')
s_f = str(i_f)
s_f = s_f + '000000'
print(f'type(s_f): {type(s_f)}')
print(f's_f: {s_f}')
print(f'len(s_f): {len(s_f)}')
i_g = int(s_f)
print(f'type(i_g): {type(i_g)}')
print(f'i_g: {i_g}')