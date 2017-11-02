
function paint(width, height, price, num_coat) {
  var area = (width * height) * num_coat
  var gallons = Math.ceil(area / 400)
  var total_cost = price * gallons

  console.log("You will need " + gallons + " gallons." + " It will cost you" + " $" + total_cost + ".")
}

paint(20, 20, 5, 2)
