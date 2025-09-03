document.getElementById('logout').addEventListener('click' ,async function(){
        try{
            const csrftoken= getCookie('csrftoken')
            const response = await fetch('http://127.0.0.1:8000/logout/',{
                method : "POST",
                credentials : "include",
                headers : {
                    "Content-Type" : "application/json",
                    "X-CSRFToken" :csrftoken
                }
            });
            if (response.ok){
                window.location.href='login.html';
            }else{
                alert("Logout Failed")
            }  
        }catch(error){  
            return({"Error": "there is error in code" , error });
        }    
        })