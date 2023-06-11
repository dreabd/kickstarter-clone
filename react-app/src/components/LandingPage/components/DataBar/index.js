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
                        <span className="databar-numerals">{projectsFunded}</span>
                        <p className="databar-text">projects funded</p>
                    </div>
                    <div className="databar-item">
                        <span className="databar-numerals">${totalFunding.toLocaleString()}</span>
                        <p className="databar-text">towards creative work</p>
                    </div>
                    <div className="databar-item">
                        <span className="databar-numerals">{totalPledges.toLocaleString()}</span>
                        <p className="databar-text">pledges</p>
                    </div>
                </div>
            </div>

        </>
    )
}

export default DataBar
