from app.models import Project, db
from flask import Blueprint, request

search_routes = Blueprint("search", __name__)


@search_routes.route("/")
def search_projects():
    """
    Searches through all of the projects based on query parameters from the search bar.
    Should return a JSON obj for the fronted to catch
    """
    args = request.args
    search_query = request.args.get("query")
    print("search param being picked up by backend route: ", search_query)
    project_query = (
        db.session.query(Project)
        .filter((Project.project_name.ilike(f"%{search_query}%")) | (Project.description.ilike(f"%{search_query}%")) | (Project.story.ilike(f"%{search_query}%")))
    )
    print("query response from search route: ", project_query.all())
    response = [project.to_dict() for project in project_query]
    return {"projects": response}
