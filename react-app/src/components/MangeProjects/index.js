import React, { useState, useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { Redirect } from 'react-router-dom';

const ManageProject =() =>{
  const dispatch = useDispatch()

  const user = useSelector(state => state.session.user)

  useEffect(()=>{
    
  },[dispatch])


  if(!user ){
    return <Redirect to = "/"/>
  }
  return(
    <h1>
      I am in the manage projects
    </h1>
  )
}

export default ManageProject
