import React  from "react";
import { useParams } from "react-router-dom";
import { getSingleProjectThunk } from "../../store/projects";
import { useEffect, useState } from "react";
import { useSelector,useDispatch } from "react-redux";
import CommentComponent from "../Comments";
import { deleteCommentThunk } from "../../store/projects";
import { updateCommentThunk } from "../../store/projects";
import UpdateCommentComponent from "../UpdateCommentComponent";
import { NavLink } from "react-router-dom/cjs/react-router-dom.min";
import FundingDetails from "../FundingDetails";
import "./projectDetails.css"





const ProjectDetails = () =>{
  const dispatch = useDispatch()
  const {projectId} = useParams()
  console.log("this is the id in components",projectId)
  const [update, setUpdate] = useState(false);
  const singleProject = useSelector( state => state.project.singleProject)
   //listen for user session
   const sessionUser = useSelector(state => state.session.user);
   let userId;
   if(sessionUser) userId = sessionUser.id

  useEffect(()=>{
    dispatch(getSingleProjectThunk(projectId))
  },[dispatch, projectId])

  const handleDelete = async (commentId) => {
    await dispatch(deleteCommentThunk(commentId))
    dispatch(getSingleProjectThunk(projectId))

  }

  const handleUpdate = async () => {
   //slice of state that makes a ternery truthy to render a component
   setUpdate(true)

  }

  const moneyRaised = () =>{
    let total = 0
    for(let people of singleProject.funding){
      total += people.amount_donated
    }
    return `$${total.toLocaleString()}`
  }

  if (!singleProject){
    return null
  }
  return(
    <div className="details-main-container">
      <div className="header">
        <h1> {singleProject.project_name} </h1>
        <h5>{singleProject.description}</h5>
      </div>
      <div className="top-portion">
        <div className="img-and-info-container">
            <img className="project-image" src={singleProject.project_image} alt="" />
            <div className="category-and-location">
              <p>{singleProject.category?.type}</p>
              <p><i class="fa-solid fa-location-dot"></i>  {singleProject.city},{singleProject.state}</p>
            </div>
        </div>

        <div>
          <h2 className="amount-pledged">{singleProject.funding && moneyRaised()}</h2>
          <h5>pledged of ${singleProject.money_goal?.toLocaleString()} goal</h5>
          <h2>{singleProject.funding?.length}</h2>
          <h5>backers</h5>
          <h3>{singleProject.end_date}</h3>
          <div>{userId !== singleProject.owner?.id ? <button className="buttons"><NavLink exact to={`/projects/${projectId}/fund`}>Back This Project!</NavLink></button> : <NavLink exact to={`/projects/${projectId}/fund`}><button className="buttons">Check Out Your Supporters</button></NavLink>}</div>
        </div>
      </div>
      <div className="second-level-container">
        <div className="story-container">
          <p>{singleProject.story}</p>
        </div>
        <div className="reward-container">
          <h4>{singleProject.reward_name}</h4>
          <p>${singleProject.reward_amount} level</p>
          <p>{singleProject.reward_description}</p>
        </div>
      </div>
      {sessionUser && !singleProject.comments?.find(comment => comment.user_id === userId) ? <CommentComponent id={projectId} setUpdate={setUpdate}/>: null}
      <div>
        <ul>
          {singleProject.comments?.map(comment => {
            return (
              <div className="comment-area">
                <li key={comment.id}>{comment.comment}</li>
                {userId === comment.user_id ? <button onClick={() => handleDelete(comment.id)}>Delete</button> : null}
                {userId === comment.user_id ? <button onClick={() => handleUpdate()}>Update</button> : null}
                {userId === comment.user_id && update ? <UpdateCommentComponent commentId={comment.id} projectId={projectId} originalText={comment.comment} setUpdate={setUpdate}/> : null}
              </div>

            )
          })}
        </ul>
      </div>



    </div>
  )
}

export default ProjectDetails
