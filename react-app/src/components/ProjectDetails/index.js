import React  from "react";
import { useParams } from "react-router-dom";
import { getSingleProjectThunk } from "../../store/projects";
import { useEffect } from "react";
import { useSelector,useDispatch } from "react-redux";



const ProjectDetails = () =>{
  const dispatch = useDispatch()
  const {projectId} = useParams()
  console.log("this is the id in components",projectId)

  const singleProject = useSelector( state => state.project.singleProject)

  useEffect(()=>{
    dispatch(getSingleProjectThunk(projectId))
  },[dispatch])

  if (!singleProject){
    return null
  }

  return(
    <div>
      <h1> {singleProject.project_name} </h1>
      <h5>{singleProject.description}</h5>
      <img src={singleProject.project_image} alt="" />
      <div>
        <p>{singleProject.category?.type}</p>
        <p>{singleProject.city},{singleProject.state}</p>
      </div>

      <div>
        {/* Place holder for backing amount */}
        <h3>${singleProject.money_goal?.toLocaleString()}</h3>
        <h3>This Project will only be funded if it reaches its goal by {singleProject.end_date}</h3>
        <button> Back This Project!</button>
      </div>

      <div>
        <p>{singleProject.story}</p>
      </div>

      <div>
        <h4>{singleProject.reward_name}</h4>
        <p>{singleProject.reward_amount}</p>
        <p>{singleProject.reward_description}</p>
      </div>


    </div>
  )
}

export default ProjectDetails
