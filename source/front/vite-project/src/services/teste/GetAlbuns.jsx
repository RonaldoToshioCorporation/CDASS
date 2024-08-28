const GetAlbuns = async () =>
{
    try {        
        let url = 'http://localhost:5001/album';
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
export default GetAlbuns;