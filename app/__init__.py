from flask import Flask
from routes.linkedin import linkedin_bp

app = Flask(__name__)
app.register_blueprint(linkedin_bp)

