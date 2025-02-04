# Python logging module

Logging is part of the Python standard library. It is a flexible logging system for Python programs. If you come from a C background or are beginning to learn Python, you may be used to using `printf` or `cout` to debug your programs. However, using the `logging` module is a more flexible and professional way to debug your programs.

We will be looking to the implementation and the best practices while using the `logging` module.

## Logging levels

Similar to Java, and its common logging framework `log4j`, Python logging has different levels of logging. The levels are the following:

1. Debug (10): Detailed information, useful for debugging.
2. Info (20): Confirmation that things are working as they should.
3. Warning (30): Indicates potential issues that don't prevent the application from working.
4. Error (40): Serious problems that prevent some functionality from working properly.
5. Critical (50): Critical issues that may cause the application to stop working.
(Sentry.io n.d.)


```python
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
```

### Basic Usage

Here is how to implement the logging setup in code:

```python
# After logger has been set up:
logger = setup_logger(
name='my_app',
log_file='app.log',
level=logging.INFO,
console_level=logging.DEBUG,
file_level=logging.WARNING
)

# Then just use differen loggin levels
logger.debug('debug information')
logger.info('Application Started')
logger.warning('warning message')
logger.error('Error ocurred')
logger.critical('Critical message')

if __name__ == '__main__':
    main()
```

## Sources:
Sentry.io. (n.d.). Logging in Python: A Developer's Guide. Sentry Blog. https://blog.sentry.io/logging-in-python-a-developers-guide/

