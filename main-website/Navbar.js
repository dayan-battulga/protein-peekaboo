import React from 'react';
import logo from '../images/dna-infinite-logo.gif';
import './Navbar.css';


export default function Navbar() {
    return (
        <nav className='navbar'>
            <div className='navbar-container'>
                <div className='navbar-logo'>
                    <img src={logo} alt="loading... " className='navbar-gif'/>
                    <p> ProteinPeekaboo</p>
                </div>
            </div>        
        </nav>
    )
}
