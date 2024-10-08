async function PutAlbum(data)
{    
    let retorno = false;
    try {
         let url = `${import.meta.env.VITE_URL_API}/${import.meta.env.VITE_URL_API_ALBUM}`;
          await fetch(url,
                {
                    method: 'PUT',
                    /*headers: {                        
                        'Content-Type': 'application/json',
                    },
                     body:JSON.stringify(data), */
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

export default PutAlbum;