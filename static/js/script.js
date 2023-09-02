let isMobile = {
	Android: function() {return navigator.userAgent.match(/Android/i);},
	BlackBerry: function() {return navigator.userAgent.match(/BlackBerry/i);},
	iOS: function() {return navigator.userAgent.match(/iPhone|iPad|iPod/i);},
	Opera: function() {return navigator.userAgent.match(/Opera Mini/i);},
	Windows: function() {return navigator.userAgent.match(/IEMobile/i);},
	any: function() {return (isMobile.Android() || isMobile.BlackBerry() || isMobile.iOS() || isMobile.Opera() || isMobile.Windows());}
};

let body = document.getElementById('body');

if(isMobile.any()){
	body.classList.add('touch');
	let menu = document.getElementById('sub-menu-list')
	let pages_selector = document.getElementById('pages-selector')
	let arrow = document.getElementById('arrow')
	pages_selector.onclick = () => {
		if (menu.classList.contains('open')){
			menu.classList.remove('open')
			arrow.classList.remove('active')
			this.classList.remove('hovered-mobile-version')
		}else{
			menu.classList.add('open')
			arrow.classList.add('active')
			this.classList.add('hovered-mobile-version')
		}
	}
}
else{
	body.classList.add('mouse');
}