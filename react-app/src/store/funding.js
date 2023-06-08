import { normalizeObj } from './helpers';



// ------------ TYPE VARIABLES ------------
const GET_PROJECT_FUNDING = 'funding/getProjectFunding';
const GET_USER_FUNDING = 'funding/getUserFunding';

// ---------- ACTION CREATORS ----------
const getProjectFunding = (funding) => {
    return {
        type: GET_PROJECT_FUNDING,
        funding
    };

}

const getUserFunding = (funded) =>{
    return {
        type: GET_USER_FUNDING,
        funded
    }
}


// ---------- THUNKS ----------
export const getProjectFundingThunk = (projectId) => async dispatch =>{
    const res = await fetch(`/api/projects/${projectId}/fund`)
    if(res.ok){
        const { funding } = await res.json();
        console.log("thunk funding",  funding )
        dispatch(getProjectFunding(funding))
    } else {
        console.log("There was an error getting all categories!")
    }
}

export const getUserFundingThunk = () => async dispatch =>{
    const res = await fetch(`/api/funds/user`)
    if(res.ok){
        const { funded } = await res.json();
        console.log("thunk funding",  funded )
        dispatch(getUserFunding(funded))
    } else {
        console.log("There was an error getting all categories!")
    }
}

const initialState = {allProject:{},project:{},userProjects:{}};

const fundingReducer = (state = initialState, action) => {
    console.log("Action", action, state)
    let newState;
    switch (action.type) {
        case GET_PROJECT_FUNDING:
            newState = { ...state };
            newState.project = normalizeObj(action.funding)
            return newState;
        case GET_USER_FUNDING:
            newState = {...state}
            newState.userProjects = normalizeObj(action.funded)
            return newState
        default:
            return state;
  }
};

export default fundingReducer;
