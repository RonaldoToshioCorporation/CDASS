import React from "react";
import { Typography, Box } from "@mui/material";
const TituloPrincipal = () => {
    return (
            <Box 
                component = "div"              
            >
                <Typography
                    variant="h6"
                    noWrap
                    component="a"            
                    sx={{style:{color:'white'}}}    
                >
                    CDASS - Sistema de Gerenciamento de Assistidos
                </Typography>
            </Box>     
            
        
        
    );
};

export default TituloPrincipal;