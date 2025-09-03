async function LoadUser() {
    try{

        const response=await fetch('http://127.0.0.1:8000/getallusers/',{
            credentials : "include"
        });
        
        if (!response.ok){
            alert("Failes to fetch users");
            return;
        };
        const data=await response.json()
        let html = "";
        data.forEach(user => {

            html += `<p style="cursor:pointer color :blue" onclick=createroom(${user.id})>${user.username}</p>`
        });
        document.getElementById('users').innerHTML=html;
    }catch(error){


    }
}
LoadUser()