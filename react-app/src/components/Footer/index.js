import React from 'react';
import "./Footer.css";

const Footer = () => {
    return (
        <>
            <hr />
            <div className='footer-bar'>
                <h2 className='footer-title'>Meet the Developers</h2>
                <div className='footer-container'>
                    <div className='person-container'>
                        <p>Andre Abad</p>
                        <div className='link-container'>
                            <a href='https://www.linkedin.com/in/andre-chris-abad-b1a55215a/'><i class="fa-brands fa-linkedin"></i></a>
                            <a href='https://github.com/dreabd'><i class="fa-brands fa-square-github"></i></a>
                        </div>
                    </div>
                    <div className='person-container'>
                        <p>Joshua Hulford</p>
                        <div className='link-container'>
                            <a href='https://www.linkedin.com/in/joshua-hulford/'><i class="fa-brands fa-linkedin"></i></a>
                            <a href='https://github.com/Jhulford88'><i class="fa-brands fa-square-github"></i></a>
                        </div>
                    </div>
                    <div className='person-container'>
                        <p>Liz Lowry</p>
                        <div className='link-container'>
                            <a href='https://www.linkedin.com/in/elizabeth-lowry-33201a14'><i class="fa-brands fa-linkedin"></i></a>
                            <a href='https://github.com/LizLow25'><i class="fa-brands fa-square-github"></i></a>
                        </div>
                    </div>
                    <div className='person-container'>
                        <p>Tia Doherty</p>
                        <div className='link-container'>
                            <a href='https://www.linkedin.com/in/tiadoherty/'><i class="fa-brands fa-linkedin"></i></a>
                            <a href='https://github.com/tiadoherty'><i class="fa-brands fa-square-github"></i></a>
                        </div>
                    </div>
                </div>
            </div>
        </>
    )
}

export default Footer
