import { normalizeObj } from './helpers';

// ------------ TYPE VARIABLES ------------
const GET_ALL_PROJECTS = 'projects/getAllProjects'
const GET_SINGLE_PROJECT = 'projects/getSingleProject'
const POST_NEW_PROJECT = 'projects/postNewProject'
const POST_NEW_COMMENT = 'projects/postNewComment'
const GET_CURRENT_PROJECT = "projects/getCurrentProject"
const DELETE_SINGLE_PROJECT = "projects/deleteSingleProject"
const DELETE_COMMENT = "projects/deleteComment"
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
const postNewComment = (comment) => {
  return {
    type: POST_NEW_COMMENT,
    comment
  }
}
const getCurrentProject = (projects) => {
  return {
    type: GET_CURRENT_PROJECT,
    projects
  }
}

const deleteSingleProject = (projectId) => {
  return {
    type: DELETE_SINGLE_PROJECT,
    projectId
  }
}

const deleteComment = (id) => {
  return {
    type: DELETE_COMMENT,
    id
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

export const getCurrentProjectThunk = () => async (dispatch) => {
  const res = await fetch('/api/projects/current')
  if (res.ok) {
    const { projects } = await res.json()
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

export const deleteSingleProjectThunk = (projectId) => async (dispatch) => {
  const res = await fetch(`/api/projects/${projectId}`, {
    method: "DELETE"
  })
  if (res.ok) {
    dispatch(deleteSingleProject(projectId))
  }
}

export const postCommentThunk = (form) => async (dispatch) => {
  // console.log('form inside of the thunk.................',form)
  // console.log('JSONIFIED form inside of the thunk.................',JSON.stringify(form))
  const res = await fetch('/api/projects/comments/new', {
    method: "POST",
    headers: { "Content-Type": "application/json", },
    body: JSON.stringify(form)
  })
  // console.log('res after returning from backend..........', res)
  if (res.ok) {
    const response = await res.json()
    // console.log("New comment added")
    dispatch(postNewComment(response))
    return response
  } else {
    const response = await res.json()
    return {
      errors: { ...response }
    }
  }
}

export const deleteCommentThunk = (id) => async (dispatch) => {
  id = parseInt(id)
  const res = await fetch(`/api/projects/comments/${id}`, {
    method: "DELETE"
  })
  if (res.ok) {
    dispatch(deleteComment(id))
  }
}

export const updateCommentThunk = (form, commentId) => async (dispatch) => {
  id = parseInt(commentId)
  const res = await fetch(`/api/projects/comments/${id}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(form)
  })

}

// --------- INITIAL STATE -------------
const initialState = { allProjects: {}, singleProject: {}, userProjects: {} }
// ---------- REDUCER ----------
const projectReducer = (state = initialState, action) => {

  switch (action.type) {
    case GET_ALL_PROJECTS:
      return { ...state, allProjects: { ...normalizeObj(action.projects) } }
    case GET_SINGLE_PROJECT:
      return { ...state, singleProject: { ...action.project } }
    case GET_CURRENT_PROJECT:
      return { ...state, userProjects: { ...normalizeObj(action.projects) } }
    case POST_NEW_PROJECT:
      return { ...state, singleProject: { ...action.project } }
    case POST_NEW_COMMENT:
      // console.log('comment entered the reducer..............', action.comment)
      let newState = { ...state, singleProject: { ...state.singleProject } }
      if (!newState.singleProject.comments) {
        newState.singleProject.comments = [action.comment]
      } else if (newState.singleProject.comments) {
        newState.singleProject.comments.push(action.comment)
      }
      // console.log('newState after updating redux store before return.............', newState)
      return newState
    case DELETE_SINGLE_PROJECT:
      let newDeleteState = { ...state }
      delete newDeleteState.allProjects[action.projectId]
      delete newDeleteState.userProjects[action.projectId]
      return newDeleteState
    case DELETE_COMMENT:
      let newDeleteCommentState = { ...state, singleProject: { ...state.singleProject } }
      let filteredComments = newDeleteCommentState.singleProject.comments.filter(comment => comment.id !== action.id)
      newDeleteCommentState.singleProject.comments = filteredComments
      return newDeleteCommentState
    default:
      return state
  }
}

export default projectReducer
