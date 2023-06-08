import React, { useState, useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { Redirect, useHistory } from 'react-router-dom';
import { getCurrentProjectThunk } from '../../store/projects';
import { getUserFundingThunk } from '../../store/funding';
import OpenModalButton from '../OpenModalButton';
import DeleteForm from '../DeleteForm';
import { NavLink } from 'react-router-dom';



const ManageProject = () => {
  const dispatch = useDispatch()
  const history = useHistory()

  const user = useSelector(state => state.session.user)
  const projects = useSelector(state => state.project.userProjects)
  const funded = useSelector(state => state.funding.userProjects)
  console.log(projects)

  const [deleted, setDeleted] = useState(false)

  useEffect(() => {
    dispatch(getCurrentProjectThunk())
    dispatch(getUserFundingThunk())
    setDeleted(false)
  }, [dispatch, deleted])

  const cards = Object.values(projects)?.map(project => {
    return (
      <div>
        <p>
          {project.project_name}
        </p>
        <button onClick={() => history.push(`/projects/${project.id}/edit`)} >Edit</button>
        <OpenModalButton
          buttonText={"Delete"}
          modalComponent={<DeleteForm projectId={project.id} setDeleted={setDeleted} />}
        />
      </div>
    )
  })

  console.log("funded.................................", funded)

  const funding_cards = Object.values(funded)?.map(fund => {
    return (
      <div style={{padding:"8px"}}>
        <button>
          <NavLink exact to={`/projects/${fund.project_id}`}>{fund.project_name}</NavLink>
        </button>
      </div>
    )
  })


  // console.log("I am the cards",cards)

  if (!user) {
    return <Redirect to="/" />
  }
  return (
    <div>
      <div>
        <h3>Your Projects</h3>
        {cards}
      </div>
      <div style={{display:"flex",flexDirection:"column"}}>
        <h3>Projects Your Are Backing</h3>
        {funding_cards}
      </div>
    </div>
  )
}

export default ManageProject
