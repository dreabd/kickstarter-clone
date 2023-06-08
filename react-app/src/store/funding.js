import { normalizeObj } from './helpers';



// ------------ TYPE VARIABLES ------------
const GET_PROJECT_FUNDING = 'funding/getProjectFunding';

// ---------- ACTION CREATORS ----------
export const getProjectFunding = (funding) => {
    return {
        type: GET_PROJECT_FUNDING,
        funding
    };

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


const initialState = {allProject:{},project:{}};

const fundingReducer = (state = initialState, action) => {
    console.log("Action", action, state)
    let newState;
    switch (action.type) {
        case GET_PROJECT_FUNDING:
            newState = { ...state };
            newState.project = normalizeObj(action.funding)
            return newState;
        default:
            return state;
  }
};

export default fundingReducer;
