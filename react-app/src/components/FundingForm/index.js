import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory, useParams } from "react-router-dom/cjs/react-router-dom.min";


import { getSingleProjectThunk } from "../../store/projects";

const FundingForm = () =>{
  // ----------- Variables -----------
  const {projectId} = useParams()
  const history = useHistory()
  const dispatch = useDispatch()


  // ----------- State Varibales -----------
  const [amount,setAmount] = useState(0)

  const project = useSelector(state=> state.project.singleProject)
  //
  useEffect(()=>{
    dispatch(getSingleProjectThunk(projectId))
  },[dispatch])
  if (!project) return <p>Project loading...</p>

  const submitFunding = () =>{

  }

  return(
    <div className="">
      <form onSubmit={submitFunding}>
        <label >
          Amount to Pledge: $
          <input
            type="number"
            value={amount}
            placeholder="Amount to Pledge"
            onChange={e=>setAmount(e.target.value)}
          />
        </label>
        <button type='submit'>Submit</button>
      </form>
      <div className="rewards">
        <h4>Donate: ${project.reward_amount}</h4>
        <p>Here's what you'll get</p>
        <h3>{project.reward_name}</h3>
        <p>{project.reward_description}</p>
      </div>
    </div>
  )
}

export default FundingForm
