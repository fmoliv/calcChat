# Calculadora Cumulativa para Chat

Calculadora interativa que funciona em chats (Discord, Slack, WhatsApp, Telegram, etc).

## 🚀 Como Funciona

A calculadora acumula resultados passo a passo. Você envia um número com sinal, ela calcula e mostra o resultado atual.

### Exemplo de Conversa

```
Você:    <calc>
Bot:     🧮 Calculadora iniciada!
         Envie números com sinal:
         + somar, - subtrair, × multiplicar, ÷ dividir
         Digite = para ver o resultado final.

Você:    +100
Bot:     📊 +100
         Resultado: 100

Você:    ×3
Bot:     📊 ×3
         Resultado: 300

Você:    -50
Bot:     📊 -50
         Resultado: 250

Você:    ÷2
Bot:     📊 ÷2
         Resultado: 125

Você:    =
Bot:     ✅ Cálculo Finalizado!
         Operações: +100 → ×3 → -50 → ÷2
         Resultado: 125
```

## 📝 Comandos

| Comando | Descrição |
|---------|-----------|
| `<calc>` | Inicia a calculadora |
| `+10` | Soma 10 |
| `-5` | Subtrai 5 |
| `×3` ou `*3` | Multiplica por 3 |
| `÷2` ou `/2` | Divide por 2 |
| `=` | Finaliza e mostra resultado |

## 💻 Uso em Código

```python
from calculadora_chat import processar_mensagem

# Inicia
resposta = processar_mensagem("user_123", "<calc>")

# Operações
resposta = processar_mensagem("user_123", "+100")   # Resultado: 100
resposta = processar_mensagem("user_123", "×3")     # Resultado: 300
resposta = processar_mensagem("user_123", "-50")    # Resultado: 250

# Finaliza
resposta = processar_mensagem("user_123", "=")
```

## 🔌 Instalação em Plataformas

Veja o guia completo em **[INSTALACAO.md](INSTALACAO.md)** para instalar em:

- 🤖 **Discord** - Bot completo com permissões
- 💬 **Slack** - App com Socket Mode
- ✈️ **Telegram** - Bot via @BotFather
- 📱 **WhatsApp** - Opções oficial e alternativas
- 🌐 **Web** - Userscript universal

### Exemplo Rápido (Discord)

```python
import discord
from calculadora_chat import processar_mensagem

@bot.event
async def on_message(message):
    resposta = processar_mensagem(str(message.author.id), message.content)
    if resposta:
        await message.reply(resposta)
```

## 👤 Autor

Criada por **Fernando Oliveira (fmoliv)**

## 📄 Licença

MIT
