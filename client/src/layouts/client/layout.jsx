import Header from "../../components/client/header/component"

import "./style.css"

function ClientUI({ children }) {
    return (
        <>
            <Header/>
            <main className="CUI-main full-screen-wrapper d-flex justify-content-center align-items-center">
                {children}
            </main>
        </>
    )
}


export default ClientUI