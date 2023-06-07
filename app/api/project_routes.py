from app.models import Project, User, Category, Comment, db
from flask import Blueprint, jsonify, session, request
from ..forms.project_form import ProjectForm
from ..forms.edit_project_form import EditForm
from ..forms.comment_form import CommentForm

from flask_login import current_user, login_user, logout_user, login_required
from .AWS_helpers import upload_file_to_s3, get_unique_filename, remove_file_from_s3


project_routes = Blueprint("projects", __name__)


@project_routes.route("/current")
def get_current_user_project():
    """
    Grabs all the spots owned by the current user
    """

    id = current_user.id
    print("This is the id of the current user.........", id)

    projects = Project.query.filter(Project.user_id == id)

    res = [project.to_dict() for project in projects]

    return {"projects": res}


@project_routes.route("/<int:id>")
def get_single_project(id):
    """ """
    single_project = Project.query.get(id)
    print("project...................................", single_project)

    if single_project is None:
        return {"errors": "Project not Found"}

    response = single_project.to_dict()
    return {"single_project": response}


@project_routes.route("/<int:id>", methods=["DELETE"])
@login_required
def delete_single_project(id):
    """
    Takes in a project_id from the frontend then uses that to initalize a
    delete
    """

    project = Project.query.get(id)
    print(id)

    if project is None:
        return {"errors": "Project does not exist"}, 404

    if project.user_id != current_user.id:
        return {"errors": "Forbidden"}, 401

    # Would want to implement something where you can not delete old projects.

    db.session.delete(project)
    db.session.commit()

    return {"message": "Succesfully Deleted"}


@project_routes.route("/new", methods=["POST"])
@login_required
def post_new_project():
    """
    Posts form data from the frontend and send back the new project.
    """
    print("I am in the backend post")
    form = ProjectForm()
    form["csrf_token"].data = request.cookies["csrf_token"]
    print("form...............", form)
    # if current_user:

    if form.validate_on_submit():
        data = form.data

        project_image = data["project_image"]
        print("PROJECT IMAGE data from the backend route ", project_image)
        project_image.filename = get_unique_filename(project_image.filename)
        upload = upload_file_to_s3(project_image)

        if "url" not in upload:
            print("Errors Occured in the AWS Upload", upload["errors"])
            return upload["errors"]

        new_project = Project(
            project_name=data["project_name"],
            description=data["description"],
            category_id=data["category_id"],
            money_goal=data["money_goal"],
            user_id=current_user.id,
            city=data["city"],
            state=data["state"],
            story=data["story"],
            project_image=upload["url"],
            end_date=data["end_date"],
            reward_name=data["reward_name"],
            reward_amount=data["reward_amount"],
            reward_description=data["reward_description"],
        )
        db.session.add(new_project)
        db.session.commit()
        print("This is your new Project", new_project)
        return (
            {"project": new_project.to_dict()},
            200,
            {"Content-Type": "application/json"},
        )

    if form.errors:
        print("There were some form errors", form.errors)
        return {"errors": form.errors}, 400, {"Content-Type": "application/json"}


@project_routes.route("/<int:id>/edit", methods=["PUT"])
@login_required
def edit_project(id):
    print("EDITING PROJECT", id)
    edit_form = EditForm()
    edit_form["csrf_token"].data = request.cookies["csrf_token"]
    print("FORM", edit_form)

    if edit_form.validate_on_submit():
        data = edit_form.data

        # TODO - add ability to upload new file
        # project_image = data["project_image"]
        # print("PROJECT IMAGE data from the backend route ", project_image)
        # project_image.filename = get_unique_filename(project_image.filename)
        # upload = upload_file_to_s3(project_image)

        # if "url" not in upload:
        #     print("Errors Occured in the AWS Upload", upload["errors"])
        #     return upload["errors"]

        new_project = Project(
            id=id,
            project_name=data["project_name"],
            description=data["description"],
            category_id=data[
                "category"
            ],  # TODO - category is not being passed correctly?
            money_goal=data["money_goal"],
            user_id=current_user.id,
            city=data["city"],
            state=data["state"],
            story=data["story"],
            project_image=data[
                "project_image"
            ],  # TODO - project_image is also not being passed correctly?
            end_date=data["end_date"],
            reward_name=data["reward_name"],
            reward_amount=data["reward_amount"],
            reward_description=data["reward_description"],
        )

        # Delete existing project in db
        project_in_db = Project.query.get(id)

        if project_in_db is None:
            return {"errors": "Project does not exist"}, 404

        if project_in_db.user_id != current_user.id:
            return {"errors": "Forbidden"}, 401

        db.session.delete(project_in_db)
        db.session.commit()

        # Add new_project in its place
        db.session.add(new_project)
        db.session.commit()
        print("This is your new Project", new_project)
        return (
            {"project": new_project.to_dict()},
            200,
            {"Content-Type": "application/json"},
        )

    if edit_form.errors:
        print("There were some form errors", edit_form.errors)
        return {"errors": edit_form.errors}, 400, {"Content-Type": "application/json"}


@project_routes.route("/")
def get_all_projects():
    """
    Grabs all the Projects with the following join: fundings, owner and category.
    Should return a JSON obj for the fronted to catch
    """
    projects = Project.query.all()
    response = [project.to_dict() for project in projects]
    return {"projects": response}


@project_routes.route("/comments/new", methods=["POST"])
# @login_required
def post_new_comment():
    """
    Posts form data from the frontend into the comments table.
    Should return a JSON obj for the fronted to catch
    """
    # print('entered the backend.................')
    form = CommentForm()
    form["csrf_token"].data = request.cookies["csrf_token"]

    if form.validate_on_submit():
        data = form.data
        # print('passed form validators.................')
        newComment = Comment(
            user_id=data["user_id"],
            project_id=data["project_id"],
            comment=data["comment"],
        )

        db.session.add(newComment)
        db.session.commit()
        # print("This is your new comment.................", newComment)
        return newComment.to_dict()

    if form.errors:
        print("There were some form errors", form.errors)
        return form.errors, 400
