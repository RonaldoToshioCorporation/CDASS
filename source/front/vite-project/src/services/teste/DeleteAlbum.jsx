async function DeleteAlbum(data)
{    
    let retorno = false;
    try {
          await fetch(`http://127.0.0.1:5000/album`,
                {
                    method: 'DELETE',                  
                    body: data
                })
                .then((response) => {
                    if (response.status === 204) 
                    {
                        retorno = true;
                    }
                })  
                return retorno;                  
    } catch (error) {
        if (error.message === "Failed to fetch")
        {
            // get error message from body or default to response status                    
            alert('A comunicação com os serviços está com problemas!');
            return Promise.reject(error);
        }                             
        return false;
    }    
}

export default DeleteAlbum;