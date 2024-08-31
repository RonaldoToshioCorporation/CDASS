const GetAlbuns = async () =>
{
    try {        
        //let url = 'http://localhost:5001/album';
        let url = 'http://localhost:5000/albuns';
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