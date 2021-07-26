import { Nav, Navbar } from "react-bootstrap";
import Link from 'next/link'
import { FC } from "react";
export const Header:FC = function(props){
    return (<><Navbar
        bg="dark"
        expand="md"
        fixed="top"
        variant="dark"
        className="card-1"
    ><Navbar.Brand>Sign Language Recognition</Navbar.Brand>
                <Navbar.Toggle aria-controls="navbar-toggleable" />
                <Navbar.Collapse id="navbar-toggleable">
                    <Nav
                        activeKey='home'
                        className="justify-content-end mr-auto"
                    >
                        <Link href="/" passHref>
                            <Nav.Link eventKey="home">Home</Nav.Link>
                        </Link>
                        
                    </Nav>
                    
                </Navbar.Collapse></Navbar></>)
}