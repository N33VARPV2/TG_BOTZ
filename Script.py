class script(object):
    START_TXT = """<b>Hᴇʟʟᴏ 👋 {}</b>

<b>Mʏ Nᴀᴍᴇ Is <a href="https://t.me/{}">{}</a>, I Cᴀɴ Pʀᴏᴠɪᴅᴇ Mᴏᴠɪᴇs, Sᴇʀɪᴇs, Aɴɪᴍᴀᴛɪᴏɴ, Cᴀʀᴛᴏᴏɴ, Aɴɪᴍᴇ, K-Dʀᴀᴍᴀ & Mᴀɴʏ Mᴏʀᴇ ☺ Jᴜsᴛ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ As Aᴅᴍɪɴ EɴJᴏʏ 😍</b>

<b>Mᴀᴅᴇ Wɪᴛʜ ❤ Bʏ @N33VARP </b>"""

    HELP_TXT = """<b>Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Mʏ Cᴏᴍᴍᴀɴᴅs.</b>"""
 
    ABOUT_TXT = """<b>
‣ Mʏ Nᴀᴍᴇ : <a href="https://t.me/{}">{}</a>
‣ Cʀᴇᴀᴛᴏʀ : <a href="https://t.me/N33VARP">ɴ𝟹𝟹ᴠᴀʀᴘ</a>
‣ Lɪʙʀᴀʀʏ : <a href="https://pyrogram.org/">Pʏʀᴏɢʀᴀᴍ</a>
‣ Lᴀɴɢᴜᴀɢᴇ : <a href="https://www.python.org/">Pʏᴛʜᴏɴ</a>
‣ Dᴀᴛᴀ Bᴀsᴇ : <a href="https://www.mongodb.com/">Mᴏɴɢᴏ DB</a>
‣ Hᴏsᴛᴇᴅ Oɴ : <a href="https://render.com/">Rᴇɴᴅᴇʀ</a>
‣ Bᴜɪʟᴅ Sᴛᴀᴛᴜs : ᴠ𝟹.𝟶 [Sᴛᴀʙʟᴇ]</b>"""
                  
    DISCLAIMER_TXT =  """<b>Tʜɪs Is Aɴ Oᴘᴇɴ Sᴏᴜʀᴄᴇ PʀᴏJᴇᴄᴛ.

Aʟʟ Tʜᴇ Fɪʟᴇs Iɴ Tʜɪs Bᴏᴛ Aʀᴇ Fʀᴇᴇʟʏ Aᴠᴀɪʟᴀʙʟᴇ Oɴ Tʜᴇ Iɴᴛᴇʀɴᴇᴛ Oʀ Pᴏsᴛᴇᴅ Bʏ Sᴏᴍᴇʙᴏᴅʏ Eʟsᴇ. Jᴜsᴛ Fᴏʀ Eᴀsʏ Sᴇᴀʀᴄʜɪɴɢ Tʜɪs Bᴏᴛ Is Iɴᴅᴇxɪɴɢ Fɪʟᴇs Wʜɪᴄʜ Aʀᴇ Aʟʀᴇᴀᴅʏ Uᴘʟᴏᴀᴅᴇᴅ Oɴ Tᴇʟᴇɢʀᴀᴍ. ᴡᴇ Rᴇsᴘᴇᴄᴛ Aʟʟ Tʜᴇ Cᴏᴘʏʀɪɢʜᴛ Lᴀᴡs Aɴᴅ Wᴏʀᴋs Iɴ Cᴏᴍᴘʟɪᴀɴᴄᴇ Wɪᴛʜ DMCA Aɴᴅ EUCD. Iғ Aɴʏᴛʜɪɴɢ Is Aɢᴀɪɴsᴛ Lᴀᴡ Pʟᴇᴀsᴇ Cᴏɴᴛᴀᴄᴛ Mᴇ Sᴏ Tʜᴀᴛ Iᴛ Cᴀɴ Bᴇ Rᴇᴍᴏᴠᴇᴅ ASAP. Iᴛ Is Fᴏʀʙɪᴅᴅᴇɴ Tᴏ Dᴏᴡɴʟᴏᴀᴅ, Sᴛʀᴇᴀᴍ, Rᴇᴘʀᴏᴅᴜᴄᴇ, Sʜᴀʀᴇ Oʀ Cᴏɴsᴜᴍᴇ Cᴏɴᴛᴇɴᴛ Wɪᴛʜᴏᴜᴛ Exᴘʟɪᴄɪᴛ Pᴇʀᴍɪssɪᴏɴ Fʀᴏᴍ Tʜᴇ Cᴏɴᴛᴇɴᴛ Wɪᴛʜᴏᴜᴛ Exᴘʟɪᴄɪᴛ Pᴇʀᴍɪssɪᴏɴ Fʀᴏᴍ Tʜᴇ Cᴏɴᴛᴇɴᴛ Cʀᴇᴀᴛᴏʀ Oʀ Lᴇɢᴀʟ Cᴏᴘʏʀɪɢʜᴛ Hᴏʟᴅᴇʀ. Iғ Yᴏᴜ Bᴇʟɪᴇᴠᴇ Tʜɪs Bᴏᴛ Is Vɪᴏʟᴀᴛɪɴɢ Yᴏᴜʀ Iɴᴛᴇʟʟᴇᴄᴛᴜᴀʟ Pʀᴏᴘᴇʀᴛʏ, Cᴏɴᴛᴀᴄᴛ Tʜᴇ Rᴇsᴘᴇᴄᴛɪᴠᴇ Cʜᴀɴɴᴇʟs Fᴏʀ Rᴇᴍᴏᴠᴀʟ. Tʜᴇ Bᴏᴛ Dᴏᴇs Nᴏᴛ Oᴡɴ Aɴʏ Oғ Tʜᴇsᴇ Cᴏɴᴛᴇɴᴛs, Iᴛ Oɴʟʏ Iɴᴅᴇx Tʜᴇ Fɪʟᴇs Fʀᴏᴍ Tᴇʟᴇɢʀᴀᴍ.

Mᴀɪɴᴛᴀɪɴᴇᴅ Bʏ : <a href="https://t.me/N33VARP">ɴ𝟹𝟹ᴠᴀʀᴘ</a></b>"""

    SETTINGS_TXT = """
Hᴇʟᴘ : <b>Sᴇᴛᴛɪɴɢꜱ</b>
    
◈ sᴇᴛᴛɪɴɢs ɪs ᴍᴏsᴛ ɪᴍᴘᴏʀᴛᴀɴᴛ ғᴇᴀᴛᴜʀᴇ ɪɴ ᴛʜɪs ʙᴏᴛ.
◈ ʏᴏᴜ ᴄᴀɴ ᴇᴀsɪʟʏ ᴄᴜsᴛᴏᴍɪᴢᴇ ᴛʜɪs ʙᴏᴛ ғᴏʀ ʏᴏᴜʀ ɢʀᴏᴜᴘ.

<b>Nᴏᴛᴇ :</b>
1. ᴏɴʟʏ ɢʀᴏᴜᴘ ᴀᴅᴍɪɴ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴀɴᴅ ᴄʜᴀɴɢᴇ sᴇᴛᴛɪɴɢs.
2. ɪᴛ ᴡᴏʀᴋs ᴏɴʟʏ ᴡʜᴇɴ ʙᴏᴛ ᴀʟʀᴇᴀᴅʏ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ.

<b>Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ :</b>
• /connect - ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴛᴏ ʙᴏᴛ
• /settings - ᴄʜᴀɴɢᴇ sᴇᴛᴛɪɴɢs ᴀs ʏᴏᴜʀ ᴡɪsʜ """
                  
    MANUELFILTER_TXT = """Hᴇʟᴘ : <b>Fɪʟᴛᴇʀꜱ</b>
    
◈ ꜰɪʟᴛᴇʀ ɪꜱ ᴀ ꜰᴇᴀᴛᴜʀᴇ ᴡᴇʀᴇ ᴜꜱᴇʀꜱ ᴄᴀɴ ꜱᴇᴛ ᴀᴜᴛᴏᴍᴀᴛᴇᴅ ʀᴇᴘʟɪᴇꜱ ꜰᴏʀ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴋᴇʏᴡᴏʀᴅ ᴀɴᴅ ɪ ᴡɪʟʟ ʀᴇꜱᴘᴏɴᴅ ᴡʜᴇɴᴇᴠᴇʀ ᴀ ᴋᴇʏᴡᴏʀᴅ ɪꜱ ꜰᴏᴜɴᴅ ɪɴ ᴛʜᴇ ᴍᴇꜱꜱᴀɢᴇ.

<b>Nᴏᴛᴇ :</b>
1. ᴛʜɪꜱ ʙᴏᴛ ꜱʜᴏᴜʟᴅ ʜᴀᴠᴇ ᴀᴅᴍɪɴ ᴘʀɪᴠɪʟᴇɢᴇ.
2. ᴏɴʟʏ ᴀᴅᴍɪɴꜱ ᴄᴀɴ ᴀᴅᴅ ꜰɪʟᴛᴇʀꜱ ɪɴ ᴀ ᴄʜᴀᴛ.
3. ᴀʟᴇʀᴛ ʙᴜᴛᴛᴏɴꜱ ʜᴀᴠᴇ ᴀ ʟɪᴍɪᴛ ᴏꜰ 64 ᴄʜᴀʀᴀᴄᴛᴇʀꜱ.

<b>Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ :</b>
• /filter - ᴀᴅᴅ ᴀ ꜰɪʟᴛᴇʀ ɪɴ ᴀ ᴄʜᴀᴛ
• /filters - ʟɪꜱᴛ ᴀʟʟ ᴛʜᴇ ꜰɪʟᴛᴇʀꜱ ᴏꜰ ᴀ ᴄʜᴀᴛ
• /del - ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴛᴇʀ ɪɴ ᴀ ᴄʜᴀᴛ
• /delall - ᴅᴇʟᴇᴛᴇ ᴛʜᴇ ᴡʜᴏʟᴇ ꜰɪʟᴛᴇʀꜱ ɪɴ ᴀ ᴄʜᴀᴛ (ᴄʜᴀᴛ ᴏᴡɴᴇʀ ᴏɴʟʏ)"""

    BUTTON_TXT = """Hᴇʟᴘ : *Bᴜᴛᴛᴏɴꜱ*
    
◈ ᴛʜɪꜱ ʙᴏᴛ ꜱᴜᴘᴘᴏʀᴛꜱ ʙᴏᴛʜ ᴜʀʟ ᴀɴᴅ ᴀʟᴇʀᴛ ɪɴʟɪɴᴇ ʙᴜᴛᴛᴏɴꜱ.

<b>Nᴏᴛᴇ :</b>
𝟷. ᴛᴇʟᴇɢʀᴀᴍ ᴡɪʟʟ ɴᴏᴛ ᴀʟʟᴏᴡꜱ ʏᴏᴜ ᴛᴏ ꜱᴇɴᴅ ʙᴜᴛᴛᴏɴꜱ ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴄᴏɴᴛᴇɴᴛ, ꜱᴏ ᴄᴏɴᴛᴇɴᴛ ɪꜱ ᴍᴀɴᴅᴀᴛᴏʀʏ.
𝟸. ᴛʜɪꜱ ʙᴏᴛ ꜱᴜᴘᴘᴏʀᴛꜱ ʙᴜᴛᴛᴏɴꜱ ᴡɪᴛʜ ᴀɴʏ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴇᴅɪᴀ ᴛʏᴘᴇ.
𝟹. ʙᴜᴛᴛᴏɴꜱ ꜱʜᴏᴜʟᴅ ʙᴇ ᴘʀᴏᴘᴇʀʟʏ ᴘᴀʀꜱᴇᴅ ᴀꜱ ᴍᴀʀᴋᴅᴏᴡɴ ꜰᴏʀᴍᴀᴛ

ᴜʀʟ ʙᴜᴛᴛᴏɴꜱ :
<code>[Button Text](buttonurl:https://t.me/MoviesDuniya4U)</code>

ᴀʟᴇʀᴛ ʙᴜᴛᴛᴏɴꜱ :
<code>[Button Text](buttonalert:ᴛʜɪꜱ ɪꜱ ᴀɴ ᴀʟᴇʀᴛ ᴍᴇꜱꜱᴀɢᴇ)</code>"""

    AUTOFILTER_TXT = """Hᴇʟᴘ : <b>Aᴜᴛᴏ Fɪʟᴛᴇʀ</b>
    
<b>Nᴏᴛᴇ :</b> Fɪʟᴇ Iɴᴅᴇx
𝟷. ᴍᴀᴋᴇ ᴍᴇ ᴛʜᴇ ᴀᴅᴍɪɴ ᴏꜰ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ɪꜰ ɪᴛ'ꜱ ᴘʀɪᴠᴀᴛᴇ.
𝟸. ᴍᴀᴋᴇ ꜱᴜʀᴇ ᴛʜᴀᴛ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴅᴏᴇꜱ ɴᴏᴛ ᴄᴏɴᴛᴀɪɴꜱ ᴄᴀᴍʀɪᴘꜱ, ᴘᴏʀɴ ᴀɴᴅ ꜰᴀᴋᴇ ꜰɪʟᴇꜱ.
𝟹. ꜰᴏʀᴡᴀʀᴅ ᴛʜᴇ ʟᴀꜱᴛ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴍᴇ ᴡɪᴛʜ ǫᴜᴏᴛᴇꜱ. ɪ'ʟʟ ᴀᴅᴅ ᴀʟʟ ᴛʜᴇ ꜰɪʟᴇꜱ ɪɴ ᴛʜᴀᴛ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴍʏ ᴅʙ.

<b>Nᴏᴛᴇ :</b> Aᴜᴛᴏ Fɪʟᴛᴇʀ
𝟷. Aᴅᴅ ᴛʜᴇ ʙᴏᴛ ᴀs ᴀᴅᴍɪɴ ᴏɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ.
𝟸. Usᴇ /connect ᴀɴᴅ ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴛᴏ ᴛʜᴇ ʙᴏᴛ.
𝟹. Usᴇ /settings ᴏɴ ʙᴏᴛ's ᴘᴍ ᴀɴᴅ ᴛᴜʀɴ ᴏɴ AᴜᴛᴏFɪʟᴛᴇʀ ᴏɴ ᴛʜᴇ sᴇᴛᴛɪɴɢs ᴍᴇɴᴜ."""

    
    RULE_TXT = """♦ 𝗚𝗿𝗼𝘂𝗽 𝗥𝘂𝗹𝗲𝘀 ♦

◈ <b>Sᴇᴀʀᴄʜ Mᴏᴠɪᴇ Wɪᴛʜ Cᴏʀʀᴇᴄᴛ Sᴘᴇʟʟɪɴɢ:</b>
• ᴀᴠᴀᴛᴀʀ 𝟸𝟶𝟶𝟿 ✅
• ᴀᴠᴀᴛᴀʀ ʜɪɴᴅɪ ✅
• ᴀᴠᴀᴛᴀʀ ᴍᴏᴠɪᴇ ❌
• ᴀᴠᴀᴛᴀʀ ʜɪɴᴅɪ ᴅᴜʙʙᴇᴅ..❌

◈ <b>Sᴇᴀʀᴄʜ Wᴇʙ Sᴇʀɪᴇs Iɴ ᴛʜɪs Fᴏʀᴍᴀᴛ:</b>
• ᴠɪᴋɪɴɢs S𝟶𝟷 ✅
• ᴠɪᴋɪɴɢs S𝟶𝟷E𝟶𝟷 ✅
• ᴠɪᴋɪɴɢs S𝟶𝟷 ʜɪɴᴅɪ ✅
• ᴠɪᴋɪɴɢs S𝟶𝟷 ʜɪɴᴅɪ ᴅᴜʙʙ... ❌
• ᴠɪᴋɪɴɢs sᴇᴀsᴏɴ 𝟷 ❌
• ᴠɪᴋɪɴɢs ᴡᴇʙ sᴇʀɪᴇs ❌

<b>➙ ᴅᴏɴ'ᴛ ᴅᴏ ᴀɴʏ ꜱᴇʟꜰ ᴘʀᴏᴍᴏᴛɪᴏɴ. 
➙ ᴅᴏɴ'ᴛ ꜱᴇɴᴅ ᴀɴʏ ᴋɪɴᴅ ᴏꜰ ᴘʜᴏᴛᴏ, ᴠɪᴅᴇᴏ, ᴅᴏᴄᴜᴍᴇɴᴛꜱ, ᴜʀʟ, ᴇᴛᴄ...
➙ ᴅᴏɴ'ᴛ ʀᴇǫᴜᴇꜱᴛ ᴀɴʏ ᴛʜɪɴɢꜱ ᴏᴛʜᴇʀ ᴛʜᴀɴ ᴍᴏᴠɪᴇꜱ, ꜱᴇʀɪᴇꜱ, ᴀɴɪᴍᴀᴛɪᴏɴ, ᴄᴀʀᴛᴏᴏɴ, ᴀɴɪᴍᴇ, ᴋ-ᴅʀᴀᴍᴀ ᴍᴀɴʏ ᴍᴏʀᴇ.</b>

🔰 <b>Nᴏᴛᴇ :</b> ᴀʟʟ ᴍᴇꜱꜱᴀɢᴇꜱ ᴡɪʟʟ ʙᴇ ᴀᴜᴛᴏ-ᴅᴇʟᴇᴛᴇᴅ ᴀꜰᴛᴇʀ 𝟷𝟶 ᴍɪɴᴜᴛᴇꜱ ᴛᴏ ᴀᴠᴏɪᴅ ᴄᴏᴘʏʀɪɢʜᴛ ɪꜱꜱᴜᴇꜱ."""

    CONNECTION_TXT = """Hᴇʟᴘ : <b>Cᴏɴɴᴇᴄᴛɪᴏɴꜱ</b>
    
◈ ᴜꜱᴇᴅ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʙᴏᴛ ᴛᴏ ᴘᴍ ꜰᴏʀ ᴍᴀɴᴀɢɪɴɢ ꜰɪʟᴛᴇʀꜱ 
◈ ɪᴛ ʜᴇʟᴘꜱ ᴛᴏ ᴀᴠᴏɪᴅ ꜱᴘᴀᴍᴍɪɴɢ ɪɴ ɢʀᴏᴜᴘꜱ.

<b>Nᴏᴛᴇ :</b>
1. ᴏɴʟʏ ᴀᴅᴍɪɴꜱ ᴄᴀɴ ᴀᴅᴅ ᴀ ᴄᴏɴɴᴇᴄᴛɪᴏɴ.
2. ꜱᴇɴᴅ /ᴄᴏɴɴᴇᴄᴛ ꜰᴏʀ ᴄᴏɴɴᴇᴄᴛɪɴɢ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴘᴍ

<b>Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ :</b>
• /connect  - ᴄᴏɴɴᴇᴄᴛ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴄʜᴀᴛ ᴛᴏ ʏᴏᴜʀ ᴘᴍ
• /disconnect  - ᴅɪꜱᴄᴏɴɴᴇᴄᴛ ꜰʀᴏᴍ ᴀ ᴄʜᴀᴛ
• /connections - ʟɪꜱᴛ ᴀʟʟ ʏᴏᴜʀ ᴄᴏɴɴᴇᴄᴛɪᴏɴꜱ"""

    EXTRAMOD_TXT = """Hᴇʟᴘ : <b>Exᴛʀᴀ Mᴏᴅᴜʟᴇs</b>
    
<b>Nᴏᴛᴇ :</b>
ᴛʜᴇꜱᴇ ᴀʀᴇ ᴛʜᴇ ᴇxᴛʀᴀ ꜰᴇᴀᴛᴜʀᴇꜱ ᴏꜰ ᴛʜɪꜱ ʙᴏᴛ

<b>Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ :</b>
• /id - ɢᴇᴛ ɪᴅ ᴏꜰ ᴀ ꜱᴘᴇᴄɪꜰɪᴇᴅ ᴜꜱᴇʀ.
• /info  - ɢᴇᴛ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴀ ᴜꜱᴇʀ.
• /imdb  - ɢᴇᴛ ᴛʜᴇ ꜰɪʟᴍ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ꜰʀᴏᴍ ɪᴍᴅʙ ꜱᴏᴜʀᴄᴇ.
• /search  - ɢᴇᴛ ᴛʜᴇ ꜰɪʟᴍ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ꜰʀᴏᴍ ᴠᴀʀɪᴏᴜꜱ ꜱᴏᴜʀᴄᴇꜱ."""

 
    ADMIN_TXT = """<b>Nᴏᴛᴇ :</b> Tʜɪs Mᴏᴅᴜʟᴇ Oɴʟʏ Wᴏʀᴋs Fᴏʀ Mʏ Aᴅᴍɪɴs.
    
<b>Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ :</b>
• /logs - ᴛᴏ ɢᴇᴛ ᴛʜᴇ ʀᴇᴄᴇɴᴛ ᴇʀʀᴏʀꜱ
• /stats - ᴛᴏ ɢᴇᴛ ꜱᴛᴀᴛᴜꜱ ᴏꜰ ꜰɪʟᴇꜱ ɪɴ ᴅʙ. <b>[Tʜɪs Cᴏᴍᴍᴀɴᴅ Cᴀɴ Bᴇ Usᴇᴅ Bʏ Aɴʏᴏɴᴇ]</b>
• /delete - ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴇ ꜰʀᴏᴍ ᴅʙ.
• /users - ᴛᴏ ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴍʏ ᴜꜱᴇʀꜱ ᴀɴᴅ ɪᴅꜱ.
• /chats - ᴛᴏ ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴍʏ ᴄʜᴀᴛꜱ ᴀɴᴅ ɪᴅꜱ
• /leave  - ᴛᴏ ʟᴇᴀᴠᴇ ꜰʀᴏᴍ ᴀ ᴄʜᴀᴛ.
• /disable  -  ᴛᴏ ᴅɪꜱᴀʙʟᴇ ᴀ ᴄʜᴀᴛ.
• /ban  - ᴛᴏ ʙᴀɴ ᴀ ᴜꜱᴇʀ.
• /unban  - ᴛᴏ ᴜɴʙᴀɴ ᴀ ᴜꜱᴇʀ.
• /channel - ᴛᴏ ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴛᴏᴛᴀʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴄʜᴀɴɴᴇʟꜱ. 
• /broadcast - ᴛᴏ ʙʀᴏᴀᴅᴄᴀꜱᴛ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴀʟʟ ᴜꜱᴇʀꜱ. 
• /grp_broadcast - ᴛᴏ ʙʀᴏᴀᴅᴄᴀsᴛ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀʟʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ɢʀᴏᴜᴘs.
• /gfilter - ᴛᴏ ᴀᴅᴅ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs. 
• /gfilters - ᴛᴏ ᴠɪᴇᴡ ʟɪsᴛ ᴏғ ᴀʟʟ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs. 
• /delg - ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀ sᴘᴇᴄɪғɪᴄ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀ. 
• /request - ᴛᴏ sᴇɴᴅ ᴀ ᴍᴏᴠɪᴇ/sᴇʀɪᴇs ʀᴇᴏ̨ᴜᴇsᴛ ᴛᴏ ʙᴏᴛ ᴀᴅᴍɪɴs. ᴏɴʟʏ ᴡᴏʀᴋs ᴏɴ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ. <b>[Tʜɪs Cᴏᴍᴍᴀɴᴅ Cᴀɴ Bᴇ Usᴇᴅ Bʏ Aɴʏᴏɴᴇ]</b>
• /delallg - ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀʟʟ ɢғɪʟᴛᴇʀs ғʀᴏᴍ ᴛʜᴇ ʙᴏᴛ's ᴅᴀᴛᴀʙᴀsᴇ.
• /deletefiles - ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴄᴀᴍʀɪᴘ ᴀɴᴅ ᴘʀᴇ-ᴅᴠᴅ ғɪʟᴇs ғʀᴏᴍ ᴛʜᴇ ʙᴏᴛ's ᴅᴀᴛᴀʙᴀsᴇ."""
 
    STATUS_TXT = """<b>⍟─────[ <b>Bᴏᴛ Sᴛᴀᴛᴜs</b> ]─────⍟
    
★ ᴛᴏᴛᴀʟ ꜰɪʟᴇꜱ :<code>{}</code>
★ ᴛᴏᴛᴀʟ ᴜꜱᴇʀꜱ :<code>{}</code>
★ ᴛᴏᴛᴀʟ ɢʀᴏᴜᴘꜱ :<code>{}</code>
★ ᴜꜱᴇᴅ ꜱᴛᴏʀᴀɢᴇ:<code>{}</code>
★ ꜰʀᴇᴇ ꜱᴛᴏʀᴀɢᴇ :<code>{}</code>

•❅──────✧❅✦❅✧──────❅•</b>"""


    LOG_TEXT_G = """#NewGroup
Gʀᴏᴜᴘ = {}(<code>{}</code>)
Tᴏᴛᴀʟ Mᴇᴍʙᴇʀs = <code>{}</code>
Aᴅᴅᴇᴅ Bʏ - {}"""

    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Nᴀᴍᴇ - {}"""

    ALRT_TXT = """ʜᴇʟʟᴏ {},
