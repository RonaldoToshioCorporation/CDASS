import React from 'react';

import TituloPagina from '../componentes/TituloPagina';
import ListaAlbuns from '../componentes/Album/ListaAlbuns';


function Teste(){
    return (
        <React.Fragment>
            <div>
            <TituloPagina titulo={'Teste - Album'} />
            <ListaAlbuns />
            </div>
        </React.Fragment>
    )
}
export default Teste;