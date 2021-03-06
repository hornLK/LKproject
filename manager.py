from app import db,create_app

import os
from flask_script import Manager,Shell
from app.common.models import Role,User,Group,Department
from app.IP_manager.models import Network, Ips
from flask_migrate import Migrate,MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app,db)

def make_shell_context():
    return dict(app=app,db=db,Role=Role,User=User,Group=Group,Department=Department,Network=Network,Ips=Ips)

manager.add_command('shell',Shell(make_context=make_shell_context))
manager.add_command('db',MigrateCommand)

if __name__=="__main__":
    manager.run()

