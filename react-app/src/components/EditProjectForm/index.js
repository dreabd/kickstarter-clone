import React, { useState, useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useHistory, useParams } from 'react-router-dom';
import { getAllProjectsThunk, editProjectThunk } from '../../store/projects';
import { getCategoriesThunk } from '../../store/categoryReducer';

import './EditProjectForm.css'

const formatDate = (dateString) => {
    if (!dateString) return;
    const date = new Date(dateString)
    return date.toISOString().split('T')[0];
}

//this is used to convert the backend errors into a format that the frontend can use
const caseHelper = (backendstring) => {
    const backendToFrontend = {
        project_name: "projectName",
        description: "description",
        category_id: "category",
        money_goal: "moneyGoal",
        city: "city",
        state: "state",
        story: "story",
        project_image: "projectImage",
        end_date: "endDate",
        reward_name: "rewardName",
        reward_amount: "rewardAmount",
        reward_description: "rewardDescription"
    };
    return backendToFrontend[backendstring]
}

const EditProjectForm = () => {
    const dispatch = useDispatch()
    const history = useHistory()
    const { projectId } = useParams()

    const categories = useSelector(state => state.category.categories);
    useEffect(() => {
        // Fetch category data
        if (!categories) dispatch(getCategoriesThunk())
    }, [dispatch])

    const project = useSelector(state => state.project.allProjects[projectId])
    console.log("PROJECT", project)
    console.log("PROJECTID", projectId)
    console.log("project end date:", project?.end_date)

    //set up a bunch of state slices
    const [projectName, setProjectName] = useState(project?.project_name || "");
    const [description, setDescription] = useState(project?.description || "");
    const [category, setCategory] = useState(project?.category.type || "");
    const [moneyGoal, setMoneyGoal] = useState(project?.money_goal || 0);
    const [city, setCity] = useState(project?.city || "");
    const [state, setState] = useState(project?.state || "");
    const [story, setStory] = useState(project?.story || "");
    const [projectImage, setProjectImage] = useState(project?.project_image || "");
    const [endDate, setEndDate] = useState(formatDate(project?.end_date) || '2024-01-01');
    const [rewardName, setRewardName] = useState(project?.reward_name || "");
    const [rewardAmount, setRewardAmount] = useState(project?.reward_amount || 0);
    const [rewardDescription, setRewardDescription] = useState(project?.reward_description || "");
    const [errors, setErrors] = useState({});

    let prevImage = project && project.project_image
    console.log(prevImage)
    console.log("This is the state variable category is defaulted to..................", category)

    useEffect(() => {
        if (!project) {
            dispatch(getAllProjectsThunk())
        } else {
            setProjectName(project.project_name)
            setDescription(project.description)
            setCategory(project.category)
            console.log("This is how it is coming back from the database.......", project.category)
            setMoneyGoal(project.money_goal)
            setCity(project.city)
            setState(project.state)
            setStory(project.story)
            setProjectImage(project.project_image)
            setEndDate(formatDate(project.end_date))
            setRewardName(project.reward_name)
            setRewardAmount(project.reward_amount)
            setRewardDescription(project.reward_description)
        }
    }, [dispatch, project])

    const handleSubmit = async (e) => {
        e.preventDefault();

        const newErrors = {};
        // validate data on the frontend here
        if (projectName.length < 1) newErrors['projectName'] = "Project name is required!"
        if (description.length < 1) newErrors['description'] = "Description is required!"
        if (category === "Select") newErrors['category'] = "Category is required!"
        if (moneyGoal < 1) newErrors['moneyGoal'] = "Financial Goal is required!"
        if (city.length < 1) newErrors['city'] = "City is required!"
        if (state.length < 1) newErrors['state'] = "State is required!"
        if (story.length < 1) newErrors['story'] = "Story is required!"
        if (endDate === "YYYY-MM-DD") newErrors['endDate'] = "Project End Date is required!"

        setErrors(newErrors);

        // If we have errors, bail out
        if (Object.keys(newErrors).length) return;

        // Build up our form data
        const formData = new FormData()
        formData.append("project_name", projectName)
        formData.append("description", description)
        formData.append("category_id", category.id)
        formData.append("money_goal", moneyGoal)
        formData.append("city", city)
        formData.append("state", state)
        formData.append("story", story)
        formData.append("project_image", projectImage)
        formData.append("end_date", endDate)
        formData.append("reward_name", rewardName)
        formData.append("reward_amount", rewardAmount)
        formData.append("reward_description", rewardDescription)

        // Log our form data
        console.log("Form Data gathered from form:")
        for (let key of formData.entries()) {
            console.log(key[0] + ' ----> ' + key[1])
        }

        const editedProjectOrErrors = await dispatch(editProjectThunk(project.id, formData))

        console.log("Data returned from edit project thunk", editedProjectOrErrors)

        // Handle backend validation errors
        if (!editedProjectOrErrors) return null
        if ('errors' in editedProjectOrErrors) {
            // handle errors from the backend which comes in as an object with a key of errors
            console.error('The backend returned validation errors when creating a new form', editedProjectOrErrors)
            const formErrors = editedProjectOrErrors.errors
            let errorObj = {}

            Object.keys(formErrors).forEach((errorKey) => {
                const frontEndErrorKey = caseHelper(errorKey)
                const frontEndErrorString = formErrors[errorKey][0]
                errorObj[frontEndErrorKey] = frontEndErrorString
            })
            setErrors(errorObj)
        } else {
            if (editedProjectOrErrors) {
                history.push(`/projects/${editedProjectOrErrors.id}`)
            } else {
                console.error("Nothing returned from edit project thunk")
            }
        }

        // TODO - redirect to edited project's show page
    }

    if (!project) return <p>Project loading...</p>

    return (
        <div>
            <h1>Edit your Project!</h1>
            <form className='form' onSubmit={handleSubmit} encType="multipart/form-data">
                <label>
                    Project Name <span className='errors'>{errors.projectName}</span>
                    <input
                        type='text'
                        value={projectName}
                        placeholder='Project Name'
                        onChange={(e) => setProjectName(e.target.value)}
                    />
                </label>
                <label>
                    Project Description <span className='errors'>{errors.description}</span>
                    <input
                        type='text'
                        value={description}
                        placeholder='Project Description'
                        onChange={(e) => setDescription(e.target.value)}
                    />
                </label>
                <label>
                    Category <span className='errors'>{errors.category}</span>
                    <select
                        value={category}
                        onChange={(e) => {
                            console.log("This is e.target.value in the on change.................", e.target.value)
                            setCategory(e.target.value)
                        }
                        }>
                        <option default>{category.type}</option>
                        {categories && Object.values(categories).map(category => (
                            <option key={category.id} value={category.id}>
                                {category.type}
                            </option>
                        ))}
                    </select>
                </label>
                <label>
                    Financial Goal <span className='errors'>{errors.moneyGoal}</span>
                    <input
                        type='number'
                        value={moneyGoal}
                        placeholder='Financial Goal'
                        onChange={(e) => setMoneyGoal(e.target.value)}
                    />
                </label>
                <label>
                    City <span className='errors'>{errors.city}</span>
                    <input
                        type='text'
                        value={city}
                        placeholder='city'
                        onChange={(e) => setCity(e.target.value)}
                    />
                </label>
                <label>
                    State <span className='errors'>{errors.state}</span>
                    <input
                        type='text'
                        value={state}
                        placeholder='State'
                        onChange={(e) => setState(e.target.value)}
                    />
                </label>
                <label>
                    Project Story <span className='errors'>{errors.story}</span>
                    <textarea
                        type='text'
                        value={story}
                        placeholder='Project Story'
                        onChange={(e) => setStory(e.target.value)}>
                    </textarea>
                </label>
                <label>
                    Project Image<span className='errors'>{errors.projectImage}</span>
                    <input
                        type='file'
                        accept='image/*'
                        placeholder='Project Image'
                        onChange={(e) => {
                            console.log("e.target.files????", e.target.files)
                            setProjectImage(e.target.files[0])
                        }}
                    />
                    <div>
                        <p><a href={projectImage}>Existing Project Image</a></p>
                        <img className="thumbnail" src={prevImage} alt="project_image" />
                    </div>
                </label>
                <label>
                    End Date <span className='errors'>{errors.endDate}</span>
                    <input
                        type='date'
                        value={endDate}
                        placeholder='End Date'
                        onChange={(e) => setEndDate(e.target.value)}
                    />
                </label>
                <label>
                    Reward Name<span className='errors'>{errors.rewardName}</span>
                    <input
                        type='text'
                        value={rewardName}
                        placeholder='Reward Name'
                        onChange={(e) => setRewardName(e.target.value)}
                    />
                </label>
                <label>
                    Reward Amount<span className='errors'>{errors.rewardAmount}</span>
                    <input
                        type='number'
                        value={rewardAmount}
                        placeholder='Reward Amount'
                        onChange={(e) => setRewardAmount(e.target.value)}
                    />
                </label>
                <label>
                    Reward Description <span className='errors'>{errors.rewardDescription}</span>
                    <textarea
                        type='text'
                        value={rewardDescription}
                        placeholder='Reward Description'
                        onChange={(e) => setRewardDescription(e.target.value)}>
                    </textarea>
                </label>
                <button className='create-project-submit-button' type='submit'>Update Project</button>
            </form>
        </div >
    )
}

export default EditProjectForm
