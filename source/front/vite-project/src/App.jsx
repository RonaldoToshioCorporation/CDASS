import { Outlet } from 'react-router-dom'
import './App.css'
import NavBar from './componentes/Navbar'
import {
  Grid
} from '@mui/material'

function App() {
  return (
    <div className="App">      
        <Grid container spacing={2}>                    
          <Grid item xs={12} >                        
            <NavBar />
          </Grid>          
          <Grid item xs={12}>
            <Outlet />
          </Grid>
        </Grid>
    </div>
  )
}

export default App
