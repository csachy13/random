function padZeros(num, size = 2) {
	num = num.toString();
	while (num.length < size) num = "0" + num;
	return num;
}

function tick() {
	var minutes = document.getElementById('minutes').value == '' ? 0 : document.getElementById('minutes').value;
	var seconds = document.getElementById('seconds').value == '' ? 0 : document.getElementById('seconds').value;
	var timeAfter = document.getElementById('timeafter');
	var currentTime = new Date();
	currentTime.setMinutes(currentTime.getMinutes() + parseInt(minutes));
	currentTime.setSeconds(currentTime.getSeconds() + parseInt(seconds));
	timeAfter.innerHTML = `<b>Time after timer:</b> ${padZeros(currentTime.getHours())}:${padZeros(currentTime.getMinutes())}:${padZeros(currentTime.getSeconds())}`;
}
var atimer = false;
function stopTimer() {
	document.getElementById('display').innerHTML = "";
	atimer = false;
}
function startTimer() {
	var minutes = parseInt(document.getElementById('minutes').value);
	var seconds = (minutes * 60) + parseInt(document.getElementById('seconds').value);
	var display = document.getElementById('display');
	atimer = true;
	var timer = setInterval(function() {
		var minutes = parseInt(seconds / 60);
		var remainingSeconds = padZeros((seconds % 60).toString());
		display.innerHTML = minutes + ':' + remainingSeconds + '<span class="dull white"> left</span>';
		if (seconds <= 0 || !atimer) {
			clearInterval(timer);
			display.innerHTML = "Timer completed";
		} else {
			seconds--;
		}
	}, 1000);
	display.innerHTML = "";
}
setInterval(tick, 500)