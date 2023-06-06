import React from 'react';
import { NavLink } from 'react-router-dom';
import { useSelector } from 'react-redux';
import ProfileButton from './ProfileButton';
import './Navigation.css';

function Navigation({ isLoaded }){
	const sessionUser = useSelector(state => state.session.user);

	return (
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
				<li className='search-link'>
					<NavLink exact to="/discover">Search</NavLink>
				</li>
			{isLoaded && (
				<li>
					<ProfileButton user={sessionUser} />
				</li>
			)}
			</div>
		</ul>
	);
}

export default Navigation;
