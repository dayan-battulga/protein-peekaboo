import React, {useEffect} from 'react';
import './DNAstrand.css';


export default function DNAstrand(props) {
    
    const numberOfNodes = 28;
    const divs = [];

    useEffect(() => {
        if (props.zoomed === 'stopAnimation') {
          const nodes = document.querySelectorAll('.node');
          nodes.forEach((node, index) => {
            const delay = index * 0.1;
            node.style.animation = `rotate 11s ease ${delay}s forwards`;
            if (index === 13) {
                node.style.transition = `opacity 9s ease ${delay}s`;
                node.style.opacity = '0';
            }
            else {
                node.style.transition = `opacity 2s ${delay}s`;
                node.style.opacity = '0';
            }
          });
        } else {
          const nodes = document.querySelectorAll('.node');
          nodes.forEach((node, index) => {
            const delay = index * 0.1;
            node.style.animation = `rotate 8s linear infinite ${delay}s`;
            node.style.opacity = '1';
          });
        }
      }, [props.zoomed]);

      

    for (let i = 0; i < numberOfNodes; i++) {
        divs.push(<div className="node" />);
    }

    return (
        <div className='dnaStrand'>
            <div className='dnaStrand-container'>
                <div className="material"></div>
                {divs}
            </div>
        </div>
    );
}