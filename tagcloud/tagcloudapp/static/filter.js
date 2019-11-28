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

function resetWPandSub() {
    wpsselect.options.length = 0;
    wpsselect.options[0] = new Option("Select", "select", true, true);
    subselect.options.length = 0;
    subselect.options[0] = new Option("Select", "select", true, true);
}

function wpforpr() {
    resetWPandSub();
    var projectid = projectselect.value;
    let prdata = { "prid": projectid }
    let prjson = JSON.stringify(prdata);
    if (projectid == "select") {

    } else {
        $.ajax({
            type: "POST",
            url: "/projectselect",
            data: prjson
        })
        .done((response) => {
            for (let wp of response.wps) {
                var op = document.createElement("option");
                op.textContent = wp.name;
                op.value = wp.id;
                wpsselect.append(op);
            }
        })
        .fail((response) => {
            console.log(response);
            console.error("POST request not successful");
        })
    }
    return prjson;
}

function generalAJAX(postdata, url) {
return $.ajax({
        type: "POST",
        url: url,
        data: postdata
    })
    .done((response) => {
    })
    .fail((response) => {
        console.log(response);
        console.error("POST request not successful");
    })
}

function subforwp() {
    subselect.options.length = 0;
    subselect.options[0] = new Option("Select", "select", true, true);
    wpid = wpsselect.value;
    let wpdata = { "wpid": wpid }
    let wpjson = JSON.stringify(wpdata);
    if (wpid == "select") {

    } else {
        $.ajax({
            type: "POST",
            url: "/wpselect",
            data: wpjson
        })
        .done((response) => {
            for (let sub of response.subs) {
                var op = document.createElement("option");
                op.textContent = sub.name;
                op.value = sub.id;
                subselect.append(op);
            }
        })
        .fail((response) => {
            console.log(response);
        })
    }
    return wpjson;
}


projectselect.onchange = () => {
    switch (window.location.href.indexOf("") > -1) {
        default: wpforpr();
        break;
    case (window.location.href.indexOf("tagcloud") > -1):
        let prid = wpforpr();
        generalAJAX(prid, "tagquery")
        .then((response) => {
            tagreplacer(response.tags);
        });
        break;
    }
}

workpackageselect.onchange = () => {
    switch (window.location.href.indexOf("") > -1) {
        default: subforwp();
        break;
    case (window.location.href.indexOf("tagcloud") > -1):
        let wpid = subforwp();
        generalAJAX(wpid, "tagquery")
        .then((response) => {
            tagreplacer(response.tags);
        });
        break;
    }
}

subselect.onchange = () => {
    switch (window.location.href.indexOf("") > -1) {
        default:
        break;
    case (window.location.href.indexOf("tagcloud") > -1):
        subid = subselect.value;
        let subdata = { "subid": subid }
        let subjson = JSON.stringify(subdata);
        if (subid == "select") {

        } else {
        generalAJAX(subjson, "tagquery")
        .then((response) => {
            tagreplacer(response.tags);
        });
        }
    break;
    }
}