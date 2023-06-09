import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory, useParams } from "react-router-dom/cjs/react-router-dom.min";
import FundingDetails from "../FundingDetails";
import "./FundingForm.css"

import { getSingleProjectThunk, postFundingThunk } from "../../store/projects";

const FundingForm = () => {
  // ----------- Variables -----------
  const { projectId } = useParams()
  const history = useHistory()
  const dispatch = useDispatch()


  // ----------- State Varibales -----------
  const [amount, setAmount] = useState(0)
  const [reward, setReward] = useState(false)
  const [errors, setErrors] = useState({})

  const project = useSelector(state => state.project.singleProject)
  const user = useSelector(state => state.session.user)
  //
  useEffect(() => {
    dispatch(getSingleProjectThunk(projectId))
  }, [dispatch])
  if (!project) return <p>Project loading...</p>

  const submitFunding = (e) => {
    e.preventDefault();
    const err = {}
    if (amount <= 0) err["amount"] = "Please enter a valid amount"

    if (Object.values(err).length) return setErrors(err)
    console.log("I have been submitted")
    console.log("values the user inputs", reward, amount)
    // Funding has three things: user_id, project_id, amount_donated and reward(boolean) one of those being collected from the user's input

    console.log("Values I will send to the backend", { reward, amount, id: user?.id, projectId: project.id })

    const formData = new FormData()
    console.log("reward..........................", reward)


    formData.append("reward", reward)
    formData.append("amount_donated", amount)
    formData.append("project_id", project.id)

    // Log our form data
    console.log("Form Data gathered from form:")
    for (let key of formData.entries()) {
      console.log(key[0] + ' ----> ' + key[1])
    }
    dispatch(postFundingThunk(formData, project.id))

    return history.push(`/projects/${projectId}`)
  }



  const rewardRendering = () => {
    return (
      <div>
        <label>
          Would you like to receive it?
          <input
            type="checkbox"
            value={reward}
            defaultValue={reward}
            onChange={e => {
              setAmount(project.reward_amount)
              setReward(!reward)
            }}
          />
        </label>
      </div>
    )
  }



  console.log("List of those who funded this project", project?.funding)
  console.log("I am the current user", user?.id)
  // Want to create some conditional rendering that would load
  // something different if a person has already funded a project

  if (user?.id === project?.owner?.id) {
    return (
      <FundingDetails
        project={project}
      />
    )
  }

  return (
    <div className="funding-form-div">
      {Object.values(errors).length ? <p className="errors-funding">{errors.amount}</p> : null}
      <form className="funding-form" onSubmit={submitFunding}>
        <label className="funding-form-pledge">
          <div className="funding-form-input-container">
          <h1>Amount to Pledge:</h1>
            <span className="dollar-sign">$</span>
            <input
              type="number"
              value={amount}
              placeholder="Amount to Pledge"
              onChange={e => setAmount(e.target.value)}
            />
            <button type='submit'>Submit</button>
          </div>
        </label>
      </form>
      <div className="rewards">
        <h2>Donate: ${project.reward_amount}</h2>
        {rewardRendering()}
        <h4>Here's what you'll get</h4>
        <h3>{project.reward_name}</h3>
        <p>{project.reward_description}</p>
      </div>
    </div>
  )
}

export default FundingForm
