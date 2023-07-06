import React from "react";
import { useParams, useHistory } from "react-router-dom";
import { getSingleProjectThunk } from "../../store/projects";
import { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import CommentComponent from "../Comments";
import { deleteCommentThunk } from "../../store/projects";
import UpdateCommentComponent from "../UpdateCommentComponent";
import { NavLink } from "react-router-dom/cjs/react-router-dom.min";
import "./projectDetails.css"
import NotFound from "../404Page";
import LoadingGIF from './green_loading.gif'

const ProjectDetails = () => {
  const dispatch = useDispatch()
  const history = useHistory()
  const { projectId } = useParams()
  console.log("this is the id in components", projectId)
  const [update, setUpdate] = useState(false);
  const [isLoading, setIsLoading] = useState(true);
  const singleProject = useSelector(state => state.project.singleProject)
  //listen for user session
  const sessionUser = useSelector(state => state.session.user);
  let userId;
  if (sessionUser) userId = sessionUser.id

  useEffect(() => {
    async function fetchSingleProject() {
      await dispatch(getSingleProjectThunk(projectId))
      setIsLoading(false)
    }

    fetchSingleProject()
  }, [dispatch, projectId])


  const handleDelete = async (commentId) => {
    await dispatch(deleteCommentThunk(commentId))
    dispatch(getSingleProjectThunk(projectId))

  }

  const handleUpdate = async () => {
    //slice of state that makes a ternery truthy to render a component
    setUpdate(true)

  }

  const moneyRaised = () => {
    let total = 0
    for (let people of singleProject.funding) {
      total += people.amount_donated
    }
    return `$${total.toLocaleString()}`
  }

  if (!Object.values(singleProject).length) {
    return <NotFound/>
  }

  // if (!singleProject) {
  //   return null
  // }

  if (Object.keys(singleProject).length === 0 || isLoading) {
    return (
      < div className="loading-screen" >
        <img src={LoadingGIF} alt="loading" />
      </div >
    )
  }


  return (
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
            <p className="city-state"><i class="fa-solid fa-location-dot"></i>  {singleProject.city}, {singleProject.state}</p>
            <p>By {singleProject.owner?.first_name} {singleProject.owner?.last_name}</p>
          </div>
        </div>

        <div>
          <h2 className="amount-pledged">{singleProject.funding && moneyRaised()}</h2>
          <h5 className="bottom-labels">pledged of ${singleProject.money_goal?.toLocaleString()} goal</h5>
          <h2>{singleProject.funding?.length}</h2>
          <h5 className="bottom-labels">backers</h5>
          <h3 className="amount-pledged">{singleProject.days_left}</h3>
          <h5 className="bottom-labels-days">days to go</h5>
          {userId ? <div>{userId !== singleProject.owner?.id ? <button className="buttons" onClick={() => history.push(`/projects/${projectId}/fund`)}><NavLink className="buttons" exact to={`/projects/${projectId}/fund`}>Back This Project!</NavLink></button> : <NavLink exact to={`/projects/${projectId}/fund`}><button className="buttons">Check Out Your Supporters</button></NavLink>}</div> : <p style={{ color: "#009e74" }}>Login to Back This Project!!</p>}
        </div>
      </div>
      <div className="second-level-container">
        <div className="story-container">
          <p>{singleProject.story}</p>
        </div>
        <div className="reward-container">
          <h2>Reward Option: </h2>
          <h4>{singleProject.reward_name}</h4>
          <p>${singleProject.reward_amount} level</p>
          <p>{singleProject.reward_description}</p>
        </div>
      </div>
      <h2>Comments</h2>
      {sessionUser && !singleProject.comments?.find(comment => comment.user_id === userId) ? <CommentComponent id={projectId} setUpdate={setUpdate} /> : !sessionUser ? <p>Please login to post a comment</p> : null}
      <div>
        <ul>
          {singleProject.comments?.map(comment => {
            return (
              <div className="comment-area">
                <span className="username-says">{comment.user.first_name} says...</span>
                <li key={comment.id} className="individual-comment"> {comment.comment}</li>
                {userId === comment.user_id ? <button onClick={() => handleDelete(comment.id)} className="update-delete-buttons">Delete</button> : null}
                {userId === comment.user_id ? <button onClick={() => handleUpdate()} className="update-delete-buttons">Update</button> : null}
                {userId === comment.user_id && update ? <UpdateCommentComponent commentId={comment.id} projectId={projectId} originalText={comment.comment} setUpdate={setUpdate} /> : null}
              </div>

            )
          })}
        </ul>
      </div>



    </div>
  )
}

export default ProjectDetails
