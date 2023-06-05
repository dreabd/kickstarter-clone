import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";


function CommentComponent() {

    //Initialing stuff
    const dispatch = useDispatch();

    //listen for user session
    const sessionUser = useSelector(state => state.session.user);

}

export default CommentComponent
