function darkMode() {
    let element = document.body;
    element.classList.toggle("dark-mode");
}

// let popup = document.getElementById("popup")

// function openPopup() {
// 	popup.classList.add("open-popup")
// }
// function closePopup() {
// 	popup.classList.remove("open-popup")
// }

// contactForm.addEventListener('input' , () => {
//     if (fname.value.length > 0 &&
//         lname.value.length > 0 &&
// 		Country.value.length > 0) {
//         submitBtn.removeAttribute9('disabled');
//     } else {
//         submitBtn.setAttribute('disabled', 'disabled'):
//     }
// });

// $(document).ready(function(){
//     $(".chat-btn").click(()=>{
//         $(".chat-bot").slideToggle("slow")
//     })
// })

//Valdas JavaScript

function sendAlert() {
    alert("Animals - friends. Not Food.");
}

//=======================javascript for adaptt.org===========================

		// Global variables: ___________________________________________________________________

var counts = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ];
var rate = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ];

// Functions: __________________________________________________________________________

function StartKillCounter() {
	var millions = [ 90000, 45895, 2262, 1244, 857, 691, 533, 515, 345, 292, 65, 63, 23, 16, 4, 4, 3, 2 ];
	var perSecond = 8;
	for (var i = 0; i < counts.length; ++i) 
		rate[i] = millions[i] * 1000000 / 365 / 24 / 60 / 60 / perSecond;
	setInterval(NewCounts, 1000 / perSecond);
}

function NewCounts() {
	var num, thous, str;
	for (var i = 0; i < counts.length; ++i) {
		counts[i] += rate[i];
		num = Math.round(counts[i]);
		str = "";
		while (num > 1000) {
			thous = num % 1000;
			if (thous < 10)
				thous = "00" + thous;
			else if (thous < 100)
				thous = "0" + thous;
			str = "," + thous + str;
			num = Math.floor(num / 1000);
		}
		str = num + str;
		document.getElementById("count" + i).innerHTML = str;
	}
}



var productBox = document.getElementById("productBox");
var frontImg = document.getElementById("frontImg");
var backImg = document.getElementById("backImg");

function flipRight(){
    productBox.style.transform = "rotateY(180deg)";
    frontImg.style.left = "650px";
    backImg.style.left = "20px";
    frontImg.style.transform = "rotate(-30deg)";
    backImg.style.transform = "rotate(0deg)";
}
function flipLeft(){
    productBox.style.transform = "rotateY(0deg)";
    frontImg.style.left = "20px";
    backImg.style.left = "-650px";
    frontImg.style.transform = "rotate(0deg)";
    backImg.style.transform = "rotate(-30deg)";
}


