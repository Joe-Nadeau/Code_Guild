const readline = require('readline-sync');

conversion_dictionary = {
    ft:0.3048,
    mi:1609.34,
    m:1,
    km:1000,
    yd:0.9144,
    in:0.0254
}

function unitConverter(distance, unit_in, unit_out) {

    if (unit_in !== "m") {
        answer = conversion_dictionary[unit_in] * distance
        return `${distance} ${unit_in} is ${answer} meters`
    } else if (unit_in === "m") {
        answer = distance / conversion_dictionary[unit_out]
        return `${distance} meters is ${answer} ${unit_out}`
    }
    }

distance = readline.question("What is the distance? \n\n");
unit_in = readline.question("What is the input unit? \n in = inches \n ft = feet \n yd = yards \n m = meters \n km = kilometers \n mi = miles \n\n")
unit_out = readline.question("What is the output unit? \n in = inches \n ft = feet \n yd = yards \n m = meters \n km = kilometers \n mi = miles \n\n")

console.log(unitConverter(distance, unit_in, unit_out))
