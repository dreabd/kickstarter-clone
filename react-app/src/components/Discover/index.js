import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getAllProjectsThunk } from "../../store/projects";

const DiscoverPage = () => {
  const projects = useSelector(state => state.project.allProjects)
  const dispatch = useDispatch()

  useEffect(() => {
    dispatch(getAllProjectsThunk())
  }, [dispatch])

  const cards = Object.values(projects)?.map(project => {
    return (
      <div style={{ border: "1px solid black", padding: "1rem 1rem" }}>
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
      <h1>I am a discover page</h1>
      {cards}
    </div>
  )
}

export default DiscoverPage
