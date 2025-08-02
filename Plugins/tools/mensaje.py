from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Plugins.Func import connect_to_db
import asyncio
import random

footer_banner1 = 'https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3anRhMTd4cW5pOGFlbW5wcXMyemFiZjd1ZTl5dWQ2MzVpYmVlb2w4ZSZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/mOUG4Y3wwnkYw/giphy.gif'

# Cargo los IDs permitidos una vez
with open('owner.txt', 'r') as file:
    IDS_PERMITIDOS = set(file.read().splitlines())

imagen_urls = [
    "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3anRhMTd4cW5pOGFlbW5wcXMyemFiZjd1ZTl5dWQ2MzVpYmVlb2w4ZSZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/mOUG4Y3wwnkYw/giphy.gif"
]

semaforo = asyncio.Semaphore(5)

async def obtener_ids_usuarios():
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT user_id FROM users")
    resultados = cursor.fetchall()
    return [str(row[0]) for row in resultados]

async def enviar_foto_con_semaforo(client, user_id, imagen_url, caption, keyboard):
    async with semaforo:
        await client.send_photo(user_id, imagen_url, caption=caption, reply_markup=keyboard)

@Client.on_message(filters.command("mensaje", prefixes=['.','/','!','?'], case_sensitive=False) & filters.text)
async def enviar_mensaje_privado(client, message):
    remitente_id = message.from_user.id

    if str(remitente_id) not in IDS_PERMITIDOS:
        await client.send_message(message.chat.id, f"Lo siento, no tienes permisos para hacer esto.<a href='{footer_banner1}'>&#8203;</a>")
        return
    
    texto_comando = message.text.split(maxsplit=1)
    if len(texto_comando) < 2:
        await message.reply(f"Debes proporcionar texto después del comando /mensaje. <a href='{footer_banner1}'>&#8203;</a>")
        return

    mensaje_personalizado = texto_comando[1]

    await client.send_message(message.chat.id, f"El mensaje se está enviando a todos los usuarios. <a href='{footer_banner1}'>&#8203;</a>")

    ids_usuarios = await obtener_ids_usuarios()

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("REFERENCIAS", url="https://t.me/UmbrellaScrapp2"),
                InlineKeyboardButton("SCRAPP FREE", url="https://t.me/UmbrellaScrapp2"),
            ],
            [
                InlineKeyboardButton("GRUPO OFICIAL", url="https://t.me/+uFwPtvTJpU42NGVh")
            ]
        ]
    )

    errores = []
    tasks = []
    for user_id in ids_usuarios:
        try:
            imagen_url = random.choice(imagen_urls)
            task = enviar_foto_con_semaforo(client, user_id, imagen_url, f"<b>{mensaje_personalizado}</b>", keyboard)
            tasks.append(task)
        except Exception as e:
            errores.append(f"{user_id}: {str(e)}")

    await asyncio.gather(*tasks)

    await client.send_message(message.chat.id, f"El mensaje se ha enviado a todos los usuarios. <a href='{footer_banner1}'>&#8203;</a>")

    if errores:
        # Envía solo resumen de errores para no spamear
        resumen = "\n".join(errores[:10])  # máximo 10 errores listados
        await client.send_message(message.chat.id, f"Errores al enviar a algunos usuarios:\n{resumen}... <a href='{footer_banner1}'>&#8203;</a>")
