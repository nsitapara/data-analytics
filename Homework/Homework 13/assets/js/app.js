// @TODO: YOUR CODE HERE!
var svgWidth = 960;
var svgHeight = 500;

var margin = {
  top: 20,
  right: 40,
  bottom: 60,
  left: 100
};

var width = svgWidth - margin.left - margin.right;
var height = svgHeight - margin.top - margin.bottom;

// Create an SVG wrapper, append an SVG group that will hold our chart, and shift the latter by left and top margins.
var svg = d3.select("#scatter")
  .append("svg")
  .attr("width", svgWidth)
  .attr("height", svgHeight);

var chartGroup = svg.append("g")
  .attr("transform", `translate(${margin.left}, ${margin.top})`);

// Import Data
d3.csv("assets/data/data.csv")
  .then(function(wholedata) {

    // Parse Data/Cast as numbers
    // ==============================
    wholedata.forEach(function(data){
        data.poverty = +data.poverty
        data.healthcare = +data.healthcare
    })

    // console.log(d3.extent(wholedata, d=>d.poverty))
    // // Create scale functions
    // // ==============================
    var xLinearScale = d3.scaleLinear()
      .domain([8,d3.max(wholedata, d=>d.poverty)])
      .range([0, width]);

    var yLinearScale = d3.scaleLinear()
      .domain([4,d3.max(wholedata, d=>d.healthcare)])
      .range([height, 0]);

    // // Create axis functions
    // // ==============================
    var bottomAxis = d3.axisBottom(xLinearScale);
    var leftAxis = d3.axisLeft(yLinearScale);

    // // Append Axes to the chart
    // // ==============================
    chartGroup.append("g")
      .attr("transform", `translate(0, ${height})`)
      .call(bottomAxis);

    chartGroup.append("g")
      .call(leftAxis);

    // // Create Circles
    // // ==============================
    selection = chartGroup.selectAll("circle")
    .data(wholedata)
    
    selection.enter()
    .append("circle")
    .attr("cx", d => xLinearScale(d.poverty))
    .attr("cy", d => yLinearScale(d.healthcare))
    .attr("r", "10")
    .attr("fill", "lightblue")

    console.log(wholedata)
    // // Create text for circles
    // // ==============================
    selection
    .data(wholedata)
    .enter()
    .append("text")
    .merge(selection)
    .attr("font-family", "sans-serif")
    .attr("font-size", "10px")
    .attr("fill", "white")
    .attr("x", d => xLinearScale(d.poverty)-7)
    .attr("y", d => yLinearScale(d.healthcare)+5)
    .text(d =>d.abbr)

    // Create axes labels
    chartGroup.append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 0 - margin.left + 40)
      .attr("x", 0 - (height / 2)-50)
      .attr("dy", "1em")
      .attr("class", "axisText")
      .text("Lacks Healthcare(%)");

    chartGroup.append("text")
      .attr("transform", `translate(${width / 2}, ${height + margin.top + 30})`)
      .attr("class", "axisText")
      .text("In Poverty(%)");
  });
