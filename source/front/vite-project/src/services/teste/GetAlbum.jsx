const GetAlbum = async(id) =>{
    try {        
        //let url = 'http://localhost:5001/album';
        let url = 'http://127.0.0.1:5000/album?id='+ id;
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