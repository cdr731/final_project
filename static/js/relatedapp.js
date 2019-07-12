// clear the table for new data
function deleteFruitRows() {
  d3.selectAll('#fruit_item').remove();
  d3.selectAll('#fruit_row').remove();
};
  
// 'Filter Table' button
var button = d3.select('#filter-btn');

function insertFruits(fruitData) {
  // iterate through all the results

  console.log(fruitData.length);

  for (i = 0; i < fruitData.length; i++) {

    var fDdistance = fruitData[i].distance;
    var fDfilename = fruitData[i].filename;
    var fDfruit = fruitData[i].fruit;
    var fDfruit_number = fruitData[i].fruit_number;
    var fDfilepath = '/static/images/' + fDfruit + '/' + fDfilename
  
    console.log(fDdistance);
    console.log(fDfilename);
    console.log(fDfruit);

    if (i % 6 == 0) {
      var fruitRow = d3.select('#results')
        .append('div')
        .attr('class', 'row')
        .attr('id', 'fruit_row');
    };

    var fruitItem = fruitRow.append('div')
      .attr('class', 'col-md-2 col-sm-4 col-xs-6')
      .attr('id', 'fruit_item')
    //fruitItem.append('a')
      //.attr('href', 'http://127.0.0.1:5000/fruit_choice/' + fDfruit_number)
    fruitItem.append('img')
      .attr('src', fDfilepath)
      .attr('onclick', 'pullRelatedData(' + fDfruit_number + ')')
      .attr('class', 'center-block')
    fruitItem.append('p')
      .attr('class', 'center small')
      .html('<b>' + fDfruit + '</b><br>' + fDdistance + '<br>' + fDfilename)
  };
};

// filter the database
function pullData(){
  deleteFruitRows();
  
  d3.json('http://127.0.0.1:5000/allFruits', function(data) {
    console.log(data);
    insertFruits(data);
  });
}

function pullRelatedData(fruitNum){
  deleteFruitRows();

d3.json('http://127.0.0.1:5000/fruit_choice/' + fruitNum, function(data) {
    console.log(data);
    insertFruits(data);
  });
}