import React , { useState, useEffect }  from 'react';
import { Link } from 'react-router-dom';
import {
    Box,
    Button,
    Divider,
    Paper,
    styled,
    Table,
    TableBody,
    TableCell,
    tableCellClasses,
    TableContainer,
    TableFooter,
    TableHead,
    TablePagination,
    TableRow,
    TextField
} from '@mui/material/';

import IconButton from '@mui/material/IconButton';
import FirstPageIcon from '@mui/icons-material/FirstPage';
import KeyboardArrowLeft from '@mui/icons-material/KeyboardArrowLeft';
import KeyboardArrowRight from '@mui/icons-material/KeyboardArrowRight';
import LastPageIcon from '@mui/icons-material/LastPage';

import EditIcon from '@mui/icons-material/Edit';

import PropTypes from 'prop-types';
import { useTheme } from '@mui/material/styles';
import Moment from 'moment';
import { registerLocale, setDefaultLocale } from "react-datepicker";
import ptBR from "date-fns/locale/pt-BR";
import "react-datepicker/dist/react-datepicker.css";
registerLocale('pt-BR', ptBR);
setDefaultLocale('pt-BR');

import GetAlbuns from '../../services/teste/GetAlbuns';

function TablePaginationActions(props) {
    const theme = useTheme();
    const { count, page, rowsPerPage, onPageChange } = props;

    const handleFirstPageButtonClick = (event) => {
        onPageChange(event, 0);
    };

    const handleBackButtonClick = (event) => {
        onPageChange(event, page - 1);
    };

    const handleNextButtonClick = (event) => {
        onPageChange(event, page + 1);
    };

    const handleLastPageButtonClick = (event) => {
        onPageChange(event, Math.max(0, Math.ceil(count / rowsPerPage) - 1));
    };

    return (
        <Box sx={{ flexShrink: 0, ml: 2.5 }}>
            <IconButton
                onClick={handleFirstPageButtonClick}
                disabled={page === 0}
                aria-label="first page"
            >
                {theme.direction === 'rtl' ? <LastPageIcon /> : <FirstPageIcon />}
            </IconButton>
            <IconButton
                onClick={handleBackButtonClick}
                disabled={page === 0}
                aria-label="previous page"
            >
                {theme.direction === 'rtl' ? <KeyboardArrowRight /> : <KeyboardArrowLeft />}
            </IconButton>
            <IconButton
                onClick={handleNextButtonClick}
                disabled={page >= Math.ceil(count / rowsPerPage) - 1}
                aria-label="next page"
            >
                {theme.direction === 'rtl' ? <KeyboardArrowLeft /> : <KeyboardArrowRight />}
            </IconButton>
            <IconButton
                onClick={handleLastPageButtonClick}
                disabled={page >= Math.ceil(count / rowsPerPage) - 1}
                aria-label="last page"
            >
                {theme.direction === 'rtl' ? <FirstPageIcon /> : <LastPageIcon />}
            </IconButton>
        </Box>
    );
}

TablePaginationActions.propTypes = {
    count: PropTypes.number.isRequired,
    onPageChange: PropTypes.func.isRequired,
    page: PropTypes.number.isRequired,
    rowsPerPage: PropTypes.number.isRequired,
};

function ListaAlbuns() {
    const [page, setPage] = React.useState(0);
    const [rowsPerPage, setRowsPerPage] = React.useState(5);
    const [codigoUsuario] = useState(1);
    const [lista, setLista] = useState([]);

    const handleChangePage = (event, newPage) => {
        setPage(newPage);
    };
    useEffect(()=>{
        GetDados();
    },[]);

    const GetDados = async ()=>
    {
        let retorno = await GetAlbuns();
        setLista(retorno);
        return retorno;
    }

    const handleChangeRowsPerPage = (event) => {
        setRowsPerPage(parseInt(event.target.value, 10));
        setPage(0);
    };
  
    const StyledTableCell = styled(TableCell)(({ theme }) => ({
        [`&.${tableCellClasses.head}`]: {
            backgroundColor: theme.palette.common.black,
            color: theme.palette.common.white,
            fontSize: 'small',
        },
        [`&.${tableCellClasses.body}`]: {
            fontSize: 'small',
        },
    }));

    const StyledTableRow = styled(TableRow)(({ theme }) => ({
        '&:nth-of-type(odd)': {
            backgroundColor: theme.palette.action.hover,                        
        },
        // hide last border
        '&:last-child td, &:last-child th': {
            border: 0,
        },
    }));

  
    Moment.locale('pt-BR');
   
    return (
        <TableContainer component={Paper}>
            <Table sx={{ minWidth: 650 }} aria-label="lista">
                <TableHead sx={{ height: 40 }}>
                    <TableRow>
                        <StyledTableCell align="center">Id</StyledTableCell>                        
                        <StyledTableCell align="center">Artista</StyledTableCell>
                        <StyledTableCell align="center">Titulo</StyledTableCell>
                        <StyledTableCell align="center">Preço</StyledTableCell>                        
                        <StyledTableCell align="center">Ação</StyledTableCell>
                    </TableRow>
                </TableHead>

                <TableBody >

                    {/* {(rowsPerPage > 0
                        ? lista.albuns.slice(page * rowsPerPage, page * rowsPerPage + rowsPerPage)
                        : lista.albuns
                    )
                        .map((row) => (
                            <StyledTableRow
                                key={row.id}
                                sx={{ '&:last-child td, &:last-child th': { border: 0 }, height: 40 }}
                            >
                                <StyledTableCell align='center' component="th" scope="row" divider={<Divider orientation="vertical" flexItem />}>
                                    {row.id}
                                </StyledTableCell>
                                <StyledTableCell align='center'>
                                    {row.artist}
                                </StyledTableCell>
                                <StyledTableCell align='center'>
                                    {row.title}
                                </StyledTableCell>
                                <StyledTableCell align='right'>
                                    {parseFloat(row.price).toFixed(2).toString().replace(',','.')}
                                </StyledTableCell>                                
                                <StyledTableCell align="center" >
                                     
                                </StyledTableCell>
                            </StyledTableRow>
                        )
                        )
                    } */}
                </TableBody>
                <TableFooter>
                    <TableRow>
                        <TablePagination
                            rowsPerPageOptions={[5, 10, 25, { label: 'All', value: -1 }]}
                            colSpan={10}
                            count={lista.length}
                            rowsPerPage={rowsPerPage}
                            labelRowsPerPage='Linhas por página'
                            page={page}
                            slotProps={{
                                select: {
                                    inputProps: {
                                        'aria-label': 'linhas por pagina'
                                    },
                                    native: true,
                                },
                            }}
                            onPageChange={handleChangePage}
                            onRowsPerPageChange={handleChangeRowsPerPage}
                            ActionsComponent={TablePaginationActions}
                        />
                    </TableRow>
                </TableFooter>
            </Table>
        </TableContainer>
    )
}
export default ListaAlbuns;