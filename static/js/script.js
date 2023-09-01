let isMobile = {
	Android: function() {return navigator.userAgent.match(/Android/i);},
	BlackBerry: function() {return navigator.userAgent.match(/BlackBerry/i);},
	iOS: function() {return navigator.userAgent.match(/iPhone|iPad|iPod/i);},
	Opera: function() {return navigator.userAgent.match(/Opera Mini/i);},
	Windows: function() {return navigator.userAgent.match(/IEMobile/i);},
	any: function() {return (isMobile.Android() || isMobile.BlackBerry() || isMobile.iOS() || isMobile.Opera() || isMobile.Windows());}
};

let body=document.getElementById('test');
console.log(body)
if(isMobile.any()){
	console.log('mobile')
	body.classList.add('touch');
	for (let i = 1; i <=3; i++) {
		let for_pc = document.getElementById(`for-pc-${i}`)
		for_pc.classList.add('display-none')
	}
	for (let i = 9; i <= 11; i++) {
		el = document.getElementById(`select-item-${i}`)
		el.classList.remove('display-none')
	}
}
else{
	body.classList.add('mouse');
}
