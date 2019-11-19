import os
import logging
from app import create_app

config_name = os.getenv('FLASK_CONFIG')
app = create_app(config_name)
#import logging
app.logger.disabled = True
log = logging.getLogger('werkzeug')
log.disabled = True

if __name__ == '__main__':
    app.run()
