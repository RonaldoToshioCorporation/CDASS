const GetAlbuns = async () =>
{
    try {
        const response = await fetch(`${import.meta.env.VITE_URL_API}/Albun?codigo=`+ id); 

        if (!response.ok) {   
            return null;            
        }

        const data = await response.json();

        return data;
        
    } catch (error) {
        return Promise.reject(error);
    }    
}
export default GetAlbuns;