import React, { useState, useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { Redirect, useHistory, useParams } from 'react-router-dom';
import { getAllProjectsThunk } from '../../store/projects';
import { getCategoriesThunk } from '../../store/categoryReducer';

// const formatDate = (dateString) => {
//     const date = new Date(dateString)
//     return date.toString().toISOString().split("T")[0]
// }

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
    const [endDate, setEndDate] = useState(project?.end_date || '2024-01-01');
    const [rewardName, setRewardName] = useState(project?.reward_name || "");
    const [rewardAmount, setRewardAmount] = useState(project?.reward_amount || 0);
    const [rewardDescription, setRewardDescription] = useState(project?.reward_description || "");
    const [errors, setErrors] = useState({});

    useEffect(() => {
        if (!project) {
            dispatch(getAllProjectsThunk())
        } else {
            setProjectName(project.project_name)
            setDescription(project.description)
            setCategory(project.category.type)
            setMoneyGoal(project.money_goal)
            setCity(project.city)
            setState(project.state)
            setStory(project.story)
            setProjectImage(project.project_image)
            setEndDate(project.end_date)
            setRewardName(project.reward_name)
            setRewardAmount(project.reward_amount)
            setRewardDescription(project.reward_description)
        }
    }, [dispatch, project])

    const handleSubmit = async (e) => {
        e.preventDefault();
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
                        onChange={(e) => setCategory(e.target.value)}>
                        <option default>{category}</option>
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
                    Project Image <span className='errors'>{errors.projectImage}</span>
                    <input
                        type='file'
                        accept='image/*'
                        // value={projectImage}
                        placeholder='Project Image'
                        onChange={(e) => {
                            console.log("e.target.files????", e.target.files)
                            setProjectImage(e.target.files[0])
                        }}
                    />
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
                <button className='create-project-submit-button' type='submit'>Create Project</button>
            </form>
        </div>
    )
}

export default EditProjectForm
