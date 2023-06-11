import React from "react";
import { useSelector } from "react-redux";

import ProjectCard from '../ProjectCard'
import './SearchResults.css'

const SearchResults = () => {
    const projects = useSelector(state => state.project.allProjects)
    const projectsArray = Object.values(projects);

    const cards = projectsArray?.map(project => {
        return (
            <ProjectCard project={project} />
        )
    })

    if (projectsArray.length === 0) {
        return (
            <div className="search-page">
                <div style={{ height: '550px' }}>
                    <h1>No Search Results. Try another search.</h1>
                </div>
            </div>
        )
    }

    console.log("Projects", projects)
    return (
        <div className="search-page">
            <div className="search-results-container">
                <h1>Search Results: {cards.length}</h1>
                {cards}
            </div>
        </div>
    )
}

export default SearchResults
