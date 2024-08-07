from typing import Optional, Union
from string import Template
import logging

from src.config import SETTINGS
from src.http import Http


logger = logging.getLogger(__name__)


class Notify(Http):
    _telegram_host = "https://api.telegram.org"
    _send_message_url = Template("/bot$token/sendMessage")
    

    def __init__(
        self,
        bot_token: str = SETTINGS.bot_token
    ):
        self._bot_token = bot_token

    def send_message(
        self,
        text: str,
        telegram_id: Union[int, str],
        reply_markup: Optional[str] = None,
        *args, **kwargs
    ) -> None:
        if not telegram_id or not text:
            return

        url = f"{self._telegram_host}{
            self._send_message_url.substitute(token=self._bot_token)}"
        params = {
            "chat_id": telegram_id,
            "text": text,
            "parse_mode": "html",
        }
        if reply_markup:
            params["reply_markup"] = reply_markup

        data = {
            "url": url,
            "params": params,
        }

        self.make_safe_request("get", data)
