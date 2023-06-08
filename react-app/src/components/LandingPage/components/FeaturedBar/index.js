import React from 'react';

import ProjectCard from '../../../ProjectCard';
import './FeaturedBar.css'

const FeaturedBar = ({ projects, title }) => {
    console.log("PROJECTS", projects)

    return (
        <div className='featured-bar'>
            <h2 className='title'>{title}</h2>
            <div className='featured-projects-container'>
                {projects?.map((project) => <ProjectCard key={project.id} project={project} />)}
            </div>
        </div>
    )
}

export default FeaturedBar;
