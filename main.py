import sys

from src.notify import Notify
from src.exceptions import FailedFetchError, FailedResponseError


def main():
    with open("text.txt", "r", encoding="utf-8") as text_file:
        text = text_file.read()

    with open("users.txt", "r", encoding="utf-8") as users_file:
        users_ids = users_file.read().splitlines()

    notify = Notify()

    for user_id in users_ids:
        try:
            notify.send_message(text, user_id.strip())
        except (FailedFetchError, FailedResponseError):
            sys.stdout.write(f"\nПользователь {user_id} - НЕ отправлено ❌")
        sys.stdout.write(f"\nПользователь {user_id} - отправлено ✅")
    sys.stdout.write(f"\nУведомления отправлены")


if __name__ == "__main__":
    main()
