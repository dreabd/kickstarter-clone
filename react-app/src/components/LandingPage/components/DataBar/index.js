import React from "react";
import './DataBar.css';

const DataBar = ({ projects }) => {
    const projectsFunded = Object.keys(projects).length
    const projectValues = Object.values(projects)
    const totalFunding = projectValues.reduce(
        (acc, project) => {
            const projectTotal = Object.values(project.funding).reduce((total, fundingItem) => {
                total += fundingItem.amount_donated
                return total
            }, 0)
            acc += projectTotal
            return acc
        }, 0
    )

    const totalPledges = projectValues.reduce(
        (acc, project) => {
            acc += Object.keys(project.funding).length
            return acc
        }, 0
    )

    return (
        <>
            <div className="label-container">
                <h3>ON JUMPSTARTER: </h3>
            </div>
            <div className="databar-container">
                <div className="databar">
                    <div className="databar-item">
                        <span>{projectsFunded}</span>
                        <p>projects funded</p>
                    </div>
                    <div className="databar-item">
                        <span>${totalFunding.toLocaleString()}</span>
                        <p>towards creative work</p>
                    </div>
                    <div className="databar-item">
                        <span>{totalPledges.toLocaleString()}</span>
                        <p>pledges</p>
                    </div>
                </div>
            </div>

        </>
    )
}

export default DataBar
