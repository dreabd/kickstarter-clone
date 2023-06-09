import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getProjectFundingThunk } from "../../store/funding";
import './FundingDetails.css'


const FundingDetails = ({ project }) => {
  // ----- Variables ------
  const dispatch = useDispatch()
  const fundings = useSelector(state => state.funding.project)

  // console.log("This is the project id in the funding detail component", project.id)
  // ----- useEffect -----
  useEffect(() => {
    dispatch(getProjectFundingThunk(project.id))
  }, [dispatch])

  // ---- HTML Element Functions -----
  const user_info =
    Object.values(fundings)?.map(funding => {
      // console.log(funding.reward)
      return (
        <div>
          <h4>{funding.user.email}</h4>
          <p>{funding.user.first_name} {funding.user.last_name}</p>
          <p>Donated: ${funding.amount_donated}</p>
          <p>{funding.reward ? "Opted in for a reward" : "Opted Out for a reward"}</p>
        </div>
      )
    })

  if (!fundings) return <h1> Loading...</h1>
  return (
    <div>
      <h1>I am in funding details</h1>
      {user_info}
    </div>
  )
}

export default FundingDetails
