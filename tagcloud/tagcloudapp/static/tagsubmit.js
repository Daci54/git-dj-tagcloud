let input = document.getElementById('taginput');
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
  tagcloud(JSON.stringify(taginput))
  .then((data) => {
      tagify.settings.whitelist = data.tags;
      tagify.dropdown.show.call(tagify, value);
  })
}

let tagsubmit = document.getElementById('tagsubmit');

tagsubmit.onclick = () => {
    let val = tagify.value;
    let subid = subselect.value;
    if (projectselect.value == "select" || wpsselect.value == "select" || subselect.value == "select") {
        alert("Bitte wählen Sie alle Felder aus");
    } else if (Object.keys(val).length === 0) {
        alert("Bitte geben Sie einen Tag ein");
    } else {
        $.ajax({
            type: "POST",
            url: "/tagtest",
            data: JSON.stringify({ "tags": val, "subid": subid }),
            success: function(response) {
                console.log(response);
                // return false;
            },
            error: function(response) {
                console.log(response, "not successful");
                // return false;
            }
        });
    }
}

let testbutton = document.getElementById('testbutton');

testbutton.onclick = () => {
    let testval = tagify.value;
    console.log(testval);
}