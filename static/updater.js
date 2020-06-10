
function updateData(){
    endpoint = $('#dataSelect').val()
    htmlList = []
    chartData = []
    cnvs = document.createElement("canvas")
    ctx = cnvs.getContext('2d')
    fetch(`/${endpoint}`).then(data=>data.json()).then(d=>{
        console.log(d);
        chartData=d.dataSetResults;
        d.dataSetResults.forEach(n=>{
            htmlList.push(`<b>Number:</b>${n}`);
    });
    var chart = new Chart(ctx, {
        // The type of chart we want to create
        type: 'bar',
    
        // The data for our dataset
        data: {
            labels: chartData,
            datasets: [{
                
                label: 'My First dataset',
                backgroundColor: 'rgb(255, 99, 132)',
                borderColor: 'rgb(255, 99, 132)',
                data: chartData
            }]
        },
    
        // Configuration options go here
        options: {}
    });
    document.getElementById('onlydiv').innerHTML=htmlList.join("<br>");
    document.getElementById('secondDiv').innerHTML=""
    document.getElementById('secondDiv').appendChild(cnvs);
})
}