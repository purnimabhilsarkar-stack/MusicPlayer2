"""
Music Player, Telegram Voice Chat Bot
Copyright (c) 2021-present Asm Safone <https://github.com/AsmSafone>

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
from dotenv import load_dotenv


load_dotenv()


class Config:
    def __init__(self) -> None:
        self.API_ID: str = os.environ.get("API_ID", "33314195")
        self.API_HASH: str = os.environ.get("API_HASH", "331fc32b4afa5ad5d07714d14fa33cda")
        self.SESSION: str = os.environ.get("SESSION", "AQH8VZMAb4SuwEoXeKbHz6eET3pujHWIRd26LQmmZ3TT1Q-Er4TMuSl0mAFJphmbKJVprw41vfxK-efzW_PGpww0rT-gs0nMEWP2al-tdCHhHLZYQ1i0MihrFmi6FJmQGAOXripHq-UaKNeCL9ud-fGJHRz4tWZnY094aLccPMOlq9IZWI1SZwg3Typs8jpTE8CVz-Cr5lnLHAXV9fXORifKxmjTbf2_rZIUKwgAuW_l3PmsJiGagoGclFZe_mFpQ60t0rNN_wLgBh3BG6_BSrOMd0ksYq89Yl_M44VrpVILztwLNzLPPnIlAC1CdZ28Dj4rdLlFml259U6184usJf9gNEUYDwAAAAIHMRooAA")
        self.BOT_TOKEN: str = os.environ.get("BOT_TOKEN", "8809843846:AAGTQHwzQDX0E1-S41EDD95jYvpuHorVGUY")
        self.SUDOERS: list = [
            int(id) for id in os.environ.get("SUDOERS", " ").split() if id.isnumeric()
        ]
        if not self.SESSION or not self.API_ID or not self.API_HASH:
            print("ERROR: SESSION, API_ID and API_HASH is required!")
            quit(0)
        self.SPOTIFY: bool = False
        self.QUALITY: str = os.environ.get("QUALITY", "high").lower()
        self.PREFIXES: list = os.environ.get("PREFIX", "!").split()
        self.LANGUAGE: str = os.environ.get("LANGUAGE", "en").lower()
        self.STREAM_MODE: str = (
            "audio"
            if (os.environ.get("STREAM_MODE", "audio").lower() == "audio")
            else "video"
        )
        self.ADMINS_ONLY: bool = os.environ.get("ADMINS_ONLY", False)
        self.SPOTIFY_CLIENT_ID: str = os.environ.get("SPOTIFY_CLIENT_ID", None)
        self.SPOTIFY_CLIENT_SECRET: str = os.environ.get("SPOTIFY_CLIENT_SECRET", None)


config = Config()
