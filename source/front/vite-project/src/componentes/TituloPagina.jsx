import React from 'react';

import {
    Box,
    Typography
}from '@mui/material';

const TituloPagina = (props) => {
    return (
        <div>
            <Box
                component={"div"}
                sx={{
                    backgroundColor: "beige",
                    height: "30px",
                    alignContent: "center",
                    marginBottom: "5px",
                    marginTop: "5px",
                    fontweight: 'bold'
                }}

            >
                <Typography variant="h5" gutterBottom>
                    {props.titulo}
                </Typography>
            </Box>
        </div>
    );
}
export default TituloPagina;