function buildMetadata(sample) {

  // @TODO: Complete the following function that builds the metadata panel

  // Use `d3.json` to fetch the metadata for a sample
  // console.log(URL)
  let URL = `/metadata/${sample}`;
  // console.log(URL)
  var panel = d3.select("#sample-metadata")

  d3.json(URL).then(function(data) {
    panel.html("")

    Object.entries(data).forEach(function(key_value){
    panel.append("p").text(`${key_value[0]}:${key_value[1]}`)  
    })
  });
    // Use d3 to select the panel with id of `#sample-metadata`
    // Use `.html("") to clear any existing metadata
    // Use `Object.entries` to add each key and value pair to the panel
    // Hint: Inside the loop, you will need to use d3 to append new
    // tags for each key-value in the metadata.

    // BONUS: Build the Gauge Chart
    // buildGauge(data.WFREQ);
}
var pie = d3.select("#pie")
var bubble = d3.select("#bubble")
function buildCharts(sample) {

  let URL = `/samples/${sample}`;
  // @TODO: Use `d3.json` to fetch the sample data for the plots
  d3.json(URL).then(function(info){
    // console.log(info["otu_ids"])
    // info.sort()
    var trace1=[{
      labels: info["otu_ids"].slice(0,10),
      values: info["sample_values"].slice(0,10),
      type:"pie"
    }]
    var trace2=[{
      x: info["otu_ids"],
      y: info["sample_values"],
      mode:"markers",
      marker:{
        size:info["sample_values"]
      }
    }]
    var layout = {
      title: {
        text:'Bubble Chart of frequence of species',
        font: {
          family: 'Courier New, monospace',
          size: 24
        },
      },
      xaxis: {
        title: {
          text: 'OTU ID',
          font: {
            family: 'Courier New, monospace',
            size: 18,
            color: '#7f7f7f'
          }
        },
      },
      yaxis: {
        title: {
          text: 'Count',
          font: {
            family: 'Courier New, monospace',
            size: 18,
            color: '#7f7f7f'
          }
        }
      }
    };
    
  
  // console.log(data)

  Plotly.newPlot("pie",trace1)

  Plotly.newPlot("bubble",trace2,layout)

  })
    // @TODO: Build a Bubble Chart using the sample data

    // @TODO: Build a Pie Chart
    
    // HINT: You will need to use slice() to grab the top 10 sample_values,
    // otu_ids, and labels (10 each).
}

function init() {
  // Grab a reference to the dropdown select element
  var selector = d3.select("#selDataset");

  // Use the list of sample names to populate the select options
  d3.json("/names").then((sampleNames) => {
    sampleNames.forEach((sample) => {
      selector
        .append("option")
        .text(sample)
        .property("value", sample);
    });

    // Use the first sample from the list to build the initial plots
    const firstSample = sampleNames[0];
    buildCharts(firstSample);
    buildMetadata(firstSample);
  });
}

function optionChanged(newSample) {
  // Fetch new data each time a new sample is selected
  buildCharts(newSample);
  buildMetadata(newSample);
}

// Initialize the dashboard
init();
