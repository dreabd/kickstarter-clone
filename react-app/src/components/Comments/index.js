import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams } from 'react-router-dom';
// import { postCommentThunk } from "../../store/projects";

function CommentComponent() {

    //Initialing stuff
    const dispatch = useDispatch();
    const {id} = useParams();

    //slices-o-state
    const [commentText, setCommentText] = useState('');
    const [errors, setErrors] = useState({});

    //listen for user session
    const sessionUser = useSelector(state => state.session.user);
    const userId = sessionUser.id

    //init form for transmital
    const form = {
        comment: commentText,
        user_id: userId,
        project_id: id
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
