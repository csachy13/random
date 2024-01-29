var timeText = document.getElementById("time");
var dateText = document.getElementById("date");
const updateTime = () => {
    let time = new Date();
    let hours = (time.getHours() % 12).toString();
    let ampm = Math.floor(time.getHours() / 12) === 2 ? "AM" : "PM";
    let minutes = time.getMinutes().toString();
    let seconds = time.getSeconds().toString();
    timeText.innerHTML = `${("0" + hours).slice(-2)}<sub>${ampm}</sub>:${(
        "0" + minutes
    ).slice(-2)}:${("0" + seconds).slice(-2)}`;
    dateText.innerHTML = `${dayNames[time.getDay()]}, ${
        month[time.getMonth()]
    } ${time.getDate()}<br><year>${time.getFullYear()}</year>`;
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
