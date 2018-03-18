import ConfigParser, os

config = ConfigParser.ConfigParser()
config.read('config.cfg')

print config.get('test', 'conn')
print config.get('test', 'pass')
