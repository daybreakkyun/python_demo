from shared import exception_handler, engine
from flask_migrate import Migrate
from modules.person import person_api
from modules.department import department_api

app = engine.create_app()

with app.app_context():
    engine.db.create_all()

db = engine.db
migrate = Migrate(app, db)

engine.api.add_namespace(person_api.api)
engine.api.add_namespace(department_api.api)

#init Global Exception Hanlder
app.register_blueprint(exception_handler.error)

if __name__ == '__main__':
    app.run(debug=True)