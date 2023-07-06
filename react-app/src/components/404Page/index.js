import React, { useState, useEffect } from "react";
import { useHistory } from "react-router-dom/cjs/react-router-dom.min";
import { useDispatch, useSelector } from "react-redux";

import { getAllProjectsThunk } from "../../store/projects";

import { getRandomInt } from "../LandingPage"

import robot from "../assets/404.png"
import "./404Page.css"

function NotFound() {
    const history = useHistory()
    const dispatch = useDispatch()

    const projects = useSelector(state => state.project.allProjects)

    const projectsArray = Object.values(projects)
    const featuredProject = projectsArray[getRandomInt(projectsArray.length)]


    useEffect(() => {
        dispatch(getAllProjectsThunk())
    }, [dispatch])

    return (
        <div className="not-found-container">
            <div className="left-container">
                <p>
                    Back it up!
                </p>
                <p>
                    We can't find this page, but we can show you a new creative project you can help bring to life.
                </p>
                <div className="button-container">
                    <button onClick={() => { history.push(`/projects/${featuredProject.id}`) }}> Take a Chance</button>
                    <button onClick={() => { history.push('/') }}>Take Me Home</button>
                </div>
            </div>
            <img className="not-found-image" src={robot}></img>

        </div>
    )
}

export default NotFound