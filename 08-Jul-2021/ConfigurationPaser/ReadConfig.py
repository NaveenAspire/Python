from configparser import ConfigParser
parser  =ConfigParser()
parser.read('sample.ini')

print(parser.sections())
print(parser.get('settings','secret_key'))
print(parser.options('settings'))

print('db' in parser)
print(parser.get('db','db_port'),type(parser.get('db','db_port')))

print(parser.getint('db','db_port'),type(parser.getint('db','db_port')))

print(parser.getint('db','db_collection',fallback="No information inside"))

print(parser.getboolean('settings','debug'))