# Advent of Code 2017
# Day 4, Problem 1
# Alex Johnson

# load input
in_file = File.open("d4-input.txt", "r")
lines_raw = in_file.readlines
in_file.close

lines = Array.new
lines_raw.each do |line|
  lines.push(line.sub("\n", "").split)
end

# run
count = 0

lines.each do |line|
  is_valid = true
  found = Array.new
  line.each do |word|
    if found.include? word then
      is_valid = false
      break
    else
      found.push(word)
    end
  end
  if is_valid then
    count = count + 1
  end
end

puts count
