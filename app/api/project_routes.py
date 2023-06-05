from app.models import Project,User, Category,db
from flask import Blueprint, jsonify, session, request
from forms.project_form import ProjectForm
from forms.reward_form import RewardForm

from flask_login import current_user, login_user, logout_user, login_required
from .AWS_helpers import upload_file_to_s3, get_unique_filename, remove_file_from_s3


project_routes = Blueprint('projects', __name__)

@project_routes.route('/')
def get_all_projects():
    '''
    Grabs all the Projects with the following join: fundings, owner and category.
    Should return a JSON obj for the fronted to catch
    '''
    projects = Project.query.all()
    response = [project.to_dict() for project in projects]
    return { "projects" : response}


@project_routes.route('/<int:id>')
def get_single_project(id):
    '''
    '''
    single_project = Project.query.get(id)
    response = single_project.to_dict()

    return { "single_project" : response}

@project_routes.route("/",methods=["POST"])
@login_required
def post_new_project():
    '''
    Posts form data from the frontend and send back the new project.
    '''
    form = ProjectForm()
    reward_form = RewardForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    # if current_user:

    if form.validate_on_submit():
        data = form.data

        project_image = data["project_image"]
        project_image.filename = get_unique_filename(project_image.filename)
        upload = upload_file_to_s3(project_image)

        category = data["category"]
        category_id = Category.query.filter(Category.type == category).to_dict()
        print("I am the category id you SHOULD have selected",category_id["id"])

        if "url" not in upload:
            print("Errors Occured in the AWS Upload", upload["errors"])
            return upload["errors"]

        '''
        If there is an instance of a submit FOR a reward form then it create a new
        project BUT with the rewards
        '''
        if(reward_form.validate_on_submit()):
            new_project = Project(
                project_name = data["project_name"],
                description = data["description"],
                category_id = category_id['id'],
                money_goal = data["money_goal"],
                user_id = current_user.id,
                city = data["city"],
                state = data["state"],
                story = data["story"],
                project_image = upload["url"],
                end_date = data["end_date"],
                reward_name = reward_form.data["reward_name"],
                reward_amount = reward_form.data["reward_amount"],
                reward_description = reward_form.data["reward_description"],
                )
            db.session.add(new_project)
            db.session.commit()
            print("This is your new Project with a reward", new_project)
            return {"project":new_project.to_dict()}

        if reward_form.errors:
            print("There were some reward form errors",reward_form.errors)
            return reward_form.errors

        new_project = Project(
            project_name = data["project_name"],
            description = data["description"],
            category_id = category_id['id'],
            money_goal = data["money_goal"],
            user_id = current_user.id,
            city = data["city"],
            state = data["state"],
            story = data["story"],
            project_image = upload["url"],
            end_date = data["end_date"],
        )

        print("This is your new Project without a reward", new_project)
        db.session.add(new_project)
        db.session.commit()

        return {"project":new_project.to_dict()}

    if form.errors:
        print("There were some form errors",form.errors)
        return form.errors
