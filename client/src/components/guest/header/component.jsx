import { Link } from "react-router-dom"

import "./style.css"

function Header() {
    const isAuth = false

    return (
        <>
            <nav className="GUI-nav navbar navbar-expand-lg bg-body-color border-bottom sticky-top">
                <div className="container-fluid">
                    <Link className="navbar-brand" to="/">Alpaca</Link>
                    {!isAuth && (
                        <Link className="btn btn-outline text-bg-primary" to="/login">Log in</Link>
                    )}
                </div>
            </nav>
        </>
    )
}

export default Header