import React from 'react';
import { useState, setStyle, style } from 'react';
import './DNAstrand.css';


export default function DNAstrand() {
    
    const numberOfNodes = 28;
    const divs = []

    for (let i = 0; i < numberOfNodes; i++) {
        divs.push(<div className="node" />);
    }


    return (
        <div className='dnaStrand'>
            <div className='dnaStrand-container'>
                <div class="material"></div>
                {divs}
            </div>
        </div>
    );
}