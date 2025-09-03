function get_Cookie(name){
    return document.cookie
    .split(';')
    .find(cookie => cookie.startsWith(name + '='))
    ?.split('=')[1] || null;
}
async function CheckLogin() {
    try{
        const response= await fetch('http://127.0.0.1:8000/checklogin/',{
            credentials : "include"
        })
        const data= await response.json()
        console.log(data)
        if(!data.Logged_in){
            window.location.href='login.html'; 
        }
    }catch(error){
        return ({"Error" : "There is error in frontend",error});

    }
    
}

CheckLogin()