// from data.js
var tableData = data;

// YOUR CODE HERE!
var tbody = d3.select("tbody");
var button = d3.select("#filter-btn")

function displayData(ufodata){
    // console.log(ufodata);
    var row = tbody.append("tr");
    Object.entries(ufodata).forEach(function([key, value]) {
    //   console.log(key, value);
      // Append a cell to the row for each value
      // in the weather report object
      var cell = tbody.append("td");
      cell.text(value);
    });
  }
 

data.forEach(displayData);



button.on("click",function (){

    d3.event.preventDefault();

    // Select the input element and get the raw HTML node
  var inputElement = d3.select("#datetime")

  // Get the value property of the input element
  var inputValue = inputElement.property("value")
  console.log(inputValue)
  var filteredData = tableData.filter(tableData => tableData.datetime === inputValue)
  console.log(filteredData)
  listlen = filteredData.length
  console.log(listlen)
  if (listlen === 0){
    data.forEach(displayData);
  }
  else{
    tbody.html("")
    filteredData.forEach(displayData)
  }

})


