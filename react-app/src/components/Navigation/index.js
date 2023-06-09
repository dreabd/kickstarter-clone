import React, { useState } from 'react';
import { NavLink, useHistory } from 'react-router-dom';
import { useSelector, useDispatch } from 'react-redux';
import ProfileButton from './ProfileButton';
import { searchAllProjectsThunk } from '../../store/projects';
import './Navigation.css';

function Navigation({ isLoaded }) {
	const [search, setSearch] = useState('')
	const sessionUser = useSelector(state => state.session.user);
	const dispatch = useDispatch();
	const history = useHistory();

	return (
		<div className='main-nav-container'>
			<ul className='navbar-ul'>
				<div className='navbar-leftmost'>
					<li>
						<NavLink exact to="/discover" className='navbarlink'>Discover</NavLink>
					</li>
					<li>
						<NavLink exact to="/projects/new" className='navbarlink'>Start a project</NavLink>
					</li>
				</div>
				<li >
					<NavLink exact to="/" ><p className='logo'>JUMPSTARTER</p></NavLink>
				</li>
				<div className='navbar-rightmost'>
					<div className='search-bar-container'>
						<input
							type='search'
							className='search-bar'
							placeholder='Search by project name or details here!'
							onChange={(e) => {
								setSearch(e.target.value)
							}}

						/>
						{/* dispatch the search thunk here, passing it e.target.value */}
						<button className='search-button'
							onClick={async (e) => {
								console.log("search query: ", search)
								await dispatch(searchAllProjectsThunk(search))
								history.push("/projects/search")
							}}><i class="fa-solid fa-magnifying-glass"></i></button>
					</div>
					{isLoaded && (
						<li>
							<ProfileButton user={sessionUser} />
						</li>
					)}
				</div>
			</ul>
			<ul className='nav-discover-ul'>
				<li><NavLink exact to="/discover/arts" className='category-link'>Arts</NavLink></li>
				<li><NavLink exact to="/discover/comics&illustration" className='category-link'>Comics & Illustration</NavLink></li>
				<li><NavLink exact to="/discover/design&tech" className='category-link'>Design & Tech</NavLink></li>
				<li><NavLink exact to="/discover/film" className='category-link'>Film</NavLink></li>
				<li><NavLink exact to="/discover/food&craft" className='category-link'>Food & Craft</NavLink></li>
				<li><NavLink exact to="/discover/games" className='category-link'>Games</NavLink></li>
				<li><NavLink exact to="/discover/music" className='category-link'>Music</NavLink></li>
				<li><NavLink exact to="/discover/publishing" className='category-link'>Publishing</NavLink></li>
			</ul>
			<hr className='bar' />
		</div>
	);
}

export default Navigation;
