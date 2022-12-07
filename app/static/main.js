let socket = new WebSocket('localhost:8000/ws/graph/')

socket.onmessage = function(e){
    let djangoData = JSON.parse(e.data)
    console.log(djangoData)
}