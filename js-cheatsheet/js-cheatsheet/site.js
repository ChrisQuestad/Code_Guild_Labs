'use strict';

// Python: print("hello world")
console.log("Hello world!");

// Variables are assigned with var, (let and const are the new ECMAScript6 defaults)
var pi = 3.1415;

// Functions...
//
// Python:
// def myFunc():
//  print("Hello")
//
// Javascript:
// Functions return undefined instead of None of nothing is returned.
//
function myFunc() {
  console.log('hello');
}

// For loop...
// for(initial_condition; stop_condition; after_interation)
//
// Python:
// for i in range(11):
//   print(i)

for(var i = 1; i <= 10; i++) {
  // if(i == 5) { Stop at any point.
  //   break;
  // }
  console.log(i);
}
// Can't say this here: console.log(i); i is out of scope.

// While loop...
// Calculates the condition before the loop.
// while(condition) {}
var i = 1;
while(true) {
  if(i > 10) {
    break;
  }
  // Actions
  console.log(i);

  // Post-increment.
  i++;
}
// Leaky loop pattern.
console.log("Last value:" + i);
// do {} while(condition), calculate the condition last.
var x = 1;
do {
  console.log(x);
  x++;
} while(x <= 10);

// Arrays...
// Python: list = array
var animals = ["Dog", "Cat", "Bird", "Llama", 3.124];

// Append = push...
animals.push("Charmander");
animals.pop();
// No Charmander's here.
animals.shift(); // Removes dog.
animals.unshift("Bob Ross"); // Adds Bob Ross to the front of the array.

// How to search an array for a value, and get it's index.
var indexOfCat = animals.indexOf("Cat");

// The simple way to iterate through an array.
for(var i = 0; i < animals.length; i++) {
  console.log(animals[i]);
}
// forEach way...
animals.forEach(function(item, index) {
  console.log(item);
});

//Example of forEach
function forEach(array, func) {
  for(var i = 0; i < array.length; i++) {
    var isEven = i % 2 == 0;
    // Arguments passed to this function are OPTIONAL.
    func(array[i], i, isEven);
  }
}
// How we'd run it.
forEach(animals, function(elem) {
  console.log(elem);
});
// What's actually happening.

// Extending the Array prototype...
Array.prototype.rickyLoop = function(func) {
  for(i = this.length - 1; i >= 0; i -= 2) {
    func(this[i], i);
  }
}

// How to use it.
var numbers = [1,2,3,4,5,6,7,9,8];
numbers.rickyLoop(function(item, index) {
  console.log(item, index);
});

// Objects...
// Python dict() = Object()
// Also kind of a class instance... (weird)
var person = {}; // Blank Object.
person["first_name"] = "Sally"; // Call members like this.
person.last_name = "Poe"; // Or this.

// Iterate through the keys.
Object.keys(person).forEach(function(key) {
  console.log(person[key])
});

// Assign a function.
person.speak = function() {
  console.log("Hey my name is "+ this.first_name +" "+ this.last_name +"!!!");
};

// How to clone/copy objects.
var zack = Object.create(person);
zack.first_name = 'Zack';
zack.last_name = 'Kollar';
zack.speak();
