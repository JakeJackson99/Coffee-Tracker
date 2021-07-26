# flake8: noqa
from app import app, db, routes
from app.models import AdminUser, Bean


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'AdminUser': AdminUser, 'Bean': Bean}


if __name__ == "__main__":
    app.run()
