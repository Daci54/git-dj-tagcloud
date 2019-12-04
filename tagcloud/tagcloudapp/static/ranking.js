let perselect = document.getElementById('personselect');
let catselect = document.getElementById('categoryselect');
perselect.add(createOption("Alle", "all"), 0);
perselect.add(createOption("Select", "select"), 0);
catselect.add(createOption("Select", "select"), 0);

perselect.onchange = () => {
    if (perselect.value == "select") {
        datareset(0);
        catselect.selectedIndex = 0;
    } else if (perselect.value !== "select" && catselect.value !== "select") {
        tagcountQuery(perselect.value, catselect.value);
    } else {
        console.log("One from perselect");
    }
}

catselect.onchange = () => {
    if (catselect.value == "select") {
        datareset(0);
    } else if (perselect.value !== "select" && catselect.value !== "select") {
        tagcountQuery(perselect.value, catselect.value);
    } else {
        console.log("One from catselect");
    }
}

function tagcountQuery(uid, catname) {
    if (catname == "created") {
        generalAJAX({'uid': uid}, "tagcountcreated")
        .then((response) => {
            datareplacer(response.tagcount);
        })
        .catch((response) => {
            console.log(response.tagcount);
            console.log("Tag count created failed");
        })
    } else {
        generalAJAX({'uid': uid}, "tagcountsubmitted")
        .then((response) => {
            datareplacer(response.tagcount);
        })
        .catch((response) => {
            console.log(response.tagcount);
            console.log("Tag count submitted failed");
        })
    }

}

