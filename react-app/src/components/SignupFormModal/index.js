import React, { useEffect, useState } from "react";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import { signUp } from "../../store/session";
import "./SignupForm.css";
import { useHistory } from "react-router-dom/cjs/react-router-dom.min";

function SignupFormModal() {
	const dispatch = useDispatch();
	const history = useHistory()
	const [email, setEmail] = useState("");
	const [username, setUsername] = useState("");
	const [firstName, setFirstName] = useState("")
	const [lastName, setLastName] = useState("")
	const [city, setCity] = useState("")
	const [state, setState] = useState("")
	const [bio, setBio] = useState("")
	const [password, setPassword] = useState("");
	const [confirmPassword, setConfirmPassword] = useState("");
	const [errors, setErrors] = useState({});
	const [submited, setSubmitted] = useState(false)
	const { closeModal } = useModal();

	// useEffect(() => {
	// 	const errors = {}

	// 	if (username.length < 4) errors["username"] = "Please make sure your username is more than 4 characters."
	// 	if (!username.length) errors["username"] = "Please type a valid username."
	// 	if (!firstName.length) errors["firstName"] = "Please type a valid first name."
	// 	if (!lastName.length) errors["lastName"] = "Please type a valid last name."
	// 	if (!city.length) errors["city"] = "Please type a valid city."
	// 	if (state.length !== 2) errors["state"] = "Please use your state's two character abbreviation."
	// 	if (!bio.length) errors["bio"] = "Please include a personal biography that is at least 50 characters."
	// 	if (bio.length < 50) errors["bio"] = "Please type at least 50 characters for your bio."
	// 	if (!email.includes('@') || !email.includes('.')) errors["email"] = "Please include a valid email."

	// 	setErrors(errors)
	// }, [email, username, firstName, lastName, city, state, bio, password,])

	const handleSubmit = async (e) => {
		e.preventDefault();
		const errors = {}

		if (username.length < 4) errors["username"] = "Please make sure your username is more than 4 characters."
		if (!username.length) errors["username"] = "Please type a valid username."
		if (!firstName.length) errors["firstName"] = "Please type a valid first name."
		if (!lastName.length) errors["lastName"] = "Please type a valid last name."
		if (!city.length) errors["city"] = "Please type a valid city."
		if (state.length !== 2) errors["state"] = "Please use your state's two character abbreviation."
		if (!bio.length) errors["bio"] = "Please include a personal biography that is at least 50 characters."
		if (bio.length < 50) errors["bio"] = "Please type at least 50 characters for your bio."
		if (!email.includes('@') || !email.includes('.')) errors["email"] = "Please include a valid email."

		setErrors(errors)

		setSubmitted(true)

		if (Object.values(errors).length) return

		if (password === confirmPassword) {

			const formData = new FormData()

			formData.append("email", email)
			formData.append("username", username)
			formData.append("first_name", firstName)
			formData.append("last_name", lastName)
			formData.append("city", city)
			formData.append("state", state)
			formData.append("bio", bio)
			formData.append("hashed_password", password)

			console.log("Form Data gathered from form:")
			for (let key of formData.entries()) {
				console.log(key[0] + ' ----> ' + key[1])
			}

			const data = await dispatch(signUp(formData));
			if (data) {
				setErrors(data);
			} else {
				history.push("/")
				closeModal();
			}
		} else {
			errors['password'] = "Confirm Password field must be the same as the Password field"
			setErrors(errors)
			// setErrors([
			// 	"Confirm Password field must be the same as the Password field",
			// ]);
		}
	};

	return (
		<>
			<form className="signupForm" onSubmit={handleSubmit}>
				<h2>Sign Up</h2>
				{/* <ul className="errors">
					{submited && Object.values(errors).map((error, idx) => (
						<li key={idx}>{error}</li>
					))}
				</ul> */}
				<label>
					First Name
					<span className='login-error-item'>{errors.firstName}</span>
					<input
						type="text"
						value={firstName}
						onChange={(e) => setFirstName(e.target.value)}
						required
					/>
				</label>
				<label>
					Last Name
					<span className='login-error-item'>{errors.lastName}</span>
					<input
						type="text"
						value={lastName}
						onChange={(e) => setLastName(e.target.value)}
						required
					/>
				</label>
				<label>
					Bio
					<span className='login-error-item'>{errors.bio}</span>
					<textarea
						value={bio}
						onChange={(e) => setBio(e.target.value)}
						required
					/>
				</label>
				<label>
					City
					<span className='login-error-item'>{errors.city}</span>
					<input
						type="text"
						value={city}
						onChange={(e) => setCity(e.target.value)}
						required
					/>
				</label>
				<label>
					State
					<span className='login-error-item'>{errors.state}</span>
					<input
						type="text"
						value={state}
						onChange={(e) => setState(e.target.value)}
						required
					/>
				</label>
				<label>
					Email
					<span className='login-error-item'>{errors.email}</span>
					<input
						type="text"
						value={email}
						onChange={(e) => setEmail(e.target.value)}
						required
					/>
				</label>
				<label>
					Username
					<span className='login-error-item'>{errors.username}</span>
					<input
						type="text"
						value={username}
						onChange={(e) => setUsername(e.target.value)}
						required
					/>
				</label>
				<label>
					Password
					<span className='login-error-item'>{errors.password}</span>
					<input
						type="password"
						value={password}
						onChange={(e) => setPassword(e.target.value)}
						required
					/>
				</label>
				<label>
					Confirm Password
					<input
						type="password"
						value={confirmPassword}
						onChange={(e) => setConfirmPassword(e.target.value)}
						required
					/>
				</label>
				<div className='signup-button-container'>
					<button className="signup-button" type="submit">Sign Up</button>
				</div>
			</form>
		</>
	);
}

export default SignupFormModal;
