"""
Programa 1: Evaluador de expresiones aritméticas con una pila
Soporta notación posfija (postfix) y prefija (prefix).
Los elementos de la expresión deben ir separados por espacios.
Ejemplo posfija: 3 4 + 2 *   -> 14
Ejemplo prefija: * + 3 4 2   -> 14
"""


class Pila:
    def __init__(self):
        self.items = []

    def push(self, elemento):
        self.items.append(elemento)

    def pop(self):
        if self.esta_vacia():
            raise IndexError("La pila está vacía")
        return self.items.pop()

    def peek(self):
        if self.esta_vacia():
            raise IndexError("La pila está vacía")
        return self.items[-1]

    def esta_vacia(self):
        return len(self.items) == 0

    def tamano(self):
        return len(self.items)


OPERADORES = {"+", "-", "*", "/", "^"}


def operar(a, b, op):
    """Aplica el operador 'op' a los operandos a y b (a op b)."""
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        if b == 0:
            raise ZeroDivisionError("División entre cero")
        return a / b
    if op == "^":
        return a ** b
    raise ValueError(f"Operador desconocido: {op}")


def evaluar_posfija(expresion):
    """Recorre la expresión de izquierda a derecha."""
    pila = Pila()
    for token in expresion.split():
        if token in OPERADORES:
            b = pila.pop()  # el primero en salir es el operando derecho
            a = pila.pop()
            pila.push(operar(a, b, token))
        else:
            pila.push(float(token))
    resultado = pila.pop()
    if not pila.esta_vacia():
        raise ValueError("Expresión mal formada (sobran operandos)")
    return resultado


def evaluar_prefija(expresion):
    """Recorre la expresión de derecha a izquierda."""
    pila = Pila()
    for token in reversed(expresion.split()):
        if token in OPERADORES:
            a = pila.pop()  # aquí el primero en salir es el operando izquierdo
            b = pila.pop()
            pila.push(operar(a, b, token))
        else:
            pila.push(float(token))
    resultado = pila.pop()
    if not pila.esta_vacia():
        raise ValueError("Expresión mal formada (sobran operandos)")
    return resultado


def main():
    while True:
        print("\n=== Evaluador de expresiones ===")
        print("1. Notación posfija")
        print("2. Notación prefija")
        print("3. Salir")
        opcion = input("Elige una opción: ").strip()

        if opcion == "3":
            print("¡Hasta luego!")
            break
        if opcion not in ("1", "2"):
            print("Opción no válida.")
            continue

        expresion = input("Escribe la expresión (separada por espacios): ")
        try:
            if opcion == "1":
                resultado = evaluar_posfija(expresion)
            else:
                resultado = evaluar_prefija(expresion)
            print(f"Resultado: {resultado:g}")
        except (IndexError, ValueError, ZeroDivisionError) as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
