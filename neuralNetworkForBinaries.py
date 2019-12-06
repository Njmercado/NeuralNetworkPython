from random import uniform as rd

v = [[0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0],
     [1, 1, 1]]  #vector entrenamiento


def get(n):
    return v[n]


def realData(ve):
    suma = ve[2] * (2**0) + ve[1] * (2**1) + ve[0] * (2**2)
    return suma


def trunc(num):  #Dos decimales despues de coma.
    return float("{0:.3f}".format(num))


#####################################################################

alfa = trunc(rd(0, 1))
error = 1

a = True
w = [trunc(rd(0, 1)), trunc(rd(0, 1)), trunc(rd(0, 1))]
p = 0

while (a):

    if p == 6:
        p = 0

    result = 0

    w_auxiliar = get(p)

    for j in range(0, 3):
        result += w[j] * w_auxiliar[j]

    error = realData(get(p)) - result
    error = trunc(error)

    if error == 0:
        a = False
    else:
        for o in range(0, 3):
            w[o] += alfa * error * get(p)[o]

    p += 1

print("Umbral: " + str(alfa))
print("Posibles pesos que generan 0 error: ")
w = [trunc(w[0]), trunc(w[1]), trunc(w[2])]
print(w)

