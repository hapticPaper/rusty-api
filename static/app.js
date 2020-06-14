function dataEndpoints() {
    fetch('/datasets').then(data=>data.json()).then(d=>{
    d.datasets.forEach(n=>{
        o = document.createElement("option")
        o.text = n
        document.getElementById('dataSelect').add(o)
    })
    updateData()
})
}



fetch('/charts').then(data=>data.json()).then(d=>{
    d.charts.forEach(n=>{
        o = document.createElement("option")
        o.text = n
        document.getElementById('chartSelect').add(o)
    })
    dataEndpoints()
})