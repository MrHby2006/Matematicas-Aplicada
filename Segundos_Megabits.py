def f(t):
    return 100 * t

for i in range(0, 1001, 100):
    print(f"A los {i} segundos se transmiten {f(i)} megabits")
    
