import { normalizeObj } from './helpers';

// ------------ TYPE VARIABLES ------------
const GET_ALL_PROJECTS = 'projects/getAllProjects'
// ---------- ACTION CREATORS ----------
const getAllProjects = (projects) =>{
  return{
    type: GET_ALL_PROJECTS,
    projects
  }
}
// ---------- THUNKS ----------
export const getAllProjectsThunk = () => async(dispatch) =>{
  const res = await fetch('api/projects')
  if(res.ok){
    const{ projects } = await res.json()
    dispatch(getAllProjects(projects))
    return
  } else{
    console.log("Problem with loading all projects")
  }
}
// --------- INITIAL STATE -------------
const initialState = {allProjects:{},oneProject:{}}
// ---------- REDUCER ----------
const projectReducer = (state =initialState,action) =>{

  switch(action.type){
    case GET_ALL_PROJECTS:
      return {...state,allProjects:{...normalizeObj(action.projects)}}
    default:
      return state
  }
}

export default projectReducer
