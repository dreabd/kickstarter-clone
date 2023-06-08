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
    const totalFunding = Object.values(project.funding).reduce((total, fundingItem) => {
      total += fundingItem.amount_donated
      return total
    }, 0)

    const percentFunded = Math.floor((totalFunding / project.money_goal * 100))
    return (
      <div className="project-card" onClick={(e) => {
        history.push(`/projects/${project.id}`)
      }}>
        <div className="project-card-img-container">
        <img src={project.project_image} alt="" className="project-card-img"/>
        </div>
        <div className="project-card-bottom">
          <h3>
            {project.project_name}
          </h3>
          <p> {project.description}</p>
          <p>{percentFunded}% funded</p>
          <p>
            By {project.owner.first_name} {project.owner.last_name}
          </p>
        </div>
      </div>
    )
  })

  console.log(projects)
  return (
    <div>
      <h1 className="header">{category}</h1>
      <div className="project-card-gallery-container">
        <div className="project-card-gallery">
          {cards}
        </div>
      </div>
    </div>
  )

}

export default DiscoverCategoriesPage
