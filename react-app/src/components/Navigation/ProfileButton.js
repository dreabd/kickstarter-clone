import React, { useState, useEffect, useRef } from "react";
import { useDispatch } from "react-redux";
import { logout } from "../../store/session";
import OpenModalButton from "../OpenModalButton";
import LoginFormModal from "../LoginFormModal";
import SignupFormModal from "../SignupFormModal";
import { NavLink } from "react-router-dom";
import './ProfileButton.css';
import { useHistory } from "react-router-dom";

function ProfileButton({ user }) {
  const dispatch = useDispatch();
  const history = useHistory()
  const [showMenu, setShowMenu] = useState(false);
  const ulRef = useRef();

  const openMenu = () => {
    if (showMenu) return;
    setShowMenu(true);
  };

  useEffect(() => {
    if (!showMenu) return;

    const closeMenu = (e) => {
      if (!ulRef.current?.contains(e.target)) {
        setShowMenu(false);
      }
    };

    document.addEventListener("click", closeMenu);

    return () => document.removeEventListener("click", closeMenu);
  }, [showMenu]);

  const handleLogout = (e) => {
    e.preventDefault();
    dispatch(logout());
    history.push("/")
  };

  const ulClassName = "profile-dropdown" + (showMenu ? "" : " hidden");
  const closeMenu = () => setShowMenu(false);

  return (
    <>
      <button onClick={openMenu} className="header-dropdown-button">Login
      </button>
      <ul className={ulClassName} ref={ulRef}>
        {user ? (
          <>
            <li>{user.username}</li>
            <li>{user.email}</li>
            <li>
              <button onClick={handleLogout}>Log Out</button>
            </li>
            <li>
              <NavLink exact to="/current">Manage My Projects</NavLink>
            </li>
          </>
        ) : (
          <>
            <OpenModalButton
              buttonText="Login"
              onItemClick={closeMenu}
              modalComponent={<LoginFormModal />}
            />
            <hr className='bar' />
            <p className="modal-text">New to Jumpstarter?</p>
            <OpenModalButton
              buttonText="Sign Up Here"
              onItemClick={closeMenu}
              modalComponent={<SignupFormModal />}

            />
          </>
        )}
      </ul >
    </>
  );
}

export default ProfileButton;
