async function CheckLogin() {
    try{
        const response=await fetch('http://127.0.0.1:8000/checklogin/',{
            credentials : "include"
        })

        const data= await response.json()
        if (!data.Logged_in){
            window.location.href='login.html';
        }
    } catch(error){
        return({"Error":"there is error in frontend",error});

    }
    
}
CheckLogin()


const roomid=localStorage.getItem('room_id');
        if (!roomid){
          alert("No roomid found");
          window.location.href='index.html'
          }
         

    async function LoadMessage() {
            try {
                const response = await fetch(`http://127.0.0.1:8000/getmessage/${roomid}/`, {
                    credentials: "include"
                });
                if (!response.ok) {
                    alert("Failed to load messages");
                    return;
                }
                const data = await response.json();
                 
                let html = "";
                data.forEach(message => {
                    //[{…}]0: {id: 4, room: 5, sender: 1, text: 'AOA', timestamp: '2025-08-21T18:39:55.246114Z', …}length: 1[[Prototype]]: Array(0)
                    console.log(message.text)
    
                        
                    html+= `
                        <div class="user-card">
                        
                             <p>${message.sender_username}</p>
                            <p>${message.text}</p>
                        </div>
                    `;
                });
                document.getElementById('messages').innerHTML = html;
            } catch (error) {
                console.error("Error fetching users:", error);
            }
        }


function getCookie(name){

    return  document.cookie
    .split(';')
    .find(cookie=> cookie.startsWith(name+'='))
    ?.split('=')[1] || null;
}

document.getElementById('messageform').addEventListener('submit',async function(e){
        e.preventDefault();
        const textinput=document.getElementById('messagetext').value;
        console.log(textinput)
        const csrftoken=getCookie('csrftoken');
        try{
            const response=await fetch('http://127.0.0.1:8000/sendmessage/',{
                method: "POST",
                credentials : "include",
                headers : {"Content-Type" : "application/json",
                    "X-CSRFToken" : csrftoken
                },
                body : JSON.stringify({
                    "room_id" :roomid,
                    "text" :textinput
                })

            });
            const data= await response.json()
            if (response.ok){
                document.getElementById('message-text').innerHTML="";
                LoadMessage()
            }
        }
        catch(error){
            console.error("Error fetching users:", error);
        }

        
    })


LoadMessage()