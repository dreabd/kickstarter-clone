from app.models import Project, User, Category, Comment, db
from flask import Blueprint, jsonify, session, request
from ..forms.project_form import ProjectForm
from ..forms.edit_project_form import EditForm
from ..forms.comment_form import CommentForm

from flask_login import current_user, login_user, logout_user, login_required
from .AWS_helpers import upload_file_to_s3, get_unique_filename, remove_file_from_s3


discover_routes = Blueprint("discover", __name__)


@discover_routes.route("/")
def get_all_projects():
    """
    Grabs all the Projects with the following join: fundings, owner and category.
    Should return a JSON obj for the fronted to catch
    """
    projects = Project.query.all()
    response = [project.to_dict() for project in projects]
    return {"projects": response}


@discover_routes.route("/<categoryName>")
def get_all_projects_in_category(categoryName):
    """
    Grabs all the Projects of the specified category with the following join: fundings, owner and category.
    Should return a JSON obj for the fronted to catch
    """
    categoryStart = categoryName[:4]

    category_id = Category.query.filter(Category.type.ilike(f"%{categoryStart}%")).first()

    # print("category id.............................",category_id.id)
    # print("category index.............................",category_id)
    # print("category index.............................",category_id.to_dict())
    projects = Project.query.filter(Project.category_id == category_id.to_dict()['id']).all()
    # projects = Project.query.join(Category).filter(
    #     Category.type.like(f'%{categoryStart}%')).all()
    response = [project.to_dict() for project in projects]
    # print("response in backend from db query.......................", response)
    return {"projects": response}
