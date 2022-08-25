# Проверить истинность утверждения not(X or Y or Z) == not X and not Y and not Z для всех значений предикат
xyz = [False, True, False]
exp_1 = not(xyz[0] or xyz[1] or xyz[2])
exp_2 = not xyz[0] and not xyz[1] and not xyz[2]

print(exp_1 == exp_2)
