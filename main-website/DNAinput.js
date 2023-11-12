import React, {useState} from 'react';
import {InputGroup} from 'react-bootstrap';
import { Form } from 'react-bootstrap';
import { Button } from 'react-bootstrap';
import './DNAinput.css';

function DNAinput() {
    

    return (
        <div className='DNAinput'>
            <div className='DNAinput-container'>
                <InputGroup className="mb-3">
                    <Form.Control
                        size="lg"
                        placeholder="DNA Sequence"
                        aria-label="DNA-Sequence"
                        aria-describedby="basic-addon2"

                    />
                    <Button variant="outline-secondary" id="button-addon2" active>
                        Compute
                    </Button>
                </InputGroup>
            </div>
        </div>
    )
}