# Guia de Instalação - calcChat

Guia passo a passo para instalar a calcChat em diferentes plataformas de chat.

---

## 📋 Pré-requisitos

- Python 3.8+
- Token de API da plataforma (Discord, Slack, etc.)

---

## 🤖 Discord

### 1. Criar Aplicação no Discord Developer Portal

1. Acesse: https://discord.com/developers/applications
2. Clique em **"New Application"**
3. Dê um nome (ex: "calcChat") e clique **Create**
4. Vá em **"Bot"** no menu lateral
5. Clique **"Add Bot"** e confirme
6. Copie o **Token** do bot (será usado no código)

### 2. Configurar Permissões

1. Em **"OAuth2"** → **"URL Generator"**
2. Selecione scopes:
   - ✅ `bot`
   - ✅ `applications.commands`
3. Selecione permissões do bot:
   - ✅ `Send Messages`
   - ✅ `Read Message History`
   - ✅ `View Channels`
4. Copie a URL gerada e abra no navegador
5. Selecione o servidor e autorize

### 3. Instalar Código

```bash
# Clone o repositório
git clone https://github.com/fmoliv/calcChat.git
cd calcChat

# Instale as dependências
pip install discord.py

# Crie o arquivo bot_discord.py
```

### 4. Código do Bot (bot_discord.py)

```python
import discord
from discord.ext import commands
from calculadora_chat import processar_mensagem, esta_calculando

# CONFIGURAÇÃO
token = "SEU_TOKEN_AQUI"  # Cole o token do passo 1
prefixo = "!"

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=prefixo, intents=intents)

@bot.event
async def on_ready():
    print(f'✅ calcChat conectado como {bot.user}')
    print(f'Convite: https://discord.com/oauth2/authorize?client_id={bot.user.id}&scope=bot')

@bot.event
async def on_message(message):
    # Ignora mensagens do próprio bot
    if message.author == bot.user:
        return
    
    user_id = str(message.author.id)
    conteudo = message.content.strip()
    
    # Processa na calculadora
    resposta = processar_mensagem(user_id, conteudo)
    
    if resposta:
        await message.reply(resposta)
    
    # Processa comandos normais
    await bot.process_commands(message)

# Comando alternativo
@bot.command()
async def calc(ctx):
    """Inicia a calculadora cumulativa."""
    user_id = str(ctx.author.id)
    resposta = processar_mensagem(user_id, "<calc>")
    await ctx.reply(resposta)

# Inicia o bot
bot.run(token)
```

### 5. Executar

```bash
python bot_discord.py
```

---

## 💬 Slack

### 1. Criar App no Slack API

1. Acesse: https://api.slack.com/apps
2. Clique **"Create New App"** → **"From scratch"**
3. Nome: "calcChat" e selecione seu workspace
4. Clique **"Create App"**

### 2. Configurar Permissões

1. Vá em **"OAuth & Permissions"**
2. Em **"Scopes"** → **"Bot Token Scopes"**, adicione:
   - `chat:write`
   - `im:read`
   - `im:write`
   - `mpim:read`
   - `mpim:write`
3. Clique **"Install to Workspace"**
4. Copie o **"Bot User OAuth Token"** (começa com `xoxb-`)

### 3. Habilitar Eventos (opcional, para DMs)

1. Vá em **"Socket Mode"** → ative
2. Vá em **"Event Subscriptions"** → ative
3. Em **"Subscribe to bot events"**, adicione:
   - `message.im` (mensagens diretas)
   - `message.channels` (canais)

### 4. Instalar Código

```bash
git clone https://github.com/fmoliv/calcChat.git
cd calcChat
pip install slack-bolt
```

### 5. Código do Bot (bot_slack.py)

