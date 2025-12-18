import { Link } from "react-router-dom"

function NotFound() {
    return (
        <>
            <div className="container text-center">
                <h1>Page not found</h1>
                <Link to="/">Home</Link>
            </div>
        </>
    )
}

export default NotFound