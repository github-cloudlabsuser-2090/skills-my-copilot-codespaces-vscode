// function to covert Celsius
// to Fahrenheit
function celsiusToFahrenheit(celsius) { 
    // formula to convert
    // celsius to Fahrenheit
    let fahrenheit = (celsius * 9/5) + 32;
    return fahrenheit;
}

//Deliver Code
let Celsius = 25;
console.log(`${Celsius} Celsius is equal to ${celsiusToFahrenheit(Celsius)} Fahrenheit`);
