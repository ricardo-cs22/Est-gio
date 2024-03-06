# Sequência a)
def sequencia_a():
    return [1, 3, 5, 7, 9]

def sequencia_b():
    seq = [2]
    for i in range(1, 6):
        seq.append(seq[i-1] * 2)
    return seq


def sequencia_c():
    return [x**2 for x in range(0, 8)]

def sequencia_d():
    return [x**2 for x in range(2, 6)]

def sequencia_e():
    seq = [1, 1]
    while len(seq) < 6:
        seq.append(seq[-1] + seq[-2])
    return seq

def sequencia_f():
    return [2, 10, 12, 16, 17, 18, 19, 20]

print("Próximos números das sequências:")
print("a) Sequência a):", sequencia_a()[-1] + 2)
print("b) Sequência b):", sequencia_b()[-1] * 2)
print("c) Sequência c):", 7**2)
print("d) Sequência d):", 8**2)
print("e) Sequência e):", sequencia_e()[-1] + sequencia_e()[-2])
print("f) Sequência f):", sequencia_f()[-1] + 1)
