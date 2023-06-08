import React from "react";
import {useSelector} from "react-redux";
import { useHistory } from "react-router-dom";

const SearchResults = () => {
    const projects = useSelector(state => state.project.allProjects)
    const history = useHistory()
    const cards = Object.values(projects)?.map(project => {
        return (
            <div onClick={(e) => {
                history.push(`/projects/${project.id}`)
            }}
            style={{ border: "1px solid black", padding: "1rem 1rem" }}>
                <h3>
                    {project.project_name}
                </h3>
                <p>
                    {project.owner.first_name} {project.owner.last_name}
                </p>
                <img src={project.project_image} alt="" />
                <p> {project.category.type}</p>
            </div>
        )
    })

    console.log(projects)
    return (
        <div>
            <h1>Search Results: </h1>
            {cards}
        </div>
    )
}

export default SearchResults
