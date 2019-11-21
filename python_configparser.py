# sample script for reading config items with configparser

import configparser

# Configurations
config = configparser.ConfigParser()
config.read(r'config.ini')
test_variable = config['DEFAULT']['test_config_item']

################ config.ini ################
[DEFAULT]
test_config_item = 'Hello World!' 
