window.onload = function(){
var name = prompt("Ваше имя?"); 
if (name === undefined) {
  name = "Неизвестный";
  };

alert("Добро пожаловать, " + name);
document.getElementById("name").innerHTML = name;}
