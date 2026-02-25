#!/usr/bin/env python3
"""
Calculadora Python
Criada por OpenClaw para Fernando Oliveira
"""

import math


class Calculadora:
    """Calculadora com operações básicas e científicas."""
    
    def __init__(self):
        self.historico = []
    
    # Operações Básicas
    def somar(self, a, b):
        """Soma dois números."""
        resultado = a + b
        self._registrar(f"{a} + {b} = {resultado}")
        return resultado
    
    def subtrair(self, a, b):
        """Subtrai dois números."""
        resultado = a - b
        self._registrar(f"{a} - {b} = {resultado}")
        return resultado
    
    def multiplicar(self, a, b):
        """Multiplica dois números."""
        resultado = a * b
        self._registrar(f"{a} × {b} = {resultado}")
        return resultado
    
    def dividir(self, a, b):
        """Divide dois números."""
        if b == 0:
            raise ValueError("Não é possível dividir por zero!")
        resultado = a / b
        self._registrar(f"{a} ÷ {b} = {resultado}")
        return resultado
    
    # Operações Científicas
    def potencia(self, base, expoente):
        """Calcula potência."""
        resultado = base ** expoente
        self._registrar(f"{base}^{expoente} = {resultado}")
        return resultado
    
    def raiz_quadrada(self, n):
        """Calcula raiz quadrada."""
        if n < 0:
            raise ValueError("Não existe raiz quadrada de número negativo!")
        resultado = math.sqrt(n)
        self._registrar(f"√{n} = {resultado}")
        return resultado
    
    def seno(self, angulo_graus):
        """Calcula seno do ângulo em graus."""
        rad = math.radians(angulo_graus)
        resultado = math.sin(rad)
        self._registrar(f"sen({angulo_graus}°) = {resultado}")
        return resultado
    
    def cosseno(self, angulo_graus):
        """Calcula cosseno do ângulo em graus."""
        rad = math.radians(angulo_graus)
        resultado = math.cos(rad)
        self._registrar(f"cos({angulo_graus}°) = {resultado}")
        return resultado
    
    def logaritmo(self, n, base=10):
        """Calcula logaritmo."""
        if n <= 0:
            raise ValueError("Logaritmo só definido para números positivos!")
        if base == 10:
            resultado = math.log10(n)
            self._registrar(f"log({n}) = {resultado}")
        else:
            resultado = math.log(n, base)
            self._registrar(f"log_{base}({n}) = {resultado}")
        return resultado
    
    def fatorial(self, n):
        """Calcula fatorial."""
        if n < 0 or not isinstance(n, int):
            raise ValueError("Fatorial só definido para inteiros não-negativos!")
        resultado = math.factorial(n)
        self._registrar(f"{n}! = {resultado}")
        return resultado
    
    # Histórico
    def _registrar(self, operacao):
        """Registra operação no histórico."""
        self.historico.append(operacao)
    
    def ver_historico(self):
        """Retorna histórico de operações."""
        return self.historico
    
    def limpar_historico(self):
        """Limpa histórico."""
        self.historico = []


def menu_interativo():
    """Menu interativo da calculadora."""
    calc = Calculadora()
    
    print("=" * 40)
    print("🧮 CALCULADORA PYTHON")
    print("Criada por OpenClaw para Fernando Oliveira")
    print("=" * 40)
    
    while True:
        print("\nOperações:")
        print("1. Somar")
        print("2. Subtrair")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Potência")
        print("6. Raiz Quadrada")
        print("7. Seno")
        print("8. Cosseno")
        print("9. Logaritmo")
        print("10. Fatorial")
        print("11. Ver Histórico")
        print("12. Limpar Histórico")
        print("0. Sair")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "0":
            print("Até logo! 👋")
            break
        
        try:
            if opcao == "1":
                a = float(input("Primeiro número: "))
                b = float(input("Segundo número: "))
                print(f"Resultado: {calc.somar(a, b)}")
            
            elif opcao == "2":
                a = float(input("Primeiro número: "))
                b = float(input("Segundo número: "))
                print(f"Resultado: {calc.subtrair(a, b)}")
            
            elif opcao == "3":
                a = float(input("Primeiro número: "))
                b = float(input("Segundo número: "))
                print(f"Resultado: {calc.multiplicar(a, b)}")
            
            elif opcao == "4":
                a = float(input("Primeiro número: "))
                b = float(input("Segundo número: "))
                print(f"Resultado: {calc.dividir(a, b)}")
            
            elif opcao == "5":
                base = float(input("Base: "))
                exp = float(input("Expoente: "))
                print(f"Resultado: {calc.potencia(base, exp)}")
            
            elif opcao == "6":
                n = float(input("Número: "))
                print(f"Resultado: {calc.raiz_quadrada(n)}")
            
            elif opcao == "7":
                ang = float(input("Ângulo em graus: "))
                print(f"Resultado: {calc.seno(ang)}")
            
            elif opcao == "8":
                ang = float(input("Ângulo em graus: "))
                print(f"Resultado: {calc.cosseno(ang)}")
            
            elif opcao == "9":
                n = float(input("Número: "))
                base = input("Base (Enter para base 10): ")
                base = float(base) if base else 10
                print(f"Resultado: {calc.logaritmo(n, base)}")
            
            elif opcao == "10":
                n = int(input("Número inteiro: "))
                print(f"Resultado: {calc.fatorial(n)}")
            
            elif opcao == "11":
                hist = calc.ver_historico()
                if hist:
                    print("\n📜 Histórico:")
                    for op in hist:
                        print(f"  {op}")
                else:
                    print("Histórico vazio!")
            
            elif opcao == "12":
                calc.limpar_historico()
                print("Histórico limpo!")
            
            else:
                print("Opção inválida!")
        
        except ValueError as e:
            print(f"Erro: {e}")
        except Exception as e:
            print(f"Erro inesperado: {e}")


if __name__ == "__main__":
    menu_interativo()
