const GetAlbum = async(id) =>{
    try {        
        let url = `${import.meta.env.VITE_URL_API}/${import.meta.env.VITE_URL_API_GET_ALBUM}${id}`;

        const response = await fetch(url,{
            headers: {
                "Access-Control-Allow-Origin": "*",
                "Content-Type": "text/plain"
            },
        }); 

        if (!response.ok) {   
            return [];            
        }

        const data = response.json();

        return data;
        
    } catch (error) {
        return Promise.reject(error);
    }    
}
export default GetAlbum;