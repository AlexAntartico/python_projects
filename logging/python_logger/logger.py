import logging  # Core logging module
import sys  # For system-level operations
from logging.handlers import RotatingFileHandler  # For rotating log files
from typing import Optional, Union  # For type hinting


def setup_logger(
    name: str,
    log_file: str,
    level: int = logging.INFO,
    console_level: Optional[int] = None,
    file_level: Optional[int] = None,
    log_format: str = '%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s'
    max_log_size: int = 500*1024*1024,  # 500 MB
    backup_count: int = 14
) -> logging.Logger:
    """
    Function to setup a custom logger, includes console and file logging.
    This should be production-ish ready. Maybe Production, depends on your needs.
    Check with your seniors or team lead for best practices and team conventions.
    If you happen to be the senior or team lead and you are wondering if this is good or not,
    welcome to the club. It gets better with time.

    Args:
        name (str): Name of the logger
        log_file (str): Path to the log file
        level (int): Logging level, defaults to logging.INFO
        console_level (Optional[int]): Console logging level, defaults to None
        file_level (Optional[int]): File logging level, defaults to None
        log_format (str): Log format, defaults to '%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s'
        max_log_size (int): Maximum log file size, defaults to 500 MB
        backup_count (int): Number of backup log files, defaults to 14, roughly 2 weeks of logs

    Returns:
        logging.Logger: Configure logger instance
    """

    # Validate inputs

    if not name or not log_file:
        raise ValueError('Name and log_file path are required')

    # Set up logger
    logger = logging.getLogger(name)

    # de-duplicate handlers if logger is already set up
    if logger.handlers:
        logger.handlers.clear()

    # Set logging level
    logger.setLevel(level)

    # Formatter
    formatter = logging.Formatter(log_format)

    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(console_level or level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # File handler and rotation
    try:
        file_handler = RotatingFileHandler(
        log_file,
        mode='a',
        maxBytes=max_log_size,
        backupCount=backup_count,
        encoding='utf-8',
        )
        file_handler.setLevel(file_level or level)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    except PermissionError as e:
        logger.error(f'Unable to create log file at {log_file} {e}')
    except Exception as e:
        logger.error(f'Error setting up file handler: {e}')

    # write logs immediately
    logger.propagate = False

    return logger