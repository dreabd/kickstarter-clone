import React, { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { Route, Switch } from "react-router-dom";
import SignupFormPage from "./components/SignupFormPage";
import LoginFormPage from "./components/LoginFormPage";
import { authenticate } from "./store/session";
import Navigation from "./components/Navigation";
import Footer from "./components/Footer";
import LandingPage from "./components/LandingPage";
import Categories from "./components/Categories";
import CreateProjectForm from "./components/ProjectForm";
import ProjectDetails from "./components/ProjectDetails";
import ManageProject from "./components/ManageProjects";
import EditProjectForm from "./components/EditProjectForm";
import DiscoverPage from "./components/Discover";
import SearchResults from "./components/SearchResults";
import DiscoverCategoriesPage from "./components/DiscoverCategoriesPage";
import FundingForm from "./components/FundingForm"
import NotFound from "./components/404Page";

function App() {
  const dispatch = useDispatch();
  const [isLoaded, setIsLoaded] = useState(false);
  useEffect(() => {
    dispatch(authenticate()).then(() => setIsLoaded(true));
  }, [dispatch]);

  return (
    <>
      <Navigation isLoaded={isLoaded} />
      {isLoaded && (
        <Switch>
          <Route path="/login" >
            <LoginFormPage />
          </Route>
          <Route path="/signup">
            <SignupFormPage />
          </Route>
          <Route exact path="/categories">
            <Categories />
          </Route>

        </Switch>
      )}
      <Switch>
        <Route exact path="/">
          <LandingPage />
        </Route>
        <Route exact path="/current">
          <ManageProject />
        </Route>
        <Route exact path="/discover">
          <DiscoverPage />
        </Route>
        <Route exact path="/discover/:category">
          <DiscoverCategoriesPage />
        </Route>
        <Route exact path="/projects/new">
          <CreateProjectForm />
        </Route>
        <Route exact path="/projects/search">
          <SearchResults />
        </Route>
        <Route exact path="/projects/:projectId">
          <ProjectDetails />
        </Route>
        <Route exact path="/projects/:projectId/edit">
          <EditProjectForm />
        </Route>
        <Route exact path="/projects/:projectId/fund">
          <FundingForm />
        </Route>
        <Route>
          <NotFound/>
        </Route>
      </Switch>
      <Footer />
    </>
  );
}

export default App;