ᴛʜɪꜱ ɪꜱ ɴᴏᴛ ʏᴏᴜʀ ᴍᴏᴠɪᴇ ʀᴇQᴜᴇꜱᴛ,
ʀᴇQᴜᴇꜱᴛ ʏᴏᴜʀ'ꜱ..."""

    OLD_ALRT_TXT = """ʜᴇʏ {},
ʏᴏᴜ ᴀʀᴇ ᴜꜱɪɴɢ ᴏɴᴇ ᴏꜰ ᴍʏ ᴏʟᴅ ᴍᴇꜱꜱᴀɢᴇꜱ, 
ᴘʟᴇᴀꜱᴇ ꜱᴇɴᴅ ᴛʜᴇ ʀᴇQᴜᴇꜱᴛ ᴀɢᴀɪɴ."""

    CUDNT_FND = """ɪ ᴄᴏᴜʟᴅɴ'ᴛ ꜰɪɴᴅ ᴀɴʏᴛʜɪɴɢ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ {}
ᴅɪᴅ ʏᴏᴜ ᴍᴇᴀɴ ᴀɴʏ ᴏɴᴇ ᴏꜰ ᴛʜᴇꜱᴇ?"""

    I_CUDNT = """<b>sᴏʀʀʏ ɴᴏ ꜰɪʟᴇs ᴡᴇʀᴇ ꜰᴏᴜɴᴅ ꜰᴏʀ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛ {} 😕

ᴄʜᴇᴄᴋ ʏᴏᴜʀ sᴘᴇʟʟɪɴɢ ɪɴ ɢᴏᴏɢʟᴇ ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ 😃

ᴍᴏᴠɪᴇ ʀᴇǫᴜᴇꜱᴛ ꜰᴏʀᴍᴀᴛ 👇

ᴇxᴀᴍᴘʟᴇ : Uncharted or Uncharted 2022 or Uncharted En

ꜱᴇʀɪᴇꜱ ʀᴇǫᴜᴇꜱᴛ ꜰᴏʀᴍᴀᴛ 👇

ᴇxᴀᴍᴘʟᴇ : Loki S01 or Loki S01E04 or Lucifer S03E24

🚯 ᴅᴏɴᴛ ᴜꜱᴇ ➠ ':(!,./)</b>"""

    I_CUD_NT = """ɪ ᴄᴏᴜʟᴅɴ'ᴛ ꜰɪɴᴅ ᴀɴʏ ᴍᴏᴠɪᴇ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ {}.
ᴘʟᴇᴀꜱᴇ ᴄʜᴇᴄᴋ ᴛʜᴇ ꜱᴘᴇʟʟɪɴɢ ᴏɴ ɢᴏᴏɢʟᴇ ᴏʀ ɪᴍᴅʙ..."""

    MVE_NT_FND = """ᴍᴏᴠɪᴇ ɴᴏᴛ ꜰᴏᴜɴᴅ ɪɴ ᴅᴀᴛᴀʙᴀꜱᴇ..."""

    TOP_ALRT_MSG = """Cʜᴇᴄᴋɪɴɢ Fᴏʀ Mᴏᴠɪᴇ Iɴ Dᴀᴛᴀʙᴀsᴇ..."""

    MELCOW_ENG = """<b>Hᴇʟʟᴏ {} 😍, Aɴᴅ Wᴇʟᴄᴏᴍᴇ Tᴏ {} Gʀᴏᴜᴘ ❤️</b>"""

    SHORTLINK_INFO = """
<b>──────「<a href=https://t.me/TG_UPDATES1/336> Hᴏᴡ ᴛᴏ Eᴀʀɴ Mᴏɴᴇʏ </a> 」──────

Yᴏᴜ ᴄᴀɴ Eᴀʀɴ Mᴏɴᴇʏ Fʀᴏᴍ Tʜɪs Bᴏᴛ Uɴᴛɪʟ ᴛʜɪs ʙᴏᴛ ɪs ᴀʟɪᴠᴇ.

Wᴀɴᴛ ᴛᴏ Kɴᴏᴡ Hᴏᴡ? Fᴏʟʟᴏᴡ Tʜᴇsᴇ Sᴛᴇᴘs:-

sᴛᴇᴘ 𝟷 : ʏᴏᴜ ᴍᴜsᴛ ʜᴀᴠᴇ ᴀᴛʟᴇᴀsᴛ ᴏɴᴇ ɢʀᴏᴜᴘ ᴡɪᴛʜ ᴍɪɴɪᴍᴜᴍ 1𝟶𝟶 ᴍᴇᴍʙᴇʀs.

sᴛᴇᴘ 𝟸 : ᴍᴀᴋᴇ ᴀᴄᴄᴏᴜɴᴛ ᴏɴ Aɴʏ <a href=https://tamizhmasters.net/ref/Kushal>Sʜᴏʀᴛᴇɴᴇʀ Wᴇʙsɪᴛᴇ</a>.

sᴛᴇᴘ 𝟹 : ꜰᴏʟʟᴏᴡ ᴛʜᴇsᴇ <a href=https://t.me/TG_UPDATES1/336> ɪɴꜱᴛʀᴜᴄᴛɪᴏɴꜱ </a>Tᴏ ᴄᴏɴɴᴇᴄᴛ sʜᴏʀᴛᴇɴᴇʀ.

➣ Yᴏᴜ ᴄᴀɴ ᴄᴏɴɴᴇᴄᴛ ᴀs ᴍᴀɴʏ ɢʀᴏᴜᴘ ʏᴏᴜ ʜᴀᴠᴇ.

Any Doubts or Not Connecting? Contact Me </b>
"""

    REQINFO = """
⚠ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ⚠

ᴀꜰᴛᴇʀ 5 ᴍɪɴᴜᴛᴇꜱ ᴛʜɪꜱ ᴍᴇꜱꜱᴀɢᴇ ᴡɪʟʟ ʙᴇ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴅᴇʟᴇᴛᴇᴅ

ɪꜰ ʏᴏᴜ ᴅᴏ ɴᴏᴛ ꜱᴇᴇ ᴛʜᴇ ʀᴇǫᴜᴇsᴛᴇᴅ ᴍᴏᴠɪᴇ / sᴇʀɪᴇs ꜰɪʟᴇ, ʟᴏᴏᴋ ᴀᴛ ᴛʜᴇ ɴᴇxᴛ ᴘᴀɢᴇ"""

    SELECT = """
MOVIES ➢ Sᴇʟᴇᴄᴛ "Lᴀɴɢᴜᴀɢᴇs"

SERIES ➢ Sᴇʟᴇᴄᴛ "Sᴇᴀsᴏɴs"

Tɪᴘ: Sᴇʟᴇᴄᴛ "Lᴀɴɢᴜᴀɢᴇs" ᴏʀ "Sᴇᴀsᴏɴs" Bᴜᴛᴛᴏɴ ᴀɴᴅ Cʟɪᴄᴋ "Sᴇɴᴅ Aʟʟ" Tᴏ ɢᴇᴛ Aʟʟ Fɪʟᴇ Lɪɴᴋs ɪɴ ᴀ Sɪɴɢʟᴇ ᴄʟɪᴄᴋ"""

    SINFO = """
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯
ꜱᴇʀɪᴇꜱ ʀᴇǫᴜᴇꜱᴛ ꜰᴏʀᴍᴀᴛ
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯

ɢᴏ ᴛᴏ ɢᴏᴏɢʟᴇ ➠ ᴛʏᴘᴇ ꜱᴇʀɪᴇꜱ ɴᴀᴍᴇ ➠ ᴄᴏᴘʏ ᴄᴏʀʀᴇᴄᴛ ɴᴀᴍᴇ ➠ ᴘᴀꜱᴛᴇ ᴛʜɪꜱ ɢʀᴏᴜᴘ

ᴇxᴀᴍᴘʟᴇ : Loki S01E01

🚯 ᴅᴏɴᴛ ᴜꜱᴇ ➠ ':(!,./)"""

    NORSLTS = """
★ #𝗡𝗼𝗥𝗲𝘀𝘂𝗹𝘁𝘀 ★

𝗜𝗗 <b>: {}</b>

𝗡𝗮𝗺𝗲 <b>: {}</b>

𝗠𝗲𝘀𝘀𝗮𝗴𝗲 <b>: {}</b>"""

    CAPTION = """ 
<b>══════════════════
🗂 {file_name}
═══════════════════ 
𝐒𝐔𝐁𝐒𝐂𝐑𝐈𝐁𝐄 𝐇𝐄𝐑𝐄 👇
╔══════════════════╗         
    <a href="https://t.me/TG_LINKS_CHANNEL">🔱 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 🔱</a>
╚══════════════════╝</b>"""
    
    IMDB_TEMPLATE_TXT = """
<b>Query: {query}
IMDb Data:

🏷 Title: <a href={url}>{title}</a>
🎭 Genres: {genres}
📆 Year: <a href={url}/releaseinfo>{year}</a>
⏱️ Result Shown in: {remaining_seconds} <i>seconds</i> 🔥
🌟 Rating: <a href={url}/ratings>{rating}</a> / 10</b>"""
    
    ALL_FILTERS = """
<b>Hᴇʏ {}, Tʜᴇsᴇ ᴀʀᴇ ᴍʏ ᴛʜʀᴇᴇ ᴛʏᴘᴇs ᴏғ ғɪʟᴛᴇʀs.</b>"""
    
    GFILTER_TXT = """
<b>Wᴇʟᴄᴏᴍᴇ ᴛᴏ Gʟᴏʙᴀʟ Fɪʟᴛᴇʀs. Gʟᴏʙᴀʟ Fɪʟᴛᴇʀs ᴀʀᴇ ᴛʜᴇ ғɪʟᴛᴇʀs sᴇᴛ ʙʏ ʙᴏᴛ ᴀᴅᴍɪɴs ᴡʜɪᴄʜ ᴡɪʟʟ ᴡᴏʀᴋ ᴏɴ ᴀʟʟ ɢʀᴏᴜᴘs.</b>
    
Aᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs:
• /gfilter - <code>Tᴏ ᴄʀᴇᴀᴛᴇ ᴀ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀ.</code>
• /gfilters - <code>Tᴏ ᴠɪᴇᴡ ᴀʟʟ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs.</code>
• /delg - <code>Tᴏ ᴅᴇʟᴇᴛᴇ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀ.</code>
• /delallg - <code>ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀʟʟ ɢʟᴏʙᴀʟ ꜰɪʟᴛᴇʀꜱ.</code>"""
    
    FILE_STORE_TXT = """
<b>Fɪʟᴇ sᴛᴏʀᴇ ɪs ᴛʜᴇ ғᴇᴀᴛᴜʀᴇ ᴡʜɪᴄʜ ᴡɪʟʟ ᴄʀᴇᴀᴛᴇ ᴀ sʜᴀʀᴇᴀʙʟᴇ ʟɪɴᴋ ᴏғ ᴀ sɪɴɢʟᴇ ᴏʀ ᴍᴜʟᴛɪᴘʟᴇ ғɪʟᴇs.</b>

Aᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs:
• /batch - <code>Tᴏ ᴄʀᴇᴀᴛᴇ ᴀ ʙᴀᴛᴄʜ ʟɪɴᴋ ᴏғ ᴍᴜʟᴛɪᴘʟᴇ ғɪʟᴇs.</code>
• /link - <code>Tᴏ ᴄʀᴇᴀᴛᴇ ᴀ sɪɴɢʟᴇ ғɪʟᴇ sᴛᴏʀᴇ ʟɪɴᴋ.</code>
• /pbatch - <code>Jᴜsᴛ ʟɪᴋᴇ /batch, ʙᴜᴛ ᴛʜᴇ ғɪʟᴇs ᴡɪʟʟ ʙᴇ sᴇɴᴅ ᴡɪᴛʜ ғᴏʀᴡᴀʀᴅ ʀᴇsᴛʀɪᴄᴛɪᴏɴs.</code>
• /plink - <code>Jᴜsᴛ ʟɪᴋᴇ /link, ʙᴜᴛ ᴛʜᴇ ғɪʟᴇ ᴡɪʟʟ ʙᴇ sᴇɴᴅ ᴡɪᴛʜ ғᴏʀᴡᴀʀᴅ ʀᴇsᴛʀɪᴄᴛɪᴏɴ.</code>"""

    RESTART_TXT = """
<b>Bᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ !

📅 Dᴀᴛᴇ : <code>{}</code>
⏰ Tɪᴍᴇ : <code>{}</code>
🌐 Tɪᴍᴇᴢᴏɴᴇ : <code>Asia/Kolkata</code>
🛠️ Bᴜɪʟᴅ Sᴛᴀᴛᴜs: <code>v2.7.1 [ Sᴛᴀʙʟᴇ ]</code></b>"""

    LOGO = """
 ____  ___    ____   __  ____  ____ 
(_  _)/ __)  (  _ \ /  \(_  _)(__  )
  )( ( (_ \   ) _ ((  O ) )(   / _/ 
 (__) \___/  (____/ \__/ (__) (____)
"""
