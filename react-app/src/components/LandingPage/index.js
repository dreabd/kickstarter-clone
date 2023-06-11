import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getAllProjectsThunk } from "../../store/projects";
import DataBar from "./components/DataBar";
import ProjectCard from "../ProjectCard";
import SmallCard from "./components/SmallCard";
import FeaturedBar from "./components/FeaturedBar";
import './LandingPage.css';

function getRandomInt(max) {
  return Math.floor(Math.random() * max);
}

const LandingPage = () => {
  const projects = useSelector(state => state.project.allProjects)
  const projectsArray = Object.values(projects)
  const dispatch = useDispatch()
  const featuredProject = projectsArray[getRandomInt(projectsArray.length)]
  const artProjects = projectsArray.filter(project => project.category.type === "Arts")
  const featuredArtProjects = [artProjects[getRandomInt(artProjects.length)], artProjects[getRandomInt(artProjects.length)], artProjects[getRandomInt(artProjects.length)]]
  // Top 5 projects with most # of funders
  const trendingProjects = projectsArray.toSorted((projectA, projectB) => {
    return projectB.funding.length - projectA.funding.length
  }).slice(0, 5)
  const lastChanceProjects = projectsArray.toSorted((projectA, projectB) => {
    return Math.abs(Date.now() - new Date(projectA.end_date)) - Math.abs(Date.now() - new Date(projectB.end_date));
  }).slice(0, 5)

  useEffect(() => {
    dispatch(getAllProjectsThunk())
  }, [dispatch])

  const feelingArtsyCards = featuredArtProjects?.map(project => {
    return (
      <SmallCard key={project?.id} project={project} />
    )
  })

  console.log(projects)
  if (!projects) return <h1>Projects loading...</h1>
  return (
    <div>
      <div className="landing-title-container">
        <h2 >Bring a creative project to life. </h2>
      </div>
      <DataBar projects={projects} />
      <div className="featured-project-container">
        <div className="featured-box">
          <p className="title">FEATURED PROJECT</p>
          <ProjectCard project={featuredProject} />
        </div>
        <div className="feeling-artsy">
          <p className="title artsy-title">FEELING ARTSY? </p>
          {feelingArtsyCards}
        </div>
      </div>
      <hr />
      <FeaturedBar projects={trendingProjects} title={'Trending'} />
      <hr />
      <FeaturedBar projects={lastChanceProjects} title={'Last Chance'} />
    </div>
  )
}

export default LandingPage
