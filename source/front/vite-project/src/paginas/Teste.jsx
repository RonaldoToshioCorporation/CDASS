import React from 'react';

import TituloPagina from '../componentes/TituloPagina';
import ListaAlbuns from '../componentes/Album/ListaAlbuns';

function Teste() {
    return (
        <React.Fragment>
            <TituloPagina titulo={'Teste - Album'} />
            <ListaAlbuns />
        </React.Fragment>
    )
}
export default Teste;