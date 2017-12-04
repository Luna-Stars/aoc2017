(function () {

// read input
fs = require('fs');
fs.readFile('d2-p1.txt', 'utf8', function(err, data) {
  if (err) { return console.log(err); }

  var final_array = [];
  var lines = data.trim("\n").split("\n");

  // process input
  for (i = 0; i < lines.length; i++) {
    split_line = lines[i].split("\t");

    for (j = 0; j < split_line.length; j++) {
      split_line[j] = parseInt(split_line[j]);
    }

    final_array.push(split_line);
  }

// perform math
checksum = 0;

for (i = 0; i < final_array.length; i++) {
  checksum += Math.max(...final_array[i]) - Math.min(...final_array[i]);
}

console.log(checksum);

});

})();
