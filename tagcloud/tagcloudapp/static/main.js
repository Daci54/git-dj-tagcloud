let projectselect = document.getElementById('projectselect');
let newop = new Option("Select", "select", true, true);
projectselect.add(newop, 0);
let wpsselect = document.getElementById('workpackageselect');
let subselect = document.getElementById('subjectselect');
let token = $("input[name=csrfmiddlewaretoken]").val();

$.ajaxSetup({
    beforeSend: function(xhr) {
        xhr.setRequestHeader("X-CSRFToken", token)
    }
});

function generalAJAX(postdata, url) {
    return $.ajax({
            type: "POST",
            url: url,
            data: postdata
        })
        .done((response) => {
            console.log('done')
        })
        .fail((response) => {
            console.log(response);
            console.error("POST request not successful");
        })
}

function resetSelElm(selelm) {
    selelm.options.length = 0;
    selelm.options[0] = new Option("Select", "select", true, true);
}

function selectQuery(someid, changingselelm) {
    generalAJAX(someid, "selectquery")
    .then((response) => {
        for (let x of response.selval) {
            var op = document.createElement("option");
            op.textContent = x.name;
            op.value = x.id;
            changingselelm.append(op);
        }
    })
    .catch((response) => {
        console.log(response);
        console.error("selectQuery not successful");
    })
}

