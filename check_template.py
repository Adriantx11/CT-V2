import requests
from func_bin import get_bin_info

def checking_template(ccvip, msg, respuesta, gateway, tiempo, username, user_rank, proxyy):
    x = get_bin_info(ccvip[:6])

    return f"""<b>
[<a href="https://t.me/UmbrellaScrapp2">✯</a>] 𝑼𝑴𝑩𝑹𝑬𝑳𝑳𝑨 𝑪𝑯𝑲
[<a href="https://t.me/UmbrellaScrapp2">✯</a>] Gateway ↯ <code>{gateway}</code>   
━━━━━━━━━━━━━━━━
[<a href="https://t.me/UmbrellaScrapp2">✯</a>] CC ↯ <code>{ccvip}</code>
[<a href="https://t.me/UmbrellaScrapp2">✯</a>] Status ↯ <b>{msg}</b> 
[<a href="https://t.me/UmbrellaScrapp2">✯</a>] Result ↯ {respuesta}
━━━━━━━━━━━━━━━━
[<a href="https://t.me/UmbrellaScrapp2">✯</a>] Bin ↯ <code>{x.get("type")}</code> | <code>{x.get("level")}</code> | <code>{x.get("vendor")}</code>
[<a href="https://t.me/UmbrellaScrapp2">✯</a>] Country ↯ <code>{x.get("country")} {x.get("flag")}</code>
[<a href="https://t.me/UmbrellaScrapp2">✯</a>] Bank ↯ <code>{x.get("bank_name")}</code>
━━━━━━━━━━━━━━━━
[<a href="https://t.me/UmbrellaScrapp2">✯</a>] Proxy  ↯ <code>{proxyy}</code>
[<a href="https://t.me/UmbrellaScrapp2">✯</a>] Time taken ↯ <code>{tiempo} (segundos)</code>
[<a href="https://t.me/UmbrellaScrapp2">✯</a>] Checked by ↯ @{username} [{user_rank}]
[<a href="https://t.me/UmbrellaScrapp2">✯</a>] Bot by ↯ @jxrdan_09 </b>"""