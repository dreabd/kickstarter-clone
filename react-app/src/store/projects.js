import { normalizeObj } from './helpers';

// ------------ TYPE VARIABLES ------------
const GET_ALL_PROJECTS = 'projects/getAllProjects'
const GET_SINGLE_PROJECT = 'projects/getSingleProject'
const POST_NEW_PROJECT = 'projects/postNewProject'
// ---------- ACTION CREATORS ----------
const getAllProjects = (projects) =>{
  return{
    type: GET_ALL_PROJECTS,
    projects
  }
}
const getSingleProject = (project) =>{
  return{
    type: GET_SINGLE_PROJECT,
    project
  }
}
const postNewProject = (project) =>{
  return{
    type: POST_NEW_PROJECT,
    project
  }
}


// ---------- THUNKS ----------
export const getAllProjectsThunk = () => async(dispatch) =>{
  const res = await fetch('/api/projects')
  if(res.ok){
    const{ projects } = await res.json()
    dispatch(getAllProjects(projects))
    return
  } else{
    console.log("Problem with loading all projects")
  }
}

export const getSingleProjectThunk = (id) => async(dispatch) =>{
  console.log("this is the id",id)
  const res = await fetch(`/api/projects/${id}`)
  if(res.ok){
    const{ single_project } = await res.json()
    dispatch(getSingleProject(single_project))
    return
  } else{
    const { errors } = await res.json()
    return errors
  }
}

export const postNewProjectThunk = (newProject) => async(dispatch) =>{
  const body = {
    project_name: newProject.projectName,
    description:newProject.description,
    category_id: newProject.category_id,
    money_goal: newProject.moneyGoal,
    city: newProject.city,
    state: newProject.state,
    story:newProject.story,
    project_image:newProject.projectImage,
    end_date: newProject.endDate,
    reward_name: newProject.rewardName,
    reward_amount: newProject.rewardAmount,
    reward_description: newProject.rewardDescription,
  }
  console.log("I am above the fetch call in the thunk",body)

  try{
    const res = await fetch('/api/projects/new',{
      method:"POST",
      headers: {"Content-Type": "application/json",},
      body: JSON.stringify(body)
    })
    console.log("I am the response",res)

    if (res.ok){
      const { project }= await res.json()
      console.log("New reward data")
      dispatch(postNewProject(project))
    }
  } catch (e) {
    console.log('catch.........................', e)
  }

}
// --------- INITIAL STATE -------------
const initialState = {allProjects:{},singleProject:{}}
// ---------- REDUCER ----------
const projectReducer = (state =initialState,action) =>{

  switch(action.type){
    case GET_ALL_PROJECTS:
      return {...state,allProjects:{...normalizeObj(action.projects)}}
    case GET_SINGLE_PROJECT:
      return {...state,singleProject:{...action.project}}
    case POST_NEW_PROJECT:
      return {...state,singleProject:{...normalizeObj(action.project)}}
    default:
      return state
  }
}

export default projectReducer
