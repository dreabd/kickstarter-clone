from app.models import Project, User, Category, db
from flask import Blueprint, jsonify, session, request
from ..forms.project_form import ProjectForm

from flask_login import current_user, login_user, logout_user, login_required
from .AWS_helpers import upload_file_to_s3, get_unique_filename, remove_file_from_s3


project_routes = Blueprint("projects", __name__)

@project_routes.route("/current")
def get_current_user_project():
    '''
    Grabs all the spots owned by the current user
    '''

    id = current_user.id
    print("This is the id of the current user.........", id)

    projects = Project.query.filter(Project.user_id == id)

    res = [project.to_dict() for project in projects  ]

    return {"projects": res }




@project_routes.route("/<int:id>")
def get_single_project(id):
    """
    Grabs a pro
    """
    single_project = Project.query.get(id)
    print("project...................................", single_project)

    if single_project is None:
        return {"errors": "Project not Found"}

    response = single_project.to_dict()
    return {"single_project": response}



@project_routes.route("/new", methods=["POST"])
# @login_required
def post_new_project():
    """
    Posts form data from the frontend and send back the new project.
    """
    print("I am in the backend post")
    form = ProjectForm()
    form["csrf_token"].data = request.cookies["csrf_token"]
    print("form...............", {form})
    # if current_user:
    print("for.errors....................", form.errors)

    if form.validate_on_submit():
        data = form.data

        project_image = data["project_image"]
        # project_image.filename = get_unique_filename(project_image)
        # upload = upload_file_to_s3(project_image)

        # category = data["category"]
        # category_id = Category.query.filter(Category.type == category).to_dict()
        # print("I am the category id you SHOULD have selected",category_id["id"])

        # if "url" not in upload:
        #     print("Errors Occured in the AWS Upload", upload["errors"])
        #     return upload["errors"]

        # Uncomment this line when actually uploading project images
        # image=upload["url"]
        image = data["project_image"]

        new_project = Project(
            project_name=data["project_name"],
            description=data["description"],
            category_id=data["category_id"],
            money_goal=data["money_goal"],
            user_id=1,
            city=data["city"],
            state=data["state"],
            story=data["story"],
            project_image=image,
            end_date=data["end_date"],
            reward_name=data["reward_name"],
            reward_amount=data["reward_amount"],
            reward_description=data["reward_description"],
        )
        db.session.add(new_project)
        db.session.commit()
        print("This is your new Project", new_project)
        return {"project": new_project.to_dict()}

    if form.errors:
        print("There were some form errors", form.errors)
        return form.errors, 400





@project_routes.route("/")
def get_all_projects():
    """
    Grabs all the Projects with the following join: fundings, owner and category.
    Should return a JSON obj for the fronted to catch
    """
    projects = Project.query.all()
    response = [project.to_dict() for project in projects]
    return {"projects": response}
