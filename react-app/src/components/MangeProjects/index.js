import React, { useState, useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { Redirect } from 'react-router-dom';
import { getCurrentProjectThunk } from '../../store/projects';
import OpenModalButton from '../OpenModalButton';
import DeleteForm from '../DeleteForm';



const ManageProject =() =>{
  const dispatch = useDispatch()

  // ----- Use Selectors -----
  const user = useSelector(state => state.session.user)
  const projects = useSelector(state => state.project.userProjects)

  // ----- State Variables ------
  const [deleted,setDeleted] = useState(false)
  console.log("deleted state variable in the manage projects component",deleted)

  useEffect(()=>{
    dispatch(getCurrentProjectThunk())
    setDeleted(false)
  },[dispatch,deleted])

  const cards = Object.values(projects)?.map(project =>{
    return(
      <div>
        <p>
          {project.project_name}
        </p>
        <OpenModalButton
          buttonText={"Delete"}
          modalComponent={<DeleteForm setDeleted={setDeleted} projectId={project.id}/>}
        />
      </div>
    )
  })


  // console.log("I am the cards",cards)

  if(!user ){
    return <Redirect to = "/"/>
  }
  return(
    <div>
      <h1>
        I am in the manage projects
      </h1>
      {cards}
    </div>
  )
}

export default ManageProject
