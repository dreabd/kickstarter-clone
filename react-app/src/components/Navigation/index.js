import React, { useState } from 'react';
import { NavLink } from 'react-router-dom';
import { useSelector, useDispatch } from 'react-redux';
import ProfileButton from './ProfileButton';
import { searchAllProjectsThunk } from '../../store/projects';
import './Navigation.css';

function Navigation({ isLoaded }) {
	const [search, setSearch] = useState('')
	const sessionUser = useSelector(state => state.session.user);
	const dispatch = useDispatch();

	return (
		<div className='main-nav-container'>
			<ul className='navbar-ul'>
				<div className='navbar-leftmost'>
					<li>
						<NavLink exact to="/discover">Discover</NavLink>
					</li>
					<li>
						<NavLink exact to="/projects/new">Start a project</NavLink>
					</li>
				</div>
				<li>
					<NavLink exact to="/">Jumpstarter Logo</NavLink>
				</li>
				<div className='navbar-rightmost'>
					<label>
						Search the Site!
						<input
							type='search'
							placeholder='Search by project name or details here!'
							onChange={(e) => {
								setSearch(e.target.value)
							}}
						/>
						{/* dispatch the search thunk here, passing it e.target.value */}
						<button onClick={(e) => {
							console.log("search query: ", search)
							dispatch(searchAllProjectsThunk(search))
						}}>Search</button>
					</label>
					{isLoaded && (
						<li>
							<ProfileButton user={sessionUser} />
						</li>
					)}
				</div>
			</ul>
			<ul className='nav-discover-ul'>
				<li><NavLink exact to="">Arts</NavLink></li>
				<li><NavLink exact to="">Comics & Illustration</NavLink></li>
				<li><NavLink exact to="">Design & Tech</NavLink></li>
				<li><NavLink exact to="">Film</NavLink></li>
				<li><NavLink exact to="">Food & Craft</NavLink></li>
				<li><NavLink exact to="">Games</NavLink></li>
				<li><NavLink exact to="">Music</NavLink></li>
				<li><NavLink exact to="">Publishing</NavLink></li>
			</ul>
		</div>
	);
}

export default Navigation;
