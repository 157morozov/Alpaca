import { Link } from "react-router-dom"

import "./style.css"

function Header() {
    return (
        <>
            <nav className="CUI-nav navbar navbar-expand-lg bg-body-color border-bottom sticky-top">
                <div className="container-fluid">
                    <Link className="navbar-brand" to="/">Alpaca</Link>
                    <Link className="btn btn-outline text-bg-primary" to="/logout">Log out</Link>
                </div>
            </nav>
        </>
    )
}

export default Header