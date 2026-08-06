import time

class Logger:
    LEVELS = ["INFO", "WARNING", "ERROR", "DEBUG"]

    def __init__(self, level: str = "INFO"):
        if level not in self.LEVELS:
            raise ValueError(f"Невідомий рівень логування: {level}")
        self.level = level

    def log(self, level: str, message: str, module: str = "System"):
        """Записує повідомлення у лог."""
        if level not in self.LEVELS:
            level = "INFO"
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(f"[{timestamp}] [{level}] [{module}] {message}")

    def info(self, message: str, module: str = "System"):
        self.log("INFO", message, module)

    def warning(self, message: str, module: str = "System"):
        self.log("WARNING", message, module)

    def error(self, message: str, module: str = "System"):
        self.log("ERROR", message, module)

    def debug(self, message: str, module: str = "System"):
        self.log("DEBUG", message, module)
