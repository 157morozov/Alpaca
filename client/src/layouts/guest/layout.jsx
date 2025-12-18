import Header from "../../components/guest/header/component"

import "./style.css"

function GuestUI({ children }) {
    return (
        <>
            <Header/>
            <main className="GUI-main full-screen-wrapper d-flex justify-content-center align-items-center">
                {children}
            </main>
        </>
    )
}


export default GuestUI