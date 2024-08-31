import React, {useState, useEffect} from 'react';
import TituloPagina from '../../componentes/TituloPagina';
import GetAlbuns from '../../services/teste/GetAlbuns';
import GetAlbum from '../../services/teste/GetAlbum';
import PostAlbum from '../../services/teste/PostAlbum';
import PutAlbum from '../../services/teste/PutAlbum';
import { confirmAlert } from 'react-confirm-alert'; // Import
import 'react-confirm-alert/src/react-confirm-alert.css'; // Import css

import {Link, useNavigate,useParams} from 'react-router-dom';

import {
Button,
Container,
FormControl,
Divider,
Stack,
TextField
}from '@mui/material';

function CadastroAlbum()
{
    const { codigo } = useParams();
    const [id, setId] = useState(0);    
    const [title,setTitle]= useState('');
    const [artist,setArtist]= useState('');
    const [price, setPrice] = useState(0);
    const navigate = useNavigate();
    const [album, setAlbum] = useState({});
    useEffect(()=>{
        GetDados();

    },[])

    useEffect (()=>{
        BuscarRegistro();
    },[codigo])

    const BuscarRegistro = async ()=>{
        if (codigo!== undefined)
        {
            let albumEncontrado = await GetAlbum(codigo);

            if (albumEncontrado!==null){
                setId(codigo);
                setTitle(albumEncontrado.title);
                setArtist(albumEncontrado.artist);
                setPrice(albumEncontrado.price);
                setAlbum(albumEncontrado);
            }
        }
        
    }

    const GetDados = async()=>{

        let lista = await GetAlbuns();
        
        if (lista.albuns!== undefined && lista.albuns.length > 0){
            let maxId =  lista.albuns.reduce((acc, i)=>(i.id > acc.id ? i : acc));
            let novoId = maxId.id + 1;
            setId(novoId);            
        }else{
            setId(1);
        }
    }

    const retornar = ()=>{
        navigate('/Teste');
    }

    const submit = () => {
        confirmAlert({
          title: '',
          message: 'Deseja continuar a gravação do registro?',
          buttons: [
            {
              label: 'Sim',
              onClick: () => SalvarNovoRegistro()
            },
            {
              label: 'Não',
              
            }
          ]
        });
      };
    
    const SalvarNovoRegistro= async () =>
    {
        //validar 
        if (id === 0 || id === undefined){
            alert('Id não informado!');
            return;
        }
        if(title ===undefined || title === ''){
            alert('Titulo não informado!');
            return;
        }
        if(artist ===undefined || artist === ''){
            alert('Artista não informado!');
            return;
        }
        if(price ===undefined || price === 0){
            alert('Preço não informado!');
            return;
        }
        const data = new FormData();
        
        data.append('id', id);
        data.append('title', title);
        data.append('artist', artist);
        data.append('price', price);

        let retorno = await codigo !== undefined ? PutAlbum(data): PostAlbum(data);

        if (retorno)
        {
            alert('Registro salvo com sucesso!');
        }
        else
        {
            alert('Ocorreu um erro ao tentar salvar o registro')
        }

    }

    const descricaoTitulo=()=>{
        return  codigo!== undefined ? 'Cadastro de Album - Editar Registro ':'Cadastro de Album - Novo Registro'
    }
    return (
        <React.Fragment>
            <Container>
                <TituloPagina titulo={descricaoTitulo()} />
                <Divider textAlign="left"><h4>Informações</h4></Divider>
                <Stack
                    component="div"
                    spacing={2}
                    noValidate
                    autoComplete="off"
                    direction={'row'}
                    sx={{  width: '100%' }}
                    
                >
                     <FormControl >
                        <TextField
                            label='Código'
                            id="txtId"
                            value={id}                            
                            inputProps={{ style: { width: '80px' } }}        
                            disabled                    
                        />
                    </FormControl>
                    <FormControl >
                        <TextField
                            label='Titulo'                             
                            id="txtTitle"
                            value={title}                            
                            inputProps={{maxLength:300, style: { width: '350px' } }}
                            onChange = {(e)=>setTitle(e.target.value)}                              
                        />                        
                    </FormControl>  
                    <FormControl >
                        <TextField
                            label='Artista'                             
                            id="txtArtist"
                            value={artist}                            
                            inputProps={{maxLength:300, style: { width: '350px' } }}
                            onChange = {(e)=>setArtist(e.target.value)}                              
                        />                        
                    </FormControl>  
                    <FormControl >
                        <TextField
                            label='Preço'                             
                            id="txtPrice"                        
                            value={price}                            
                            inputProps={{maxLength:300, style: { width: '350px' } }}
                            onChange = {(e)=>setPrice(e.target.value)}                              
                        />                        
                    </FormControl>  
                </Stack>
                <Stack
                    component="div"
                    spacing={2}
                    noValidate
                    autoComplete="off"
                    direction={'row-reverse'}
                    sx={{  width: '100%', marginTop:1 }}
                >
                    <Button variant = 'contained'color = 'primary' onClick = {submit}>
                        Salvar
                    </Button>

                    <Button variant = 'contained' color='secondary' onClick={retornar}>
                        Voltar
                    </Button>
                    
                </Stack>
            </Container>
            

        </React.Fragment>       
    )
}

export default CadastroAlbum;