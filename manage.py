import os

from flask_script import Manager
from flask_migrate import MigrateCommand
from Apps import create_app


env = os.environ.get('TestEnv', 'dev')
app = create_app(env)
manage = Manager(app)
manage.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manage.run()
