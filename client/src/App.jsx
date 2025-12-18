import { Route, Routes } from 'react-router-dom'
import { AppContext } from './scripts/app-context'

import GuestUI from './layouts/guest/layout'

import Home from './pages/page'
import NotFound from './pages/not-found/page'

import './assets/global.css'
import ClientUI from './layouts/client/layout'

function App() {
  return (
    <>
      <AppContext.Provider value={{

      }}>
        <Routes>
          <Route path="/" element={<ClientUI><Home /></ClientUI>} />
          <Route path="*" element={<GuestUI><NotFound /></GuestUI>} />
        </Routes>
      </AppContext.Provider>
    </>
  )
}

export default App
