import { normalizeObj } from './helpers';

// ------------ TYPE VARIABLES ------------
const GET_ALL_PROJECTS = 'projects/getAllProjects'
const GET_SINGLE_PROJECT = 'projects/getSingleProject'
const POST_NEW_PROJECT = 'projects/postNewProject'
const GET_CURRENT_PROJECT = "projects/getCurrentProject"
const DELETE_SINGLE_PROJECT = "projects/deleteSingleProject"
// ---------- ACTION CREATORS ----------
const getAllProjects = (projects) => {
  return {
    type: GET_ALL_PROJECTS,
    projects
  }
}
const getSingleProject = (project) => {
  return {
    type: GET_SINGLE_PROJECT,
    project
  }
}
const postNewProject = (project) => {
  return {
    type: POST_NEW_PROJECT,
    project
  }
}
const getCurrentProject = (projects) => {
  return {
    type: GET_CURRENT_PROJECT,
    projects
  }
}

const deleteSingleProject = (projectId) => {
  return{
    type: DELETE_SINGLE_PROJECT,
    projectId
  }
}




// ---------- THUNKS ----------
export const getAllProjectsThunk = () => async (dispatch) => {
  const res = await fetch('/api/projects')
  if (res.ok) {
    const { projects } = await res.json()
    dispatch(getAllProjects(projects))
    return
  } else {
    console.log("Problem with loading all projects")
  }
}

export const getCurrentProjectThunk = () => async (dispatch) =>{
  const res =await fetch('/api/projects/current')
  if(res.ok){
    const {projects} = await res.json()
    console.log(projects)
    dispatch(getCurrentProject(projects))
    return
  }
}

export const getSingleProjectThunk = (id) => async (dispatch) => {
  console.log("this is the id", id)
  const res = await fetch(`/api/projects/${id}`)
  if (res.ok) {
    const { single_project } = await res.json()
    dispatch(getSingleProject(single_project))
    return
  } else {
    const { errors } = await res.json()
    return errors
  }
}

export const postNewProjectThunk = (newProject) => async (dispatch) => {
  try {
    console.log("Making post request to new project route")
    const res = await fetch('/api/projects/new', {
      method: "POST",
      body: newProject
    })
    console.log("Post request", res)

    if (res.ok) {
      console.log("Response OK")
      const response = await res.json()
      console.log("Response data", response)
      dispatch(postNewProject(response.project))
      return response.project
    } else {
      console.error("Response not OK. Status code:", res.status)
      const response = await res.json()
      console.log("Response when res is not okay and there are errors:", response)
      return {
        errors: { ...response }
      }
    }
  } catch (e) {
    console.error('Error caught in postNewProjectThunk', e)
    return e
  }
}

export const deleteSingleProjectThunk = (projectId) => async (dispatch) =>{
  const res = await fetch(`/api/projects/${projectId}`,{
    method:"DELETE"
  })
  if(res.ok){
    dispatch(deleteSingleProject(projectId))
  }
}
// --------- INITIAL STATE -------------
const initialState = { allProjects: {}, singleProject: {}, userProjects:{}}
// ---------- REDUCER ----------
const projectReducer = (state = initialState, action) => {

  switch (action.type) {
    case GET_ALL_PROJECTS:
      return { ...state, allProjects: { ...normalizeObj(action.projects) } }
    case GET_SINGLE_PROJECT:
      return { ...state, singleProject: { ...action.project } }
    case GET_CURRENT_PROJECT:
      return{...state,userProjects:{...normalizeObj(action.projects)}}
    case POST_NEW_PROJECT:
      return { ...state, singleProject: { ...action.project } }
    case DELETE_SINGLE_PROJECT:
      let newState = {...state}
      delete newState.allProjects[action.projectId]
      delete newState.userProjects[action.projectId]
      return newState
    default:
      return state
  }
}

export default projectReducer
