const category = document.location.href.split("/")[3];

if (category === "today_diary") {
	const item = document.querySelector('#nav-morning-diary');
	item.classList.add('active');
}

if (category === "friends") {
	const item = document.querySelector('#nav-friends');
	item.classList.add('active');
}

if (category === "ubno_study") {
	const item = document.querySelector('#nav-ubno-study');
	item.classList.add('active');
}