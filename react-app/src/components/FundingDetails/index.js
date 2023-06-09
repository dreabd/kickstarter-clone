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
        <div className="funding-details-card">
          <h4>{funding.user.first_name} {funding.user.last_name}</h4>
          <p>{funding.user.email}</p>
          <p>Donated: ${funding.amount_donated}</p>
          <p>{funding.reward ? "Opted in for a reward" : "Opted Out for a reward"}</p>
        </div>
      )
    })

  if (!fundings) return <h1> Loading...</h1>
  return (
    <div>
      <h1 className="title-funding-details">Check out you Backers:</h1>
      <div className="funding-details-container">
        {user_info}
      </div>
    </div>
  )
}

export default FundingDetails
