var myForm = document.getElementById("kamla");
var myInput = document.getElementById("myInput");
var myItem = document.getElementById("myItem");
myForm.addEventListener("submit", function (event) {
    event.preventDefault();
    createItem(myInput.value);
});
function createItem(inputItems) {
    var items = `<li>${inputItems}<button onclick = "deleteElement(this)">delete product</button> </li>`;
    myItem.insertAdjacentHTML("beforeend", items);
    myInput.value = "";
    myInput.focus();
}