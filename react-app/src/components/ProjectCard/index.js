import React from "react";
import { useHistory } from "react-router-dom";
import './ProjectCard.css'

const ProjectCard = ({ project }) => {
    const history = useHistory()
    if (!project) return <p>Loading...</p>
    return (
        <div className="card" onClick={(e) => {
            history.push(`/projects/${project.id}`)
        }}>
            <div className="card-img-container">
                <img src={project.project_image} alt="" className="card-img" />
            </div>
            <div className="card-bottom">
                <h3>
                    {project.project_name}
                </h3>
                <p> {project.description}</p>
                <p>
                    {project.owner.first_name} {project.owner.last_name}
                </p>
            </div>
        </div>
    )
}

export default ProjectCard
