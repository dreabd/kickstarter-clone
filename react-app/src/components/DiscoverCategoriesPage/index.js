import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams, useHistory } from "react-router-dom/cjs/react-router-dom.min";
import { getAllProjectsByCategoryThunk } from "../../store/projects";

const DiscoverCategoriesPage = () => {

  const projects = useSelector(state => state.project.allProjects);
  const dispatch = useDispatch();
  const { category } = useParams();
  const history = useHistory()

  useEffect(() => {

    dispatch(getAllProjectsByCategoryThunk( category ))

  }, [dispatch, category]);

  const cards = Object.values(projects)?.map(project => {
    return (
      <div style={{ border: "1px solid black", padding: "1rem 1rem" }} onClick={(e) => {
        history.push(`/projects/${project.id}`)
      }}>
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

  return (
    <div>
      <h1>{category}</h1>
      {cards}
    </div>
  )

}

export default DiscoverCategoriesPage
