import logging
from datetime import datetime


class Logger:
    """Custom logger for the project"""

    _logger = None

    @classmethod
    def get_logger(cls, name=None):
        """Get or create a logger instance"""
        if cls._logger is None:
            cls._setup_logger(name or "playwright-demo")
        return cls._logger

    @classmethod
    def _setup_logger(cls, name):
        """Setup logger with formatting"""
        cls._logger = logging.getLogger(name)
        cls._logger.setLevel(logging.DEBUG)

        # Create a console handler
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # Create formatter
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
        )

        ch.setFormatter(formatter)

        # Add handler to logger
        if not cls._logger.handlers:
            cls._logger.addHandler(ch)

    @classmethod
    def info(cls, message):
        """Log info message"""
        cls.get_logger().info(message)

    @classmethod
    def debug(cls, message):
        """Log debug message"""
        cls.get_logger().debug(message)

    @classmethod
    def warning(cls, message):
        """Log warning message"""
        cls.get_logger().warning(message)

    @classmethod
    def error(cls, message):
        """Log error message"""
        cls.get_logger().error(message)

    @classmethod
    def critical(cls, message):
        """Log critical message"""
        cls.get_logger().critical(message)
