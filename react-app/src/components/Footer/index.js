import React from 'react';
import "./Footer.css";

const Footer = () => {
    return (
        <>
            <h2 className='title'>Meet the Developers</h2>
            <div className='footer-container'>
                <div className='link-container'>
                    <p>Andre Abad</p>
                    <a><i class="fa-brands fa-linkedin"></i></a>
                    <a><i class="fa-brands fa-square-github"></i></a>
                </div>
                <div className='link-container'>
                    <p>Joshua Hulford</p>
                    <a><i class="fa-brands fa-linkedin"></i></a>
                    <a><i class="fa-brands fa-square-github"></i></a>
                </div>
                <div className='link-container'>
                    <p>Liz Lowry</p>
                    <a><i class="fa-brands fa-linkedin"></i></a>
                    <a><i class="fa-brands fa-square-github"></i></a>
                </div>
                <div className='link-container'>
                    <p>Tia Doherty</p>
                    <a><i class="fa-brands fa-linkedin"></i></a>
                    <a><i class="fa-brands fa-square-github"></i></a>
                </div>
            </div>
        </>
    )
}

export default Footer
