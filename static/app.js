

fetch('/endpoints').then(data=>data.json()).then(d=>{
    d.endpoints.forEach(n=>{
        o = document.createElement("option")
        o.text = n
        document.getElementById('dataSelect').add(o)
        updateData()
    })
})
