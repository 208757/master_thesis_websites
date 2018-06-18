function getCSRFTokenValue()
{
    window.getElementsByName('csrfmiddlewaretoken')[0].
}

function verify() {
    var transfer_radio = document.getElementById("transfer_id");
    var delete_radio = document.getElementById("delete_id");
    var phone_radio = document.getElementById("change_phone_id");

    var state_span = document.getElementById("operation_state");

    var option;
    if (transfer_radio.checked)
    {
        window.alert("tm")
        option = "transfer money";
    }
    else if (delete_radio.checked)
    {
        window.alert("da")
        option = "delete account";
    }
    else if (phone_radio.checked)
    {
        window.alert("cpn")
        option = "change phone number"
    }
     $.ajaxSetup({
        headers : {
            'CSRFToken' : getCSRFTokenValue()
        }
    });
    $.post("/", function(data) {
        state_span.innerText = "Waiting for aprovement for operation \"" + option + "\"";
    })
}