var tabs = document.querySelectorAll( "#choice");
var BestPlayers = document.querySelector(".BestPlayers");
var Amateur = document.querySelector(".Amateur");
var Inter = document.querySelector(".Inter");
var Prof = document.querySelector(".Prof");
var WrdClass = document.querySelector(".WrdClass");
var Champ = document.querySelector(".Champ");
var items = document.querySelectorAll(".lboard_item");


tabs.forEach(function (tab){
    tab.addEventListener("click", function (){
        var currentdatali = tab.getAttribute("data-li");

        tabs.forEach(function (tab){
            tab.classList.remove("active");
        })
        tab.classList.add("active");

        items.forEach(function (item){
            item.style.display = "none";
        })

        if(currentdatali == "BestPlayers"){
            BestPlayers.style.display = "block";
        }
        else if(currentdatali == "Amateur"){
            Amateur.style.display = "block";
        }
        else if(currentdatali == "Inter"){
            Inter.style.display = "block";
        }
        else if(currentdatali == "Prof"){
            Prof.style.display = "block";
        }
        else if(currentdatali == "WrdClass"){
            WrdClass.style.display = "block";
        }
        else{
            Champ.style.display = "block";
        }
    })
})


var cw2 = $('.dropdown-content').height();

function myFunction(x) {
  document.getElementById("lboard").style.top= 50+cw2+"px";
  document.getElementById("lboard").style.transitionDuration= "0.5s";
}
function fun2() {
  document.getElementById("lboard").style.top= "70px";
  document.getElementById("lboard").style.transitionDuration= "0.5s";
}
