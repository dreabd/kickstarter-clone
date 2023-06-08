import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getAllProjectsThunk } from "../../store/projects";
import "./discoverPage.css"

const DiscoverPage = () => {
  const projects = useSelector(state => state.project.allProjects)
  const dispatch = useDispatch()

  useEffect(() => {
    dispatch(getAllProjectsThunk())
  }, [dispatch])

  const cards = Object.values(projects)?.map(project => {
    return (
      <div className="project-card">
        <div className="project-card-img-container">
        <img src={project.project_image} alt="" className="project-card-img"/>
        </div>
        <div className="project-card-bottom">
          <h3>
            {project.project_name}
          </h3>
          <p> {project.description}</p>
          <p>95% funded</p>
          <p>
            {project.owner.first_name} {project.owner.last_name}
          </p>
        </div>
      </div>
    )
  })

  console.log(projects)
  return (
    <div>
      <h1 className="header">Discover</h1>
      <div className="project-card-gallery-container">
        <div className="project-card-gallery">
          {cards}
        </div>
      </div>
    </div>
  )
}

export default DiscoverPage
