import { normalizeObj } from './helpers';

// ------------ TYPE VARIABLES ------------
const GET_ALL_PROJECTS = 'projects/getAllProjects'
const POST_NEW_PROJECT = 'projects/postNewProject'
// ---------- ACTION CREATORS ----------
const getAllProjects = (projects) =>{
  return{
    type: GET_ALL_PROJECTS,
    projects
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
    return e
  }

}
// --------- INITIAL STATE -------------
const initialState = {allProjects:{},oneProject:{}}
// ---------- REDUCER ----------
const projectReducer = (state =initialState,action) =>{

  switch(action.type){
    case GET_ALL_PROJECTS:
      return {...state,allProjects:{...normalizeObj(action.projects)}}
    case POST_NEW_PROJECT:
      return {...state,oneProject:{...normalizeObj(action.project)}}
    default:
      return state
  }
}

export default projectReducer
