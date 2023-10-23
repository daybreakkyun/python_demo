from shared import exception_handler, sql_engine
from modules.person import person_route
from modules.department import department_route
from flask_migrate import Migrate

app = sql_engine.create_app()

with app.app_context():
    sql_engine.db.create_all()

db = sql_engine.db
migrate = Migrate(app, db)

#init API templates
app.register_blueprint(person_route.api)
app.register_blueprint(department_route.api)

#init Global Exception Hanlder
app.register_blueprint(exception_handler.error)

if __name__ == '__main__':
    app.run(debug=True)