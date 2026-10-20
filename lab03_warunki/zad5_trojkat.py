# Lab 03 – Zadanie 5 (☆, dodatkowe): Jaki to trójkąt?
#
# Program wczytuje trzy długości boków (float) i wypisuje:
#   - "Nie da się zbudować trójkąta", jeśli nie spełniają nierówności trójkąta
#     (każdy bok musi być krótszy od sumy dwóch pozostałych),
#   - w przeciwnym razie rodzaj: "równoboczny", "równoramienny" albo "różnoboczny",
#   - dodatkowo "prostokątny", jeśli a² + b² = c² dla najdłuższego boku c
#     (porównuj z tolerancją: abs(x - y) < 1e-9).

# TODO: Twój kod poniżej
a = float(input("Podaj długość pierwszego boku: "))
b = float(input("Podaj długość drugiego boku: "))
c = float(input("Podaj długość trzeciego boku: "))
if a + b <= c or a + c <= b or b + c <= a:
    print("Nie da się zbudować trójkąta")
else:
    if a == b == c:
        print("Trójkąt równoboczny")
    elif a == b or a == c or b == c:
        print("Trójkąt równoramienny")
    else:
        print("Trójkąt różnoboczny")
    longest = max(a, b, c)
    if longest == a:
        other1, other2 = b, c
    elif longest == b:
        other1, other2 = a, c
    else:
        other1, other2 = a, b
    if abs(longest**2 - (other1**2 + other2**2)) < 1e-9:
        print("Trójkąt prostokątny")