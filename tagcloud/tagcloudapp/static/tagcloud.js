let projectselect = document.getElementById('projectselect');
let wpsselect = document.getElementById('workpackageselect');
let subselect = document.getElementById('subjectselect');
let perselect = document.getElementById('personselect');
projectselect.add(createOption("Select", "select"), 0);
perselect.add(createOption("Alle", "all"), 0);
perselect.add(createOption("Select", "select"), 0);

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
        tagreplacer(0);
        resetSelElm(wpsselect);
        resetSelElm(subselect);
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
        tagreplacer(0);
        resetSelElm(subselect);
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
        tagreplacer(0);
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
        tagreplacer(0);
    } else {
        let uid = { 'uid': perselect.value }
        tagQuery(uid);
    }
}