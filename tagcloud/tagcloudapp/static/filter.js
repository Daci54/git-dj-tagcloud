document.addEventListener('DOMContentLoaded', function() {

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

    function wpforpr() {
        wpsselect.options.length = 0;
        wpsselect.options[0] = new Option("Select", "select", true, true);
        subselect.options.length = 0;
        subselect.options[0] = new Option("Select", "select", true, true);
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
            .done((data) => {
                for (let wp of data.wps) {
                    var op = document.createElement("option");
                    op.textContent = wp.name;
                    op.value = wp.id;
                    wpsselect.append(op);
                }
            })
            .fail((data) => {
                console.log(data);
                console.error("POST request not successful");
            })
        }
        return prjson;
    }

    function tagcloud(postdata) {
    return $.ajax({
            type: "POST",
            url: "/tagquery",
            data: postdata
        })
        .done((data) => {
        })
        .fail((data) => {
            console.log(data);
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
            .done((data) => {
                for (let sub of data.subs) {
                    var op = document.createElement("option");
                    op.textContent = sub.name;
                    op.value = sub.id;
                    subselect.append(op);
                }
            })
            .fail((data) => {
                console.log(data);
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
                tagcloud(prid)
                .then((data) => {
                    tagreplacer(data.tags);
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
                tagcloud(wpid)
                .then((data) => {
                    tagreplacer(data.tags);
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
                tagcloud(subjson)
                .then((data) => {
                    tagreplacer(data.tags);
                });
                }
                break;
        }
    }

    // tagsubmit.onclick = () => {
    //     var val = tagify.value;
    //     var selval = { "prid": projectselect.value, "wpid": wpsselect.value, "subid": subselect.value };
    //     if (projectselect.value == "select" || wpsselect.value == "select" || subselect.value == "select") {
    //         alert("Bitte wählen Sie alle Felder aus");
    //     } else if (Object.keys(val).length === 0) {
    //         alert("Bitte geben Sie einen Tag ein");
    //     } else {
    //         $.ajax({
    //             type: "POST",
    //             url: "/tagsubmit",
    //             contentType: "application/json; charset=utf-8",
    //             data: JSON.stringify({ "tags": val, "selectval": selval }),
    //             success: function(response) {
    //                 console.log(response);
    //                 return false;
    //             },
    //             error: function(response) {
    //                 console.log(response, "not successful");
    //                 return false;
    //             }
    //         });
    //     }
    // }
}







)