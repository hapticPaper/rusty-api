
function updateData(){
    endpoint = $('#dataSelect').val()
    fetch(`/${endpoint}`).then(data=>data.json()).then(d=>{
    document.getElementById('onlydiv').innerHTML=d.dataSetResults.map(n=>{return `<b>Number: ${n}</b>`}).join("<br>");
    console.log(d)
})
}