import React, { useState, useEffect } from 'react';
import { useHistory } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import { postNewProjectThunk } from '../../store/projects';
import { getCategoriesThunk } from '../../store/categoryReducer';

function CreateProjectForm() {

    //Intialize things
    const history = useHistory();
    const dispatch = useDispatch();

    //useSelectors
    // const sessionUser = useSelector(state => state.session.user);
    const categories = useSelector(state => state.category.categories);
    // const categoryArray = Object.values(categories);

    useEffect(()=>{
        dispatch(getCategoriesThunk())
    },[dispatch])

    // const userId = sessionUser.id

    //set up a bunch of state slices
    const [projectName, setProjectName] = useState('');
    const [description, setDescription] = useState('');
    const [category, setCategory] = useState('');
    const [moneyGoal, setMoneyGoal] = useState(0);
    const [city, setCity] = useState('');
    const [state, setState] = useState('');
    const [story, setStory] = useState('');
    const [projectImage, setProjectImage] = useState('');
    const [endDate, setEndDate] = useState('YYYY-MM-DD');//////////////
    const [rewardName, setRewardName] = useState('');
    const [rewardAmount, setRewardAmount] = useState(0);
    const [rewardDescription, setRewardDescription] = useState('');
    const [errors, setErrors] = useState({});

    //create form for transmital
    const form = {projectName,
                  description,
                  category,
                  moneyGoal,
                  city,
                  state,
                  story,
                  projectImage,
                  endDate,
                  rewardName,
                  rewardAmount,
                  rewardDescription,
                //   userId
                }

    const handleSubmit = async (e) => {
        e.preventDefault();

        const newErrors = {};
        //validate data here
        if(projectName.length < 1) newErrors['projectName'] = "Project name is required!"
        if(description.length < 1) newErrors['description'] = "Description is required!"
        if(category == "Select") newErrors['category'] = "Category is required!"
        if(moneyGoal < 1) newErrors['moneyGoal'] = "Financial Goal is required!"
        if(city.length < 1) newErrors['city'] = "City is required!"
        if(state.length < 1) newErrors['state'] = "State is required!"
        if(story.length < 1) newErrors['story'] = "Story is required!"
        // if(projectImage.length < 1) newErrors['ProjectImage'] = "Project Image is required!"
        if(endDate == "YYYY-MM-DD") newErrors['endDate'] = "Project End Date is required!"
        // if(rewardName.length < 1) newErrors['rewardName'] = "Reward Name is required!"
        // if(rewardAmount < 1) newErrors['rewardAmount'] = "Reward Amount is required!"
        // if(rewardDescription.length < 1) newErrors['rewardDescription'] = "Reward Description is required!"

        setErrors(newErrors);

        if(!Object.keys(newErrors).length) {
            const newProject = await dispatch(postNewProjectThunk(form))

            setProjectName('');
            setDescription('');
            setCategory('');
            setMoneyGoal(0);
            setCity('');
            setState('');
            setStory('');
            setProjectImage('');
            setEndDate('YYYY-MM-DD');
            setRewardName('');
            setRewardAmount(0);
            setRewardDescription('');

            history.push(`/projects`)
        }

    }

    return (
        <div>
            <h1>Create your new Project!</h1>
            <form className='form' onSubmit={handleSubmit}>
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
                    <option default>Select</option>
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
                    value={projectImage}
                    placeholder='Project Image'
                    onChange={(e) => setProjectImage(e.target.files[0])}
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


export default CreateProjectForm
