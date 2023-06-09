import React, { useState } from "react";
import { login } from "../../store/session";
import { useDispatch, } from "react-redux";
import { useModal } from "../../context/Modal";
import * as sessionActions from "../../store/session";
import { useHistory } from "react-router-dom/cjs/react-router-dom.min";
import "./LoginForm.css";


function LoginFormModal() {
  const dispatch = useDispatch();
  const history = useHistory()
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errors, setErrors] = useState([]);
  const { closeModal } = useModal();

  const handleSubmit = async (e) => {
    e.preventDefault();
    const data = await dispatch(login(email, password));
    if (data) {
      setErrors(data);
    } else {
      history.push("/")

      closeModal()
    }
  };

  const handleClickDemoUser = async (e) => {
    e.preventDefault();
    const data = await dispatch(sessionActions.login('frankly@email.io', "password"));
    if (data) {
      setErrors(data);
    } else {
      history.push("/")
      closeModal()
    }
  }

  return (
    <div className="form-container">
      <h1 className="login-header">Login</h1>
      <form className="loginForm" onSubmit={handleSubmit}>
        <ul className="login-error-container">
          {errors?.map((error, idx) => (
            <li className="login-error-item" key={idx}>{error}</li>
          ))}
        </ul>
        <label>
          Email
          <input
            type="text"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </label>
        <label>
          Password
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </label>
        <div className='login-button-container'>
          <button className="login-button" type="submit">Log In</button>
          <button className="demo-user-button" href="#" onClick={handleClickDemoUser}>Log in as Demo User</button>
        </div>
      </form>
    </div>
  );
}

export default LoginFormModal;
