
const reverseSentence = (sentence) => {
    return sentence
        .split(' ')
        .reverse()
        .join(' ')
        .replace(/^\w/, (c) => c.toUpperCase());
};

console.log(reverseSentence("hello world from copilot")); // Output: "Copilot from world hello"


const data = [
    [
      { name: 'John', age: 25 },
      { name: 'Jane', age: 30 }
    ],
    [
      { name: 'Bob', age: 40 }
    ]
  ];
// As an illustration, pull names out of the data array
const names = data.flatMap((group) => group.map((person) => person.name));
console.log(names); // Output: ["John", "Jane", "Bob"]