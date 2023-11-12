import React, { useState } from 'react';
import {InputGroup, Form, Button } from 'react-bootstrap';


import './App.css';
import './components/DNAinput.css';

import DNAstrand from './components/DNAstrand';
import Navbar from './components/Navbar';


function App() {

  const[fadeProp, setFadeProp] = useState();
  const[zoomProp, setZoom] = useState();

  function increaseDnaStrand() {
    
  }

  async function ComputeHandler () {
    const dtext = document.getElementById("DNA-sequence-input").value;
    setFadeProp("fade-out");
    setZoom("zoomed-in");

    try{
      let data = await fetch("http://localhost:4000/api/content", {
        method: "POST",
        headers: {
          'Content-Type': 'application/JSON',
          'insecure': 'true', 
        },
        body: JSON.stringify({text: dtext}),
      })
      console.log(data);
    } catch(error){
        console.log(error);
    }

  }

  return (
    <div className='app'>
      <div className={fadeProp}>

        <Navbar/>
        
        <div className='DNAinput'>
              <div className='DNAinput-container'>
                  <InputGroup className="mb-3">
                      <Form.Control
                      id="DNA-sequence-input"
                          size="lg"
                          placeholder="DNA Sequence"
                          aria-label="DNA-Sequence"
                          aria-describedby="basic-addon2"
                      />
                      <Button onClick={ComputeHandler} variant="outline-secondary" id="button-addon2" active>
                          Compute
                      </Button>
                  </InputGroup>
              </div>
          </div>
        
          <div className={zoomProp}>
            <DNAstrand/>
          </div>
      </div>
    </div>
  );
}

export default App;
