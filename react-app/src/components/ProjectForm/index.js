import React, { useState, useEffect } from "react";
import { useHistory } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { postNewProjectThunk } from "../../store/projects";
import { getCategoriesThunk } from "../../store/categoryReducer";
import OpenModalButton from "../OpenModalButton";
import LoginFormModal from "../LoginFormModal";
import SignupFormModal from "../SignupFormModal";
import "./ProjectFormStyles.css";

//this is used to convert the backend errors into a format that the frontend can use
const caseHelper = (backendstring) => {
  const backendToFrontend = {
    project_name: "projectName",
    description: "description",
    category_id: "category",
    money_goal: "moneyGoal",
    city: "city",
    state: "state",
    story: "story",
    project_image: "projectImage",
    end_date: "endDate",
    reward_name: "rewardName",
    reward_amount: "rewardAmount",
    reward_description: "rewardDescription",
  };
  return backendToFrontend[backendstring];
};

function CreateProjectForm() {
  //set up a bunch of state slices
  const [projectName, setProjectName] = useState("");
  const [description, setDescription] = useState("");
  const [category, setCategory] = useState("");
  const [moneyGoal, setMoneyGoal] = useState(0);
  const [city, setCity] = useState("");
  const [state, setState] = useState("");
  const [story, setStory] = useState("");
  const [projectImage, setProjectImage] = useState("");
  const [endDate, setEndDate] = useState("2024-01-01");
  const [rewardName, setRewardName] = useState("");
  const [rewardAmount, setRewardAmount] = useState(0);
  const [rewardDescription, setRewardDescription] = useState("");
  const [errors, setErrors] = useState({});

  //Intialize things
  const history = useHistory();
  const dispatch = useDispatch();

  //useSelectors
  const categories = useSelector((state) => state.category.categories);
  const loggedIn = useSelector((state) => state.session.user);
  useEffect(() => {
    // Fetch category data
    dispatch(getCategoriesThunk());
  }, [dispatch]);

  const handleSubmit = async (e) => {
    e.preventDefault();

    const newErrors = {};
    // validate data on the frontend here
    if (projectName.length < 1)
      newErrors["projectName"] = "Project name is required!";
    if (description.length < 1)
      newErrors["description"] = "Description is required!";
    if (category === "Select") newErrors["category"] = "Category is required!";
    if (moneyGoal < 1) newErrors["moneyGoal"] = "Financial Goal is required!";
    if (city.length < 1) newErrors["city"] = "City is required!";
    if (state.length < 1) newErrors["state"] = "State is required!";
    if (story.length < 1) newErrors["story"] = "Story is required!";
    if (endDate === "YYYY-MM-DD")
      newErrors["endDate"] = "Project End Date is required!";

    setErrors(newErrors);

    // If we have errors, bail out
    if (Object.keys(newErrors).length) return;

    // Build up our form data
    const formData = new FormData();
    formData.append("project_name", projectName);
    formData.append("description", description);
    formData.append("category_id", category);
    formData.append("money_goal", moneyGoal);
    formData.append("city", city);
    formData.append("state", state);
    formData.append("story", story);
    formData.append("project_image", projectImage);
    formData.append("end_date", endDate);
    formData.append("reward_name", rewardName);
    formData.append("reward_amount", rewardAmount);
    formData.append("reward_description", rewardDescription);

    // Log our form data
    console.log("Form Data gathered from form:");
    for (let key of formData.entries()) {
      console.log(key[0] + " ----> " + key[1]);
    }

    // Post project to the backend
    const newProjectOrErrors = await dispatch(postNewProjectThunk(formData));

    // Handle backend validation errors
    if ("errors" in newProjectOrErrors) {
      // handle errors from the backend which comes in as an object with a key of errors
      console.error(
        "The backend returned validation errors when creating a new form",
        newProjectOrErrors
      );
      const formErrors = newProjectOrErrors.errors.errors;
      let errorObj = {};

      Object.keys(formErrors).forEach((errorKey) => {
        const frontEndErrorKey = caseHelper(errorKey);
        const frontEndErrorString = formErrors[errorKey][0];
        errorObj[frontEndErrorKey] = frontEndErrorString;
      });
      setErrors(errorObj);
    } else {
      if (newProjectOrErrors) {
        console.log("Project successfully created! ");
        setProjectName("");
        setDescription("");
        setCategory("");
        setMoneyGoal(0);
        setCity("");
        setState("");
        setStory("");
        setProjectImage("");
        setEndDate("YYYY-MM-DD");
        setRewardName("");
        setRewardAmount(0);
        setRewardDescription("");

        history.push(`/projects/${newProjectOrErrors.id}`);
      } else {
        console.error(
          "The postNewProjectThunk returned undefined when creating this project"
        );
      }
    }
  };

  if (!loggedIn) {
    return (
      <div className="logged-out-project-form">
        <h2>Please login or signup with Jumpstarter to create a project!</h2>
        <div>
          <OpenModalButton
            buttonText="Log In"
            modalComponent={<LoginFormModal />}
          />

          <OpenModalButton
            buttonText="Sign Up"
            modalComponent={<SignupFormModal />}
          />
        </div>
      </div>
    );
  }

  return (
    <div>
      <form
        className="signupForm"
        onSubmit={handleSubmit}
        encType="multipart/form-data"
      >
        <h1>Create your new project!</h1>
        <label>
          Project Name <span className="errors">{errors.projectName}</span>
          <input
            type="text"
            value={projectName}
            placeholder="Project Name"
            onChange={(e) => setProjectName(e.target.value)}
          />
        </label>
        <label>
          Project Description{" "}
          <span className="errors">{errors.description}</span>
          <input
            type="text"
            value={description}
            placeholder="Project Description"
            onChange={(e) => setDescription(e.target.value)}
          />
        </label>
        <label>
          Category <span className="errors">{errors.category}</span>
          <select
            value={category}
            onChange={(e) => setCategory(e.target.value)}
          >
            <option default>Select a Category</option>
            {categories &&
              Object.values(categories).map((category) => (
                <option key={category.id} value={category.id}>
                  {category.type}
                </option>
              ))}
          </select>
        </label>
        <label>
          Financial Goal <span className="errors">{errors.moneyGoal}</span>
          <div className="dollar-sign-div">
            <span className="just-the-dollar-sign">$</span>
            <input
              type="number"
              value={moneyGoal}
              placeholder="0"
              onChange={(e) => setMoneyGoal(e.target.value)}
              className="dollar-input"
            />
          </div>
        </label>
        <label>
          City <span className="errors">{errors.city}</span>
          <input
            type="text"
            value={city}
            placeholder="city"
            onChange={(e) => setCity(e.target.value)}
          />
        </label>
        <label>
          State <span className="errors">{errors.state}</span>
          {/* <input
            type="text"
            value={state}
            placeholder="State"
            onChange={(e) => setState(e.target.value)}
          /> */}
          <select value={state} onChange={(e) => setState(e.target.value)}>
            <option default>Select a State</option>
            <option value="AL">Alabama (AL)</option>
            <option value="AK">Alaska (AK)</option>
            <option value="AZ">Arizona (AZ)</option>
            <option value="AR">Arkansas (AR)</option>
            <option value="CA">California (CA)</option>
            <option value="CO">Colorado (CO)</option>
            <option value="CT">Connecticut (CT)</option>
            <option value="DE">Delaware (DE)</option>
            <option value="DC">District Of Columbia (DC)</option>
            <option value="FL">Florida (FL)</option>
            <option value="GA">Georgia (GA)</option>
            <option value="HI">Hawaii (HI)</option>
            <option value="ID">Idaho (ID)</option>
            <option value="IL">Illinois (IL)</option>
            <option value="IN">Indiana (IN)</option>
            <option value="IA">Iowa (IA)</option>
            <option value="KS">Kansas (KS)</option>
            <option value="KY">Kentucky (KY)</option>
            <option value="LA">Louisiana (LA)</option>
            <option value="ME">Maine (ME)</option>
            <option value="MD">Maryland (MD)</option>
            <option value="MA">Massachusetts (MA)</option>
            <option value="MI">Michigan (MI)</option>
            <option value="MN">Minnesota (MN)</option>
            <option value="MS">Mississippi (MS)</option>
            <option value="MO">Missouri (MO)</option>
            <option value="MT">Montana (MT)</option>
            <option value="NE">Nebraska (NE)</option>
            <option value="NV">Nevada (NV)</option>
            <option value="NH">New Hampshire (NH)</option>
            <option value="NJ">New Jersey (NJ)</option>
            <option value="NM">New Mexico (NM)</option>
            <option value="NY">New York (NY)</option>
            <option value="NC">North Carolina (NC)</option>
            <option value="ND">North Dakota (ND)</option>
            <option value="OH">Ohio (OH)</option>
            <option value="OK">Oklahoma (OK)</option>
            <option value="OR">Oregon (OR)</option>
            <option value="PA">Pennsylvania (PA)</option>
            <option value="RI">Rhode Island (RI)</option>
            <option value="SC">South Carolina (SC)</option>
            <option value="SD">South Dakota (SD)</option>
            <option value="TN">Tennessee (TN)</option>
            <option value="TX">Texas (TX)</option>
            <option value="UT">Utah (UT)</option>
            <option value="VT">Vermont</option>
            <option value="VA">Virginia</option>
            <option value="WA">Washington</option>
            <option value="WV">West Virginia</option>
            <option value="WI">Wisconsin</option>
            <option value="WY">Wyoming</option>
          </select>
        </label>
        <label>
          Project Story <span className="errors">{errors.story}</span>
          <textarea
            type="text"
            value={story}
            placeholder="Tell people all about your project..."
            onChange={(e) => setStory(e.target.value)}
            rows="7"
            cols="50"
          ></textarea>
        </label>
        <label>
          Project Image <span className="errors">{errors.projectImage}</span>
          <input
            type="file"
            accept="image/*"
            // value={projectImage}
            placeholder="Project Image"
            onChange={(e) => {
              console.log("e.target.files????", e.target.files);
              setProjectImage(e.target.files[0]);
            }}
          />
        </label>
        <label>
          End Date <span className="errors">{errors.endDate}</span>
          <input
            type="date"
            value={endDate}
            placeholder="End Date"
            onChange={(e) => setEndDate(e.target.value)}
            className="end-date"
          />
        </label>
        <label>
          Reward Name<span className="errors">{errors.rewardName}</span>
          <input
            type="text"
            value={rewardName}
            placeholder="Reward Name"
            onChange={(e) => setRewardName(e.target.value)}
          />
        </label>
        <label>
          Reward Amount<span className="errors">{errors.rewardAmount}</span>
          <div className="dollar-sign-div">
            <span className="just-the-dollar-sign">$</span>
            <input
              type="number"
              value={rewardAmount}
              placeholder="0"
              onChange={(e) => setRewardAmount(e.target.value)}
              className="dollar-input"
            />
          </div>
        </label>
        <label>
          Reward Description{" "}
          <span className="errors">{errors.rewardDescription}</span>
          <textarea
            type="text"
            value={rewardDescription}
            placeholder="Tell people about your reward..."
            onChange={(e) => setRewardDescription(e.target.value)}
            rows="5"
            cols="50"
          ></textarea>
        </label>
        <div className="signup-button-container">
          <button className="signup-button" type="submit">
            Create Project
          </button>
        </div>
      </form>
    </div>
  );
}

export default CreateProjectForm;
