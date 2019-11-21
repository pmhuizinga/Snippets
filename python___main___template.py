# sample code for a model __main__ file

import configparser
import logging.config
from pathlib import Path
import argparse

def read_settings(config_location: str):
    """
    Read in the application settings from a configuration file (config.ini).

    :param config_location: The location of the configuration files to use.
    :return: A dictionary with the read in settings.
    """

    config = configparser.ConfigParser()
    config.read(Path(config_location) / r'config.ini')

    testvar = config['DEFAULT']['testvar']
	
class MainProcessClassName:
    """
    This class is used to process the data.
    """

    def __init__(self, _logger, _settings):
        """
        Constructor

        :param _logger: Logger to use.
        :param _settings:  Settings dictionary.
        """
        self.logger = _logger
        self.settings = _settings


    def run(self):
        """
        Processes the data.

        :return: None
        """
        self.logger.info('Start process')

        start_function(self.settings)


def main(args=None):
    """
    Main module.

    :param args: Input arguments (parsed by argparse).
    :return: dictionary with the processed data frames.
    """

    if args is None:
        # read in command line arguments. the calculation date is mandatory.
        parser = argparse.ArgumentParser(description='Argument description')
        parser.add_argument('-config_path', help='The path of the configuration files', type=general.is_valid_path,
                            required=True)
        args = parser.parse_args()

    # read setting
    settings = read_settings(args.config_path)

    # setup the logger, use the configuration path to load the settings.
    logger = init_logger(args.config_path, settings['testvar'])

    try:
        logger.info('Starting program')

        program = MainProcessClassName(logger, settings)

        program.run()

    except Exception as _:
        logger.exception("Unexpected error")
        raise


if __name__ == "__main__":

    results = main()
