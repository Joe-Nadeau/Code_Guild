let btn = document.querySelector("#newItemButton")
let input = document.querySelector("#itemText")
let ul = document.querySelector("#theList")
let btnRemove = document.querySelector("#removeItems")

btn.addEventListener("click", function(){
    let li = document.createElement("li");
    let linode = document.createTextNode(input.value)
    li.appendChild(linode)
    ul.insertBefore(li, ul.childNodes[0]);
})

document.querySelector("#theList").addEventListener('click', event => {
    event.target.classList.toggle("mark")
})

btnRemove.addEventListener("click", function(){
    let all_li = document.querySelectorAll("li")
    for (let i=0; i < all_li.length; i++){
        if (all_li[i].classList.contains("mark")){
            all_li[i].remove()
        }
    }
})


