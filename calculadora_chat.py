#!/usr/bin/env python3
"""
Calculadora Cumulativa para Chat
Criada por Fernando Oliveira (fmoliv)

Uso em chats (Discord, Slack, WhatsApp, etc):
- Usuário: <calc>
- Bot: Pronto! Envie número com sinal (+, -, ×, ÷) ou '=' para finalizar
- Usuário: +100
- Bot: Resultado: 100
- Usuário: ×3
- Bot: Resultado: 300
- Usuário: -50
- Bot: Resultado: 250
- Usuário: =
- Bot: Cálculo final: 250
"""

import re
from typing import Optional, Tuple


class CalculadoraChat:
    """Calculadora cumulativa para uso em chats."""
    
    def __init__(self):
        self.reset()
    
    def reset(self):
        """Reseta o estado da calculadora."""
        self.total = 0
        self.historico = []
        self.ativa = False
        self.primeira_operacao = True
    
    def iniciar(self) -> str:
        """Inicia uma nova sessão de cálculo."""
        self.reset()
        self.ativa = True
        return "🧮 **Calculadora iniciada!**\n\nEnvie números com sinal:\n`+` somar\n`-` subtrair\n`×` ou `*` multiplicar\n`÷` ou `/` dividir\n\nDigite `=` para ver o resultado final."
    
    def processar(self, entrada: str) -> str:
        """Processa uma entrada do usuário."""
        entrada = entrada.strip()
        
        # Comando para iniciar
        if entrada.lower() in ['<calc>', 'calc', 'calculadora', '/calc']:
            return self.iniciar()
        
        # Se não está ativa, ignora
        if not self.ativa:
            return ""
        
        # Comando para finalizar
        if entrada in ['=', 'resultado', 'fim', 'end']:
            return self.finalizar()
        
        # Processa operação
        return self._calcular(entrada)
    
    def _calcular(self, entrada: str) -> str:
        """Realiza o cálculo cumulativo."""
        # Regex para capturar: sinal + número
        padrao = r'^([+\-×÷*/])\s*(\d+(?:\.\d+)?)$'
        match = re.match(padrao, entrada)
        
        if not match:
            return "❌ Formato inválido! Use: `+10`, `-5`, `×3`, `÷2`"
        
        sinal = match.group(1)
        numero = float(match.group(2))
        
        # Converte sinais alternativos
        if sinal == '*':
            sinal = '×'
        elif sinal == '/':
            sinal = '÷'
        
        # Na primeira operação, se for +, apenas atribui
        if self.primeira_operacao:
            if sinal == '+':
                self.total = numero
            elif sinal == '-':
                self.total = -numero
            elif sinal == '×':
                self.total = numero
            elif sinal == '÷':
                if numero == 0:
                    return "❌ Não posso dividir por zero!"
                self.total = numero
            self.primeira_operacao = False
        else:
            # Operações subsequentes
            if sinal == '+':
                self.total += numero
            elif sinal == '-':
                self.total -= numero
            elif sinal == '×':
                self.total *= numero
            elif sinal == '÷':
                if numero == 0:
                    return "❌ Não posso dividir por zero!"
                self.total /= numero
        
        # Registra no histórico
        self.historico.append(f"{sinal}{numero}")
        
        # Formata o resultado
        resultado_formatado = self._formatar_numero(self.total)
        
        # Monta resposta
        if len(self.historico) == 1:
            return f"📊 `{sinal}{self._formatar_numero(numero)}`\n**Resultado:** `{resultado_formatado}`"
        else:
            return f"📊 `{sinal}{self._formatar_numero(numero)}`\n**Resultado:** `{resultado_formatado}`"
    
    def _formatar_numero(self, numero: float) -> str:
        """Formata número para exibição."""
        if numero == int(numero):
            return str(int(numero))
        return f"{numero:.2f}"
    
    def finalizar(self) -> str:
        """Finaliza o cálculo e mostra resumo."""
        if not self.historico:
            return "⚠️ Nenhuma operação realizada."
        
        resultado_final = self._formatar_numero(self.total)
        operacoes = " → ".join(self.historico)
        
        self.ativa = False
        
        return f"""✅ **Cálculo Finalizado!**

📝 Operações: `{operacoes}`
🏆 **Resultado: `{resultado_final}`**

Use `<calc>` para nova calculadora."""
    
    def esta_ativa(self) -> bool:
        """Verifica se há uma calculadora ativa."""
        return self.ativa


# Instância global para manter estado
_calculadoras = {}


def processar_mensagem(user_id: str, mensagem: str) -> str:
    """
    Processa mensagem de um usuário.
    
    Args:
        user_id: ID único do usuário (para manter estado individual)
        mensagem: Mensagem recebida
    
    Returns:
        Resposta da calculadora ou string vazia
    """
    if user_id not in _calculadoras:
        _calculadoras[user_id] = CalculadoraChat()
    
    calc = _calculadoras[user_id]
    resposta = calc.processar(mensagem)
    
    # Limpa se finalizou
    if not calc.esta_ativa() and resposta and "Cálculo Finalizado" in resposta:
        del _calculadoras[user_id]
    
    return resposta


def esta_calculando(user_id: str) -> bool:
    """Verifica se o usuário está em modo calculadora."""
    return user_id in _calculadoras and _calculadoras[user_id].esta_ativa()


# Exemplo de uso direto
if __name__ == "__main__":
    print("🧮 Calculadora Cumulativa para Chat")
    print("=" * 40)
    print()
    
    user_id = "teste"
    
    # Simulação
    print("Usuário: <calc>")
    print("Bot:", processar_mensagem(user_id, "<calc>"))
    print()
    
    print("Usuário: +100")
    print("Bot:", processar_mensagem(user_id, "+100"))
    print()
    
    print("Usuário: ×3")
    print("Bot:", processar_mensagem(user_id, "×3"))
    print()
    
    print("Usuário: -50")
    print("Bot:", processar_mensagem(user_id, "-50"))
    print()
    
    print("Usuário: ÷2")
    print("Bot:", processar_mensagem(user_id, "÷2"))
    print()
    
    print("Usuário: =")
    print("Bot:", processar_mensagem(user_id, "="))
