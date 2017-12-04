(function() {

// read input
fs = require('fs');
fs.readFile('d2-input.txt', 'utf8', function(err, data) {
  if (err) { return console.log(err); }

  // process input
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

  running_sum = 0;

  for (i = 0; i < final_array.length; i++) {
    row = final_array[i];

    for (j = 0; j < row.length; j++) {
      curr = row[j];
      for (k = j + 1; k < row.length; k++) {
        comp = row[k];
        if (curr % comp == 0) {
          running_sum += curr / comp;
        } else if (comp % curr == 0) {
          running_sum += comp / curr;
        }
      }
    }
  }

  console.log(running_sum);

});

})();
