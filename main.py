from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes
import os
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading

# --- CONFIGURAÇÕES ---
TOKEN = "8759967028:AAGdQroAvTQppGuvISc0AUEtGxQOTIV7CY0"
MEU_ID_TELEGRAM = 7585540402 

# --- FUNÇÕES DO BOT ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("📊 Ver Tabela de Preços", callback_data="tabela")]]
    await update.message.reply_text("Bem-vindo! Clique abaixo para ver a tabela:", reply_markup=InlineKeyboardMarkup(keyboard))

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    query = update.callback_query
    
    if query.data == "tabela":
        texto_fiel = """PREÇOS DE VIDEOS ARQUIVOS MEGA LINK/GRUPO
CP 9-14 ANOS E ADOLESCENTES 15-17.
R$20: POR 75 GB = 100 VIDEOS HD
R$25: POR 99GB = 350 VIDEOS HD
R$30: POR 148GB = 800 VIDEOS HD
R$35: por 252GB = 1.000 videos HD
R$45: por 349GB = 2.000 videos HD
R$50: por 500GB = 5.600 videos HD
R$55: por 745GB = 7.678 videos HD
R$60: por 1.000GB = 14.000 videos
R$75: por 1.350GB = 17.000 videos
R$200: acesso total e atualizações
R$500: contato do fornecedor.

Ao realizar pagamento mande o comprovante OBRIGATORIAMENTE."""

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
        pix_msg = "✅ **CHAVE PIX**\n\n`36b739bf-a587-4ed5-b32c-f57225f85c2a`\n\n👤 **Dono:** Deivid Aprígio\n\nEnvie o comprovante agora!"
        await query.message.reply_text(pix_msg, parse_mode='Markdown')

async def receber_comprovante(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Comprovante recebido! Aguarde a verificação.")
    await context.bot.forward_message(chat_id=MEU_ID_TELEGRAM, from_chat_id=update.message.chat_id, message_id=update.message.message_id)
    await context.bot.send_message(chat_id=MEU_ID_TELEGRAM, text=f"📩 **Novo comprovante de:** @{update.message.from_user.username}")

# --- SERVIDOR PARA O RENDER ---
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is alive!")

def run_server():
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(("", port), Handler)
    server.serve_forever()

# --- INICIALIZAÇÃO ---
if __name__ == '__main__':
    threading.Thread(target=run_server, daemon=True).start()
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.add_handler(MessageHandler(filters.PHOTO, receber_comprovante))
    
    print("Bot online!")
    app.run_polling(poll_interval=0.5)
        
