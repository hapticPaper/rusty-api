function render(data){
    console.log(data)
    chartData=data.dataSetResults;
    data.dataSetResults.forEach(n=>{
            htmlList.push(`<b>Number:</b>${n}`);
            colors.push(`rgb(${100 * Math.random()},${10 * Math.random()},${255 * Math.random()})`)
    });
    
    var chart = new Chart(ctx, {
        // The type of chart we want to create
        type: chartType,
    
        // The data for our dataset
        data: {
            labels: chartData,
            datasets: [{
                
                label: endpoint,
                backgroundColor: colors,
                borderColor: colors,
                data: chartData
            }]
        },
    
        // Configuration options go here
        options: {}
    });
    document.getElementById('onlydiv').innerHTML=htmlList.join("<br>");
    document.getElementById('secondDiv').innerHTML=""
    document.getElementById('secondDiv').appendChild(cnvs);
}



function updateData(){
    endpoint = $('#dataSelect').val()
    chartType = $('#chartSelect').val()
    points = $('#lengthInput').val()
    formula = $('#formulaInput').val()
    htmlList = []
    chartData = []
    colors = []
    cnvs = document.createElement("canvas")
    ctx = cnvs.getContext('2d')

    if (endpoint=='custom') {
        console.log("Do custom post request")
        //$('#formulaInput').attr('hidden', 'false');
        $.ajax({
            url: "/custom?" + $.param({
                "length": points,
            }),
            type: "POST",
            headers: {
                "Content-Type": "application/json; charset=utf-8",
            },
            contentType: "application/json",
            data: JSON.stringify({
                "formula": formula ? formula : '2x'
            }),
            beforeSend: function(xhr){
                console.log("Post prefetch")
                //$('secondDiv').html('<div class="loader"> </div>');
             },

             success: function(msg){
                 console.log("Completed")
             }
            
        })
        .done(function(data, textStatus, jqXHR) {
            console.log("HTTP Request Succeeded: " + jqXHR.status);
            //console.log(data);

            render(data)

        })
        .fail(function(jqXHR, textStatus, errorThrown) {
            console.log("HTTP Request Failed");
        })
        .always(function() {
            /* ... */
        });
        
        
    }
    else {

        //$('#formulaInput').attr('hidden', 'true')
        fetch(`${endpoint}?length=${points}`).then(data=>data.json()).then(d=>{
        render(d)
    })
}

    

}