```python
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from calculadora_chat import processar_mensagem

# CONFIGURAÇÃO
bot_token = "xoxb-SEU-TOKEN-AQUI"  # Do passo 2
app_token = "xapp-SEU-APP-TOKEN"    # Socket Mode → App-Level Token

app = App(token=bot_token)

@app.message(r"<calc>|^[+\-×÷*/].*")
def handle_calc(message, say, context):
    user_id = message['user']
    text = message['text'].strip()
    
    resposta = processar_mensagem(user_id, text)
    
    if resposta:
        say(resposta)

@app.command("/calc")
def handle_command(ack, command, say):
    ack()
    user_id = command['user_id']
    resposta = processar_mensagem(user_id, "<calc>")
    say(resposta)

if __name__ == "__main__":
    print("✅ calcChat iniciado no Slack!")
    handler = SocketModeHandler(app, app_token)
    handler.start()
```

### 6. Executar

```bash
python bot_slack.py
```

---

## ✈️ Telegram

### 1. Criar Bot no Telegram

1. Abra o Telegram e procure por **@BotFather**
2. Envie `/newbot`
3. Escolha um nome (ex: "calcChat")
4. Escolha um username (ex: "calcchat_bot")
5. Copie o **token** fornecido

### 2. Instalar Código

```bash
git clone https://github.com/fmoliv/calcChat.git
cd calcChat
pip install python-telegram-bot
```

### 3. Código do Bot (bot_telegram.py)

```python
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
from calculadora_chat import processar_mensagem

# CONFIGURAÇÃO
token = "SEU_TOKEN_AQUI"  # Do @BotFather

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    text = update.message.text.strip()
    
    resposta = processar_mensagem(user_id, text)
    
    if resposta:
        await update.message.reply_text(resposta, parse_mode='Markdown')

def main():
    application = Application.builder().token(token).build()
    
    # Processa todas as mensagens
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    print("✅ calcChat iniciado no Telegram!")
    application.run_polling()

if __name__ == "__main__":
    main()
```

### 4. Executar

```bash
python bot_telegram.py
```

---

## 📱 WhatsApp

**Nota:** O WhatsApp não permite bots oficiais facilmente. As opções são:

### Opção A: WhatsApp Business API (Oficial)
- Requer Meta Business Verification
- Pago (aprox. $0.005 por mensagem)
- Complexo de configurar

### Opção B: Bibliotecas não-oficiais (Desenvolvimento/Teste)

**Aviso:** Use apenas para testes. Pode violar Termos de Serviço.

```bash
pip install pywhatkit  # ou whatsapp-web-api
```

**Recomendação:** Para produção, use **Twilio WhatsApp API**:

1. Crie conta em https://www.twilio.com/whatsapp
2. Siga o guia de sandbox do Twilio
3. Use a API do Twilio para enviar/receber mensagens

---

## 🌐 Web (Navegador)

Para usar em qualquer chat web:

### 1. Instalar Tampermonkey/Greasemonkey

### 2. Criar Userscript

```javascript
// ==UserScript==
// @name         calcChat Universal
// @match         *://*/*
// @grant        none
// ==/UserScript==

// Este é um exemplo simplificado
// Implementação completa requer adaptação por site

(function() {
    'use strict';
    
    // Detecta campo de input do chat
    // Processa comandos <calc>
    // Mostra resultado
    
    console.log('calcChat carregado!');
})();
```

---

## 🐳 Docker (Todas as Plataformas)

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "bot_discord.py"]  # ou bot_slack.py, etc.
```

```bash
# Build
docker build -t calchat .

# Run
docker run -e DISCORD_TOKEN=seu_token calchat
```

---

## 🔧 Solução de Problemas

| Problema | Solução |
|----------|---------|
| Bot não responde | Verifique se o token está correto |
| "Intents não habilitados" | Ative Message Content Intent no portal |
| Erro de permissão | Reconvide o bot com permissões corretas |
| Mensagem não processada | Verifique se a mensagem começa com `<calc>` ou operador |

---

## 📞 Suporte

- **GitHub Issues:** https://github.com/fmoliv/calcChat/issues
- **Autor:** Fernando Oliveira (fmoliv)

---

## 📄 Licença

MIT - Veja LICENSE para detalhes
