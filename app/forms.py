from app import app, routes, db
from app.models import Note


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Note': Note}


if __name__ == "__main__":
    app.run()