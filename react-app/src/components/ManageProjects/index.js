import React, { useState, useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { Redirect, useHistory } from 'react-router-dom';
import { getCurrentProjectThunk } from '../../store/projects';
import OpenModalButton from '../OpenModalButton';
import DeleteForm from '../DeleteForm';



const ManageProject = () => {
  const dispatch = useDispatch()
  const history = useHistory()

  const user = useSelector(state => state.session.user)
  const projects = useSelector(state => state.project.userProjects)

  console.log(projects)

  useEffect(() => {
    dispatch(getCurrentProjectThunk())
  }, [dispatch])

  const cards = Object.values(projects)?.map(project => {
    return (
      <div>
        <p>
          {project.project_name}
        </p>
        <h1>In the cards map function</h1>
        <button onClick={() => history.push(`/projects/${project.id}/edit`)} >Edit</button>
        <OpenModalButton
          buttonText={"Delete"}
          modalComponent={<DeleteForm />}
        />
      </div>
    )
  })


  // console.log("I am the cards",cards)

  if (!user) {
    return <Redirect to="/" />
  }
  return (
    <div>
      <h1>
        I am in the manage projects
      </h1>
      {cards}
    </div>
  )
}

export default ManageProject
