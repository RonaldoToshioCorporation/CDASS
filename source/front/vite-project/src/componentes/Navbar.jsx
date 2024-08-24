import * as React from 'react';
import PropTypes from 'prop-types';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import CssBaseline from '@mui/material/CssBaseline';
import Divider from '@mui/material/Divider';
import Drawer from '@mui/material/Drawer';
import IconButton from '@mui/material/IconButton';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemButton from '@mui/material/ListItemButton';
import MenuIcon from '@mui/icons-material/Menu';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import Logo from '../assets/images/logo.png';
import {Link} from 'react-router-dom';

const drawerWidth = 240;
const navItems = [{nome :'Home', pagina : 'Home'},
                  {nome :'Teste', pagina : 'Teste'},
                  {nome : 'Assistido', pagina : 'Assistido'},
                  {nome :'Palestras', pagina : 'Assistido'},
                  {nome :'Contato', pagina : 'Assistido'}];

const tituloNavBar = 'C.E.A.E - Divina Luz';

function Navbar(props) {
  const { window } = props;
  const [mobileOpen, setMobileOpen] = React.useState(false);

  const handleDrawerToggle = () => {
    setMobileOpen((prevState) => !prevState);
  };

  const handleOpenUserMenu =()=>{

  }
  const drawer = (
    <Box onClick={handleDrawerToggle} sx={{ textAlign: 'center', color:'black'}}>
      <IconButton onClick={handleOpenUserMenu} sx={{ p: 0 }}>        
        <img src={Logo} alt="Logo" />
      </IconButton>
      
      <Typography variant="h6" sx={{ my: 2}} >
        {tituloNavBar}
      </Typography>
      <Divider />
      <List>
        {navItems.map((item) => (
          <ListItem key={item.nome} disablePadding>
            <ListItemButton sx={{ textAlign: 'center' }}>
              {/* <ListItemText href={`${item.pagina}`}>{item.nome}</ListItemText> */}
              <Link style = {{textDecoration: "none", color : "black"}} to={`/${item.pagina}`}>{item.nome}</Link>
            </ListItemButton>
          </ListItem>
        ))}
      </List>
    </Box>
  );

  const container = window !== undefined ? () => window().document.body : undefined;

  return (
    <Box sx={{ display: 'flex' }}>
      <CssBaseline />
      <AppBar component="nav" sx={{backgroundColor:'white'}}>
        <Toolbar>
          <IconButton
            color="black"
            aria-label="open drawer"
            edge="start"
            onClick={handleDrawerToggle}
            sx={{ mr: 2, display: { sm: 'none' } }}
          >
            <MenuIcon />
          </IconButton>            
            <img src={Logo} alt="Logo" />
          
          <Typography
            variant="h6"
            component="div"
            sx={{ flexGrow: 1, 
                  display: { xs: 'none', sm: 'block' },     
                  color:'black'             
            }}            
          >
            {tituloNavBar}
          </Typography>
          <Box sx={{ display: { xs: 'none', sm: 'block' } }}>
            {navItems.map((item) => (
               <Button key={item.nome} sx={{ color: 'black' }}>
                  <Link   style = {{textDecoration: "none", color : "black"}} to={`/${item.pagina}`}>{item.nome}</Link>
              </Button> 
             
            ))}
          </Box>
        </Toolbar>
      </AppBar>
      <nav>
        <Drawer
          container={container}
          variant="temporary"
          open={mobileOpen}
          onClose={handleDrawerToggle}          
          ModalProps={{
            keepMounted: true, // Better open performance on mobile.
          }}
          sx={{
            display: { xs: 'block', sm: 'none' },
            '& .MuiDrawer-paper': { boxSizing: 'border-box', width: drawerWidth },color: 'black' 
          }}
        >
          {drawer}
        </Drawer>
      </nav>
      <Box component="main" sx={{ p: 3 }}>
        <Toolbar />       
      </Box>
    </Box>
  );
}

Navbar.propTypes = {
  /**
   * Injected by the documentation to work in an iframe.
   * You won't need it on your project.
   */
  window: PropTypes.func,
};
export default Navbar;
