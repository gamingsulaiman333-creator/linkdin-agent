from flask import Blueprint, render_template
from services.linkedin_service import LinkedInService

linkedin_bp = Blueprint("linkedin", __name__)

@linkedin_bp.route("/linkedin")
def linkedin_home():
    return render_template("linkedin.html")

