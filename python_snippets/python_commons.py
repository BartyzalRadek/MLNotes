import logging
import logging.handlers
import os
import sys
import time
import json
import psutil

logger = logging.getLogger(__name__)


def ensure_dir_exists(path):
    # print("Created directories for path '{}' if needed.".format(path))
    return os.makedirs(path, exist_ok=True)


def get_timestamp_filename() -> str:
    return time.strftime("%Y_%m_%d-%H_%M_%S")


def get_subdirs(dir_path) -> list:
    return [f for f in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, f))]


def get_files_in_dir(dir_path) -> list:
    return [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]


def write_lines_to_file(lines, filepath):
    with open(filepath, 'w') as f:
        for line in lines:
            f.write(line + '\n')  # recommended to use \n on all platforms


def load_lines_from_file(filepath):
    lines = None
    try:
        with open(filepath, 'r') as f:
            lines = [x.strip() for x in f.readlines()]
    except Exception as ex:
        logger.info("{}\nCouldn't open file {}. Returning None.".format(ex, filepath))
    return lines


def load_json(path):
    """
    Load a JSON file.
    :param path:    Path to the file.
    :return:        The loaded JSON file.
    """
    with open(path, "r") as file:
        try:
            # return ujson.load(file)
            logger.warning('Import ujson and use it instead of json library for significant speed up!')
            return json.load(file)
        except ValueError as err:
            logger.warning('load_json({}): ValueError {}\nTrying standard json library.'.format(path, err))
            return json.load(file)


def save_json(data, path):
    """
    Save JSON into a file.
    :param data:      The JSON data.
    :param path:      Where to save the JSON data.
    :return:          None.
    """
    with open(path, "w") as file:
        json.dump(data, file, indent=4, sort_keys=True)


def print_memory_info(indent_level=0):
    """
    logging.debug total used, available memory and this process's memory.
    :param indent_level: How many spaces should be used for indentation.
    """
    indent = ' ' * indent_level
    process = psutil.Process(os.getpid())
    # logger.debug('{}Total used memory:      {:.3f} GB'.format(indent, psutil.virtual_memory().used / 1e9))
    logger.debug('{}Total available memory: {:.3f} GB'.format(indent, psutil.virtual_memory().available / 1e9))
    logger.debug('{}This process memory:    {:.3f} GB'.format(indent, process.memory_info().rss / 1e9))


def init_logging(log_dir=None, log_filename=None, level=logging.DEBUG,
                 fmt='%(asctime)s %(name)s %(levelname)s: %(message)s'):
    """
    Initializes logging with handlers for both stdout and file if provided.
    How to use:
     - call this method to init logging in whole project (typically in main)
     - in every file:
        import logging
        logger = logging.getLogger(__name__)
        logger.info(...)
    :param log_dir: Directory to store logfile in, will be created if it does not exist. None = '.'
    :param log_filename: If None = do not log to file.
    :param level: Default is logging.DEBUG.
    :param fmt: Format of all log messages, default is '%(asctime)s %(message)s'
    :return: Nothing
    """
    if log_dir is None:
        log_dir = '.'

    formatter = logging.Formatter(fmt)

    # add std output
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(formatter)
    stream_handler.setLevel(level)

    handlers = [stream_handler]

    normal_log_filename = None
    error_log_filename = None
    if log_filename is not None:
        ensure_dir_exists(log_dir)

        log_filename = get_timestamp_filename() + '_' + log_filename

        normal_log_filename = 'NORMAL_' + log_filename
        normal_file_handler = logging.handlers.RotatingFileHandler(filename=normal_log_filename, mode='a',
                                                                   maxBytes=1024 * 1024, backupCount=20,
                                                                   encoding='utf8')
        normal_file_handler.setFormatter(formatter)
        normal_file_handler.setLevel(level)

        error_log_filename = 'ERROR_' + log_filename
        error_file_handler = logging.handlers.RotatingFileHandler(filename=error_log_filename, mode='a',
                                                                  maxBytes=1024 * 1024, backupCount=20, encoding='utf8')
        error_file_handler.setFormatter(formatter)
        error_file_handler.setLevel(logging.ERROR)

        handlers.append(normal_file_handler)
        handlers.append(error_file_handler)

    logging.basicConfig(level=level, handlers=handlers)
    if log_filename is not None:
        logger.info('NORMAL LOG FILE PATH = {}'.format(os.path.join(log_dir, normal_log_filename)))
        logger.info('ERROR LOG FILE PATH = {}'.format(os.path.join(log_dir, error_log_filename)))
