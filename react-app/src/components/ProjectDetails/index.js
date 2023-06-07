import React  from "react";
import { useParams } from "react-router-dom";
import { getSingleProjectThunk } from "../../store/projects";
import { useEffect, useState } from "react";
import { useSelector,useDispatch } from "react-redux";
import CommentComponent from "../Comments";
import { deleteCommentThunk } from "../../store/projects";
import { updateCommentThunk } from "../../store/projects";
import UpdateCommentComponent from "../UpdateCommentComponent";



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
      {!singleProject.comments?.find(comment => comment.user_id === userId) ? <CommentComponent id={projectId}/>: null}
      <div>
        <ul>
          {singleProject.comments?.map(comment => {
            return (
              <div>
                <li key={comment.id}>{comment.comment}</li>
                {userId === comment.user_id ? <button onClick={() => handleDelete(comment.id)}>Delete</button> : null}
                {userId === comment.user_id ? <button onClick={() => handleUpdate()}>Update</button> : null}
                {userId === comment.user_id && update ? <UpdateCommentComponent commentId={comment.id} projectId={projectId} originalText={comment.comment} setUpdate={setUpdate}/> : null}
              </div>

            )
          })}
        </ul>
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
