const GetAlbuns = async () =>
{
    try {
        let url = `${import.meta.env.VITE_URL_API}/${import.meta.env.VITE_URL_API_ALBUM}`;
        const response = await fetch(url); 

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