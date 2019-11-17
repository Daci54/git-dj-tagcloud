document.addEventListener('DOMContentLoaded', function() {

    let projectselect = document.getElementById('projectselect');
    let newop = new Option("Select", "select", true, true);
    projectselect.add(newop, 0);
    let wpsselect = document.getElementById('workpackageselect');
    let subselect = document.getElementById('subjectselect');
    var token = $("input[name=csrfmiddlewaretoken]").val();
    $.ajaxSetup({
        beforeSend: function(xhr) {
            xhr.setRequestHeader("X-CSRFToken", token)
        }
    });

    projectselect.onchange = () => {
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
                data: prjson,
                success: function(data) {
                    console.log(data.wps);
                    for (let wp of data.wps) {
                        var op = document.createElement("option");
                        op.textContent = wp.name;
                        op.value = wp.id;
                        wpsselect.append(op);
                    }
                    return false;
                },
                error: function(data) {
                    console.log(data);
                    return false;
                }
            });
        }
    }

    workpackageselect.onchange = () => {
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
                data: wpjson,
                success: function(data) {
                    console.log(data.subs);
                    for (let sub of data.subs) {
                        var op = document.createElement("option");
                        op.textContent = sub.name;
                        op.value = sub.id;
                        subselect.append(op);
                    }
                    return false;
                },
                error: function(data) {
                    console.log(data);
                    return false;
                }
            });
        }
    }

    var taginput = document.getElementById('taginput');
    var tagify = new Tagify(taginput, {
        
    })

    var tagsubmit = document.getElementById('tagsubmit');

    tagsubmit.onclick = () => {
        var val = tagify.value;
        var selval = {"prid": projectselect.value, "wpid": wpsselect.value, "subid": subselect.value};
        if (projectselect.value == "select" || wpsselect.value == "select" || subselect.value == "select") {
            alert("Bitte wählen Sie alle Felder aus");
        } else if (Object.keys(val).length === 0) {
            alert("Bitte geben Sie einen Tag ein");
        } else {
            $.ajax({
                type: "POST",
                url: "/test",
                contentType: "application/json; charset=utf-8",
                data: JSON.stringify({"tags": val, "selectval": selval}),
                success: function(response) {
                    console.log(response);
                    return false;
                },
                error: function(response) {
                    console.log(response, "not successful");
                    return false;
                }
            });
        }
    }
})