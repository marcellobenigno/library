#!/usr/bin/env python

CONFIG_STRING = """
DEBUG=True
SECRET_KEY=THIS-IS-NOT-A-GOOD-SECRET-KEY
ALLOWED_HOSTS=127.0.0.1, .localhost
#DATABASE_URL=postgres://USER:PASSWORD@HOST:PORT/NAME
""".strip()

# Writing our configuration file to '.env'
with open('.env', 'w') as configfile:
    configfile.write(CONFIG_STRING)
