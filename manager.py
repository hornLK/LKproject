from app import db,create_app

import os
from flask_script import Manager,Shell
from app.lk_cmdb.models import account
from flask_migrate import Migrate,MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app,db)

print (dir(db.Column))
def make_shell_context():
    return dict(app=app,db=db,Role=account.Role,User=account.User,Group=account.Group)

manager.add_command('shell',Shell(make_context=make_shell_context))
manager.add_command('db',MigrateCommand)

if __name__=="__main__":
    manager.run()

