import requests
import html

@friday.on(friday_on_cmd(pattern="analyse"))
async def mar(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("Reply To Message To Scan")
        return
    sadly = await event.get_reply_message()
    if not sadly.text:
        await event.edit("`I Can Only Scan Texts !`")
        return
    lol_s = {
      'text': sadly.raw_text
      }
    r = requests.get("https://devsexpo.me/spam", headers=lol_s).json()
    sed_rip = f"""<b><u>Text Scanned SucessFully !</b></u>
<b>Text :</b> <code>{sadly.raw_text}</code>
<b>Spam Percentage :</b> <code>{r['spam']}</code>
<b>Ham Percentage :</b> <code>{r['ham']}</code>
<b>Prediction :</b> <code>{r['prediction']}</code>
"""
    await event.edit(sed_rip, parse_mode="HTML")
