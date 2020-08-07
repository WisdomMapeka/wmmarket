function myFunction() {
  var w = window.innerWidth;
  var h = window.innerHeight;
  document.getElementById("demo").innerHTML = "Width: " + w + "<br>Height: " + h;
}

function mylen(){
	var v = window.innerWidth;
	document.getElementById('w').innerHTML = v;
}


function myf(u){
	var container_three_id = document.getElementById("container-three-id");
	var dropdown_content_id = document.getElementById("dropdown-content-id");
	var dropdown = document.getElementById("dropdown");
	var electro = document.getElementById("electro");
	var dropdown = document.getElementById("dropdown");
	if(u.matches){
		dropdown_content_id.appendChild(electro);
	}else{
		if (dropdown_content_id.contains(electro)) {
			container_three_id.insertBefore(electro, dropdown);}
	}
}

var u = window.matchMedia("(max-width: 950px)")
myf(u)
u.addListener(myf)
// ----------------------------------------------------------------------
function myf2(v){
	var container_three_id = document.getElementById("container-three-id");
	var dropdown_content_id = document.getElementById("dropdown-content-id");
	var dropdown = document.getElementById("dropdown");
	var computers = document.getElementById("computers");
	var dropdown = document.getElementById("dropdown");

	if(v.matches){
		dropdown_content_id.appendChild(computers);
	}else{
		if (dropdown_content_id.contains(computers)) {
		container_three_id.insertBefore(computers, dropdown);}
	}
}
var v = window.matchMedia("(max-width: 880px)")
myf2(v)
v.addListener(myf2)
// -----------------------------------------------------------

function myf3(w){
	var container_three_id = document.getElementById("container-three-id");
	var dropdown_content_id = document.getElementById("dropdown-content-id");
	var dropdown = document.getElementById("dropdown");
	var book =  document.getElementById("book");
	var dropdown = document.getElementById("dropdown");

	if(w.matches){
		dropdown_content_id.appendChild(book);
	}else{
		if (dropdown_content_id.contains(book)) {
		container_three_id.insertBefore(book, dropdown);}
	}
}
var w = window.matchMedia("(max-width: 750px)")
myf3(w)
w.addListener(myf3)
// ----------------------------------

function myf4(x){
	var container_three_id = document.getElementById("container-three-id");
	var dropdown_content_id = document.getElementById("dropdown-content-id");
	var dropdown = document.getElementById("dropdown");
	var beauty = document.getElementById("beauty");
	var dropdown = document.getElementById("dropdown");

	if(x.matches){
		dropdown_content_id.appendChild(beauty);
	}else{
		if (dropdown_content_id.contains(beauty)) {
		container_three_id.insertBefore(beauty, dropdown);}
	}
}
var x = window.matchMedia("(max-width: 690px)")
myf4(x)
x.addListener(myf4)
// ------------------------------------

function myf5(y){
	var container_three_id = document.getElementById("container-three-id");
	var dropdown_content_id = document.getElementById("dropdown-content-id");
	var dropdown = document.getElementById("dropdown");
	var baby = document.getElementById("baby");
	var dropdown = document.getElementById("dropdown");

	if(y.matches){
		dropdown_content_id.appendChild(baby);
	}else{
		if (dropdown_content_id.contains(baby)) {
		container_three_id.insertBefore(baby, dropdown);}
	}
}
var y = window.matchMedia("(max-width: 570px)")
myf5(y)
y.addListener(myf5)
// ------------------------------------------------
function myf6(z){
	var container_three_id = document.getElementById("container-three-id");
	var dropdown_content_id = document.getElementById("dropdown-content-id");
	var dropdown = document.getElementById("dropdown");
	var automo = document.getElementById("automo");
	var dropdown = document.getElementById("dropdown");

	if(z.matches){
		dropdown_content_id.appendChild(automo);
	}else{
		if (dropdown_content_id.contains(automo)) {
		container_three_id.insertBefore(automo, dropdown);}
	}
}
var z = window.matchMedia("(max-width: 500px)")
myf6(z)
z.addListener(myf6)
// -----------------------------------------------------------------

