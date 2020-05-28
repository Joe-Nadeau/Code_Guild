const readline = require('readline-sync');

function pick_six() {
    const winning_numbers = []
    let loop_count = 0
    while (loop_count < 6) {
        let next_num = Math.floor(Math.random() * 100);
        winning_numbers.push(next_num);
        loop_count++
    }
    return winning_numbers
}

function num_matches(winner, ticket) {
    let matches = 0

    for ( i in (winner)) {
        if ( ticket[i] === winner[i]) {
            matches++
        }
        return matches
    }
}

function balance_tracker(matches) {
    let balance = 0

    if (matches === 0) {
        balance = balance
    } else if (matches === 1) {
        balance = (balance + 4)
    } else if (matches === 2) {
        balance = (balance + 7)
    } else if (matches === 3) {
        balance = (balance + 100)
    } else if (matches === 4) {
        balance = (balance + 50000)
    } else if (matches === 5) {
        balance = (balance + 1000000)
    } else if (matches === 6) {
        balance = (balance + 25000000)
    }
    return balance
}

function ROI(final_balance, x) {
    let earnings = (final_balance)
    let expenses = (x * -2)
    const return_on_investment = (earnings - expenses) / (expenses)
    return return_on_investment
}

let final_balance = 0
let x = 0
let winner = pick_six();

while (x < 100000 ) {

    let ticket = pick_six();
    let match_count = num_matches(winner, ticket);
    final_balance = final_balance + balance_tracker(num_matches(winner, ticket))
    x++
}

console.log(`Winning numbers are: ${winner}`)
console.log(`Final balance is: ${final_balance}`)
console.log('Your return on investement is:')
console.log(ROI(final_balance, x))
