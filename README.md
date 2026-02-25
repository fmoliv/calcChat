# Calculadora Python

Calculadora completa em Python com operações básicas e científicas.

## 🚀 Funcionalidades

### Operações Básicas
- ➕ Soma
- ➖ Subtração
- ✖️ Multiplicação
- ➗ Divisão

### Operações Científicas
- 🔢 Potência
- √ Raiz quadrada
- 📐 Seno e Cosseno
- 📊 Logaritmo
- ❗ Fatorial

### Extras
- 📜 Histórico de operações
- 🎯 Menu interativo

## 📦 Instalação

```bash
git clone https://github.com/fmoliv/calculadora.git
cd calculadora
```

## 🎮 Uso

### Modo Interativo
```bash
python calculadora.py
```

### Uso como Biblioteca
```python
from calculadora import Calculadora

calc = Calculadora()

# Operações básicas
print(calc.somar(10, 5))        # 15
print(calc.subtrair(10, 5))     # 5
print(calc.multiplicar(10, 5))  # 50
print(calc.dividir(10, 5))      # 2.0

# Operações científicas
print(calc.potencia(2, 3))      # 8
print(calc.raiz_quadrada(16))   # 4.0
print(calc.seno(30))            # 0.5
print(calc.fatorial(5))         # 120

# Histórico
print(calc.ver_historico())
```

## 👤 Autor

Criada por **OpenClaw** para **Fernando Oliveira**

## 📄 Licença

MIT
