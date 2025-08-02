from asyncio import sleep
from pyrogram import Client, filters
import datetime

from Plugins.Func import connect_to_db

def buscar_info_usuario(user_id):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute('SELECT rango, creditos, antispam, dias FROM users WHERE user_id = ?', (user_id,))
    user_info = cursor.fetchone()
    conn.close()
    return user_info

@Client.on_message(filters.command(["buscar"], ["/", "."]))
async def buscar(client, message):
    conn = connect_to_db()
    cursor = conn.cursor()
    user_id2 = message.from_user.id

    cursor.execute('SELECT rango FROM users WHERE user_id = ?', (user_id2,))
    user_data = cursor.fetchone()

    if not user_data:
        return await message.reply("❌ No estás registrado en la base de datos.")

    if all(role not in user_data[0] for role in ["Seller", "Owner"]):
        return await message.reply(
            "<b>Access Denied.❌</b> <a href='https://imgur.com/a/PKhb18E.jpeg'>&#8203;</a>"
        )

    # Validar que se haya enviado un ID a buscar
    parts = message.text.strip().split()
    if len(parts) < 2:
        return await message.reply("❌ Usa: /buscar <user_id>")

    user_id = parts[1]

    # Obtener info del usuario a buscar
    try:
        user = await client.get_users(user_id)
        username = user.username or "Sin username"
    except Exception as e:
        return await message.reply(f"❌ Error al obtener el usuario: {e}")

    user_info = buscar_info_usuario(user_id)
    if user_info:
        rango, creditos, antispam, dias = user_info
        footer_banner1 = 'https://imgur.com/a/PKhb18E.jpeg'
        
        respuesta = f"""<a href='{footer_banner1}'>&#8203;</a>[<a href="https://t.me/UmbrellaScrapp2">✯</a>] 𝑼𝑴𝑩𝑹𝑬𝑳𝑳𝑨 𝑪𝑯𝑲
[<a href="https://t.me/UmbrellaScrapp2">✯</a>] User ID ↯ {user_id} 
[<a href="https://t.me/UmbrellaScrapp2">✯</a>] Info User ↯ @{username} 
━━━━━━━━━━━━━━━━
[<a href="https://t.me/UmbrellaScrapp2">✯</a>] Rango ↯ <code>{rango}</code>
[<a href="https://t.me/UmbrellaScrapp2">✯</a>] Días de acceso ↯ <code>{dias}</code>
[<a href="https://t.me/UmbrellaScrapp2">✯</a>] Créditos ↯ <code>{creditos}</code>
━━━━━━━━━━━━━━━━"""
        await message.reply(respuesta)
    else:
        await message.reply("❌ Usuario no encontrado en la base de datos.")
