from configparser import ConfigParser

config = ConfigParser()

config['settings'] = {
    'debug':'1',
    'secret_key':'abc123',
    'log_path':'CongigParser'
    }

config['db']={
    'db_name' : 'myapp_dev',
    'db_host' : 'localhost',
    'db_port' : '8899'
}

config['files']={
    'use_cdn' : 'false',
    'images_path' : '/user/pictures',
}
with open('sample.ini','w') as f:
    config.write(f)
