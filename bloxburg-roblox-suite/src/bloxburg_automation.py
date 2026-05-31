import time
import logging
from colorama import Fore, Style, init

init(autoreset=True)

logger = logging.getLogger(__name__)

class BloxburgBot:
    """Core automation bot for Bloxburg on Roblox."""

    def __init__(self, username: str = None):
        self.username = username
        self.running = False
        self._current_job = None

    def start(self):
        """Start the bot session."""
        if self.running:
            logger.warning("Bot is already running.")
            return
        self.running = True
        print(Fore.GREEN + "[BOT] Bloxburg bot started successfully.")
        logger.info("Bot session started.")

    def stop(self):
        """Stop the bot session."""
        if not self.running:
            logger.warning("Bot is not running.")
            return
        self.running = False
        print(Fore.RED + "[BOT] Bloxburg bot stopped.")
        logger.info("Bot session stopped.")

    def perform_task(self, task_name: str):
        """Simulate performing a task in-game."""
        if not self.running:
            print(Fore.YELLOW + "[BOT] Cannot perform task. Bot not running.")
            return
        print(Fore.CYAN + f"[TASK] Performing task: {task_name}")
        time.sleep(0.3)
        print(Fore.CYAN + f"[TASK] Task '{task_name}' completed.")

    def set_job(self, job_name: str):
        """Assign a job to the bot."""
        self._current_job = job_name
        print(Fore.BLUE + f"[JOB] Job set to: {job_name}")

    def get_status(self):
        """Return current bot status as dict."""
        return {
            "username": self.username,
            "running": self.running,
            "current_job": self._current_job
        }