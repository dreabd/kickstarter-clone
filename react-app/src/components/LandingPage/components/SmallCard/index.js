import React from 'react'
import './SmallCard.css'

const SmallCard = ({ project }) => {
    if (!project) return <p>Loading...</p>

    const totalFunding = Object.values(project.funding).reduce((total, fundingItem) => {
        total += fundingItem.amount_donated
        return total
    }, 0)
    const percentFunded = Math.floor((totalFunding / project.money_goal * 100))
    
    return (
        <div className='small-card-container'>
            <img src={project.project_image} className='small-card-image' />
            <div className='small-card-info-container'>
                <h3 className='small-card-title'>{project.project_name}</h3>
                <p className="funded">{percentFunded}% funded</p>
                <p className='owner'>By {project.owner.first_name} {project.owner.last_name}</p>
            </div>
        </div>
    )
}

export default SmallCard
