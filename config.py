"""
VC Music Player, Telegram Voice Chat Userbot
Copyright (C) 2021  ZauteKm <https://telegram.dog/ZauteKm>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""
import os
import re
from youtube_dl import YoutubeDL
ydl_opts = {
    "geo-bypass": True,
    "nocheckcertificate": True
    }
ydl = YoutubeDL(ydl_opts)
links=[]
finalurl=""
STREAM=os.environ.get("STREAM_URL", "https://node-31.zeno.fm/4g65yz9gg0quv.aac?rj-ttl=5&rj-tok=AAABdtuvkw4A9ORsR7htLe8_1Q")
regex = r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+"
match = re.match(regex,STREAM)
if match:
    meta = ydl.extract_info(STREAM, download=False)
    formats = meta.get('formats', [meta])
    for f in formats:
        links.append(f['url'])
    finalurl=links[0]
else:
    finalurl=STREAM

class Config:
    ADMIN = os.environ.get("ADMINS", '709294532')
    ADMINS = [int(admin) if re.search('^\d+$', admin) else admin for admin in (ADMIN).split()]
    API_ID = int(os.environ.get("API_ID", 7670903))
    CHAT = int(os.environ.get("CHAT", "-1001215436654"))
    LOG_GROUP=os.environ.get("LOG_GROUP", "-1001215436654")
    if LOG_GROUP:
        LOG_GROUP=int(LOG_GROUP)
    else:
        LOG_GROUP=None
    STREAM_URL=finalurl
    ADMIN_ONLY=os.environ.get("ADMIN_ONLY", "N")
    ARQ_API=os.environ.get("ARQ_API", "MWSEUQ-ONSQUT-VVDWHA-PUCXHR-ARQ")
    REPLY_MESSAGE=os.environ.get("REPLY_MESSAGE", None)
    if REPLY_MESSAGE:
        REPLY_MESSAGE=REPLY_MESSAGE
    else:
        REPLY_MESSAGE=None
    EDIT_TITLE = os.environ.get("EDIT_TITLE", True)
    if EDIT_TITLE == "NO":
        EDIT_TITLE=None
    DURATION_LIMIT=int(os.environ.get("MAXIMUM_DURATION", 15))
    DELAY = int(os.environ.get("DELAY", 10))
    API_HASH = os.environ.get("API_HASH", "518da36fc2b883e74036028ac6c6d854")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "1914403790:AAFBfFSp7sldc8E1SqfjbApkrcFlk0NiQt8") 
    SESSION = os.environ.get("SESSION_STRING", "BAAPVHhQtTIDBR_Nk9uuDUEMISWVi53ghirWho97vfLOKyhhBrV_Qlw7-w0J9gDzxV2I2MyDfFgnsJ6gXqh4UC1J_3y40MmQvNoLx-UhfBU2GwWQgUV9eQ_BVXMjFUeCwWNEdxzQFDwFMYqbKe625-XJ6WAVPM8aakas2I1if_1Onrgciu7tWroXJUMw6uXvl4VRIuNcMR9E3xNPtTVZiipyF8dqimezZvG52zr_uB1DcvAZyiTzvEhoFoK9-QDy3kwvvdO_e3oHoMWN4bN2MASbFcdAra8ggHmF6e6tImD6V41v6AMtNVMsm4f1Jy_QM9AF9A5Pt1sGYTV6ZelMr2jBc7YdvAA")
    playlist=[]
    msg = {}
