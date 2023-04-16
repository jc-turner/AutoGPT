import asyncio
import os
import sys
import traceback
from threading import Lock, Semaphore

from telegram import Update
from telegram.ext import Application, CallbackContext, CommandHandler 

try:
    from autogpt.config.config import Config
    from autogpt.telegram_chat import TelegramUtils, is_authorized_user
except ModuleNotFoundError:
    from config import Config
    from telegram_chat import TelegramUtils, is_authorized_user

cfg = Config()

main_started = False


mutex_lock = Lock()  # Ensure only one sound is played at a time
# The amount of sounds to queue before blocking the main thread
queue_semaphore = Semaphore(1)


async def stop(update: Update, context: CallbackContext):
    if is_authorized_user(update):
        await update.message.reply_text("Stopping Auto-GPT now!")
        exit(0)


async def start(update: Update, context: CallbackContext):
    global main_started
    print("Starting Auto-GPT...")
    if is_authorized_user(update):
        if main_started:
            TelegramUtils.send_message("Already started!")
        else:
            main_started = True
            TelegramUtils.send_message("Auto-GPT is starting now!")
            os.system("python -m autogpt {}".format(" ".join(sys.argv[1:])))


def main():
    print("Starting up...")

    telegramUtils = TelegramUtils()
    telegramUtils.send_message("Starting Auto-GPT...")

    # Delete old messages
    asyncio.run(telegramUtils.delete_old_messages())

    TelegramUtils().send_message(
        "Hello! I need you to confirm with /start to start me. <3")

    application = Application.builder().token(cfg.telegram_api_key).build()
    application.add_handler(CommandHandler("stop", stop))
    application.add_handler(CommandHandler("start", start))

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        print("Check your Telegram chat to start Auto-GPT! ;-)")
        loop.run_until_complete(application.run_polling())
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    try:
        main()
        # queue_semaphore.acquire(True)
        # thread = threading.Thread(target=main)
        # thread.start()
    except KeyboardInterrupt:
        print("Exiting...")
        TelegramUtils.send_message(
            "I hope I could help! :) \n \n Bye bye! <3")

        exit(0)
    except Exception as e:
        print(e)
        print(traceback.format_exc())
        TelegramUtils.send_message(
            "Sorry, I have to stop. \n \n An error occurred: " + str(e))
        exit(1)
