async function PostAlbum(data)
{    
    let retorno = false;
    try {
          await fetch(`http://localhost:5000/album`,
                {
                    method: 'POST',
                    /*headers: {                        
                        'Content-Type': 'application/json',
                    },
                     body:JSON.stringify(data), */
                    body: data
                })
                .then((response) => {
                    if (response.status === 200) 
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

export default PostAlbum;