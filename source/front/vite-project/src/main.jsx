import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import App from './App.jsx'
import './index.css'
import {  createBrowserRouter, RouterProvider} from "react-router-dom";
import ErrorPage from "./paginas/ErrorPage";
import Home from './paginas/Home.jsx';
import Teste from './paginas/Teste';
import CadastroAlbum from './componentes/Album/CadastroAlbum';

const router = createBrowserRouter([
  {
    path: "/",
    errorElement: <ErrorPage />,
    element: <App />,
    children:[      
        {
          path: "Home",
          element: <Home />
        },            
        {
          path: "Teste",
          element: <Teste />
        },
        {
          path:"Teste/CadastroAlbum",
          element: <CadastroAlbum />
        }
    ],
  }
  
]);

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <RouterProvider router = {router} />
  </StrictMode>
);

