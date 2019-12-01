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
    if (wpsselect.value == "select") {

    } else {
    resetSelElm(subselect);
    let wpid = { 'wpid': wpsselect.value }
    selectQuery(wpid, subselect);
    tagQuery(wpid);
    }
}

subselect.onchange = () => {
    if (subselect.value == "select") {

    } else {
    let subid = { 'subid': subselect.value }
    tagQuery(subid);
    }
}