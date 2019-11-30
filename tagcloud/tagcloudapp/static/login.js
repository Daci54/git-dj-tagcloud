let token = $("input[name=csrfmiddlewaretoken]").val();
let form = document.getElementById('loginform');

$.ajaxSetup({
    beforeSend: function(xhr) {
        xhr.setRequestHeader("X-CSRFToken", token)
    }
});

function loginAJAX(postdata, url) {
    return $.ajax({
            type: "POST",
            url: url,
            data: postdata
        })
        .done((response) => {
            console.log("done response");
            console.log(response);
        })
        .fail((response) => {
            console.log(response);
            console.error("POST request not successful");
        })
    }

form.onsubmit = () => {
    event.preventDefault();
    let un = document.forms['loginform']['username'].value;
    let pw = document.forms['loginform']['password'].value;
    let logindata = {'username': un, 'password': pw};
    loginAJAX(logindata, "test")
    .then((data) => {
        console.log(data);
        console.log("this is in the then")
        window.location = data.url;
    })
    .catch((data) => {
        errorToast();
    })
}

function errorToast() {
    Swal.fire({
        toast: true,
        title: 'Login fehlgeschlagen',
        text: 'Bitte überprüfen Sie Ihre eingegebenen Daten oder kontaktieren Sie Ihren Administrator',
        icon: 'error',
        timer: '3500',
        timerProgressBar: false,
        showConfirmButton: false
        })
}