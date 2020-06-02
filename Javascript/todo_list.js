let btn = document.querySelector("#newItemButton")
let input = document.querySelector("#itemText")
let ul = document.querySelector("#theList")

btn.addEventListener("click", function(){
    let li = document.createElement("li");
    let linode = document.createTextNode(input.value)
    li.appendChild(linode)
    console.log(li);
    console.log(li.innerText)
    ul.insertBefore(li, ul.childNodes[0]);
})