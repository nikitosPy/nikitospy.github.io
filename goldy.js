window.onload = function(){
var name = prompt("Ваше имя?"); 
if (name == undefined || name == null || name == "") {
  name = "Неизвестный";
  };

alert("Добро пожаловать, " + name);};
