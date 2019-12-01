let input = document.getElementById('taginput');
let tagsubmit = document.getElementById('tagsubmit');

let tagify = new Tagify(taginput, {
    whitelist: [],
    dropdown : {
        enabled   : 1,
        maxItems  : 20
    }
});

tagify.on('input', onInput)

function onInput( e ){
  let value = e.detail.value;
  tagify.settings.whitelist.length = 0; // reset the whitelist

  let taginput = {'taginput': value};
  generalAJAX(taginput, "tagquery")
  .then((response) => {
      tagify.settings.whitelist = response.tags;
      tagify.dropdown.show.call(tagify, value);
  })
}

projectselect.onchange = () => {
    if (projectselect.value == "select") {

    } else {
    resetSelElm(wpsselect);
    resetSelElm(subselect);
    let prid = { "prid": projectselect.value }
    selectQuery(prid, wpsselect);
    }
}

workpackageselect.onchange = () => {
    if (wpsselect.value == "select") {

    } else {
    resetSelElm(subselect);
    let wpid = { 'wpid': wpsselect.value }
    selectQuery(wpid, subselect);
    }
}

tagsubmit.onclick = () => {
    let val = tagify.value;
    let subid = subselect.value;
    if (projectselect.value == "select" || wpsselect.value == "select" || subselect.value == "select") {
        infoModal("Bitte wählen Sie alle Felder aus");
    } else if (Object.keys(val).length === 0) {
        infoModal("Bitte geben Sie einen Tag ein");
    } else {
        generalAJAX(JSON.stringify({ "tags": val, "subid": subid }), "tagsubmit")
        .then((response) => {
            console.log(response);
            projectselect.selectedIndex = 0;
            resetSelElm(wpsselect);
            resetSelElm(subselect);
            tagify.removeAllTags();
            successModal();
        })
        .catch((response) => {
            console.log(response);
            projectselect.selectedIndex = 0;
            resetSelElm(wpsselect);
            resetSelElm(subselect);
            tagify.removeAllTags();
            errorModal();
        })
    }
}

function successModal() {
    Swal.fire({
        title: 'Vielen Dank!',
        text: 'Ihre Daten wurden erfolgreich gespeichert',
        icon: 'success',
        timer: '3500',
        timerProgressBar: false,
        showConfirmButton: false
        })
}

function errorModal() {
    Swal.fire({
        title: 'Scheisse',
        text: 'Etwas ist schief gelaufen.',
        icon: 'error',
        timer: '3500',
        timerProgressBar: false,
        showConfirmButton: false
        })
}

function infoModal(alerttext) {
    Swal.fire({
        toast: false,
        title: 'Fehlende Daten',
        text: alerttext,
        icon: 'info',
        timerProgressBar: false,
        showConfirmButton: true
        })
}