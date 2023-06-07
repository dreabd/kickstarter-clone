import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory } from 'react-router-dom';
import { getSingleProjectThunk, updateCommentThunk } from "../../store/projects";

//<UpdateCommentComponent commentId={comment.id} projectId={projectId} commentText={comment.comment}/>

function UpdateCommentComponent({commentId, projectId, originalText, setUpdate}) {

    //Initialing stuff
    const dispatch = useDispatch();


    //slices-o-state
    const [commentText, setCommentText] = useState(originalText);
    const [errors, setErrors] = useState({});

    //listen for user session
     const sessionUser = useSelector(state => state.session.user);
     let userId;
     if(sessionUser) userId = sessionUser.id

    // //init form for transmital
     const form = {
        comment: commentText,
        user_id: userId,
        project_id: projectId
     }

    const handleSubmit = async (e) => {
        e.preventDefault();

        //validate data here
        const newErrors = {};
        if (commentText.length < 1) newErrors['commentText'] = "Comment text is required!"

        setErrors(newErrors);
        if (!Object.keys(newErrors).length) {
            const newComment = await dispatch(updateCommentThunk(form, commentId))
            await dispatch(getSingleProjectThunk(projectId))
        }
        setCommentText('')
        setUpdate(false)
    }

    return (
        <div>
            <form className='project-form' onSubmit={handleSubmit}>
                    <textarea
                        type='text'
                        value={commentText}
                        placeholder='Leave your comment here...'
                        onChange={(e) => setCommentText(e.target.value)}>
                    </textarea>
                <button className='create-comment-submit-button' type='submit'>Update Comment</button>
            </form>
        </div>
    )

}

export default UpdateCommentComponent
