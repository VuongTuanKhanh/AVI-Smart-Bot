def get_logger(name='logger', file='', stream_fmt='%(name)s - %(levelname)s - %(message)s', file_fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s'):
    import logging

    logger = logging.getLogger(name)

    # Create handlers
    stream_handler = logging.StreamHandler()
    if file:
        file_handler = logging.FileHandler(file)

    # Configure level and formatter and add it to handlers
    stream_handler.setLevel(logging.INFO) # warning and above is logged to the stream
    file_handler.setLevel(logging.INFO) # error and above is logged to a file

    stream_format = logging.Formatter(stream_fmt)
    file_format = logging.Formatter(file_fmt)

    stream_handler.setFormatter(stream_format)
    file_handler.setFormatter(file_format)

    # Add handlers to the logger
    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)

    return logger