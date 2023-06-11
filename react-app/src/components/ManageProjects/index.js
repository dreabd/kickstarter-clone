import React, { useState, useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { Redirect, useHistory } from 'react-router-dom';
import { getCurrentProjectThunk } from '../../store/projects';
import { getUserFundingThunk } from '../../store/funding';
import OpenModalButton from '../OpenModalButton';
import DeleteForm from '../DeleteForm';
import { NavLink } from 'react-router-dom';
import "./ManageProjects.css"



const ManageProject = () => {
  const dispatch = useDispatch()
  const history = useHistory()

  const user = useSelector(state => state.session.user)
  const projects = useSelector(state => state.project.userProjects)
  const funded = useSelector(state => state.funding.userProjects)
  // console.log(projects)

  const [deleted, setDeleted] = useState(false)

  useEffect(() => {
    dispatch(getCurrentProjectThunk())
    dispatch(getUserFundingThunk())
    setDeleted(false)
  }, [dispatch, deleted])

  const cards = Object.values(projects)?.map(project => {
    return (
      <div className='manage-cards'>
        <h4>{project.project_name}</h4>

        <NavLink exact to={`/projects/${project.id}`}>
          <img className='manage-project-img' src={project.project_image} alt="" />
        </NavLink>
        <div className='manage-button-container'>
          <button onClick={() => history.push(`/projects/${project.id}/edit`)} >Edit</button>
          <OpenModalButton
            className="project-delete-button"
            buttonText={"Delete"}
            modalComponent={<DeleteForm projectId={project.id} setDeleted={setDeleted} />}
          />
        </div>
      </div>
    )
  })

  // console.log("funded.................................", funded)

  const funding_cards = Object.values(funded)?.map(fund => {
    return (
      <div style={{ padding: "8px" }}>
        <button className='buttons'>
          <NavLink style={{ textDecoration: 'none', color: "white" }} exact to={`/projects/${fund.project_id}`}>{fund.project_name}</NavLink>
        </button>
      </div>
    )
  })


  // console.log("I am the cards",cards)

  // if (!user) {
  //   return <Redirect to="/" />
  // }
  return (
    <div>
      <h2>Your Projects: {cards.length}</h2>
      <div className='manage-your-projects'>
        {cards}
      </div>
      <div style={{ display: "flex", flexDirection: "column" }}>
        <h2>Projects You Are Backing: {funding_cards.length}</h2>
        {funding_cards.length ? funding_cards : <NavLink exact to="/discover"><button className='buttons'>Discover Projects To Back!</button></NavLink>}
      </div>
    </div>
  )
}

export default ManageProject
