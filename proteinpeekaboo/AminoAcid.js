import React from "react";
import Button from 'react-bootstrap/Button';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faArrowsRotate } from '@fortawesome/free-solid-svg-icons'
import './AminoAcid.css';


export default function AminoAcid(props) {

    const {result} = props.data;

    if (Array.isArray(result) && result.length > 0) {

        return (
            <div className="main-acid-container">
                <div className="amino-acid-container">
                    {result.map((item, index) => {
                        const importAll = (r) => r.keys().map(r);
                        const images = importAll(require.context('../images', false, /\.(png|jpe?g|svg)$/));

                        // Choose a random image for each iteration
                        const randomIndex = Math.floor(Math.random() * images.length);
                        const randomImage = images[randomIndex];

                        return (
                          <div key={index} className="amino_acid">
                            <h3>{item}</h3>
                            <img src={randomImage} alt="random amino acid" />
                          </div>
                        );
                    })}
                </div>
                <div className="refresh-container">
                    <Button variant="secondary" size="lg">
                        <FontAwesomeIcon icon={faArrowsRotate} />
                    </Button>
                </div>
            </div>
        );
    } else {
        return (
            <div className="no-results-page">
                <p>No results available</p>
                <div className="refresh-container">
                    <Button variant="secondary" size="lg">
                        <FontAwesomeIcon icon={faArrowsRotate} />
                    </Button>
                </div>
            </div>
    )}
}