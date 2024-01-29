function primeFactors(n) {
    if (n === 0) {
        return 0;
    } else if (n === 1) {
        return 1;
    }
    let unCountedFactors = [];
    let countedFactors = [];
    while (n % 2 == 0) {
        unCountedFactors.push(2);
        n = Math.floor(n / 2);
    }
    for (let i = 3; i <= Math.floor(Math.sqrt(n)); i = i + 2) {
        while (n % i == 0) {
            unCountedFactors.push(i);
            n = Math.floor(n / i);
        }
    }
    if (n > 2) unCountedFactors.push(n);
    unCountedFactors.forEach(function (x) {
        countedFactors[x] = (countedFactors[x] || 0) + 1;
    });
    return countedFactors;
}
function padZero(num) {
    return ("0" + num).slice(-2);
}
function formatPrimeFactors(num) {
    if (num === 0) return "0";
    if (num === 1) return "1";
    var code = "";
    let factors = primeFactors(num);
    for (const [key, value] of Object.entries(factors)) {
        code =
            code + `<mult></mult>${key}<sup>${value === 1 ? "" : value}</sup>`;
    }
    return code.substring(13, code.length);
}
var timeText = document.getElementById("time");
var dateText = document.getElementById("date");
const updateTime = () => {
    let time = new Date();
    let ampm = Math.floor(time.getHours() / 12) === 0 ? "AM" : "PM";

    let hours = time.getHours() % 12;
    hours = hours === 0 ? 12 : hours;
    let minutes = time.getMinutes();
    let seconds = time.getSeconds();

    //minutes = padZero(minutes.toString())
    //hours = padZero(hours.toString())
    //seconds = padZero(seconds.toString())
    minutes = formatPrimeFactors(minutes);
    hours = formatPrimeFactors(hours);
    seconds = formatPrimeFactors(seconds);
    timeText.innerHTML = `${hours}<sub>${ampm}</sub><colon></colon>${minutes}<colon></colon>${seconds}`;
    dateText.innerHTML = `${dayNames[time.getDay()]}, ${
        month[time.getMonth()]
    } ${formatPrimeFactors(time.getDate())}<br><year>${formatPrimeFactors(
        time.getFullYear()
    )}</year>`;
};
var month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
];
var dayNames = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
];
updateTime();
setInterval(updateTime, 1000);
