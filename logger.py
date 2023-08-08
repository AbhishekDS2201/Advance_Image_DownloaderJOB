import logging

class Logging:
    def _init_(self, name):
        """
        Initializes the custom logger.
        :param name: Custom name for the logger.
        """
        try:
            # Create a custom logger
            self.logger = logging.getLogger(name)

        except Exception as e:
            raise Exception(e)

    def initialize_logger(self):
        """
        Configures the logger with custom formatters and handlers.
        """
        try:
            if len(self.logger.handlers) == 0:

                # Set the logger's level to INFO
                self.logger.setLevel(logging.INFO)

                # Create a formatter for log messages
                formatter = logging.Formatter(
                    '%(asctime)s:%(levelname)s:%(name)s:%(message)s')

                # Create a file handler to write log messages to a file
                file_handler = logging.FileHandler('Advance Image Downloader.log')

                # Attach the formatter to the file handler
                file_handler.setFormatter(formatter)

                # Add the file handler to the logger
                self.logger.addHandler(file_handler)

            return self.logger
        except Exception as e:
            raise Exception(e)

    # Rest of the methods remain unchanged


    def print_log(self, log_statement, log_level):
        """
        Prints and logs the statements.
        
        :param log_statement: Statement for logging.
        :param log_level: Level of log to be maintained ('info', 'error', 'exception', 'warning', etc.).
        """
        try:
            valid_log_levels = ['info', 'debug', 'warning', 'error', 'exception']
            if log_level.lower() in valid_log_levels:
                if log_level.lower() == 'info':
                    self.logger.info(log_statement)
                elif log_level.lower() == 'debug':
                    self.logger.debug(log_statement)
                elif log_level.lower() == 'warning':
                    self.logger.warning(log_statement)
                elif log_level.lower() == 'error':
                    self.logger.error(log_statement)
                elif log_level.lower() == 'exception':
                    self.logger.exception(log_statement)
            else:
                raise ValueError(f"Invalid log level '{log_level}'. Supported levels are: {', '.join(valid_log_levels)}")
        except Exception as e:
            raise Exception(e)