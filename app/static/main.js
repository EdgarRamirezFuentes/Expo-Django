const ctx = document.getElementById('myChart');

let graphdata = {
    type: 'line',
    data: {
      labels: ['8.8.8.8', '8.8.8.8', '8.8.8.8','8.8.8.8'],
      datasets: [{
        label: 'Pins a la ip de GOOG',
        data: [10.96, 12.74, 8.1 ,12.12],
        borderWidth: 1
      }]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  }

let mychart = new Chart(ctx, graphdata);

let socket = new WebSocket('ws://localhost:8000/ws/graph/')
socket.onmessage = function(e){
    
    let djangoData = JSON.parse(e.data)
    console.log(djangoData["rtt_min"])


    let newgraph = graphdata.data.datasets[0].data
    newgraph.shift();
    newgraph.push(djangoData["rtt_min"]);
    graphdata.data.datasets[0].data = newgraph
    mychart.update();
    /* let newgraph = graphdata.data.datasets[0].data
    newgraph.shift()
    newgraph.push(djangoData["rtt_min"])

    graphdata.data.datasets[0].data = newgraph
    mychart.update() */
    
    
}