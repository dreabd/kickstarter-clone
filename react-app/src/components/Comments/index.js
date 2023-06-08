import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams } from 'react-router-dom';
import { postCommentThunk } from "../../store/projects";
import { getSingleProjectThunk } from "../../store/projects";

function CommentComponent({id}) {

    //Initialing stuff
    const dispatch = useDispatch();
    // const {id} = useParams();

    //slices-o-state
    const [commentText, setCommentText] = useState('');
    const [errors, setErrors] = useState({});

    //listen for user session
    const sessionUser = useSelector(state => state.session.user);
    let userId;
    if(sessionUser) userId = sessionUser.id

    //init form for transmital
    const form = {
        comment: commentText,
        user_id: userId,
        project_id: parseInt(id)
    }

    const handleSubmit = async (e) => {
        e.preventDefault();

        //validate data here
        const newErrors = {};
        if (commentText.length < 1) newErrors['commentText'] = "Comment text is required!"

        setErrors(newErrors);

        if (!Object.keys(newErrors).length) {
            const newComment = await dispatch(postCommentThunk(form))
        }
        setCommentText('')
        await dispatch(getSingleProjectThunk(parseInt(id)))

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
                <button className='create-comment-submit-button' type='submit'>Create Comment</button>
            </form>
        </div>
    )

}

export default CommentComponent
