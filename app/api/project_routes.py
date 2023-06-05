from app.models import Project,User, db
from flask import Blueprint

project_routes = Blueprint('projects', __name__)

@project_routes.route('/')
def get_all_projects():
    '''
    Grabs all the Projects with the following join: fundings, owner and category.
    Should return a JSON obj for the fronted to catch
    '''
    projects = Project.query.all()
    response = []

    for project in projects:
        owner = project.user
        category = project.category
        project = project.to_dict()
        project["owner"] = owner.to_dict()
        project["category"] = category.to_dict()
        response.append(project)

    # response = [project.to_dict() for project in projects]
    return { "projects" : response}


