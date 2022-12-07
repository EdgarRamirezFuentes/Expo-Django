console.log("sssssssssss")

let socket = new WebSocket('ws://localhost:8000/ping-management/ws/graph/')

socket.onmessage = function(e){
    let djangoData = JSON.parse(e.data)
    console.log(djangoData)
}