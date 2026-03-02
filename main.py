from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

TOKEN = "8759967028:AAGdQroAvTQppGuvISc0AUEtGxQOTIV7CY0"
MEU_ID_TELEGRAM = 7585540402  # <--- COLOQUE SEU ID AQUI (Ex: 123456789)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("📊 Ver Tabela de Preços", callback_data="tabela")]]
    await update.message.reply_text("Bem-vindo! Clique abaixo para ver a tabela:", reply_markup=InlineKeyboardMarkup(keyboard))

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    query = update.callback_query
    
    if query.data == "tabela":
        texto_fiel = """PREÇOS DE VIDEOS ARQUIVOS MEGA LINK/GRUPO
CP 9-14 ANOS E ADOLESCENTES 15-17.
$20:POR 75 GB =100 VIDEOS HD
R$25 POR 99GB =350 VIDEOS HD
R$30POR 148GB =800 VIDEOS HD
R$35:por 252GB =1.000 videos HD
R$45:por349GB =2.000 videos HD
R$50:por 500GB =5.600 videos HD
55$:por 745GB =7.678 videos HD
R$60:por 1.000GB = 14.000 videos
R$75:por 1.350GB =17.000 videos
R$200:acesso a todos os 40 mil videos (grupo e arquivos) e as atualizações do grupo Mensalmente
R$500: contato do fornecedor.

Ao realizar pagamento mande o comprovante OBRIGATORIAMENTE.
Lembre-se que cada valor é um grupo diferente.

Se tentar adicionar alguem ao grupo,será REMOVIDO sem rembolso.

                   LEIA COM ATENÇÃO.

Após o pagamento será mandado imediatamente link do grupo correspondente a sua escolha."""

        keyboard = [
            [InlineKeyboardButton("Pagar R$20", callback_data="v1"), InlineKeyboardButton("Pagar R$25", callback_data="v2")],
            [InlineKeyboardButton("Pagar R$30", callback_data="v3"), InlineKeyboardButton("Pagar R$35", callback_data="v4")],
            [InlineKeyboardButton("Pagar R$45", callback_data="v5"), InlineKeyboardButton("Pagar R$50", callback_data="v6")],
            [InlineKeyboardButton("Pagar R$55", callback_data="v7"), InlineKeyboardButton("Pagar R$60", callback_data="v8")],
            [InlineKeyboardButton("Pagar R$75", callback_data="v9"), InlineKeyboardButton("Pagar R$200", callback_data="v10")],
            [InlineKeyboardButton("💎 Fornecedor R$500", callback_data="v11")]
        ]
        await query.edit_message_text(texto_fiel, reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data.startswith("v"):
        pix_msg = "✅ **CHAVE PIX**\n\n`36b739bf-a587-4ed5-b32c-f57225f85c2a`\n\n👤 **Dono:** \"Deivid Aprígio\" 🍊\n\nEnvie o comprovante agora!"
        await query.message.reply_text(pix_msg, parse_mode='Markdown')

# NOVA FUNÇÃO PARA RECEBER O COMPROVANTE
async def receber_comprovante(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if MEU_ID_TELEGRAM == 0:
        print("Erro: Você esqueceu de colocar seu ID na linha 6!")
        return

    # Avisa o cliente
    await update.message.reply_text("✅ Comprovante recebido! Aguarde enquanto verificamos seu acesso.")
    
    # Encaminha a foto para você
    await context.bot.forward_message(
        chat_id=MEU_ID_TELEGRAM, 
        from_chat_id=update.message.chat_id, 
        message_id=update.message.message_id
    )
    # Avisa você quem mandou
    await context.bot.send_message(
        chat_id=MEU_ID_TELEGRAM, 
        text=f"📩 **Novo comprovante recebido de:** @{update.message.from_user.username}"
    )
# ... (resto do seu código acima)

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    
    # Registra seus handlers aqui
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    
    print("Bot online! Agora você receberá as notificações.")
    
    import os
    from http.server import HTTPServer, BaseHTTPRequestHandler
    import threading

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Bot is alive!")

    def run_server():
        port = int(os.environ.get("PORT", 8080))
        server = HTTPServer(("", port), Handler)
        server.serve_forever()

    threading.Thread(target=run_server, daemon=True).start()
    app.run_polling(poll_interval=0.5)
    
