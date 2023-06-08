from app.models import Funding, db,Project
from flask import Blueprint

from flask_login import current_user, login_user, logout_user, login_required

funding_routes = Blueprint('fund', __name__)

@funding_routes.route('/user')
def get_user_funding():
    # fundeds = Project.query.filter(Project.funding.user_id == current_user.id).first()
    funded = Project.

    # res = [funded.to_dict() for funded in fundeds]

    return {"funded": "res"}
