import React, { useState } from 'react';
import {InputGroup, Form, Button } from 'react-bootstrap';


import './App.css';
import './components/DNAinput.css';

import DNAstrand from './components/DNAstrand';
import Navbar from './components/Navbar';
import AminoAcid from './components/AminoAcid';
import CitationBlock from './components/CitationBlock';


function App() {

  const[fadeProp, setFadeProp] = useState();
  const[zoomProp, setZoom] = useState();
  const [showComponent, setShowComponent] = useState(true);
  const [data, setData] = useState([]);


  async function ComputeHandler () {
    const dtext = document.getElementById("DNA-sequence-input").value;
    setFadeProp("fade-out");

    console.log(dtext);
    try{
      let response = await fetch("http://localhost:4000/api/content", {
        method: "POST",
        headers: {
          'Content-Type': 'application/JSON',
          'insecure': 'true', 
        },
        body: JSON.stringify({text: dtext}),
      })
      let fetchedData = await response.json();
      console.log(typeof fetchedData)
      setData(fetchedData);
      console.log(data);
    } catch(error){
        console.log(error);
    }

    setZoom("stopAnimation");
    setTimeout(() => {
      setShowComponent(false)
    }, 8000)
  }

  return (
    <div className='app'>
      <div className={fadeProp}>

        <Navbar/>
        
        <div className='DNAinput'>
              <div className='DNAinput-container'>
                  <InputGroup className="mb-3" >
                      <Form.Control
                      id="DNA-sequence-input"
                          size="lg"
                          placeholder="DNA Sequence"
                          aria-label="DNA-Sequence"
                          aria-describedby="basic-addon2"
                          autoComplete='off'
                      />
                      <Button onClick={ComputeHandler} variant="outline-secondary" id="button-addon2" active>
                          Compute
                      </Button>
                  </InputGroup>
              </div>
          </div>
        </div>
        <div>
          {showComponent ? (<DNAstrand zoomed={zoomProp}/>) : (<AminoAcid data={data}/>)}
        </div>
        <div className='citation-block'>
          <CitationBlock/>
        </div>
    </div>
  );
}

export default App;
