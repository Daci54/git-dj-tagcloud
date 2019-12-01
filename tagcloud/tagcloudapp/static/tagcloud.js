let perselect = document.getElementById('personselect');
let testop = new Option("Select", "select", true, true);
perselect.add(testop, 0);

function tagQuery(someid) {
    generalAJAX(someid, "tagquery")
    .then((response) => {
        tagreplacer(response.tags);
    })
    .catch((response) => {
        console.log(response);
        console.error('tagQuery not successful');
    });
}

projectselect.onchange = () => {
    perselect.selectedIndex = 0;
    if (projectselect.value == "select") {

    } else {
    resetSelElm(wpsselect);
    resetSelElm(subselect);
    let prid = { "prid": projectselect.value }
    selectQuery(prid, wpsselect);
    tagQuery(prid);
    }
}

workpackageselect.onchange = () => {
    perselect.selectedIndex = 0;
    if (wpsselect.value == "select") {

    } else {
    resetSelElm(subselect);
    let wpid = { 'wpid': wpsselect.value }
    selectQuery(wpid, subselect);
    tagQuery(wpid);
    }
}

subselect.onchange = () => {
    perselect.selectedIndex = 0;
    if (subselect.value == "select") {

    } else {
    let subid = { 'subid': subselect.value }
    tagQuery(subid);
    }
}

perselect.onchange = () => {
    projectselect.selectedIndex = 0;
    resetSelElm(wpsselect);
    resetSelElm(subselect);
    if (perselect.value == "select") {
        
    } else {
    let uid = { 'uid': perselect.value }
    tagQuery(uid);
    }
}