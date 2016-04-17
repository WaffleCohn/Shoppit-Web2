function add(obj)
{
    var quantityAlert = document.getElementById("quantity-alert-container");
    quantityAlert.style.display = "block";
    quantityAlert.sender = obj;
}

function cancel()
{
    var quantityAlert = document.getElementById("quantity-alert-container"),
        input = quantityAlert.getElementsByTagName("input")[0];

    quantityAlert.style.display = "none";

    input.value = "";
}

function addItem()
{
    var quantityAlert = document.getElementById("quantity-alert-container"),
        input = quantityAlert.getElementsByTagName("input")[0];

    if (input.value == "")
        return;

    quantityAlert.style.display = "none";

    console.log("you added " + input.value + " " + quantityAlert.sender.getElementsByTagName("p")[0].innerHTML + " to your grocery list");

    input.value = "";
}

function toggleOptions(obj)
{
    var detail = obj.nextElementSibling;

    if (detail.style.display == "none" || detail.style.display == "" || detail.style.display == null)
        detail.style.display = "block";
    else
        detail.style.display = "none";
}

function closeDetail(obj)
{
    obj.style.display = "none";
    obj.getElementsByTagName("input")[0].value = "";
}
